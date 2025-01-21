from flask import Blueprint, request, render_template, flash, redirect, url_for
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Initialize Nominatim API
geolocator = Nominatim(user_agent="AntipodeCalculator", timeout=10)

# Predefined list of oceans and approximate latitudes/longitudes (approximations)
oceans = {
    'Oceano Pacifico': {'lat_range': (-60, 60), 'lon_range': (-180, 180)},
    'Oceano Atlantico': {'lat_range': (-80, 80), 'lon_range': (-80, 0)},
    'Oceano Indiano': {'lat_range': (-60, 60), 'lon_range': (30, 150)},
    'Oceano Antartico': {'lat_range': (-90, -60), 'lon_range': (-180, 180)},
    'Oceano Artico': {'lat_range': (60, 90), 'lon_range': (-180, 180)},
}

app = Blueprint('api', __name__)
app.secret_key = 'una_chiave_segreta_super_sicura'

@app.route('/location', methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        try:
            # Controlla se l'input è lat/lon o city/state/country
            if request.form.get('lat') and request.form.get('lon'):
                latitude = float(request.form.get('lat'))
                longitude = float(request.form.get('lon'))
            else:
                city = request.form.get('city')
                state = request.form.get('state')
                country = request.form.get('country')

                if not city or not country:
                    flash("Errore: Devi specificare almeno città e nazione.", "danger")
                    return redirect(url_for('api.get_location'))

                # Trova le coordinate usando la città, lo stato e la nazione
                location_query = f"{city}, {state}, {country}" if state else f"{city}, {country}"
                location = geolocator.geocode(location_query, language="it")
                if not location:
                    flash("Errore: Luogo non trovato. Controlla i dati inseriti.", "danger")
                    return redirect(url_for('api.get_location'))

                latitude = location.latitude
                longitude = location.longitude

            # Calcola l'antipodo
            antipode_lat = -latitude
            antipode_lon = (longitude + 180) % 360
            if antipode_lon > 180:
                antipode_lon -= 360

            # Ottieni i nomi delle località
            original_location = geolocator.reverse((latitude, longitude), language="it")
            antipode_location = geolocator.reverse((antipode_lat, antipode_lon), language="it")

            # Dettagli della località originale
            original_name = f"{original_location.raw['address'].get('city', 'Sconosciuto') or original_location.raw['address'].get('town', '') or original_location.raw['address'].get('village', '')}, " \
                f"{original_location.raw['address'].get('state', 'Sconosciuto')}, " \
                f"{original_location.raw['address'].get('country', 'Sconosciuto')}" if original_location else "Località sconosciuta"

            # Funzione per trovare l'oceano
            def find_ocean(lat, lon):
                for ocean, bounds in oceans.items():
                    if bounds['lat_range'][0] <= lat <= bounds['lat_range'][1] and bounds['lon_range'][0] <= lon <= bounds['lon_range'][1]:
                        return ocean
                return "Unknown Ocean"

            # Dettagli dell'antipodo
            if antipode_location:
                antipode_name = f"{antipode_location.raw['address'].get('city', 'Sconosciuto') or antipode_location.raw['address'].get('town', '') or antipode_location.raw['address'].get('village', '')}, " \
                    f"{antipode_location.raw['address'].get('state', 'Sconosciuto')}, " \
                    f"{antipode_location.raw['address'].get('country', 'Sconosciuto')}"
            else:
                antipode_name = find_ocean(antipode_lat, antipode_lon)

            # Prepara il risultato
            return render_template(
                'result.html',
                original_name=f"{original_name} - {latitude, longitude}",
                original_lat=latitude,
                original_lon=longitude,
                antipode_name=f"{antipode_name} - {antipode_lat, antipode_lon}",
                antipode_lat=antipode_lat,
                antipode_lon=antipode_lon
            )
        except ValueError:
            flash("Errore: Assicurati di inserire dati validi.", "danger")
        except GeocoderTimedOut:
            flash("Errore: Il servizio di geocoding non ha risposto. Riprova più tardi.", "danger")

        return redirect(url_for('api.get_location'))

    # Renderizza il form di input
    return render_template('search.html')

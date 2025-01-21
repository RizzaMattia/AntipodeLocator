from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import User, Favorite
from models.conn import db

# Blueprint per le rotte
app = Blueprint('routes', __name__)

# Decoratore per proteggere le rotte
def login_required(f):
    from functools import wraps

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Devi effettuare il login per accedere a questa pagina.", "danger")
            return redirect(url_for('routes.login'))
        return f(*args, **kwargs)

    return decorated_function

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Ottieni i dati dal modulo
        username = request.form['username']
        password = request.form['password']

        # Verifica se l'utente esiste nel database
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Se l'utente esiste e la password è corretta, salva l'ID nella sessione
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login avvenuto con successo!", "success")
            return redirect(url_for('routes.home'))

        flash("Credenziali errate!", "danger")
    
    if session.get('user_id'):
        return redirect(url_for('routes.home'))
    else:
        return render_template('login.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ottieni i dati dal modulo
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Convalidazione
        if not username or not password:
            flash("Username e password sono obbligatori!", "danger")
            return redirect(url_for('routes.register'))

        if password != confirm_password:
            flash("Le password non corrispondono!", "danger")
            return redirect(url_for('routes.register'))

        # Verifica se l'utente esiste già
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username già esistente.', 'danger')
            return redirect(url_for('routes.register'))

        # Crea un nuovo utente
        new_user = User(username=username)
        new_user.set_password(password)  # Imposta la password criptata

        # Salva l'utente nel database
        db.session.add(new_user)
        db.session.commit()

        flash('Registrazione avvenuta con successo! Puoi ora effettuare il login.', 'success')
        return redirect(url_for('routes.login'))

    return render_template('register.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash("Logout avvenuto con successo!", "success")
    return redirect(url_for('routes.login'))

# Search Page (Protetta)
@app.route('/search')
def search():
    return render_template('search.html', username=session.get('username'))


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    if 'user_id' not in session:
        flash("Devi essere loggato per aggiungere ai preferiti.", "warning")
        return redirect(url_for('routes.login'))

    user_id = session['user_id']
    original_name = request.form['original_name']
    original_lat = float(request.form['original_lat'])
    original_lon = float(request.form['original_lon'])
    antipode_name = request.form['antipode_name']
    antipode_lat = float(request.form['antipode_lat'])
    antipode_lon = float(request.form['antipode_lon'])

    # Crea un nuovo preferito
    new_favorite = Favorite(
        user_id=user_id,
        original_name=original_name,
        original_lat=original_lat,
        original_lon=original_lon,
        antipode_name=antipode_name,
        antipode_lat=antipode_lat,
        antipode_lon=antipode_lon
    )

    # Salva nel database
    db.session.add(new_favorite)
    db.session.commit()

    flash("Aggiunto ai preferiti con successo!", "success")
    return redirect(url_for('routes.favorites'))


@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        flash("Devi essere loggato per vedere i preferiti.", "warning")
        return redirect(url_for('routes.login'))

    user_id = session['user_id']
    user = User.query.get(user_id)
    return render_template('favorites.html', favorites=user.favorites)


# Rotta per rimuovere un preferito
@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    if 'user_id' not in session:
        flash("Devi essere loggato per modificare i preferiti.", "warning")
        return redirect(url_for('routes.login'))

    favorite_id = request.form['favorite_id']
    favorite = Favorite.query.get(favorite_id)

    if favorite and favorite.user_id == session['user_id']:
        db.session.delete(favorite)
        db.session.commit()
        flash("Preferito rimosso con successo.", "success")
    else:
        flash("Operazione non autorizzata.", "danger")

    return redirect(url_for('routes.favorites'))


@app.route('/details', methods=['GET'])
def details():
    original_lat = request.args.get('original_lat', type=float)
    original_lon = request.args.get('original_lon', type=float)
    antipode_lat = request.args.get('antipode_lat', type=float)
    antipode_lon = request.args.get('antipode_lon', type=float)

    # Simula i nomi, oppure puoi implementare una funzione per recuperarli
    original_name = "Luogo originale"
    antipode_name = "Antipodo"

    return render_template(
        'result.html',
        original_name=original_name,
        original_lat=original_lat,
        original_lon=original_lon,
        antipode_name=antipode_name,
        antipode_lat=antipode_lat,
        antipode_lon=antipode_lon
    )
    
    
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    user_id = session['user_id']
    
    # Elimina i preferiti dell'utente
    user = User.query.get(user_id)
    if user:
        # Elimina i preferiti prima dell'utente
        for favorite in user.favorites:
            db.session.delete(favorite)
        
        # Elimina l'utente
        db.session.delete(user)
        db.session.commit()

        # Rimuovi l'utente dalla sessione
        session.pop('user_id', None)
        session.pop('username', None)

        flash("Il tuo account è stato eliminato con successo!", "success")
    else:
        flash("Errore durante l'eliminazione dell'account.", "danger")
    
    return redirect(url_for('routes.home'))



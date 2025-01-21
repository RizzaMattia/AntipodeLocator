# Antipode Calculator

Antipode Calculator è un'applicazione web che consente agli utenti di trovare l'antipodo di una determinata posizione geografica sulla Terra. Offre una mappa interattiva per visualizzare sia il luogo originale che il suo antipodo, permettendo agli utenti di salvare i risultati come preferiti e gestire il proprio profilo.

## Caratteristiche principali

- **Calcolo dell'antipodo**: Inserisci una posizione geografica e ottieni il punto opposto sulla superficie terrestre.
- **Mappe interattive**: Visualizza il luogo originale e il suo antipodo su due mappe separate.
- **Preferiti**: Salva i tuoi risultati preferiti per accedervi facilmente in futuro.
- **Gestione dell'account**: Accedi al tuo profilo, elimina il tuo account e mantieni i tuoi preferiti.
- **Interfaccia moderna**: Utilizza Bootstrap per un design responsivo e accattivante.

## Requisiti di sistema

- **Python**: Versione 3.8 o superiore
- **Flask**: Framework web utilizzato per sviluppare l'applicazione
- **Database**: SQLite (incluso nella configurazione di base)
- **Librerie aggiuntive**:
  - Flask-Session
  - Flask-WTF
  - Leaflet (per le mappe interattive)
  - Bootstrap (per il design del frontend)

## Installazione

Segui questi passaggi per configurare ed eseguire il progetto in locale:

1. Clona il repository:
   ```bash
   git clone https://github.com/username/antipode-calculator.git
   cd antipode-calculator
   ```

2. Crea un ambiente virtuale e attivalo:
   ```bash
   python -m venv venv
   source venv/bin/activate # Su Windows: venv\Scripts\activate
   ```

3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

4. Esegui il server Flask:
   ```bash
   flask run
   ```

5. Apri il browser e visita `http://127.0.0.1:5000`.

## Configurazione

### File di configurazione
Puoi configurare l'app modificando il file `config.py` per:

- Impostare una chiave segreta per la sessione:
  ```python
  SECRET_KEY = 'your-secret-key'
  ```
- Configurare il database:
  ```python
  SQLALCHEMY_DATABASE_URI = 'sqlite:///antipode.db'
  ```

## Funzionalità principali

### Calcolo dell'antipodo
Inserisci una latitudine e longitudine per ottenere il punto opposto sulla Terra. I risultati verranno mostrati su due mappe separate utilizzando Leaflet.

### Salvataggio nei preferiti
Accedi con il tuo account e salva i risultati nei tuoi preferiti per accedervi facilmente in futuro.

### Gestione dell'account
Gli utenti registrati possono:
- Visualizzare il proprio profilo.
- Eliminare il proprio account (conferma richiesta).

### Mappe interattive
Utilizza Leaflet per visualizzare le mappe del luogo originale e del suo antipodo. Puoi interagire con le mappe per esplorare ulteriormente le aree.

## Struttura del progetto

```plaintext
antipode-calculator/
├── static/          # File statici (CSS, JavaScript, immagini)
├── templates/       # Template HTML
├── app.py           # File principale dell'app Flask
├── config.py        # Configurazione dell'app
├── models.py        # Modelli del database
├── requirements.txt # Librerie richieste
└── README.md        # Documentazione del progetto
```

## Contribuire

Siamo aperti a contributi! Se vuoi migliorare questo progetto:

1. Fai un fork del repository.
2. Crea un branch per le tue modifiche:
   ```bash
   git checkout -b nome-branch
   ```
3. Fai un commit delle tue modifiche:
   ```bash
   git commit -m "Descrizione delle modifiche"
   ```
4. Fai push delle modifiche:
   ```bash
   git push origin nome-branch
   ```
5. Apri una pull request.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Consulta il file `LICENSE` per ulteriori dettagli.

## Contatti

Per domande o segnalazioni, contatta:

- **Autore**: Mattia Rizza
- **Email**: mattia.rizza@example.com
- **GitHub**: [username](https://github.com/username)

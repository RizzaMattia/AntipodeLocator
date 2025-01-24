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
  - Tutti i requisiti presenti nel file ```requirements.txt```

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
Inserisci una latitudine e longitudine per ottenere il punto opposto sulla Terra. I risultati verranno mostrati su due mappe separate.

### Salvataggio nei preferiti
Accedi con il tuo account e salva i risultati nei tuoi preferiti per accedervi facilmente in futuro.

### Gestione dell'account
Gli utenti registrati possono:
- Visualizzare il proprio profilo.
- Eliminare il proprio account.

### Mappe interattive
Utilizza OpenStreetMap per visualizzare le mappe del luogo originale e del suo antipodo. Puoi interagire con le mappe per esplorare ulteriormente le aree.


- **Autore**: Mattia Rizza
- **Email**: mattia.rizza@samtrevano.ch

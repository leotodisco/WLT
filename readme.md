# WLT

## Descrizione
WLT (Whisper Lecture Transcriber) è un tool che utilizza la tecnologia Whisper per trascrivere le lezioni universitarie. 
Può essere utilizzato per convertire file audio in testo.
Apre la strada anche ad attività di estrazione di keywords o text summarization.

## Requisiti
Per utilizzare WLT, assicurati di soddisfare i seguenti requisiti:

1. **Python 3.11**: Assicurati di avere installato Python 3.11 o versioni successive.
2. **Ambiente Virtuale**: Si consiglia di creare un ambiente virtuale per isolare le dipendenze del progetto. Puoi farlo eseguendo il seguente comando:
```bash
    python -m venv venv
```
3. **Installazione delle dipendenze**: Installa le dipendenze necessarie eseguendo il seguente comando dopo aver attivato l'ambiente virtuale:    
```bash
    pip install -r requirements.txt
```

## Utilizzo
Dopo aver soddisfatto i requisiti, puoi trascrivere una lezione seguendo questi passaggi:
personalmente suggerisco di inserire le lezioni nella directory "audio" in modo da essere più ordinati
```bash
    python main.py (path_file_da_trascrivere) (size_modello) (lingua) (secondo_dal_quale_tagliare)
```
- path_file_da_trascrivere: Percorso del file audio da trascrivere.
- size_modello: Dimensione del modello da utilizzare (small, base, medium, large).
- lingua: Lingua del file audio (it per italiano, en per inglese).
- secondo_da_tagliare (opzionale): Secondo dall'inizio del file audio da cui iniziare la trascrizione.

ecco un esempio:
```bash
    python main.py path/to/lezione.mp3 medium it 30
```

## Sviluppi futuri:
- Creare un server per il bot telegram in modo da bypassare il limite dei 50 mb delle API;
- Creare una desktop application con una GUI per semplificare l'utilizzo;
- Refactoring e pulizia del codice sorgente;
- Testing per garantire maggiore robustezza al progetto.

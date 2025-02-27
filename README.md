# DOIT-NAO
## Script connect.bat : 
    

Questo script batch (`connect.bat`) è utilizzato per connettersi a un robot NAO e caricare il codice sorgente

## Prerequisiti

- Un robot NAO connesso alla rete.
- Un file di chiave SSH (`key_ed25519`) per l'autenticazione.
- Il comando `ssh` e `scp` installati sul sistema.

## Configurazione

Assicurati di aggiornare le seguenti variabili nel file `connect.bat`:

- `IP`: L'indirizzo IP del robot NAO.
- `KEY`: Il percorso del file di chiave SSH.

## Utilizzo

1. Apri un terminale.
2. Naviga alla directory contenente `connect.bat`.
3. Esegui il comando:

    ```sh
    connect.bat
    ```

## Descrizione dello Script

Lo script esegue i seguenti passaggi:

1. Imposta l'indirizzo IP del robot NAO e il percorso della chiave SSH.
2. Stampa l'indirizzo IP.
3. Si connette al robot NAO tramite SSH e rimuove la directory `/home/nao/4ci/src` se esiste, quindi crea una nuova directory `/home/nao/4ci/src`.
4. Copia la directory locale [src](http://_vscodecontentref_/1) al robot NAO nella directory `/home/nao/4ci`.

## Note

- Assicurati che il file di chiave SSH abbia i permessi corretti.
- Lo script `start_4ci.sh` deve essere presente sul robot NAO nella directory `/home/nao/4ci`.


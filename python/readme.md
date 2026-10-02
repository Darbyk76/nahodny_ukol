# šifrovací textový program
## instrukce pro spuštění:
 - stáhnout si soubor sifra.py z webu od Radka
 - spustit soubor
  - v terminálu napiště pip install cryptography
  - jakmile bude nainstalovaná knihovna můžete pokročit na další bod
 - spustit soubor
 ## příkazy
  - číst - dešifruje a přečte co je v souboru
   - psát - můžete přidávat text k šifrování
   - příkazy - vypíše příkazy

## ukázka kódu
 ```python
def derive_key(password: str, salt: bytes) -> bytes:
    password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1_200_000
    )

    key = kdf.derive(password.encode())
    
    return key
 
 ```
























 
 *zbytek pod tímto je pouze pro mě jak pracovat s readme*
 **větší poznámka**

 ### ukázka kódu
 `code`



 ### TODO
- [x] dokumentace
- [] funkční UI
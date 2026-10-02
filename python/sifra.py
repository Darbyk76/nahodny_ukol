from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import math
import json
import os


dir_path = os.path.dirname(os.path.abspath(__file__))
json_path = dir_path + "\data.json"
print(json_path)



data = {}
# sul = ""


print("Vítejte v šifrující aplikaci RaDeK_šifra")
print("Veškeré příkazy: číst, psát, příkazy")

# ZÍSKÁNÍ KLÍČE
def derive_key(password: str, salt: bytes) -> bytes:
    password  # .encode() zjistit proč encode - encode se dává pokud chcem dát string na nějkou věc - utf-8 ascii atd. proč? idk
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1_200_000
    )

    key = kdf.derive(password.encode())
    # print(f"{key.hex()} je klic")
    return key


# Š I F R O V Á N Í
def encrypt(data: bytes, password: str):  # šifrování
    print("Sifruji")

    salt = os.urandom(16)  # generuju salt, 16 bitů

    key = derive_key(
        password, salt
    )  # generuju klíč přes volání funkce, zadávám heslo a salt(může být veřejný)

    nonce = os.urandom(
        12
    )  # generuji nonce - číslo co je jen jednou použito při šifrování

    aes = AESGCM(key)

    crypted_text = aes.encrypt(nonce, data, None)
    # print(f"Crypted text: {crypted_text}")
    # print(
    #     f"vracím:{salt+nonce+crypted_text} kde salt je: {salt} nonce je {nonce} a crypted text je {crypted_text}"
    # )
    sul = salt
    return salt + nonce + crypted_text  # vracím salt nonce a šifrovaný text


# D E Š I F R O V Á N Í
def decrypt(encrypted_data: bytes, password: str) -> bytes:  # dešifrování
    # print("desifruji")
    salt = encrypted_data[0:16]
    # print(f"SALT: {salt}")
    nonce = encrypted_data[16:28]
    # print(f"NONCE: {nonce}")
    data = encrypted_data[28:]
    # print(f"DATAAA: {data}")

    key = derive_key(password, salt)

    aes = AESGCM(key)

    return aes.decrypt(nonce, data, None)


# načtení dat
def load_data(heslo, json_path):
    if not os.path.exists(json_path):
        return None, False
    if os.path.getsize(json_path) == 0:
        return new_data(heslo, json_path)
    try:
        with open(json_path, "rb") as f:
            data_bytes = f.read()

            # print(f"náhodná xxxx ")
            desifrovana_bytes = decrypt(data_bytes, heslo)
            json_string = desifrovana_bytes.decode("utf-8")
            data = json.loads(json_string)
            return data
    except Exception as e:
        print(f"nelze: {e}")
        return None


# Uložení dat
def save_data(
    heslo: str,
    user_dir_path: str,
    data: dict,
):
    try:
        json_bytes = json.dumps(data, ensure_ascii=False).encode("utf-8")
        # print(json_bytes)
        zasifrovano = encrypt(json_bytes, heslo)
        with open(user_dir_path, "wb") as f:
            f.write(zasifrovano)
            return True
    except Exception as e:
        print(f"Chyba při uložení: {e}")
        return False


# Pokud již uživatel má svůj soubor ale je prázdný.
def new_data(heslo, user_dir_path):

    # print("nová data")
    data = {
        "nešifrovaný text": "",
        "normalni_data": [],
    }
    save_data(heslo, user_dir_path, data)
    return data


while True:
    print("\n")
    prikaz = input(":  ")
    
    if prikaz == "příkazy":
        print("Veškeré příkazy: číst, psát, příkazy")
        pass
    if prikaz == "psát":
        heslo = input("zadejte heslo:  ")
        try:
            data = load_data(heslo, json_path)
            print("try")
            zprava = input("Zadejte velmi tajnou zprávu....")
            print(f"Data jsoi: {zprava}")
            data["normalni_data"].append(zprava)
            print(f"po appendu {zprava} je zprava a data {data}")
            save_data(heslo, json_path, data)

        except:
            print("Špatné heslo...")

        print("wdgadxwsda")
    if prikaz == "číst":
        print("čtem?")
        heslo = input("zadejte heslo:  ")
        try:
            precteno = load_data(heslo, json_path)
            print(precteno)
        except:
            print("problém")
    else:
        print("Neplatný příkaz...")

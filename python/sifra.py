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



print("Vítejte v šifrující aplikaci RaDeK_šifra")
print("Veškeré příkazy: číst, psát, příkazy")

def new_data():
    plain_data = {
        "salt": "",
        "nonce": "",
        "user_data":""
    }
    save(plain_data)
    return plain_data, True

def save(data):
    with open(json_path,"w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)


def load():
    if  os.path.getsize(json_path) == 0:
        print("Nula")
        return new_data()
    else:
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print("čtu")
        except:
            with open(json_path,"w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent = 4)
                print("vytvořil jsem")
            with open(json_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        print("čtu")
        return data
   

def zasifrovat(data:bytes,heslo:str):
    salt = os.urandom(16)

    key = derive_key(heslo, salt)

    nonce = os.urandom(12)

    aes = AESGCM(key)

    zasifrovana_data = aes.encrypt(
        nonce,
        data,
        None
    )
    data[salt] = salt
    data[nonce] = nonce
    data[user_data] = zasifrovana_data

    return salt,nonce, zasifrovana_data

def desifruji(sifrovane:bytes, heslo:str) -> bytes:
    print("Dešifruji")
    if  os.path.getsize() == 0:
        print("Nula")
        return new_data(heslo, json_path)
    print("více jak 0")
    salt = data[salt]
    nonce = data[nonce]
    data = data[data]

    key = derive_key(heslo, salt)

    aes = AESGCM(key)
    
    return aes.decrypt(
        nonce,
        data,
        None
    )



def derive_key(password:str, salt:bytes)-> bytes:
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000

    )
    
    key = kdf.derive(password.encode("utf-8"))
    print(f"{key.hex()} je klic")
    return key


while True:
    print("\n")
    prikaz = input(":  ")
    
    if prikaz == "příkazy":
        print("Veškeré příkazy: číst, psát, příkazy")
        pass
    if prikaz == "psát":
        heslo = input("zadejte heslo:  ")
        try:
            desifruji(heslo)
        except:
            print("Špatné heslo...")
        print("wdgadxwsda")

    else:
        print("Neplatný příkaz...")

#
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# import json
# import os

# dir_path = os.path.dirname(os.path.abspath(__file__))
# json_path = os.path.join(dir_path, "data.json")

# print(json_path)

# print("Vítejte v šifrující aplikaci RaDeK_šifra")
# print("Veškeré příkazy: číst, psát, příkazy")


# def save(data):
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)


# def load():
#     if not os.path.exists(json_path):
#         save({})
#         return {}

#     with open(json_path, "r", encoding="utf-8") as f:
#         try:
#             return json.load(f)
#         except json.JSONDecodeError:
#             return {}


# def new_data():
#     plain_data = {
#         "salt": "",
#         "nonce": "",
#         "user_data": ""
#     }

#     save(plain_data)
#     return plain_data


# def derive_key(password: str, salt: bytes) -> bytes:

#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=1_200_000
#     )

#     key = kdf.derive(password.encode("utf-8"))

#     print(f"{key.hex()} je klíč")
#     return key


# def zasifrovat(data: bytes, heslo: str):

#     salt = os.urandom(16)

#     key = derive_key(heslo, salt)

#     nonce = os.urandom(12)

#     aes = AESGCM(key)

#     ciphertext = aes.encrypt(
#         nonce,
#         data,
#         None
#     )

#     ulozena_data = {
#         "salt": salt.hex(),
#         "nonce": nonce.hex(),
#         "user_data": ciphertext.hex()
#     }

#     save(ulozena_data)

#     return ulozena_data


# def desifruji(heslo: str) -> bytes:

#     data = load()

#     if not data:
#         raise Exception("Žádná data nejsou uložena")

#     salt = bytes.fromhex(data["salt"])
#     nonce = bytes.fromhex(data["nonce"])
#     ciphertext = bytes.fromhex(data["user_data"])

#     key = derive_key(heslo, salt)

#     aes = AESGCM(key)

#     return aes.decrypt(
#         nonce,
#         ciphertext,
#         None
#     )


# while True:

#     print()
#     prikaz = input(": ")

#     if prikaz == "příkazy":
#         print("Veškeré příkazy: číst, psát, příkazy")

#     elif prikaz == "psát":

#         heslo = input("zadejte heslo: ")
#         text = input("zadejte text: ")

#         zasifrovat(
#             text.encode("utf-8"),
#             heslo
#         )

#         print("Data uložena.")

#     elif prikaz == "číst":

#         heslo = input("zadejte heslo: ")

#         try:
#             plaintext = desifruji(heslo)

#             print(
#                 "Dešifrováno:",
#                 plaintext.decode("utf-8")
#             )

#         except Exception:
#             print("Špatné heslo nebo poškozená data.")

#     else:
#         print("Neplatný příkaz...")
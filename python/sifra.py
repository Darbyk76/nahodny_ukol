import cryptography
import math
import json
import os


dir_path = os.path.dirname(os.path.abspath(__file__))
json_path = dir_path + "\data.json"
print(json_path)

plain_data = {

}
data = {}

try:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        print("čtu")
except:
    with open(json_path,"w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)
        print("vytvořil jsem")

print("Vítejte v šifrující aplikaci RaDeK_šifra")
print("Veškeré příkazy: číst, psát, příkazy")

def zasifrovat():
    print("Šifruji")

def desifruji():
    print("Dešifruji")


def derive_key(password:str, salt:bytes) -> bytes:
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000

    )
    
    key = kdf.derive(password.encode())
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
        derive_key(heslo)

    else:
        print("Neplatný příkaz...")


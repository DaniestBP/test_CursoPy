# import hashlib
from hashlib import sha256

# pwd_e = hashlib.sha256("15441".encode()) ó

# pwd_e = hashlib.sha256(b"15441")

# print(pwd_e.hexdigest())
pwd= "1234"

pwd_e_bytes = sha256(pwd.encode())  # Devuelve una contraseña en bytes que no es legible por JSON
pwd_e_str = pwd_e_bytes.hexdigest() # Lo transformamos a una string manteniendo la encriptacion con hexdigest()


print(pwd_e_str)

# def e(pwd):
#     result= ""
#     for char in pwd:
#         char_ascii = ord(char)
#         char_ascii = char_ascii*2/3+7
#         result += str(char_ascii)
#     return result

# pwd = "hola"


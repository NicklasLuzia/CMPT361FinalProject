from Crypto.PublicKey import RSA
import os

def generate_keys(name):
       key = RSA.generate(2048)
       
       private_key = key.export_key()
       public_key = key.publickey().export_key()
       
       with open(f"{name}_private.pem", "w") as file:
              file.write(private_key)
              
       with open(f"{name}_public.pem", "w") as file:
              file.write(public_key)
              

generate_pair("server")
generate_pair("client1")
generate_pair("client2")
generate_pair("client3")
generate_pair("client4")
generate_pair("client5")

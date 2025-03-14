import cryptography 
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes

pvt_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pub_key = pvt_key.public_key()

private_pem = pvt_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print(private_pem)


public_pem = pub_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print('------------')

with open('pvt.pem', 'wb') as f:
    f.write(private_pem)

print(f'Pvt: {private_pem.decode()}')
print(f'Pub: {public_pem.decode()}')

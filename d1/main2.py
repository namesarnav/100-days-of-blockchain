import hashlib

block = open('pvt.pem','r')
nonce = 0

while True:
    data = f"{block}{nonce}".encode()
    hash_result = hashlib.sha256(data).hexdigest()

    if hash_result.startswith("00"):
        print(f"Nonce: {nonce}, Hash: {hash_result}")
        break
    nonce += 1
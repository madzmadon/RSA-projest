from rsa_keys import *

def privateUserMenu(publicKey, privateKey):

    while True:
        print('As the owner of the keys, what would you like to do?')
        print('1. Decrypt a received message')
        print('2. Digitally sign a message')
        print('3. Show the keys')
        print('4. Generating a new set of the keys')
        print('5. Exit') 
        choice = input('Enter your choice:')
   
        if choice == '1':
            message = input("Enter message to encrypt: ")
            encrypted = encrypt(message, publicKey)
            print("Encrypted message:", encrypted)
      
        elif choice == '2':
            encrypted = input("Enter ciphertext to decrypt: ")
            decrypted = decrypt(encrypted, privateKey)
            print("Decrypted message:", decrypted)
      
        elif choice == '3':
            message = input("Enter message to sign: ")
            print(f"Public Key: {publicKey}")
            print(f"Private Key: {privateKey}")
            signature = generateSignature(message, privateKey)
            print("Signature:", signature)
      
        elif choice == '4':
            message = input("Enter message: ")
            signature = input("Enter signature: ")
            result = verifySignature(message, signature, publicKey)
            print("Signature valid:", result)
      
        elif choice == '5':
            break
    
        else:
            print("Invalid choice")

def publicUserMenu(publicKey, privateKey):
    while True:
        print('As a public user, what would you like to do?')
        print('1. Send an encrypted message')
        print('2. Authenticate a digital signature')
        print('3. Exit')
        choice = input('Enter your choice:')

        if choice == '1':
            message = input('Enter a message: ')
            encrypted = encrypt(message, publicKey)
            print("Encrypted message:", encrypted)
        elif choice == '2':
            if result == '':
                print('There are no signature to authenticate.') 
            else:
                signature = input("Enter signature: ")
                result = verifySignature(message, signature, publicKey)
                print("Signature valid:", result)
        
        elif choice == '3':
            break
from rsa_keys import *
messages = []
signatures = []

def promptList(options, message = 'Invalid selection'):
    count = 1
    choice = 0
    while choice <= 0 or choice > len(options):
        count = 1
        for i in options:
            print(f"{count}. {i}")
            count += 1
        choice = int(input("> "))
        if choice > 0 or choice < len(options):
            print(message)
    return (choice - 1)

def privateUserMenu(publicKey, privateKey):

    choice = ''    

    while choice != '5':
        print('As the owner of the keys, what would you like to do?')
        print('1. Decrypt a received message')
        print('2. Digitally sign a message')
        print('3. Show the keys')
        print('4. Generating a new set of the keys')
        print('5. Exit') 
        choice = input('Enter your choice:')
   
        #if choice == '1':
            #message = input("Enter message to encrypt: ")
            #encrypted = encrypt(message, publicKey)
            #print("Encrypted message:", encrypted)
      
        if choice == '1':
            ciphertext = messages[promptList([f'Length {len(i)}' for i in messages], "Invalid selection")]
            decrypted = decrypt(ciphertext, privateKey)
            print(f"Decrypted Message: {decrypted}")
            #encrypted = input("Enter ciphertext to decrypt: ")
            #decrypted = decrypt(encrypted, privateKey)
            #print("Decrypted message:", decrypted)
      
        elif choice == '2':
            message = input("Enter message to sign: ")
            signature = generateSignature(message, privateKey)
            signatures.append(signature)
            print("Signature:", signature)
      
        elif choice == '3':
            (public, ring) = publicKey
            (private, ring) = privateKey
            print(f"Public Key: {public}")
            print(f"Private Key: {private}")
            #message = input("Enter message: ")
            #signature = input("Enter signature: ")
            #result = verifySignature(message, signature, publicKey)
            #print("Signature valid:", result)
      
        elif choice == '4':
            (public_key, private_key) = generateKeys()
    
        else:
            print('Invalid choice')

def publicUserMenu(publicKey):
    while True:
        print('As a public user, what would you like to do?')
        print('1. Send an encrypted message')
        print('2. Authenticate a digital signature')
        print('3. Exit')
        choice = input('Enter your choice:')

        if choice == '1':
            message = input('Enter a message: ')
            encrypted = encrypt(message, publicKey)
            messages.append(encrypted)
        elif choice == '2':
            if len(signatures) <= 0:
                print('There are no signatures to authenticate.') 
            else:
                (message, signature) = signatures[promptList([ sign for (sign, encodded) in signatures])]
                result = verifySignature(message, signature, publicKey)
                print("Signature valid:", result)
        elif choice == '3':
            break
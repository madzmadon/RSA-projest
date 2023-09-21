from rsa_keys import *
messages = []
signatures = []

class RSA_Keys:
    def __init__(self, public, private, ring):
        self.public = public
        self.private = private
        self.ring = ring
    def getPublicKey(self):
        return self.public
    def getPrivateKey(self):
        return self.private
    def getRing(self):
        return self.ring
    def setPublicKey(self, public):
        self.public = public
    def setPrivateKey(self, private):
        self.private = private
    def setRing(self, ring):
        self.ring = ring

def promptList(options, message = 'Invalid selection'):
    '''Display a list of options for the user to choose from'''
    count = 1
    choice = 0
    while choice <= 0 or choice > len(options):
        count = 1
        for i in options:
            print(f'{count}. {i}')
            count += 1
<<<<<<< Updated upstream
        try:
            choice = int(input("> "))
        except:
            print("Input must be a valid number")
        if choice <= 0 or choice > len(options):
            print(message)
    return (choice - 1)

def privateUserMenu(keys):

=======
        choice = int(input('Enter your choice: '))
        if choice > 0 or choice < len(options):
            print(message)
    return (choice - 1)

def privateUserMenu(publicKey, privateKey):
    '''Display a menu for an owner of the keys with functionality attached'''
>>>>>>> Stashed changes
    choice = ''    

    while True:
        print('\nAs the owner of the keys, what would you like to do?')
        print('1. Decrypt a received message')
        print('2. Digitally sign a message')
        print('3. Show the keys')
        print('4. Generating a new set of the keys')
        print('5. Exit') 
<<<<<<< Updated upstream
        choice = input('Enter your choice:')
=======
        choice = input('Enter your choice: ')
>>>>>>> Stashed changes
      
        #Decrypt a received message
        if choice == '1':
<<<<<<< Updated upstream
            if len(messages) <= 0:
                print("There are no messages.")
            else:
                ciphertext = messages[promptList([f'Length {len(i)}' for i in messages], "Invalid selection")]
                decrypted = decrypt(ciphertext, keys.getPrivateKey(), keys.getRing())
                print(f"Decrypted Message: {decrypted}")
=======
            ciphertext = messages[promptList([f'(length = {len(i)})' for i in messages], 'Invalid selection')]
            decrypted = decrypt(ciphertext, privateKey)
            print(f'Decrypted Message: {decrypted}')
>>>>>>> Stashed changes
      
        #Digitally sign a message
        elif choice == '2':
<<<<<<< Updated upstream
            message = input("Enter message to sign: ")
            signature = generateSignature(message, keys.getPrivateKey(), keys.getRing())
=======
            message = input('Enter message to sign: ')
            signature = generateSignature(message, privateKey)
>>>>>>> Stashed changes
            signatures.append(signature)
            print('Signature:', signature)
            print('Message signed and sent.')

        #Show the keys
        elif choice == '3':
<<<<<<< Updated upstream
            print(f"Public Key: {keys.getPublicKey()}")
            print(f"Private Key: {keys.getPrivateKey()}")
=======
            (public, ring) = publicKey
            (private, ring) = privateKey
            print(f'Public Key: {public}')
            print(f'Private Key: {private}')
>>>>>>> Stashed changes
      
        #Generating a new set of the keys
        elif choice == '4':
<<<<<<< Updated upstream
            public_key, private_key, ring = generateKeys()
            keys.setPublicKey(public_key)
            keys.setPrivateKey(private_key)
            keys.setRing(ring)
        else:
            print('Invalid choice')

def publicUserMenu(keys):
    choice = ''
    while choice != '3':
        print('As a public user, what would you like to do?')
=======
            (public_key, private_key) = generateKeys()
            print('Your new keys have been generated.')
    
        #Exit
        elif choice == '5':
            break

        #Error handling for invalid choice
        else:
            print('Invalid choice')

def publicUserMenu(publicKey):
    '''Display a menu for a public user with the functionality attached'''
    while True:
        print('\nAs a public user, what would you like to do?')
>>>>>>> Stashed changes
        print('1. Send an encrypted message')
        print('2. Authenticate a digital signature')
        print('3. Exit')
        choice = input('Enter your choice:')

        #Send an encrypted message
        if choice == '1':
            message = input('Enter a message: ')
            encrypted = encrypt(message, keys.getPublicKey(), keys.getRing())
            messages.append(encrypted)
            print('Messages encrypted and sent.')

        #Authenticate a digital signature
        elif choice == '2':
            if len(signatures) <= 0:
                print('There are no signatures to authenticate.') 
            else:
                (message, signature) = signatures[promptList([ sign for (sign, encodded) in signatures])]
<<<<<<< Updated upstream
                result = verifySignature(message, signature, keys.getPublicKey(), keys.getRing())
                print("Signature valid:", result)
=======
                result = verifySignature(message, signature, publicKey)
                print('Signature valid:', result)
        #Exit
        elif choice == '3':
            break

        else:
            print('Invalid choice')
>>>>>>> Stashed changes

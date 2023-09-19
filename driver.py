from rsa_keys import *
from rsa_ui import *

print('RSA Program')
print('Please wait while we generate keys...')

# Generate keys
publicKey, privateKey = generateKeys()

while True:
    print('Please select your user type: ')
    print('1. A public user') 
    print('2. The owner of the keys')
    print('3. Exit program')
    choice = input('Enter your choice:')

    if choice == '1':
        publicUserMenu(publicKey, privateKey)
    elif choice == '2':
        privateUserMenu(publicKey, privateKey)
    elif choice == '3':
        break
    else:
        print('Invalid input')

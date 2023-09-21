from rsa_keys import *
from rsa_ui import *

print('RSA Program')

# Generate keys
publicKey, privateKey, ring = generateKeys()
keys = RSA_Keys(publicKey, privateKey, ring)

# Run the main menu option selection.
while True:
    print('Please select your user type: ')
    print('1. A public user') 
    print('2. The owner of the keys')
    print('3. Exit program')
    choice = input('Enter your choice:')

    # Determine the option that the user selected.
    if choice == '1':
        publicUserMenu(keys)
    elif choice == '2':
        privateUserMenu(keys)
    elif choice == '3':
        break
    else:
        print('Invalid input')

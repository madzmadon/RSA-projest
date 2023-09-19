'''
    This file contains the utility functions to encrypt/decrypt messages and 
    signatures using the RSA system.
'''
    
import random as rand

def generateKeys():
  '''RSA key generation algorithm. Source: lecture notes slide '''
  # Declare variables.
  prime1 = generatePrimeNumber(1000000, 10000000, 100000)
  prime2 = generatePrimeNumber(1000000, 10000000, 100000)
  n = prime1 * prime2
  phi = (prime1 - 1) * (prime2 - 1)
  public_key = rand.randint(2, phi)
  private_Key = 2
  
  # Generate the public key.
  while gcd(public_key, phi)[2] != 1:
    public_key = rand.randint(2, phi)
  
  # Obtain the private key.
  private_key = gcd(public_key, phi)[0] % phi
  
  return ((public_key, n), (private_key, n))

def encrypt(msg, public_key):
    
  '''RSA encryption equation. Source: lecture notes slide '''
  # Declare variables.
  ciphertext = ''
  key, n = public_key
  
  #Iterate over ever character within the parameter 'msg'.
  for c in msg:
    ciphertext += chr(pow(ord(c), key, n))

  return ciphertext

def decrypt(ciphertext, private_key):
  '''RSA decryption equation.'''
  return encrypt(ciphertext, private_key)

def generateSignature(message, private_key):
  '''Encrypt the message into a signature for owner verification.'''
  return (message, encrypt(message, private_key))

def verifySignature(message, signature, public_key):
  '''Decrypt a signature for owner verification.'''
  return bool(message == decrypt(signature, public_key))

def isPrime(num):
  '''Determines if a number is prime. Source: lecture notes slide 60'''
  for i in range(1, num):
    if (pow(i, (num - 1), num) > 1):
      return False
  return True

def generatePseudoPrime(min, max, k):
  '''Generates a pseudo prime number. Source: lecture notes slide 65'''
  p = rand.randint(min, max)
  is_prime = False
  while not is_prime:
    for i in range(k):
      j = rand.randint(2, p)
      if (pow(j, (p - 1), p) == 1):
        is_prime = True
        break
      else:
        p = rand.randint(min, max)
  return p

def generatePrimeNumber(min, max, k=10000):
  '''Generates a random prime number.'''
  num = generatePseudoPrime(min, max, k)
  while not isPrime(num):
    num = generatePseudoPrime(min, max, k)
  return num

def gcd(a, b):
  '''Finds the gcd of two numbers. Source: lecture notes slide 36'''
  if b == 0:
    return (1, 0, a)
  (x, y, d) = gcd(b, a%b)
  return (y, (x - a//b * y), d)

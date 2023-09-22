'''
  This file contains the utility functions to encrypt/decrypt messages and 
  signatures using the RSA system.
'''
    
import random as rand
import math

def generateKeys():
  '''RSA key generation algorithm. Source: lecture notes slide 22-24.'''
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
  
  return (public_key, private_key, n)

# TODO: Add the prime number validation function.
def is_prime(num):
    '''Verify that a number is prime. Source: lecture notes slide 59.'''
    if num == 2:
        return True
    for b in range(2, math.floor(math.sqrt(num)) + 1):
        if gcd(num, b)[2] > 1:
            return False
    return True

def encrypt(ciphertext, key, n):
    
  '''RSA encryption equation. Source: Lecture notes slide 23.'''
  # Declare variables.
  output = []
  
  #Iterate over ever character within the parameter 'msg'.
  for c in ciphertext:
    output.append(pow(ord(c), key, n))

  return output

def decrypt(ciphertext, key, n):
  '''RSA decryption equation.'''
  # Declare variables.
  msg = ''

  # Iterate over the elements of the parameter 'ciphertext'.
  for i in ciphertext:
     msg += chr(pow(i, key, n))
     
  return msg

def generateSignature(message, private_key, n):
  '''Encrypt the message into a signature for owner verification.'''
  return (message, encrypt(message, private_key, n))

def verifySignature(message, signature, public_key, n):
  '''Decrypt a signature for owner verification.'''
  return bool(message == decrypt(signature, public_key, n))

def generatePseudoPrime(min, max, k):
  '''Generates a pseudo prime number. Source: lecture notes slide 65.'''
  prime = rand.randint(min, max)
  is_prime = False
  while not is_prime:
      prime = rand.randint(min, max)
      is_prime = True
      for i in range(k):
          if pow(i, (prime - 1), prime) > 1:
              is_prime = False
              break
  return prime

def generatePrimeNumber(min, max, k=10000):
  '''Generates a random prime number.'''
  prime = generatePseudoPrime(min, max, k)
  while not is_prime(prime):
      prime = generatePseudoPrime(min, max, k)
  return prime

def gcd(a, b):
  '''Finds the gcd of two numbers. Source: lecture notes slide 36.'''
  if b == 0:
    return (1, 0, a)
  (x, y, d) = gcd(b, a%b)
  return (y, (x - a//b * y), d)

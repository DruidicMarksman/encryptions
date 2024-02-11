import math, random


def getRandomPrime(minimum=0,maximum=100):
    # create prime number generator
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            
        return True

    # initialising primes

    cached_primes = [i for i in range(minimum,maximum) if isPrime(i)]

    return random.choice(cached_primes)

secret_number=getRandomPrime(0,1000)

# Get message, then convert it to numbers
def encrypt(string):
    """ Encrypts STRING into effectively random numbers""" 
    # the next 3 or so lines i don't really understand
    # i got them from nerds on google
    msg_unencrypted = string # msg is for the encrypted version
    mybytes = msg_unencrypted.encode('utf-8') + b'\x01'  # Pad with 1 to preserve trailing zeroes
    msg = int.from_bytes(mybytes, 'little')*math.pi
    encrypted = [msg,secret_number]
    return encrypted
def decrypt(encrypted_message_as_list):
    """ Decrypts the ENCRYPTED_MESSAGE from effectively random numbers to actual text"""
    encrypted_message = encrypted_message_as_list[0]/math.pi
    secret_number = encrypted_message_as_list[1]
    real_message = int(encrypted_message/secret_number)
    recoveredbytes = real_message.to_bytes((encrypted_message.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes[:-1].decode('utf-8') # Strip pad before decoding
    print(recoveredstring)



# This section doesn't work too well, so I commented it out. It was SUPPOSED to be an ACTUAL "RSA Algorithm", but the results were dissapointing. 

### step 1
##p = random.choice([i for i in cached_primes_P if minPrime<i<maxPrime])
##
##q = random.choice([i for i in cached_primes_Q if minPrime<i<maxPrime])
##
##
##
### step 2
##n = p*q
##print("n =", n)
## 
### step 3
##phi = (p-1)*(q-1)
## 
### step 4
##e = 2
##while(e<phi):
##    if (math.gcd(e, phi) == 1):
##        break
##    else:
##        e += 1
## 
##print("e =", e)
### step 5
##k = 2
##d = ((k*phi)+1)/e
##print("d =", d)
##print(f'Public key: {e, n}')
##print(f'Private key: {d, n}')
## 
### plain text
##print(f'Original message:{msg}')
## 
### encryption
##C = pow(msg, e)
##C = math.fmod(C, n)
##print(f'Encrypted message: {C}')
## 
### decryption
##M = pow(C, d)
##M = math.fmod(M, n)

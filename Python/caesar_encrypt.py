def encrypt(plain_text,inc):
    caesar_text =""
    global lowercase
    global uppercase
    for letter in plain_text:
        if letter in uppercase:
            index = uppercase.index(letter)
            crypt = (index + inc )%26
            new_letter = uppercase[crypt]
            caesar_text+=new_letter   
        else:
            index = lowercase.index(letter)
            crypt = (index + inc)%26
            new_letter = lowercase[crypt]
            caesar_text+=new_letter
    return caesar_text

def decrypt(caesar_text,dec):
    plain_text =""
    global lowercase
    global uppercase
    for letter in caesar_text:
        if letter in uppercase:
            index = uppercase.index(letter)
            crypt = (index - dec )%26
            new_letter = uppercase[crypt]
            plain_text +=new_letter
        else:
            index = lowercase.index(letter)
            crypt = (index - dec)%26
            new_letter = lowercase[crypt]
            plain_text +=new_letter
    return plain_text

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
plain_text = str(input("Enter Plain Text: "))
inc = int(input("Enter inc: "))
code = encrypt(plain_text, inc)

print(code)
ch = str(input("Do you want to decrypt it: "))
if ch=="yes" or ch=="y":
    pt = decrypt(code,inc)
    for j in pt:
        print(j,end="")
print()

# from pycipher import Caesar 
# a = str(input("Enter Text: "))
# en = Caesar(key=1).encipher(a)
# print("Encrypt: ",en)
# print("Decrypt: ",Caesar(key=1).decipher(en))
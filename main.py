alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():
    plain_text = input("Enter the plain text: ")
    shift = int(input("Enter the number of places to shift: "))
    encrypt_text = ""
    for char in plain_text:
        if char in alphabets:
            pos = alphabets.index(char)
            new_pos = (pos + shift)%26
            encrypt_text += alphabets[new_pos]
        else:
            encrypt_text += char
    print("The encrypted text is:\n" + encrypt_text)

def decrypt():
    encrypted_text = input("Enter the encrypted text: ")
    shift = int(input("Enter the number of places to shift: "))
    decrypt_text = ""
    for char in encrypted_text:
        if char in alphabets:   
            pos = alphabets.index(char)
            new_pos = (pos - shift)%26
            decrypt_text += alphabets[new_pos]
        else:
            decrypt_text += char
    print("The decrypted text is:\n" + decrypt_text)

while True:
    userin = int(input("Please choose:\n1.Encrypt\n2.Decrypt\n"))
    if(userin == 1):
        encrypt()
    elif(userin == 2):
        decrypt()
    else:
        print("Please choose a valid option")
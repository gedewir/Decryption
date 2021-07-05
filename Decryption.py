def decrypt(rot_key, text):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            char_num = ord(char)
            print(char_num)
            if char_num >= 65 and char_num <= 90:
                if (char_num-rot_key) < 65:
                    x = (char_num-rot_key) - 65
                    print('x:',x)
                    decrypted_text += decrypted_text.join(chr(x+ord('Z')+1))
                else:
                    decrypted_text += decrypted_text.join(chr(char_num-rot_key))
            elif char_num >= 97 and char_num <= 122:
                if (char_num-rot_key) < 97:
                    x = (char_num-rot_key) - 97
                    print('x: ',x)
                    decrypted_text += decrypted_text.join(chr(x + ord('z')+1))
                else:
                    decrypted_text += decrypted_text.join(chr(char_num-rot_key))
        else:
            decrypted_text += decrypted_text.join(char)
    for x in decrypted_text:
        print('this is end: ',ord(x))
    return decrypted_text

nameFile = input("Enter the text file you want to decrypt (include .txt): ")

with open(nameFile, 'r') as file:
    text = file.read()

print(text)

while True:
    numKey = int(input("Enter the encryption key number between 0 and 25: "))
    if numKey < 0 or numKey > 25:
        print('Please enter a encryption key between 0 and 25')
    else:
        break

decrypted_message = decrypt(numKey, text)

print('writing the decrypted text to file: ', decrypted_message)

with open('DecryptedFile.txt', 'w+') as decryptFile:
    decryptFile.write(decrypted_message)

nameFile = input("Enter the text file you want to decrypt (include .txt): ")

with open(nameFile, 'r') as file:
    text = file.read()

print(text)

numKey = input("Enter the encryption key number between 0 and 25: ")

def decrypt(rot_key):
    
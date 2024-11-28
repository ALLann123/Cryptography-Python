#!/usr/bin/python3
#1)Read key from file
key=''
with open('myTopSecretKey.key', 'rb') as file:
	key = file.read()
#2) Read Data from file
files=['friends.mkv']
for file_path in files:
	data=''
	with open(file_path, 'rb') as file:
		data = file.read()
	#3) Encrypt Data
	from cryptography.fernet import Fernet
	#create an object from fernet class
	f=Fernet(key)

	encryptedData=f.encrypt(data)

	#4) Save encrypted data into a file
	with open(file_path, 'wb') as file:
		file.write(encryptedData)

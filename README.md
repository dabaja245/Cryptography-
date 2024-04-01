AES Cryptography Script

This Python script allows users to encrypt and decrypt files using the AES encryption algorithm. It leverages the cryptography library for encryption and decryption and integrates with Azure Key Vault for secure key storage.

Installation
Before using the script, ensure you have Python installed on your system. You can download Python from the official website.
Next, install the required dependencies using pip: install cryptography azure-identity

you will be prompted to choose whether you want to encrypt or decrypt a file. Enter 1 to encrypt a file or 2 to decrypt a file.
Depending on your choice, follow the prompts to provide the necessary information:
For encryption:
Enter the filename of the file you want to encrypt.
For decryption:
Enter the filename of the encrypted file.
Enter the encryption key used for encryption.
Once the process is complete, the script will output the result or any error messages encountered.

Example
To encrypt a file named example.txt, run the script and choose option 1 when prompted. Enter example.txt as the filename, and the script will encrypt the file and save the encrypted version as example.txt.encrypted.
To decrypt the encrypted file example.txt.encrypted, run the script and choose option 2 when prompted. Enter example.txt.encrypted as the filename and the encryption key used for encryption.

Notes
Ensure you remember the encryption key used for encryption as it will be required for decryption.
This script integrates with Azure Key Vault for secure key storage. Ensure you have appropriate permissions and configurations set up for Azure Key Vault access.


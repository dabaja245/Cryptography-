import os
from cryptography.fernet import Fernet
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def user_choice():
    while True:
        try:
            choice = int(input("Welcome to AES cryptography. Enter 1 to encrypt a file or enter 2 to decrypt a file: "))
            if choice == 1:
                get_file()
            elif choice == 2:
                decrypt_file()
            else:
                print("Please choose between 1 and 2!")
        except ValueError:
            print("Please enter a valid number (1 or 2)!")


#reads in file 
            

def get_file():
    filename = input("\nPlease enter the filename to encrypt: ")
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            encrypted_content, encryption_key = AES_encryption(content)
            encrypted_filename = filename + ".encrypted"
            with open(encrypted_filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)
            print(f"\nEncrypted file saved as: {encrypted_filename}")
            azure_key_vault(filename, encryption_key.decode())  # Call Azure Key Vault function here

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("No permission to access file.")
    except Exception as e:
        print(f"Error: {e}")


def AES_encryption(data):
    key = Fernet.generate_key() #generates encryption key 
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data, key


def decrypt_file():
    filename = input("Enter the filename to decrypt: ")
    encryption_key = input("Enter the encryption key: ")
    if not validate_key(encryption_key):
        print("Invalid key format.")
        return
    try:
        with open(filename, 'rb') as file:
            encrypted_content = file.read()
            decrypted_content = AES_decryption(encrypted_content, encryption_key)
            if decrypted_content:
                decrypted_filename = os.path.splitext(filename)[0]
                with open(decrypted_filename, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_content)
                print(f"\nDecryption successful. Decrypted file: {decrypted_filename}")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("No permission to access file.")
    except Exception as e:
        print(f"Error: {e}")


def AES_decryption(encrypted_data, key):
    try:
        f = Fernet(key.encode())
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data
    except Exception as e:
        print(f"Decryption error: {e}")
        return None


def validate_key(key):
    try:
        Fernet(key.encode())  # This validates the key
        return True
    except:
        return False


def azure_key_vault(filename, key):
    keyVaultName = "AES-keys"
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    # Modify filename to ensure it adheres to Azure Key Vault naming conventions
    # For example, replace '.' with '-'
    secretName = filename.replace('.', '-')
    secretValue = key

    print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

    client.set_secret(secretName, secretValue)

    print(" done.")

    print(f"Retrieving your secret from {keyVaultName}.")

    retrieved_secret = client.get_secret(secretName)

    print(f"Your secret is '{retrieved_secret.value}'.")


    print(" done.")


user_choice()

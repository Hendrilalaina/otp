from cryptography.fernet import Fernet
import os
import json

class PasswordManager:
    def __init__(self):
        self.key = self.load_key()
        self.accounts = self.load_accounts()

    def load_key(self):
        key_file = "key.key"
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key
    
    def load_accounts(self):
        accounts_file = 'accounts.json'
        if os.path.exists(accounts_file):
            with open(accounts_file, 'rb') as f:
                cipher_suit = Fernet(self.key)
                encrypted_data = f.read()
                decrypted_data = cipher_suit.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        else:
            return {}
    
    def save_accounts(self):
        accounts_file = 'accounts.json'
        with open(accounts_file, 'wb') as f:
            cipher_suit = Fernet(self.key)
            data = json.dumps(self.accounts).encode()
            encrypted_data = cipher_suit.encrypt(data)
            f.write(encrypted_data)

    def add_account(self, account_name, username, password):
        self.accounts[account_name] = {
            'username': username,
            'password': password
        }
        self.save_accounts()
        print(f"Account {account_name} added successfully!")
    
    def get_password(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name]['password']
        else:
            return "Account not found!"

password_manager = PasswordManager()
# account_name = input("Please enter your account name: ")
# username = input("Enter your user name: ")
# password = input("Enter your password: ")
# password_manager.add_account(account_name, username, password)
password = password_manager.get_password(input("Please enter your account name: "))
print(f"Your password is {password}")
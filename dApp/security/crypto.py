from cryptography.fernet import Fernet

class SecurityEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.encryption_key = Fernet.generate_key()

    def encrypt_data(self, data):
        fernet = Fernet(self.encryption_key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def verify_api_access(self, provided_key):
        return self.api_key == provided_key

import pickle
from hashlib import sha256

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = sha256(password.encode()).hexdigest()

    def authenticate(self, password):
        return self.password == sha256(password.encode()).hexdigest()

    @staticmethod
    def save_user(user):
        try:
            with open('users.pkl', 'ab') as f:
                pickle.dump(user, f)
        except FileNotFoundError:
            with open('users.pkl', 'wb') as f:
                pickle.dump(user, f)

    @staticmethod
    def load_users():
        users = []
        try:
            with open('users.pkl', 'rb') as f:
                while True:
                    try:
                        users.append(pickle.load(f))
                    except EOFError:
                        break
        except FileNotFoundError:
            pass
        return users
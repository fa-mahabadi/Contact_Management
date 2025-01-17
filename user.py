import pickle

class User:
    accounts = {}

    @classmethod
    def save_users(cls):
        '''save users in pickle file '''
        with open("data/users.pkl", "wb") as f:
            pickle.dump(cls.accounts, f)

    @classmethod
    def load_users(cls):
        '''load users from file '''
        try:
            with open("data/users.pkl", "rb") as f:
                cls.accounts = pickle.load(f)
        except FileNotFoundError:
            cls.accounts={}

    @classmethod
    def create_account(cls, username, password):
        '''create account'''
        cls.accounts[username] = password
        cls.save_users()

    @classmethod
    def authentication(cls, username, password):
        '''authenticate user '''
        cls.load_users()
        if username in cls.accounts and cls.accounts[username] == password:
            return True
        else:
            return False

    @classmethod
    def modify_account(cls,username, new_password):
        '''modify account user '''
        if username in cls.accounts:
            cls.accounts[username] = new_password
            cls.save_users()

    

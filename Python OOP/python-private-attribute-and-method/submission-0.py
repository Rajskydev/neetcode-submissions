class PasswordManager:
    def __init__(self, password):
        self._password = password
    
    def verify_password(self, pwd: str) -> bool:
        if pwd == self._password:
            return True
        else:
            return False
    




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False

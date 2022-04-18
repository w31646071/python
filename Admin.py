class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"mr/miss.{self.first_name}，how are you")

    def increment_login_attempts(self, number):
        self.login_attempts = number + 1
        print(f"={self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'={self.login_attempts}')
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

    def read_served(self):
        print(f"有{self.number_served}人在这里就餐")

    def set_number_server(self, number):
        self.number_served = number

    def increment_number_server(self, number):
        self.number_served += number
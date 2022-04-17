class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 此处给属性指定了默认值

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    '''def update_odometer(self, mileage):
        """将里程表读书设置为指定的值"""
        self.odometer_reading = mileage
        """将里程表读数设置为指定的值，禁止将里程表读书往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer!")
    # 此处新加入一个方法，该方法可以修改属性的值，无须直接访问属性，直接将值传递给方法，在类内部更新'''

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        # 此处新增了一个方法，可以向方法传递一个增量，并相应的增加


my_car = Car('audi', 'RS7', '2022')
print(my_car.get_descriptive_name())
"""my_car.odometer_reading = 23  # 此处通过实例直接访问属性odometer_reading并将其值修改为23"""
"""my_car.update_odometer(23)"""
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()

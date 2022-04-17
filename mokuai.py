# 在main文件外创建一个函数模块库

def make_pizza(size,*toppings):
    print(f"\nmakeing {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
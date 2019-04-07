import make_pizza as p

print("---------------------------------------------")


def greet_user():
    print("hello")


greet_user()

print("---------------------------------------------")


def greet_user1(username):
    print("Hello: " + username.title())


greet_user1("yuan")
print("---------------------------------------------")


def hello(first_name, last_name):
    print("Hello:" + first_name.title() + last_name.title())


hello(first_name="yuan", last_name="tuo")
print("---------------------------------------------")


def hello(first_name, last_name="xxx"):
    print("Hello:" + first_name.title() + last_name.title())


hello(first_name="yuan")

print("---------------------------------------------")


def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


my_name = get_full_name("yuan", "tuo")
print(my_name)

print("---------------------------------------------")


def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = "test"
    else:
        full_name = first_name.title() + " " + last_name.title()
    return full_name


my_name = get_full_name("yuan", "tuo", "xx")
print(my_name)

print("---------------------------------------------")


def get_name(first, last):
    return {"first": first, "last": last.title()}


person = get_name("yuan", "tuo")
print(person)

print("---------------------------------------------")


# while True:
#     first_name = input("Please input your first name!")
#     last_name = input("Please input your last name!")
#     full_name = get_full_name(first_name, last_name)
#     print(full_name)

def greet_user(names):
    for names in names:
        print("Hello " + names.title())


name = ["yuan", "tuo", "han"]
greet_user(name)


def print_models(unprinted_designs, completed_designs):
    """
    模拟打印每个设计
    :param unprinted_designs:
    :param completed_designs:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:" + current_design)
        completed_designs.append(current_design)


my_unprinted_designs = ["case1", "case2", "case3"]
my_completed_designs = []
print_models(my_unprinted_designs[:], my_completed_designs)

print(my_completed_designs)
print(my_unprinted_designs)

print("------------------------------------------")


def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('mushrooms', 'green peppers', 'extra cheese', "test")

print("------------------------------------------")


def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first.title()
    profile["last_name"] = last.title()

    for key, val in user_info.items():
        profile[key] = val
    return profile


my_profile = build_profile("yuan", "tuo", location="石窝", sex="男")
print(my_profile)
print("------------------------------------------")
p.make_pizza_again(12, "test1", "test2")
print("------------------------------------------")

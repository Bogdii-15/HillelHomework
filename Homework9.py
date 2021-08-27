# №1

def reverse_list(some_list: list) -> list:
    result = []
    for index in range(len(some_list)):
        if index % 2:
            result.append(some_list[index][::-1])
        else:
            result.append(some_list[index])
    return result


my_fruits = ['Apple', 'Banana', 'Orange', 'Strawberry']


###########################################
# №2


def create_startswith(some_list: list) -> list:
    result_list = [word for word in some_list if word.lower().startswith('a')]
    return result_list


my_startswith_list = ["Apple", 'Plane', 'Home', 'Automation']


###########################################
# №3

def new_list(my_list) -> list:
    names = [name for name in my_list if name.lower().count('a')]
    return names


my_list = ["Apple", 'Plane', 'Home', 'Automation']


###############################################
# №4

def create_str(some_list: list):
    result_list = [element for element in some_list if isinstance(element, str)]
    return result_list

my_list = ["Apple", 1, 3, 4, 'Plane', 'Home', 'Automation', 3, 4, 5]


#################################################
#№5

def create_list_symbol(some_str: str) -> list:
    my_list = [letter for letter in set(some_str) if my_str.count(letter) == 1]
    return my_list

my_str = '12132345654167899'

################################################
#№6

def create_list_2str(some_str_1: str, some_str_2: str) -> list:
    result_list = list(set(some_str_1) & set(some_str_2))
    return result_list

my_str1 = '123456'
my_str2 = '123789'


############################################
#№7

def create_list_2_str(str_1: str, str_2: str) -> list:
    result_list = [char for char in set(str_2) if str_1.count(char) == str_2.count(char) == 1]
    return result_list

my_str1 = 'country87'
my_str2 = 'country456'

#############################################
#№8

from random import choice
from random import randint
from string import ascii_lowercase


def create_email(names_list: list, domains_list: list) -> str:
    name = choice(names_list)
    domain = choice(domains_list)
    name_after_dog = ''

    for _ in range(randint(4, 6)):
        name_after_dog += choice(ascii_lowercase)

    res = name + '.' + str(randint(100, 999)) + '@' + name_after_dog + '.' + domain

    return res


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(names, domains)

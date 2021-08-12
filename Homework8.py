# №1

my_list = ['Apple', 'Banana', 'Orange', 'Fruits', '1234']
result = []
for index in range(len(my_list)):
    if index % 2:
        result.append(my_list[index][::-1])
    else:
        result.append(my_list[index])

############################################################
# №2

my_list = ["Apple", 'Plane', 'Home', 'Automation']
result = []
for word in my_list:
    if word.lower().startswith('a'):
        result.append(word)

#########################################################
# №3

my_list = ["Apple", 'Plane', 'Home', 'Automation']
names = []
for name in my_list:
    if name.lower().count('a'):
        names.append(name)

######################################################
# №4

my_list = ["Apple", 1, 3, 4, 'Plane', 'Home', 'Automation', 3, 4, 5]
result = []
for element in my_list:
    if isinstance(element, str):
        result.append(element)

######################################################
# №5

my_str = '12132345654167899'
my_set = set(my_str)
my_list = []
for letter in my_set:
    if my_str.count(letter) == 1:
        my_list.append(letter)

####################################################
# №6

my_str1 = '123456'
my_str2 = '123789'

result_list = list(set(my_str1) & set(my_str2))

###################################################
# №7
my_str1 = 'country87'
my_str2 = 'country456'
result_list = list()
for char in set(my_str2):
    if my_str1.count(char) == my_str2.count(char) == 1:
        result_list.append(char)

####################################################
# №8

residence_dict = {'Страна': 'Украина',
                  'Город': 'Киев',
                  'Улица': 'Победы'}

work_dict = {'Наличие': "Трудоустроен",
             'Должность': "QA Manual"}

my_dict = {'Фамилия': 'Иванов',
           'Имя': 'Василий',
           'Возраст': '21',
           'Проживание': residence_dict,
           'Работа': work_dict}

####################################################
# №9
cake_dict = {'Мука': '300 грамм',
             'Молоко': "200 мл",
             'Масло': "100 грамм",
             'Яйцо': "2 штуки"}

cream_dict = {'Сахар': "50 грамм",
              'Масло': "45 млгр",
              'Ваниль': "20 грамм",
              'Сметана': "60 милиграмм"}

glaze_dict = {'Какао': "2 чайные ложки",
              'Сахар': "100 грамм",
              'Масло': "50 грамм"}

ingredients_dict = {'Коржи': cake_dict,
                    'Крем': cream_dict,
                    'Глазурь': glaze_dict}

########################################################
#№10

persons = [{"name": "John", "age": 22},
           {"name": "Jack", "age": 13},
           {"name": "Alex", "age": 30},
           {"name": "Andrew", "age": 13}]

#a)
age = []
for person in persons:
    age.append(person["age"])

min_age = min(age)
for person in persons:
    if person["age"] == min_age:
        print(person["name"])

#b)
max_len_name = []
for human in persons:
    max_len_name.append(human["name"])

max_len = max(max_len_name, key=len)
print(max_len)

#в)
average_age = 0

for human in persons:
    average_age += human.get('age')

average_age /= len(persons)
print(average_age)

###################################
#№11

my_dict1 = {'Key1': 'Value1',
             'Key2': 'Value2',
             'Key3': 'Value3'}

my_dict2 = {'Key1': 555,
             'Key4': 'Value4',
             'Key5': 'Value5'}

# а)
result_list1 = list(set(list(my_dict1.keys()) + list(my_dict2.keys())))


# б)
result_list2 = list(set(my_dict1.keys()) - set(my_dict2.keys()))

# в)
result_dict = dict()

for value in result_list2:
    result_dict[value] = my_dict1.get(value)

# г)

new_dict = dict()

for key in result_list1:
    if key in my_dict1 and key in my_dict2:
        new_dict[key] = [my_dict1.get(key), my_dict2.get(key)]
    elif key in my_dict1:
        new_dict[key] = my_dict1.get(key)
    else:
        new_dict[key] = my_dict2.get(key)

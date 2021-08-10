#№1
#value = 1020304050
#result = str(value).count('0')


#############################################
#№2
#value = 1233456000
#result = len(str(value)) - len(str(int(str(value)[::-1])))

##############################################
#3
#my_list1 = ['Я', 'самолет', 'хочу', 'привет', 'летать']
#my_list2 = ['огурец', 'в', 'вертолет', 'облаках']

#my_result = my_list1[::2] + my_list2[1::2]

#############################################
#№4
#my_list = [11, 23, 5, 8, 13, 17]
#new_list = my_list
#new_list.pop(0)
#new_list.append(11)


###############################################
#№5
#my_list = [11, 23, 5, 8, 13, 17]
#my_list.pop(0)
#my_list.append(11)


###############################################
#№6
#my_str = "25 больше чем 20 но меньше чем 30"
#words = my_str.split(' ')
#product = 0
#for word in words:
#    try:
#        value = int(word)
#        product += value
#    except:
#        pass

##############################################
#№7
#my_str = "My best music"
#l_limit = "e"
#r_limit = "c"
#w1 = my_str.find(l_limit)
#w2 = my_str.rfind(r_limit)
#sub_str = my_str[w1+1 : w2]

###########################################
#№8
#my_str = '245678956'
#my_list = list()
#for index in range(0, len(my_str), 2):
#    if index < len(my_str) - 1:
#        my_list.append(my_str[index] + my_str[index + 1])
#    else:
#        my_list.append(my_str[index] + "_")


################################################
#№9
#my_list = [2, 5, 8, 2, 13, 5, 20]
#count = 0
#for digit in range(1, len(my_list)-1):
#    if int(my_list[digit-1]) < int(my_list[digit]) and int(my_list[digit]) > int(my_list[digit+1]):
#        count += 1


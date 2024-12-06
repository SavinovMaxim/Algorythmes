str = input()
list1 = []
flag = True

for i in str:
    if i in '([{':
        list1.append(i)
    elif i in ')]}':
        #Если длина строки равна нулю
        if len(list1) == 0:
            flag = False
            break
        list2 = list1.pop()
        if (list2 == '(' and i == ')') or (list2 == '[' and i == ']') or (list2 == '{' and i == '}'):
            continue
        #если скобки не соответствуют
        flag = False

if flag == True and len(list1) == 0:
    print('Всё верно')
else:
    print('Строка не существует')
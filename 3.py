def correct_digits(digit): #функция для поиска и вывода чисел
    list_with_correct_digits = []
    for K in range(digit): #степень цифры 3
        # Анулируем предполагаемое число, чтобы избежать раннего окончания программы
        desired_number = 0
        for L in range(digit): #степень цифры 5
            # Если в выражении L слишком велико
            if 3**K * 5**L > digit:
                break
            for M in range(digit): #степень цифры 7
                desired_number = 3**K * 5**L * 7**M
                # Если предполагаемое число в промежутке до "x", то число подходит, иначе M слишком великo
                if desired_number <= digit:
                    list_with_correct_digits.append(desired_number)
                else:
                    break
        # Если K слишком велико, то все варианты были подобраны
        if 3**K > digit:
            break
    # Отсортировываем полученные числа и исключаем все дубликаты
    print(sorted(set(list_with_correct_digits)))

correct_digits(10009000)

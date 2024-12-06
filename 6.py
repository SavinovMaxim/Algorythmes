def choice_sort(array):

    i = 0  # Индекс ячейки, с минимальным элементом

    while i < len(array) - 1:
        m = i  # индекс ячейки с минимальным значением, предполагаем, что в i содержится минимальный элемент
        j = i + 1  # начинаем поиск с ячейки i+1
        while j < len(array):  # пока не дойдем до конца списка
            if array[j] < array[m]:  # сравниваем ячейку j с ячейкой m
                m = j
            j += 1

        array[i], array[m] = array[m], array[i]  # в ячейку i записывается найденный минимум, а значение из прошлого i переносится на старое место
        i += 1  # переходим к следующей необработанной строке
    print(array)


choice_sort([4, 5, 2, 24, 23, 1, 12, 54, 34, 57, 13])
def shell_sort(array):
    n = len(array) #длина списка
    gap = n // 2 #интервал для сравнения элементов
    while gap > 0: #пока интервал больше 0
        for i in range(gap, n):
            temp = array[i] #сохраняет текущий элемент в переменную temp
            j = i
            while j >= gap and array[j - gap] > temp:  #пока j больше или равно gap и элемент, расположенный на расстоянии gap от текущего элемента, больше чем temp.
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp #вставляет текущий элемент на место j
        gap //= 2
    print(array)


shell_sort([4, 5, 2, 31, 8, 1, 12, 54, 34, 23, 42])

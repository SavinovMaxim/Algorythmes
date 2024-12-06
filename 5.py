def insertion_sort(array):
    n = len(array) 
    for i in range(1, n):
        x = array[i] #Сохраняет элемент списка [i] в переменную x. 
        j = i #индекс для сравнения с предыдущим элементом в цикле while.

        while j > 0 and array[j - 1] > x: #пока не достигнет начала списка и предыдущий элемент больше, чем текущий элемент x.
            array[j] = array[j - 1] #Перемещает предыдущий элемент на место текущего элемента.
            j -= 1 

        array[j] = x

    print(array)


insertion_sort([6, 23, 12, 53, 11, 56, 5, 3, 8, 14, 81, 33, 9, 1])
def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок
    r = 2 * i + 2  # Правый потомок
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): # Построение кучи из массива
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами корень и последний элемент
        heapify(arr, i, 0)  # Вызываем heapify для кучи, исключая последний элемент
arr = [4, 5, 2, 31, 8, 1, 12, 54, 34, 23, 42]
heap_sort(arr)
print(arr)

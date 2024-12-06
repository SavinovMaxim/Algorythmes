def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива

        # Разделяем массив на две половины
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # сортируем левую и правую половины
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Объединяем отсортированные половины
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr

print(merge_sort([4, 5, 2, 31, 8, 1, 12, 54, 34, 23, 42]))

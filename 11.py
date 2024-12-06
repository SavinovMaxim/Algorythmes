import random


def quicksort(nums):
    if len(nums) <= 1: # если список содержит 0 или 1 элемент, он уже отсортирован.
        return nums
    else:
        q = random.choice(nums) # Выбирает случайный элемент из списка в качестве опорного элемента
        s_nums = []  # Список для хранения элементов, меньших, чем опорный.
        m_nums = []  # Список для хранения элементов, больших, чем опорный.
        e_nums = []  # Список для хранения элементов, равных опорному.
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums) # Cортирует списки "меньше" и "больше" и объединяет их со списком "равно".
print(quicksort([1,3,12,56,13,2,6,17,15,9,4]))

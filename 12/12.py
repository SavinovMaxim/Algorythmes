import heapq
import os


def merge_files(output_file: str, temp_files: list[str], path: str) -> (None): 
    # Функция, выполняющая слияние отсортированных временных файлов в один выходной файл.
    # Для этого она
    # использует очередь с приоритетом (min-heap) для
    # эффективного извлечения минимальных элементов из
    # каждого временного файла и записи их в результирующий файл.
    heap_array = [] # Инициализация пустого списка для хранения кучи.
    temp_files = [open(temp_file, "r", encoding="utf-8") for temp_file in temp_files] # Открывает все временные файлы в режиме чтения.
    with open(output_file, "w") as output: # Открывает выходной файл в режиме записи.
        for i in range(len(temp_files)): # Цикл по всем временным файлам.
            element = temp_files[i].readline().strip() # Читает первую строку из каждого файла.
            if element: # Проверяет, есть ли данные в строке.
                heapq.heappush(heap_array, (int(element), i))

        counter = 0 # Счетчик для отслеживания кооличества обработанных файлов.
        while counter < len(temp_files):  # Цикл, пока не обработаны все файлы.
            root = heapq.heappop(heap_array)
            output.write(str(root[0]) + "\n")

            element = temp_files[root[1]].readline().strip() # Читает следующую строку из соответствующего файла.
            if element: # Проверяет, есть ли данные в строке.
                heapq.heappush(heap_array, (int(element), root[1])) # Добавляет новый элемент в кучу.
            else:
                counter += 1

        for temp_file in temp_files: # Закрывает все временные файлы.
            temp_file.close()


def create_initial_runs(input_file: str, run_size: str, path: str) -> list[str]: 
    # функция разбивает входной файл на
    # несколько временных файлов
    # (каждый из которых содержит
    # отсортированные данные).
    temp_files = [] # Инициализация пустого списка для хранения имен временных файлов.
    with open(input_file, "r", encoding="utf-8") as input: # Открывает входной файл в режиме чтения.
        end_of_file = False # Флаг, указывающий на конец файла.
        temp_files_counter = 0 # Счетчик для нумерации временных файлов.

        if not os.path.exists(path): # Проверяет существование директории.
            os.makedirs(path) # Создает директорию, если её нет.

        while True: # Пока мы не в конце файла.
            data = [] # Список для хранения данных текущего временного файла.
            for _ in range(run_size): # Пробегаемся по строкам.
                line = input.readline().strip()
                if not line: # Проверяет, достигнут ли конец файла.
                    end_of_file = True # Устанавливает флаг конца файла
                    break
                data.append(int(line)) # Преобразует строку в число и добавляет в список.
            data.sort()

            with open(path + r"\f_" + str(temp_files_counter) + ".txt", "w", encoding="utf-8") as output: # Открывает временный файл в режиме записи.
                temp_files.append(path + r"\f_" + str(temp_files_counter) + ".txt") # Добавляет имя временного файла в список.
                output.write("\n".join(str(i) for i in data)) # Записывает отсортированные данные в файл.

            temp_files_counter += 1 # Увеличивает счетчик временных файлов.

            if end_of_file: # Проверяет, достигнут ли конец файла.
                break
    return temp_files


def external_multiphase_sort(path: str, run_size: int) -> None: 
    # вызывает create_initial_runs,
    # чтобы создать отсортированные временные файлы,
    # а затем вызывает merge_files, чтобы объединить их в итоговый файл.

    input_file = f"{path}/input.txt"
    output_file = f"{path}/output.txt"
    path += "\Temp_files_linear"

    temp_files = create_initial_runs(input_file, run_size, path)
    merge_files(output_file, temp_files, path)

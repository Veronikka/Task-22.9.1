def bubble_sort(numbers_list):
    for i in range(0, len(numbers_list)):
        for j in range(0, len(numbers_list)-i-1):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    return numbers_list


def binary_search(numbers_list, to_find):
    low = 0
    high = len(numbers_list) - 1
    while True:
        middle = (low + high) // 2
        if (numbers_list[middle] < to_find) and (numbers_list[middle+1] >= to_find):
            return middle
        if to_find > numbers_list[middle]:
            low = middle
        else:
            high = middle


try:
    numbers = bubble_sort(list(map(int, input("Введите последовательность чисел : ").split())))
    to_find = int(input("Введите число для поиска : "))
    if to_find < numbers[0] or to_find > numbers[-1]:
        print("Искомое число вне границ списка!")
    else:
        print("Индекс в списке : ", binary_search(numbers, to_find))
except ValueError:
    print("Вводите числа!")
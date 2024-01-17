def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = right + left // 2
    if array[middle - 1] < element and element <= array[middle]:
        return[middle - 1]
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, left, middle + 1)
array = list(map(int, input('Введите числа через пробел: ').split()))
element = int(input('Введите положительное число из списка: '))
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print('Вне диапазона')
else:
    print(binary_search(array, element, 0, len(array) - 1))
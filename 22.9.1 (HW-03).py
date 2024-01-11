def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid

    return low

def main():
    input_sequence = input("Введите последовательность чисел через пробел: ")
    user_number = input("Введите любое число: ")

    try:
        sequence_list = [float(x) for x in input_sequence.split()]
        user_number = float(user_number)

        sorted_sequence = sorted(sequence_list)
        position = binary_search(sorted_sequence, user_number)

        print("Отсортированная последовательность:", sorted_sequence)
        print(f"Позиция числа {user_number}:", position)

        if position < len(sorted_sequence):
            print(f"Следующий элемент: {sorted_sequence[position]}")
        else:
            print("Введенное число больше всех в последовательности.")
    except ValueError:
        print("Ошибка ввода. Убедитесь, что введены корректные числа.")

if __name__ == "__main__":
    main()
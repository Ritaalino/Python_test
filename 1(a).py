def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

#Example to be in use
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(input_list)
print(even_numbers)

# List comprehension to generate one hundred numbers
numbers = [n for n in range(100)]

# Lambda function is even
is_even = lambda x: x % 2 == 0

# Filter all even numbers

even_numbers_first_way = [n for n in numbers if is_even(n)]

even_numbers_second_way = list(filter(lambda n: n % 2 == 0, numbers))

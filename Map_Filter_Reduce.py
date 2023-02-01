from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(f"Original List: {my_list}")

square_list = list(map(lambda x: x**2, my_list))
print(f"Squared List: {square_list}")

even_list = list(filter(lambda x: not (x & 1), my_list))
print(f"Even List: {even_list}")

product_of_list = reduce(lambda x, y: x * y, my_list)
print(product_of_list)

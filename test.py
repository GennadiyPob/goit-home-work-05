
#print('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))

# #print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111

# def formatted_numbers():
    
#     print('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))
#     for i in range(16):
#         print('|{:<10}|{:^10}|{:>10}|'.format( i, hex(i), bin(i)))
#         #print(formatted_list)
   


# for el in formatted_numbers():
#     print(el)



# formatted_numbers()



# def formatted_numbers():
#     table = []
#     for num in range(16):
#         decimal_str = f"{num:<10}"
#         hexadecimal_str = f"{hex(num)[2:].lower():^10}"
#         binary_str = f"{bin(num)[2:]:>10}"

#         row = f"| {decimal_str} | {hexadecimal_str} | {binary_str} |"
#         table.append(row)

#     # Додати заголовок таблиці
#     header = "| decimal  |   hex    |  binary  |"
#     table.insert(1, header)
    

#     return table


# # Виведення таблиці
# for el in formatted_numbers():
#     print(el)

# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

# import re 
# s = "I am 25 years old"
# age = re.search('\d+', s)
# print(age)  # <re.Match object; span=(5, 7), match='25'>

import re

s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s)
print(numbers)  # ['7', '6', '10', '3']




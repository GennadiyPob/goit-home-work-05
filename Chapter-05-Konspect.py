
# jingle_bells = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"
# print('  ')
# print(' \n ', jingle_bells)

# jingle_bells = "Jingle bells, jingle bells\fJingle all the way\fOh, what fun it is to ride\fIn a one horse open sleigh"
# print('  ')
# print(' \f ',jingle_bells)

# jingle_bells = "Jingle bells, jingle bells\ringle all the way\rOh, what fun it is to ride\rIn a one horse open sleigh"
# print('  ')
# print(' \r ',jingle_bells)

# jingle_bells = "Jingle bells, jingle bells\tJingle all the way\tOh, what fun it is to ride\tIn a one horse open sleigh"
# print('  ')
# print(' \t ',jingle_bells)

# jingle_bells = "Jingle bells, jingle bells\vingle all the way\vOh, what fun it is to ride\vIn a one horse open sleigh"
# print('  ')
# print(' \v ',jingle_bells)



# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5 вказано діапазон пошуку.
# print(s.find("er")) # 5 не вказано діапазон пошуку
# print(s.find("H"))  # 0 
# print(s.find("i"))  # 1 
# print(s.find(" "))  # 2 
# print(s.index("q"))  # ValueError: substring not found

# s = 'Some words'
# print(s.find('o'))  # 1 знайшли першу букву о з лівої сторони
# print(s.rfind('o'))  # 6 знайшли першу букву о з правої сторони

# print(s.index('o'))  # 1 знайшли першу букву о з лівої сторони
# print(s.rindex('o'))  # 6 знайшли першу букву о з правої сторони

'''Розбиття рядка на декілька підрядків'''

# s = "I am learning strings in Python. Some new methods got now."
# sentences = s.split(" S")

# print(sentences[0]) # I am learning strings in Python
# print('S'+sentences[1]) # Some new methods got now.
import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

#pattern = r'[0-9]+' #Виводить всі числа

#pattern = r'\d' #Виводить всі цифри

# result = re.search(pattern, string)
# print(result.span())
# first_index, second_index = result.span()
# print(string[first_index:second_index])
# print(result.group())
# print(result.string)

#result = re.findall(pattern, string)
#print(result)

'''Шукаємо числа чотиризначні'''

# pattern = r'[0-9]{4}'
# result = re.findall(pattern, string)
# print(result)

'''Шукаємо слова з великої літери'''

#pattern = r'[A-Z]\w+'
#result = re.findall(pattern, string)
'''second variant'''
# new_list = re.compile(pattern)
# result = new_list.findall(string) 
#print(result)

'''Пошук через функцію'''
# def count_digits(string):
#     pattern = r'\d'
#     return re.findall(pattern, string)

# print(count_digits(string))
# print(count_digits(''))



# url_query = "kolichestvo-osnovnih-kamer=3630926;producer=huawei;23777=6-6-5;38435=677049"
# url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

# def get_url_parameters(url_query, pattern=r'&|;', key_split='='):
#     object_dict = dict()
#     #result = re.split(pattern, url_query)
#     #for elem in result:
#     for elem in re.split(pattern, url_query):
#         key, value = elem.split(key_split)
#         object_dict.update({key: value.replace('+', ' ')})
#     return object_dict 
    

# print(get_url_parameters(url_query))
# print(get_url_parameters(url_search))

'''Replacement'''

# lang = "The best language is Java"
# pattern = 'Java'
# print(re.sub(pattern, 'Python', lang))


'''Видалення тексту в квадратних дужках'''


# string = "Exclude from this [string the groups of] characters [located between] brackets [, ]."

# def clean_up(string):
#     pattern = r'(\[.*?\])'
#     return re.sub(pattern, '', string)

# print(clean_up(string))
# #print(re.findall(pattern, string))


'''Видалення тексту в квадратних дужках'''

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.findall(r'^\w+', string))
# print(re.findall(r'\w+\.$', string))


'''Знайти перші дві букви в словах'''

# pattern = r'\b[A-Z,a-z]{2}'
# print(re.findall(pattern, string))

'''Пошук і групування чотиризначних чисел'''

# pattern_one = r'\d{4}-\d{4}'
# print(re.findall(pattern_one, string))

# pattern_two = r'\d{4}-(\d{4})'
# print(re.findall(pattern_two, string))

# pattern_three = r'(\d{4})-(\d{4})'
# print(re.findall(pattern_three, string))


'''Пошук і групування чотиризначних чисел (2 спосіб)'''

# def find_years(string):
#     result = list()
#     pattern = r'(\d{4})-(\d{4})'
#     iterator = re.finditer(pattern, string)
#     for match in iterator:
#         #print(match)
#         result.append(match.group())
#     return result 

# print(find_years(string))

'''Пошук електронних адрес в тексті'''

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "

#print(re.findall(r'([\w.]+@(\w+\.)+\w{2,})', text)) #вивід електронних адрес і імен користувачів
#print(re.findall(r'[\w.]+@(?:\w+\.)+\w{2,}', text)) #вивід електронних адрес без імен користувачів


#print(re.findall(r'[\w.]+@(?:\w+\.)+\w{2,}', text)) #вивід електронних адрес без імен користувачів

# def find_emails(string):
#     result = list()
#     pattern = r'[\w.]+@(?:\w+\.)+\w{2,}'
#     iterator = re.finditer(pattern, string)
#     for match in iterator:
#         result.append(match.group())
#     return result

# print(find_emails(string))

'''Пошук валідного URL
Шукаємо силки тільки з протоколом'''

# text_url = "The main search site in the world is https://www.google.com The main social network for people in the " \
#            "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
#            "they share their code. some url to check https://www..youtube.com/ www.facebook.com https://www.app.facebook.com My site: https://krabaton.info"

# print(re.findall(r'https?:\/\/\w{3}\.?(?:\w+\.)+\w{2,4}', text_url))




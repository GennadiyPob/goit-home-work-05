
''' Задача 1. Видалення символів з рядку'''

# text = 'Alex\nKdfe23\t\f\v.\r'
# def real_len(text):
    
#     special_symbol = ['\n', '\f', '\r', '\t', '\v']
#     new_text = ''
#     for char in text:
#         if char in special_symbol:
#             new_text += ''
#         else:
#             new_text += char
#     return len(new_text)

# print("Довжина рядка:", real_len(text))    

''' Задача 2. Пошук інформації в словнику'''

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]


# def find_articles(key, letter_case=False):
#     actual_states = list()
#     if letter_case:
#         for i in range(len(articles_dict)):
#             if articles_dict[i]['title'].find(key) != -1 \
#                 or articles_dict[i]['author'].find(key) != -1: 
                
#                 actual_states.append(articles_dict[i])

#     else:
#         for i in range(len(articles_dict)):
#             if (articles_dict[i]['title'].lower(key)).find(key) != -1 \
#                 or (articles_dict[i]['author'].lower()).find(key) != -1:
                    
#                     actual_states.append(articles_dict[i])
#     return actual_states


# print(find_articles('Ocean', True)) 


# def find_articles(articles_dict, key, letter_case=False):
#     results = []

#     for article in articles_dict:
#         author = article['author']
#         title = article['title']

#         if letter_case:
#             if key in author or key in title:
#                 results.append(article)
#         else:
#             if key.lower() in author.lower() or key.lower() in title.lower():
#                 results.append(article)

#     return results

# # Приклад виклику функції find_articles
# articles_dict = [
#     {'author': 'John Smith', 'title': 'Python Programming', 'year': 2022},
#     {'author': 'Jane Doe', 'title': 'Introduction to Python', 'year': 2021},
#     {'author': 'Alex Johnson', 'title': 'Advanced Python', 'year': 2023},
# ]

# result1 = find_articles(articles_dict, 'Python')
# print(result1)  # Виведе: [{'author': 'John Smith', 'title': 'Python Programming', 'year': 2022}, {'author': 'Jane Doe', 'title': 'Introduction to Python', 'year': 2021}]

# result2 = find_articles(articles_dict, 'Python', letter_case=True)
# print(result2)  # Виведе: [{'author': 'John Smith', 'title': 'Python Programming', 'year': 2022}]


''' Задача 2. Пошук інформації в словнику (ментор)'''

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
  

# def find_articles(key, letter_case=False):
#     result = []  
#     if not letter_case:  
#         key = key.lower()  
#     for el in articles_dict:  
#         has_found = False  
#         title = el.get("title")  
#         if not letter_case:  
#             title = title.lower()  
#         t = title.find(key)  
#         if t != -1:  
#             has_found = True  
#         author = el.get("author")  
#         if not letter_case:  
#             author = author.lower()  
#         a = author.find(key)  
#         if a != -1:  
#             has_found = True  
#         if has_found:  
#             result.append(el)  
#     return result 

# result = find_articles('Ocean', True)
# print(result)

''' Задача 3. Стандартизація номерів телефонів'''

# def sanitize_phone_number(phone):
#     phone = phone.rstrip() #видаляємо пробіли праворуч
#     phone = phone.lstrip() #видаляємо пробіли ліворуч
#     symbol_range = ['(', ')', '+', '-', ' ']
#     for char in phone:
#         if char in symbol_range:
#             phone = phone.replace(char, '')
#     print(phone)
    
#     return phone

# new = sanitize_phone_number('      +38(050)    350-11-23    ')
# print(new)  

''' Задача 3. Стандартизація номерів телефонів (ментор)'''

# def sanitize_phone_number(phone):
#     new_phone = (  
#         phone.strip()  
#         .removeprefix("+")  
#         .replace("(", "")  
#         .replace(")", "")  
#         .replace("-", "")  
#         .replace(' ', '')  
#     )  
#     return new_phone  

# new = sanitize_phone_number('      +38(050)    350-11-23    ')
# print(new)  

''' Задача 4. Перевірка чи є ім'я префіксом повного імені '''

# def is_check_name(fullname, first_name):
#     fullname = fullname.lower()
#     first_name = first_name.lower()
#     check = fullname.startswith(first_name)

#     return check

# f = is_check_name('Gena Pob', 'gena')
# print(f)

''' Задача 5. Валідності телефонів і їх сортування '''

# phone_storage = ["380669640547", "0637306465    ", " 420961935171", "632643973", "050832520 ", "38066964O547",
#                  "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
#                  "+42(050)123-32-34", "38986223575","38(950)123 32 34", "38(050)123 32 3b", '380998759405', '818765347', '8867658976', '657658976']

# codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# def get_phone_numbers_for_countries(list_phones):
#     number_dict = dict()
#     for i in range(len(list_phones)):
#         phone = sanitize_phone_number(list_phones[i])
#         if phone.startswith('38'):
#             number_dict.setdefault('UA', []).append(phone)
#         if phone.startswith('42'):
#             number_dict.setdefault('IT', []).append(phone)
#         if phone.startswith('37'):
#             number_dict.setdefault('UK', []).append(phone)
#         if phone.startswith('48'):
#             number_dict.setdefault('PL', []).append(phone)
#         if phone.startswith('65'):
#             number_dict.setdefault('SG', []).append(phone)
#     return number_dict

# print(get_phone_numbers_for_countries(phone_storage))


# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

''' Задача 5. Валідності телефонів і їх сортування (my home work) '''

# list_phones = ['380998759405', '818765347', '8867658976', '657658976']

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):

#     number_dict = dict()
#     for i in range(len(list_phones)):
#         phone = sanitize_phone_number(list_phones[i])
#         if phone.startswith('38'):
#             number_dict.setdefault('UA', []).append(phone)
#             print(number_dict)
#         elif phone.startswith('81'):
#             number_dict.setdefault('JP', []).append(phone)
#             print(number_dict)
#         elif phone.startswith('886'):
#             number_dict.setdefault('TW', []).append(phone)
#             print(number_dict)
#         elif phone.startswith('65'):
#             number_dict.setdefault('SG', []).append(phone)
#             print(number_dict)
#         else: 
#             number_dict.setdefault('UA', []).append(phone)
#             print(number_dict)
            
#     return number_dict

# print(get_phone_numbers_for_countries(list_phones))


# phone_storage = ["380669640547", "0637306465    ", " 420961935171", "632643973", "050832520 ", "38066964O547",
#                  "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
#                  "+42(050)123-32-34", "38986223575","38(950)123 32 34", "38(050)123 32 3b"]

# codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}

# # 38 - UA, 42 - IT,  37 - UK 48 - PL
# def clean_up_phone(phone):
#     return (phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", ""))

# def is_valid_phone(phone):
#     if phone.isdigit():
#         if len(phone) == 12:
#             if phone[2] == '0':
#                 if phone[2:5] in codes_operators:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False

#         if len(phone) == 10:
#             if phone[:3] in codes_operators:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     return False


# # 38 - UA, 42 - IT,  37 - UK 48 - PL
# def phone_by_country(list_of_phones):
#     number_dict = dict()
#     for i in range(len(list_of_phones)):
#         phone = clean_up_phone(list_of_phones[i])
#         if phone.startswith('38'):
#             number_dict.setdefault('UA', []).append(phone)
#         if phone.startswith('42'):
#             number_dict.setdefault('IT', []).append(phone)
#         if phone.startswith('37'):
#             number_dict.setdefault('UK', []).append(phone)
#         if phone.startswith('48'):
#             number_dict.setdefault('PL', []).append(phone)
#     return number_dict

# print(phone_by_country(phone_storage))

''' Задача 6. Перевірка спаму (заборонене слово) '''

def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    print(text)
    for word in spam_words:
        word = word.lower()
        print(word)
        if space_around:
            if f" {word} " in text or text.startswith(word + " ") or text.endswith(" " + word) or text.endswith('.' + word) or text == word:
                return True
        if word in text:
            print(word)
            return True

    return False

text = 'Ти ок, але виглядаєш як лох'
spam_words = 'лох'
print(is_spam_words(text, spam_words, True))


#У цьому прикладі, функція is_spam_words приймає рядок text, список заборонених слів spam_words, та параметр space_around, який за замовчуванням дорівнює False.
#Спочатку, за допомогою методу lower(), ми перетворюємо рядок text до нижнього регістру і зберігаємо його в змінній text_lower.
#Потім за допомогою методу split(), ми розділяємо рядок text_lower на окремі слова та зберігаємо їх у список words.
#Залежно від значення параметра space_around, ми визначаємо, чи слід шукати окреме слово (якщо space_around=False) чи як підстроку (якщо space_around=True). Якщо заборонене слово знайдено в рядку text_lower, функція повертає True, щоб позначити, що текст містить заборонені слова. Якщо жодне заборонене слово не знайдено, функція повертає False.


# def is_spam_words(text, spam_words, space_around=False):
#     text_lower = text.lower()
#     words = text_lower.split()

#     for word in words:
#         if space_around:
#             # Перевіряємо, чи слово є окремим і знаходиться у списку spam_words
#             if word in spam_words:
#                 return True
#         else:
#             # Перевіряємо, чи слово входить у список spam_words як підстрока
#             for spam_word in spam_words:
#                 if spam_word in word:
#                     return True

#     return False

# # Приклад виклику функції is_spam_words
# spam_words = ['лох', 'спам']

# result1 = is_spam_words("Молох", spam_words)
# print(result1)  # Виведе: True

# result2 = is_spam_words("Молох", spam_words, True)
# print(result2)  # Виведе: False

# result3 = is_spam_words("Ты лох.", spam_words)
# print(result3)  # Виведе: True

# result4 = is_spam_words("Ты лох.", spam_words, True)
# print(result4)  # Виведе: True


''' Задача 7. Перевірка спаму (заборонене слово) '''


''' Задача 8. Перевірка спаму (заборонене слово) '''


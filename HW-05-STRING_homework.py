
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


def find_articles(articles_dict, key, letter_case=False):
    results = []

    for article in articles_dict:
        author = article['author']
        title = article['title']

        if letter_case:
            if key in author or key in title:
                results.append(article)
        else:
            if key.lower() in author.lower() or key.lower() in title.lower():
                results.append(article)

    return results

# Приклад виклику функції find_articles
articles_dict = [
    {'author': 'John Smith', 'title': 'Python Programming', 'year': 2022},
    {'author': 'Jane Doe', 'title': 'Introduction to Python', 'year': 2021},
    {'author': 'Alex Johnson', 'title': 'Advanced Python', 'year': 2023},
]

result1 = find_articles(articles_dict, 'Python')
print(result1)  # Виведе: [{'author': 'John Smith', 'title': 'Python Programming', 'year': 2022}, {'author': 'Jane Doe', 'title': 'Introduction to Python', 'year': 2021}]

result2 = find_articles(articles_dict, 'Python', letter_case=True)
print(result2)  # Виведе: [{'author': 'John Smith', 'title': 'Python Programming', 'year': 2022}]
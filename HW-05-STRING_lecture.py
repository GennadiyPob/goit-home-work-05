'''ТЕМА 5. Просунута робота з рядками. '''

# numbers = ['123', '456', '321', '10', '75', 'abc', '23c']

# def delete_str(data):
#     result = list()
#     for element in data:
#         if element.isdigit():
#             result.append(element)
#     return result

# def transform_number(data):
#     result = list()
#     for i in data:
#         result.append(int[i])
#     return result




# only_numbers = delete_str(numbers)
# print(only_numbers)
# #print(delete_str(numbers))
# print(f'Diffeence {max(only_numbers) - min(only_numbers)}')


# articles_dict = [
#     {
#         "playset": "Semi final voleyball strike",
#         "command": "Super Star",
#         "year": 1989,
#     },
#     {
#         "playset": "Quater final Finansial competition",
#         "command": "Actual price",
#         "year": 2020,
#     },
#     {
#         "playset": "Glory speed test call centre of East Erope",
#         "command": "Modern Operators",
#         "year": 1921,
#     },
#     {
#         "playset": "Endless war From Age of Dragons",
#         "command": "Kings of Glory",
#         "year": 2012,
#     },
# ]

# def find_states(key_word, letter_case=False):
#     actual_states = list()
#     if letter_case:
#         for i in range(len(articles_dict)):
#             if articles_dict[i]['playset'].find(key_word) != -1 or articles_dict[i]['command'].find(key_word) != -1:
#                 actual_states.append(articles_dict[i])

#     else
#         for i in range(len(articles_dict)):
#             if articles_dict[i]['playset'].find(key_word) != -1 or articles_dict[i]['command'].find(key_word) != -1:
#                 actual_states.append(articles_dict[i])        





# # string = 'text for text and text for text'
# # print(string.find)



'''Перевірити чи строка містить певні слова або частини цих слів'''

# text = '''
# This is samlpe paragraph. It contains some words, like sample, paragraph,  ''' 

# stop_words = ['some', 'stop', 'this', 'start']

# def find_stop_words(text, stop_words, is_space=False):
#     if is_space:
#         new_text = text.split(' ')
#         for word in new_text:
#             for stop in stop_words:
#                 word = word.replace(',', '').replace('.', '')
#                 if stop.lower() in word.lower() and len(stop) == len(word):
#                     return True
#     else:
#         for stop in stop_words:
#             if stop.lower() in text.lower():
#                 return True
#     return False

# print(find_stop_words(text, 'start', True))

'''Валідація номеру телефону'''

# phone_storage = ["380669640547", "0637306465 ", " 420961935171", "632643973", "050832520 ",
#                  "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
#                  "+42(050)123-32-34", "38986223575","38(950)123 32 34", "38(050)123 32 3b"]

# codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}

# def clean_up_phone(phone):
#     return (phone.strip()
#             .removeprefix('+')
#             .replace('(', '')
#             .replace(')', '')
#             .replace('-', '')
#             .replace(' ', ''))

# def is_valid_phone(phone):
#     if len(phone) == 'a':
#         if phone[2] == '0':
#             if phone[2:5] in codes_operators:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False

# for phone in phone_storage:
#     phone = clean_up_phone(phone)
#     is_valid = is_valid_phone(phone)
#     if is_valid:
#         print('Phone {:^4}| {:>12}| {:^4}  valid'.format(' ', phone, ' '*4))
#     else:
#         print('Phone {:>12} invalid'.format(phone))

# def phone_by_country(list_of_phones):
#     numbers_dict = dict()
#     for i in range(len(list_of_phones)):
#         phone = clean_up_phone(list_of_phones)

'''Валідація карток'''

# pay_system = {
#     5: "MasterCard",
#     4: "Visa",
#     3: "American Express"
# }

# card_number = ["5375414112345678", "2346236356566475", "4168757587879876", "216875758787987d", "5345345O45879876"]

# for card in card_number:
#     print('Payment system {:<15} Is card valid {:6}'.format(pay_system.get(int(card[0])), 'Unknown'),
#                                                             str(card.isdigit() and len(card) == 16)))

'''Translate and Zip'''    

# map = {ord('з'): 'z', ord('ю'): 'uu'}
# translated = 'зюзю'.translate(map)
# print(translated)  # zu


'''Переведення в 16-ти річну систему'''  

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# print(zip(symbols, code))

# for key, value in zip(symbols, code):
#     MAP[ord(key)] = value
#     MAP[ord(key.lower())] = value

# print(MAP)

# result = '34 DE 5C B0'.translate(MAP)

'''Підрахунок слів у параграфі'''

import re
from collections import defaultdict

paragraph = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""

def word_frequency_counter(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())

    word_frequency = defaultdict(int)

    for word in words:
        word_frequency[word] += 1

    return dict(word_frequency)

print(word_frequency_counter(paragraph))




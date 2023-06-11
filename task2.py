# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import string
import sys
from collections import Counter
text = 'БОЛЬШАЯ СКИДКА рублей! В акции участвуют все даты и города вылета до конца 2023 года.'
'Промокод действует только на новые брони с 11 августа (с 11:30 по московскому времени) до 20 августа включительно до 23:59 по московскому времени!'
'Подробности акции по тел. — круглосуточно и в офисах продаж. ПРОМОКОДЫ ПО ССЫЛКЕ'
# myLine = text.split()  # split() без аргументов делит по пробельным символам, в том числе и по переносам строк
# d = Counter(myLine)  # один проход с подсчетом в словаре - примерно O(n)
# max_encounters = max(d.values())  # нахождение максимума - О(n)
# most_common_word = min(word for word, count in d.items() if count == max_encounters)  # нахождение минимального из максимально частых слов O(n*m) (m - количество самых частых слов)
# print(most_common_word)  # получаем слово "in"

# d = {}
#  text = sys.stdin.read()
# myLine = [a for b in text.split('\n') for a in b.split()]
# for word in myLine:
#     d[word] = d.get(word, 0) + 1
# for i in sorted(d.items(), key=lambda x: (x[0])):
#     if i[1] == max(d.values()):
#         print(i[0])
#         break


for char in string.punctuation:                    # меняем все знаки препинания на пробелы
    text = text.lower().replace(char, ' ')

counter_dict = {}                               # создаем словарь

for word in text.split():                         # разбиваем строки( будут такого вида ['Пример', 'строки', 'Python']
    counter_dict[word] = counter_dict.get(word, 0) + 1

counter_dict = sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)[:10]
for index, word in enumerate(counter_dict, 1):
    print(f'{index}. {word[0]:>10} {word[1]} раз')

# for i in range(len(text)):
#     if text[i].istitle():
#         text[i] = text[i].lower()
#     if "." in text[i]:
#         text[i] = text[i].replace(".", "")
#     if "," in text[i]:
#         text[i] = text[i].replace(".", "")
#
# temp_dict = dict()
# for item in text:
#     key = temp_dict.setdefault(item, text.count(item))
#
# values = temp_dict.values()
# sorted_values = list(sorted(values, reverse=True))
#
# result = {}
# top = 10
#
# for value in sorted_values:
#     for element in temp_dict.keys():
#         if temp_dict[element] == value:
#             if element not in result:
#                 result[element] = temp_dict[element]
#                 top -= 1
#                 break
#     if top <= 0: break
#
# print(result)

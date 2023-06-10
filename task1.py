# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


data = [12, 34, 45, 12, 12, 55, 2, 4, 1, 1, 55]
# res = []
# count = 0
# for elem in data:
#     if elem in data:
#         count += 1
#         res.append[elem] += 1
#     else:
#         res[elem] = 1
# print(res)

print(data)
dublicate_list = list({item for item in data if data.count(item) > 1})
print(dublicate_list)

# seen = set()
# for n in data:
#   if n in seen:
#     print ("duplicate:", n)
#   else:
#     seen.add(n)
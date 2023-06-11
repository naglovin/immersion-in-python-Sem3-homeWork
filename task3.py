# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


backpack = int(input("Введите вес вашего рюкзака: "))

things = {"Вода": 5,
          "Удочки": 5,
          "Палатка": 8,
          "Плита": 1,
          "Шашлык": 4,
          "Алкоголь": 10,
          "Жена": 1000,
          "Дом": 5000,
          "Подушка": 3,
          "Мыльно-рыльно": 2}

# total = sum(things.values())
# print(total)
result = []
# for item in things.values():
#     if item > backpack
#     print(item)

for elements in things:
    if backpack > things[elements]:
        result.append(elements)
        backpack = backpack - things[elements]
    else: break
print(result)


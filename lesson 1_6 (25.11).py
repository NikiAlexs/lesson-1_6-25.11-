# Словари
phone_book = {"Niki": 89232449144, "Alex": 89231723511}
print(phone_book)
print(phone_book["Niki"])
phone_book["Niki"] = 1234567890
print(phone_book)
phone_book["Alix"] = 1234567891
print(phone_book)
del phone_book["Niki"]
print(phone_book)
phone_book.update({"Sahsa": 9876543210, "Lola": 6547891230})
print(phone_book)
print(phone_book.get("Niki","Net tyt takogo"))
a = phone_book.pop("Sahsa")
print(phone_book)
print(a)

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

# Множества
set_ = {1,2,3,4,5,1,2,3,4, "Niki", 'String', (1,2,3)}
print(set_)
list_ = [1,1,1,1,1,2,3,5,4,6,8,8,8,5,3,2,2]
#print(set(list_))
list_ = set(list_)
print(list_)
print(list_.discard(1))
print(list_)
print(list_.add(11))
print(list_)

# Практическое задание Словари и множества
#Словарь
print("Словарь:")
my_dict = {'Niki': 1991, 'Alex': 1993, 'Sem': 2012, 'Georg': 2014, 'Stef': 2020}
print(my_dict)
print(my_dict['Sem'])
my_dict['Lilit'] = 2010
print(my_dict)
my_dict.update({'Alix': 2008, 'Lila': 2004})
print(my_dict)
b = my_dict.pop('Lilit')
print(b)
print(my_dict)
#Множества
print("Множества")
my_set = {'Niki','Niki','Alex','Alex','Alex', 2022,2022,2023,2024,2024, True, False, True,True}
print(my_set)
my_set.add('Niki',)
my_set.add('Tom',)
print(my_set)
my_set.discard(False)
print(my_set)
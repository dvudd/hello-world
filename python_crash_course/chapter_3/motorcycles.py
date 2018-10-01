#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Lista med motorcyklar
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Skriv ut den första i listan
motorcycles[2] = 'kawazaki'
print(motorcycles)
# Lägg till i listan
motorcycles.append('ducati')
print(motorcycles)
# Lägg till först i listan
motorcycles.insert(0, 'bmw')
print(motorcycles)
#Lägg till en i taget
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('kawazaki')
motorcycles.append('ducati')
motorcycles.append('suzuki')
print(motorcycles)
# Ta bort från listan
del motorcycles[1]
print(motorcycles)
# Använd pop() metoden, tar bort den sista i listan men låter dig använda den borttagna
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title())
first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title())
# ta bort från listan
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")
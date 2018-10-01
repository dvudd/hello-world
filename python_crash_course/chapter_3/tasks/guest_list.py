#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Gäst lista
guest_list = ['linda', 'maja', 'iris', 'svante']
guest_list.insert(0, 'ulla')
guest_list.insert(2, 'mats-ola')
guest_list.append('johan')
guest_list.append('peter')

# Invitationer
print("Welcome " + guest_list[0].title() + " to this year's dinner party")
print("Welcome " + guest_list[1].title() + " to this year's dinner party")
print("Welcome " + guest_list[2].title() + " to this year's dinner party")
print("Welcome " + guest_list[3].title() + " to this year's dinner party")
print("Welcome " + guest_list[4].title() + " to this year's dinner party")
print("Welcome " + guest_list[5].title() + " to this year's dinner party")
print("Welcome " + guest_list[6].title() + " to this year's dinner party")
print("Welcome " + guest_list[7].title() + " to this year's dinner party")
print("")
# Svante kan inte komma
cant_make_it = 'svante'
guest_list.remove(cant_make_it)
print("Unfortunately " + cant_make_it.title() + " can't not make it.")
print("")
# Finns bara bord för 2, ta bort alla förrutom 2 personer, dessa 2 ska få en ny invitation.
guest_list_popped = guest_list.pop(0)
print("Sorry " + guest_list_popped.title() + " but we are overbooked, you are no longer invited")
guest_list_popped = guest_list.pop(0)
print("Sorry " + guest_list_popped.title() + " but we are overbooked, you are no longer invited")
guest_list_popped = guest_list.pop(0)
print("Sorry " + guest_list_popped.title() + " but we are overbooked, you are no longer invited")
guest_list_popped = guest_list.pop(0)
print("Sorry " + guest_list_popped.title() + " but we are overbooked, you are no longer invited")
guest_list_popped = guest_list.pop(0)
print("Sorry " + guest_list_popped.title() + " but we are overbooked, you are no longer invited")
print("")
# Berätta för de som blev kvar
print("Welcome " + guest_list[0].title() + " to this year's dinner party")
print("Welcome " + guest_list[1].title() + " to this year's dinner party")
# Radera allt innehåll i listan
del guest_list[0]
del guest_list[0]
print(guest_list)

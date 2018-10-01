#!/usr/bin/env python
# -*- coding: utf-8 -*- 

guest_list = ['linda', 'maja', 'iris', 'svante']
guest_list.insert(0, 'ulla')
guest_list.insert(2, 'mats-ola')
guest_list.append('johan')
guest_list.append('peter')

print("Welcome " + guest_list[0].title() + " to this year's dinner party")
print("Welcome " + guest_list[1].title() + " to this year's dinner party")
print("Welcome " + guest_list[2].title() + " to this year's dinner party")
print("Welcome " + guest_list[3].title() + " to this year's dinner party")
print("Welcome " + guest_list[4].title() + " to this year's dinner party")
print("Welcome " + guest_list[5].title() + " to this year's dinner party")
print("Welcome " + guest_list[6].title() + " to this year's dinner party")
print("Welcome " + guest_list[7].title() + " to this year's dinner party")
print("")
cant_make_it = 'svante'
guest_list.remove(cant_make_it)
print("Unfortunately " + cant_make_it.title() + " can't not make it.")

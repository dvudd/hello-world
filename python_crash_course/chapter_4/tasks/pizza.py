pizza_list = ['calzone', 'capri', 'hawaii']

for pizza in pizza_list:
     print(pizza.title())
print("I really like pizza!\n")

animals = ['dog', 'cat', 'tiger', 'spider']
for pet in animals:
    print("A " + pet.title() + " would make a great pet")
print("Almost any of these animals would make a great pet")

friends_pizza = pizza_list[:]
friends_pizza.append('kebabpizza')

print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza.title())
print("My friends favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza.title())
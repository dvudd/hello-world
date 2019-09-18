username = ['admin']

for user in username:
    if user == 'admin':
        print("Good morning " + user.title() + ', what would the first sequence of the day be? ')
    else:
        print("Hello " + user.title())
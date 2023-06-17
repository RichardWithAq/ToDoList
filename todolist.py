running = True
start = 0
addorcheck = []
todolist = []
remove = 0

with open('todolist.txt', 'r') as file:
    prelist = file.read()
prelist = prelist.split()

while running == True:
    while start == 0:
        addorcheck = input('Would you like to add to or check your list? Use "add" or "check" or "remove" or "exit": ').upper()
        if addorcheck == 'CHECK':
            with open('todolist.txt', 'r') as file:
                print(file.read())
            addorcheck = []
            break
        elif addorcheck == 'ADD':
            start = 1
            break
        elif addorcheck == 'EXIT':
            running = False
            break
        elif addorcheck == 'REMOVE':
            start = 2
            break
        else:
            print('I am sorry. I do not understand, try typing "add" to add items to the list or "check" to check the list or "remove" to delete something from the list or "exit" to leave. ')


    while start == 1:
        print('Please use a comma "," after every item')
        todolist = input('''What would you like to add to your list
---------------------------------------
''')
        todolist = todolist.split(',')
        todolist = prelist + todolist
        with open('todolist.txt', 'w') as file:
            for item in todolist:
                file.write(item + '\n')
        start = 0
        break


    while start == 2:
        while start == 2:
            with open('todolist.txt', 'r') as file:
                savedlist = file.readlines()

            for index, word in enumerate(savedlist, start = 1):
                print(f'{index}. {word.strip()}')
            try:
                remove = input('To remove an item type the number next to the item you wish to remove: ')
                remove = int(remove)
                savedlist.pop(remove - 1)
                break
            except IndexError:
                print('No item has that number.')
    
        with open('todolist.txt', 'w') as file:
            for item in savedlist:
                file.write(item)

        addorcheck = input('Do you want to remove anything else. "yes" or "no": ')
        if addorcheck == 'yes':
            addorcheck = []
        elif addorcheck == 'no':
            start = 0
            addorcheck = []
            break
        else:
            print('Sorry, I do not understand that try "yes" or "no". ')
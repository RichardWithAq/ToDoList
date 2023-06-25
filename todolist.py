import os
running = True
start = 0
addorcheck = []
todolist = []
remove = 0

if os.path.exists('todolist.txt'):
    pass
else:
    open('todolist.txt', 'x')

with open('todolist.txt', 'r') as file:
    prelist = file.read()
prelist = prelist.split()

while running == True:
    while start == 0:
        addorcheck = input('Would you like to add to or check your list? Use "add" or "check" or "remove" or "exit": ').upper()
#CHECK
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

#ADD
    while start == 1:
        print('Please use a comma "," after every item')
        todolist = input('''What would you like to add to your list
---------------------------------------
''')
        todolist = todolist.split(',')
        todolist = prelist + todolist
        todolist = [item.strip() for item in todolist]
        with open('todolist.txt', 'w') as file:
            for item in todolist:
                file.write(item + '\n')
        start = 0
        break

#REMOVE
    while start == 2:
        while start == 2:
            with open('todolist.txt', 'r') as file:
                savedlist = file.readlines()

            for index, word in enumerate(savedlist, start = 1):
                print(f'{index}. {word.strip()}')
            remove = input('To remove an item type the number next to the item you wish to remove and split numbers with a comma: ')
            remove = remove.replace(' ', '')
            remove.split(',')
            remove = [int(num) for num in remove if num.isdigit()]

            if remove:
                remove = [num - 1 for num in remove if 0 < num <= len(savedlist)]
                remove.sort(reverse = True)
                for index in remove:
                    savedlist.pop(index)
                break
            else:
                print('Try using numbers instead of letters.')
            #except IndexError:
               # print('No item has that number.')
    
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
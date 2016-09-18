'''Basic Shopping List script
A basic CLI shopping list application.

Created: 2016
Author: Edward Haigh
'''

shopping_list = []


def show_help():
    print("\nSeparate each item with a comma.")
    print("Type 'DONE' to quit, 'SHOW' to see the current list, or HELP to bring up this message.'")


def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {}".format(count, item))
        count += 1


print("Give me a list of things you want to shop for.")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("Here is your list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    else:
        new_list = new_stuff.split(",")
        for item in new_list:
            shopping_list.append(item.strip())

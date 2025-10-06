def show_menu():
    print("options:\n"
          "1) please enter the number\n"  
          "2) please enter the name\n"     
          "3) show the list of numbers\n"
          "4) show the list of names\n"
          "5) show the result of numbers\n"
          "6) remove an item\n"
          "7) exit")
    choose = int(input("please enter the number: "))
    return choose


list_of_the_number = []
list_of_the_name = []


def add_number():
    number = int(input("please enter the number: "))
    list_of_the_number.append(number)
    return number


def add_name():
    name = input("please enter the name: ")
    list_of_the_name.append(name)
    return name


def show_the_list_number():
    print("your current list of numbers:", list_of_the_number)


def show_the_result_number():
    result = sum(list_of_the_number) / len(list_of_the_number)
    print("result is:", result)
    return result


def show_the_list_name():
    print("your current list of names:", list_of_the_name)


def remove_item():
    choose = input("please input which list do you want to remove from (numbers/names): ")
    if choose== "numbers":
        remove_the_item = int(input("please enter the number you want to remove: "))
        list_of_the_number.remove(remove_the_item)

    elif choose== "names":
        remove_the_item = input("please enter the name you want to remove: ")
        list_of_the_name.remove(remove_the_item)
    else:
        print("invalid choice.")


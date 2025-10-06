from my_modul import *

while True:
    first_attempt = show_menu()

    if first_attempt == 1:
        first_performance=add_number()
        print("Result:", first_performance)
        print("*" * 50)
    elif first_attempt == 2:
        second_performance=add_name()
        print("Result:", second_performance)
        print("*" * 50)
    elif first_attempt == 3:
        show_the_list_number()
        print("*" * 50)
    elif first_attempt == 4:
        show_the_list_name()
        print("*" * 50)
    elif first_attempt == 5:
        show_the_result_number()
        print("*" * 50)
    elif first_attempt == 6:
        remove_item()
        print("*" * 50)
    elif first_attempt == 7:
        print("Goodbye!")
        break
    else:
        print("invalid number!!!")


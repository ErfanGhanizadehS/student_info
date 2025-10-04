Program Topic:
This program is a simple menu where I can enter some numbers and names, view them, calculate the average of the numbers, or remove an item from the list if I want.

Relation Between Parts:
At the beginning, the program displays a menu with several options, such as adding a number, adding a name, showing the lists, calculating the average, and deleting an item.
Each option calls a specific function that performs that task.
There is one list for numbers (list_of_the_number) and one for names (list_of_the_name).
Whatever I enter gets stored in the appropriate list.

Solution Method (Algorithm):
First, the menu appears and asks the user what they want to do.
Then, depending on the number they enter, one of the following actions happens:

If the user enters 1, the program asks for a number and adds it to the list of numbers.

If they enter 2, it asks for a name and adds it to the list of names.

If they enter 3, it shows the current list of numbers.

If they enter 4, it shows the current list of names.

If they enter 5, it calculates and displays the average of the numbers.

If they enter 6, it asks which list they want to remove an item from (numbers or names) and deletes that item.

If they enter 7, the program exits.

In general, the menu keeps repeating until the user chooses option 7, so they can add, view, or delete items as many times as they like.

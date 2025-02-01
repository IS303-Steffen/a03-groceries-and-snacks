#### Assignment 4
# Groceries and Snacks
This assignment has two .py files: `a04_grocery_list.py` and `a04_snack_dictionary.py`. In the first file you'll write a simple program to practice using a list, in the second you'll use a dictionary.

## Logical Flow for `a04_grocery_list.py`

1. Create a grocery list:  
    - Create a list with three grocery foods inside it of your choice (e.g., `"apples"`, `"bananas"`, `"milk"`, etc.). Make sure there are exactly 3 items in the list (otherwise the automated tests won't work).
    - Please don't put `"pasta"` in your list. It's the input the automated tests will use so it might mess up the automated tests if you use it.

2. Print out the list:
    - Print out the following:
        - `Current grocery list:`
    - Then print out your list. It's fine that it appears with the square brackets:
        - for example, something like:
        - `['apples', 'bananas', 'milk']`

3. Add a new item to the list:  
    - Prompt the user to add another item:
        - `Enter a new grocery item to add: `
    - Add the entered item to the end of your list

4. Check for a specific item in your list:  
    - Prompt the user to enter an item to see if it is in your list
        - `Enter an item to see if it's in your list: `
    - Then if the item the user enters is in your list already, print:
        - `<item entered> is in your list`.
    - If the item isn't in your list, print:
        - `<item entered> is not in your list.`
    - Note: you don't need to check or adjust your code for proper capitalization.

5. Remove an item by name:  
    - Prompt the user to enter the name of an item they want to remove.  
        - `Enter an item to remove from the list: `
    - If the item exists in the list, remove it and print out:
        - `<item entered> was removed from the list.`  
    - If the item is not in the list, don't remove anything and print out:
        - `<item entered> is not in your list.`

6. Remove the first item:  
    - Remove the first item from the list, and print out:
        - `The first item, <removed item>, was removed from the list.`

8. Print the final list:  
    - Print out:
        - `Final grocery list:`
    - Then print out your grocery list variable.

## Logical Flow for `a04_snack_dictionary.py`

1. Create a snack inventory:  
    - Create a dictionary where the keys are snack names and the values are the quantities of those snacks. You can use whatever snacks and numbers you want. (e.g., `"chips": 3`, `"cookies": 5`, `"granola bars": 2`, etc.).  
    - Make sure there are exactly 3 snacks in the dictionary (otherwise the automated tests won't work).
    - Please don't put `"starburst"` in your dictionary. It's the input the automated tests will use so it might mess up the automated tests if you use it.

2. Print out the snack inventory:  
    - Print out the following:  
        - `Current snack inventory:`  
    - Then print out your dictionary. It's fine that it appears with the curly braces:
        - for example, something like:  
        - `{'chips': 3, 'cookies': 5, 'granola bars': 2}`  

3. Add a new snack:  
    - Prompt the user to add a new snack:  
        - `Enter the name of a new snack to add: `  
    - If the snack is already in the dictionary, print:  
        - `<new snack> is already in your inventory.`  
    - If the snack is not in the dictionary, prompt the user to enter the quantity:  
        - `Enter the count for <new snack>:  `  
        - Then add the new snack name and quantity to the dictionary and print:  
            - `<new snack> was added to your inventory.`  

4. Update the count for an existing snack**:  
    - Prompt the user to enter the name of a snack they want to update:  
        - `Enter the name of a snack to update: `  
    - If the snack is in the dictionary, prompt the user to enter the new count:  
        - `Enter the new count for <snack>: `  
        - Then update the count for the snack and print:  
            - `The count for <snack> was updated.`  
    - If the snack is not in the dictionary, print:  
        - `<snack> is not in your inventory.`  

5. Remove a snack by name:  
    - Prompt the user to enter the name of a snack they want to remove:  
        - `Enter the name of a snack to remove: `  
    - If the snack is in the dictionary, remove it and print:  
        - `<snack> was removed from your inventory.`  
    - If the snack is not in the dictionary, print:  
        - `<snack> is not in your inventory.`  

6. Print the final snack inventory:  
    - Print out the following:  
        - `Final snack inventory:`  
    - Then print out your dictionary with all updates applied.


## Grading Rubric
See the Rubric.md file.

Remember to right click the file and choose "Open Preview" to view the nicely formatted version.

## Example Output for `a04_grocery_list.py`

```
Current grocery list:
['apples', 'bananas', 'milk']

Enter a new grocery item to add: pasta

Enter an item to see if it's in your list: pasta
pasta is in your list.

Enter an item to remove from the list: pasta
pasta was removed from the list.

The first item, apples, was removed from the list.

Final grocery list:
['bananas', 'milk']
```

## Example Output for `a04_snack_dictionary.py`

```
Current snack inventory:
{'chips': 3, 'cookies': 5, 'granola bars': 2}

Enter the name of a new snack to add: starburst
Enter the count for starburst: 55
starburst was added to your inventory.

Enter the name of a snack to update: starburst
Enter the new count for starburst: 10
The count for starburst was updated.

Enter the name of a snack to remove: starburst
starburst was removed from your inventory.

Final snack inventory:
{'chips': 3, 'cookies': 5, 'granola bars': 2}
```

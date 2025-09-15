# Test Case 4

## Description
Adding a new snack, but providing an invalid name for the update and deleting. The final dictionary should have 4 items in it.

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
```
1: "starburst"
2: "55"
3: "NotInTheDictionary"
4: "NotInTheDictionary"
```

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
```
Current snack inventory:
{'chips': 3, 'cookies': 5, 'granola bars': 2}

Enter the name of a new snack to add: starburst
Enter the count for starburst: 55
starburst was added to your inventory.

Enter the name of a snack to update: NotInTheDictionary
NotInTheDictionary is not in your inventory.

Enter the name of a snack to remove: NotInTheDictionary
NotInTheDictionary is not in your inventory.

Final snack inventory:
{'chips': 3, 'cookies': 5, 'granola bars': 2, 'starburst': 55}
```

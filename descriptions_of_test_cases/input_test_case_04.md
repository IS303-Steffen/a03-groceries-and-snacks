# Test Case 4

## Description
Adding a new snack, but providing an invalid name for the update and deleting. The final dictionary should have 4 items in it.

Note that below, this is using the starting dictionary `{'chips': 3, 'cookies': 5, 'granola bars': 2}` but the tests will work with any other items in the dictionary (as long as there are 3 items in it). 

## Inputs
```
1: "starburst"
2: "55"
3: "NotInTheDictionary"
4: "NotInTheDictionary"
```

## Expected Input Prompts
```
1: "Enter the name of a new snack to add: "
2: "Enter the count for starburst: "
3: "Enter the name of a snack to update: "
4: "Enter the name of a snack to remove: "
```

## Expected Printed Messages
```
1: "Current snack inventory:"
2: "{'chips': 3, 'cookies': 5, 'granola bars': 2}"
3: "starburst was added to your inventory."
4: "NotInTheDictionary is not in your inventory."
5: "Final snack inventory:"
6: "{'chips': 3, 'cookies': 5, 'granola bars': 2, 'starburst': 55}"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
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

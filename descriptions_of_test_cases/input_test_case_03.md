# Test Case 3

## Description
adding a new snack, updating that snack, and then removing it. The ending dictionary should have 3 items in it.

Note that below, this is using the starting dictionary `{'chips': 3, 'cookies': 5, 'granola bars': 2}` but the tests will work with any other items in the dictionary (as long as there are 3 items in it). 

## Inputs
```
1: "starburst"
2: "55"
3: "starburst"
4: "10"
5: "starburst"
```

## Expected Input Prompts
```
1: "Enter the name of a new snack to add: "
2: "Enter the count for starburst: "
3: "Enter the name of a snack to update: "
4: "Enter the new count for starburst: "
5: "Enter the name of a snack to remove: "
```

## Expected Printed Messages
```
1: "Current snack inventory:"
2: "{'chips': 3, 'cookies': 5, 'granola bars': 2}"
3: "starburst was added to your inventory."
4: "The count for starburst was updated."
5: "starburst was removed from your inventory."
6: "Final snack inventory:"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
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

# Test Case 2

## Description
Adding an item from the list, checking if an item that isn't in the list is in the list, then trying to remove an item that isn't in the list. At the end, your list should have 3 items in it.

Note that below, this is using the list `['apples', 'bananas', 'milk']` to start, but the tests will work with any starting list that has 3 items in it.

## Inputs
```
1: "pasta"
2: "thisWillNotBeInTheList"
3: "thisWillNotBeInTheList"
```

## Expected Input Prompts
```
1: "Enter a new grocery item to add: "
2: "Enter an item to see if it's in your list: "
3: "Enter an item to remove from the list: "
```

## Expected Printed Messages
```
1: "Current grocery list:"
2: "['apples', 'bananas', 'milk']"
3: "thisWillNotBeInTheList is not in your list."
4: "was removed from the list."
5: "Final grocery list:"
6: "['bananas', 'milk', 'pasta']"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Current grocery list:
['apples', 'bananas', 'milk']

Enter a new grocery item to add: pasta

Enter an item to see if it's in your list: thisWillNotBeInTheList
thisWillNotBeInTheList is not in your list.

Enter an item to remove from the list: thisWillNotBeInTheList
thisWillNotBeInTheList is not in your list.

The first item, apples, was removed from the list.

Final grocery list:
['bananas', 'milk', 'pasta']
```

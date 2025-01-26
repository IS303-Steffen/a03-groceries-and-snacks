# Test Case 1

## Description
Adding an item, checking if that same item is in the list (it should be), and then removing that item from the list. The list should have 2 things in it at the end.

Note that below, this is using the list `['apples', 'bananas', 'milk']` to start, but the tests will work with any starting list that has 3 items in it.

## Inputs
```
1: "pasta"
2: "pasta"
3: "pasta"
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
3: "pasta is in your list."
4: "pasta was removed from the list."
5: "was removed from the list."
6: "Final grocery list:"
7: "['bananas', 'milk']"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
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

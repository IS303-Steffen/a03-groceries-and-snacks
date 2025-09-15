# Test Case 2

## Description
Adding an item from the list, checking if an item that isn't in the list is in the list, then trying to remove an item that isn't in the list. At the end, your list should have 3 items in it.

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
```
1: "pasta"
2: "thisWillNotBeInTheList"
3: "thisWillNotBeInTheList"
```

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
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


# Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

<table border="1" style="width: 100%; text-align: center;">
<thead>
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Input Prompts: List</td>
        <td>
        <b>Input test cases used:</b> 1, 2<br><br>
        This is for the <code>a03_grocery_list.py</code> file. Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected input prompts for each input test case.
        </td>  
        </td>
        <td>15</td>
    </tr>
        <tr style="text-align: left">
        <td>2. Input Prompts: Dictionary</td>
        <td>
        <b>Input test cases used:</b> 3, 4<br><br>
        This is for the <code>a03_snack_dictionary.py</code> file. Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected input prompts for each input test case.
        </td>  
        </td>
        <td>15</td>
    </tr>
    <tr style="text-align: left">
        <td>3. Printed Messages: List</td>
        <td>
        <b>Input test cases used:</b> 1, 2<br><br>
        This is for the <code>a03_grocery_list.py</code> file. Your printed output must be the same as the expected output of each input test case. This includes the correct BMI calculations and BMI categories.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected printed messages for each input test case.       
        </td>
        <td>15</td>
    <tr style="text-align: left">
        <td>4. Printed Messages: Dictionary</td>
        <td>
        <b>Input test cases used:</b> 3, 4<br><br>
        This is for the <code>a03_snack_dictionary.py</code> file. Your printed output must be the same as the expected output of each input test case. This includes the correct BMI calculations and BMI categories.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected printed messages for each input test case.       
        </td>
        <td>15</td>
    </tr>
        <tr style="text-align: left">
        <td>5. List Properly Updated</td>
        <td>
        <b>Input test cases used:</b> 1, 2<br><br>
        Your code must create a list variable, and properly add and delete from it. It doesn't matter what you call the variable.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for inputs used in each test case to see what your list should hold.    
        </td>
        <td>15</td>
    </tr>
        <tr style="text-align: left">
        <td>6. Dictionary Properly Updated</td>
        <td>
        <b>Input test cases used:</b> 3, 4<br><br>
        Your code must create a dictionary variable, and properly add and delete from it. It doesn't matter what you call the variable.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for inputs used in each test case to see what your dictionary should hold.    
        </td>
        <td>15</td>
    </tr>
    <tr style="text-align: left">
        <td>7. Sufficient Comments </td>
        <td>
        <b>Input test cases used:</b> None<br><br>
        Your code must include at least <code>7</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>Adding an item, checking if that same item is in the list (it should be), and then removing that item from the list. The list should have 2 things in it at the end.</td>
  </tr>
  <tr>
    <td>Input Test Case 02</td>
    <td>Adding an item from the list, checking if an item that isn't in the list is in the list, then trying to remove an item that isn't in the list. At the end, your list should have 3 items in it.</td>
  </tr>
  <tr>
    <td>Input Test Case 03</td>
    <td>adding a new snack, updating that snack, and then removing it. The ending dictionary should have 3 items in it.</td>
  </tr>
  <tr>
    <td>Input Test Case 04</td>
    <td>Adding a new snack, but providing an invalid name for the update and deleting. The final dictionary should have 4 items in it.</td>
  </tr>
</table>
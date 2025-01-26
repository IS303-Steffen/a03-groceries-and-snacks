max_score = 15  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
from conftest import default_module_to_test

# Checks if a correct dictionary is created given certain inputs
def test_03_proper_dictionary_values(current_test_name, input_test_cases):
    try:
       # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case, current_test_name) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        for input_test_case in input_test_cases[0:2]:
            try:
                inputs = input_test_case["inputs"]
                # This provides a dictionary of dictionaries. Each key is a variable name,
                # the value is the actual dictionary we care about.
                expected_lists = input_test_case["lists"].values()

                # Normalize expected dictionaries
                normalized_expected_lists = []
                for expected_list in expected_lists:
                    if expected_list is not None:
                        normalized_expected_list = [normalize_text(value) for value in expected_list]
                        normalized_expected_lists.append(normalized_expected_list)

                        expected_lists_string = ''

                for idx, normalized_expected_list in enumerate(normalized_expected_lists, 1):
                    expected_lists_string += f"Expected List {idx}: {normalized_expected_list}\n\n"
                

                # Load in the student's code and get globals
                manager_payload = load_student_code(current_test_name, inputs, input_test_case, module_to_test=default_module_to_test)
                
                student_globals = manager_payload.get('module_globals')

                # Get the locals from 'main' function
                student_locals = student_globals.get('__main_locals__', {})

                # Find all variables in student's code that are of type dictionary
                student_lists = {name: value for name, value in student_globals.items() if isinstance(value, list)}

                # Also include dictionaries from student_locals
                student_lists.update({name: value for name, value in student_locals.items() if isinstance(value, list)})

                # Assert that there is at least one list
                assert student_lists, format_error_message(
                        custom_message=(
                            f"The tests couldn't find any list variables in your code. This input test case expects this "
                            f"list to exist when your code is run:\n\n"
                            f"EXPECTED LIST VALUES:\n"
                            f"--------------------------\n"
                            f"The expected list values (ignoring capitalization / punctuation) are:\n\n"
                            f"{expected_lists_string}"
                            f"Make sure you are storing the groceries in a list, or that you aren't overwriting "
                            f"your list by calling another variable the same name as your list.\n"),
                        current_test_name=current_test_name,
                        input_test_case=input_test_case,
                        display_inputs=True
                    )

                list_match_found = False
                list_length_matched = False
                student_lists_string = ''  # Used to provide details if the test fails

                # Iterate over all dictionaries found in the student's code
                for list_name, student_list in student_lists.items():
                    # String is useful for error reporting if test fails
                    normalized_student_list = [normalize_text(value) for value in student_list]

                    student_lists_string += f"{list_name}: {normalized_student_list}\n\n"

                    # Check if student list matches any of the expected dictionaries
                    for normalized_expected_list in normalized_expected_lists:
                        if 'pasta' in normalized_student_list or input_test_case.get('id_input_test_case') == 1:
                            list_match_found = True
                            break  # Stop once we find a matching dictionary
                    if list_match_found:
                        break

                # If a list with the correct value is found, make sure it has the proper number of elements too
                if list_match_found:
                    if len(normalized_student_list) == len(normalized_expected_list):
                        list_length_matched = True

                assert list_match_found, format_error_message(
                    custom_message=(
                        f"None of the lists found in your code "
                        f"matched any of the expected value for this input test case.\n\n"
                        f"EXPECTED LIST VALUE:\n"
                        f"--------------------\n"
                        f"The test expects your list to have this value (ignoring capitalization / punctuation):\n\n"
                        f"pasta\n\n"
                        f"YOUR LIST VALUES:\n"
                        f"-----------------\n"
                        f"Your list(s) (ignoring capitalization / punctuation) look like this:\n\n"
                        f"{student_lists_string}\n"
                        f"Make sure you are correctly adding values to your list, or "
                        f"that you aren't transforming the inputs in an unexpected way.\n"),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    display_inputs=True
                )

                assert list_length_matched, format_error_message(
                    custom_message=(
                        f"None of the lists found in your code "
                        f"had the expected number of elements expected for this input test case.\n\n"
                        f"EXPECTED LIST ELEMENTS:\n"
                        f"-----------------------\n"
                        f"The test expects your dictionary to have this # of elements:\n\n"
                        f"{len(normalized_expected_list)}\n\n"
                        f"YOUR LIST VALUES:\n"
                        f"-----------------\n"
                        f"Your list has {len(normalized_student_list)} elements and looks like this (ignoring capitalization / punctuation):\n\n"
                        f"{student_lists_string}\n"
                        f"Make sure you are correctly adding values to your list, or "
                        f"that you aren't transforming the inputs in an unexpected way.\n"),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    display_inputs=True
                )


            # assert raises an AssertionError, but I don't want to actually catch it
            # this is just so I can have another Exception catch below it in case
            # anything else goes wrong.
            except AssertionError:
                raise
            
            except Exception as e:
                # Handle other exceptions
                exception_message_for_students(e, input_test_case)
    
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case)
## Chpt. 1 Overview - TDD (test-driven development)
    - Levels of Testing
        - Unit
            - testing at the functional level
        - Component
            - testing in library and compiled binary level
        - System
            - testing external interfaces of system which is a collection of sub-systems
        - Performance
            - testing at sub-system and system level to verify acceptable timing and resource usage
    
    - Unit Testing
        - tests individual functions
        - tests should be written for each test case for a function (all positive and negative test cases)
        - execution of tests occurs in dev environment and should be automated
        - typically features setup, action, and assertion steps
    
            ex.// production code//
                def string_len(str):
                    return len(str)

                //unit test//
                def test_stringlen_function():
                    testStr = '1'
                    result = str_len(testStr)
                    assert result == 1
    
    - What is TDD
        - unit testing written *before* production code
        - not all at once, write one unit test per use case, then the production code
        - test and production code are written together to enable small bits of functionality
    
    - TDD Workflow
        - workflow = `red`, `green`, `refactor` and phases
            - red: write a failing unit test for a piece of functionality 
            - green: write just enough production code to make the test pass
            - refactor: cleanup unit test and production code
        - Three `Laws` of TDD
            - May not write any production code until a failing unit test is written
            - May not write more of a unit test than is sufficient to fail, and not compiling is failing
            - May not write more production code than is sufficient to pass the currently failing unit test

    - Fizzbuzz kata
        - refactor step means also eliminating duplicated test calls to a function, so should remove or rewrite to generalize
            - ex. replace with general utility function s.a.
                //with a fizzbuzz function defined above
                def checkFizz(value, expectedRetVal):
                    retval = fizzbuzz(value)
                    assert reval == expectedRetVal

## Chpt. 2 - Python Virtual Environments
    - by default all python packages are installed to single directory on host system
        - this is a problem when different projects require different versions of a package
        - virtual environments solve by creating isolated python envs customizable for each project
    - venvs are directories containing links to systems python install and additional subdirectories for installing particular python packages in that particular venv
    - when a venv is activated, the PATH var is updated to point to the venv
    - Python2 requires pip install virtualenv, python3 has built-in module = `venv` 

## Chpt. 3 - PyTest
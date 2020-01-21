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
    - python unit testing framework
        - allows for testing of modules, classes, fixtures
        - uses built-in `assert` statement
        - adds CL arguments to specify order of test run
    - setup
        - mkdir a test directory
        - `virtualenv [thatdirectory]`
        - check if pytest installed `pytest --version`
        - make a test, run as `pytest my_test.py`
        
    - how to build unit test
        - tests are functions with `test` in beginning of name
        - test runs and verifies values based on `assert` statement

    - XUnit Style Setup and Teardown
        - pytest supports xunit style functionality allowing user to execute code before and after test modules, functions, classes and methods
            - explanation from S.O.:
                For example you have a test that requires items to exist, or certain state - so you put these actions(creating object instances, initializing db, preparing rules and so on) into the setUp.

                Also as you know each test should stop in the place where it was started - this means that we have to restore app state to it's initial state - e.g close files, connections, removing newly created items, calling transactions callback and so on - all these steps are to be included into the tearDown.

                So the idea is that test itself should contain only actions that to be performed on the test object to get the result, while setUp and tearDown are the methods to help you to leave your test code clean and flexible.

                You can create a setUp and tearDown for a bunch of tests and define them in a parent class - so it would be easy for you to support such tests and update common preparations and clean ups.

                If you are looking for an easy example please use the following link with example.
    
    - Test Fixtures
        - allow for reuse of code across tests by specifying functions that should be executed before test runs
        - pytest.fixture decorator applied to functions to specify as fixture
        - adding fixture test to parameter list of function (ie. adding as argument) will specify that the test uses the fixture
            - or using @pytest.mark.usefixture("fixturename") decorator before test
            - or setting fixture `autouse` attribute to true will make all tests within fixture scope execute fixture before running 
                - `@pytest.fixture(autouse=True)`
        - each fixture can specify teardown that is called after fixture goes out of scope
            - specify with `yield` in fixture code or with `addFinalizer`
                - addFinalizer ex. @pytest.fixture()
                      def setup(request):
                        //do sth
                        def teardown():
                            //teardown
                        request.addFinalizer(teardown)
                    - using addFinalizer allows for multiple teardown functions to be specified (ie. with multiple `request.addFinalizer() calls)
            - fixture scopes:
                - function: run fixture once for each test
                - class: run once for each class
                - module: run once when module goes in-scope
                - session: run when pytest starts
            - fixtures can also optionally return data to be used in the test
                - given in `params` argument in fixture decorator
                    - @pytest.fixture(params=[1, 2, 3])
                      def test(request):
                        return request.params
            
            - assert statements and exception testing
                - assert statements perform validations in test
                    - pytest expands messages returned from assert failures to provide more context
                    - can use `approx` function to validate floating point values that may other wise fail arbitrarily
                        - ex. assert val == approx(0.3)
                - exception verification
                    - pytest uses `with raises(valueError)` to test that a function correctly throws error under certain conditions
                        - if specified error not thrown in the block after the `raises` statement, the test fails
            
            - Pytest CL arguments
                - can specify module name to run only tests in that module (eg. `pytest test_file1.py`)
                - `-k "expression"` runs tests that match evaluatable expression in the string (eg. module/class/function names)
                    - eg. `pytest -k "functionName"`
                - `-m "expression"` runs tests with `pytest.mark` decorator matching the expression
                - `-v` verbose output
                - `q` 'quiet' ie. minimal output
                - `s` dont capture console output
                - `--ignore` specifiy path to ignore for test discovery
                - `--maxfail` stop after number of test failures  

## Chpt. 5 Unit Test Isolation
    - often need to query external services or other parts of a system that if included in tests might run slowly, or are difficult to replicate in test environment
    - `test doubles`: objects used in unit tests as replacements for real production system collaborators
        - types
            - dummy: object that can be passed around but dont have any type of test implementation
            - fake: simplified functional implementation of an interface suitable for testing but not production
            - stub: objects providing implementations with canned answers suitable for testing
            - spy: object providing implementations that record values passed in so they can be used by the test
            - mock: objects preprogrammed to expect specific calls and params and can throw exceptions when neccessary. 
        
        - unittest.mock is is a python mocking framework
            - built-in python 3.3 and later
            - older versions req `pip install mock`
            - has `Mock` class used to create doubles
                - provides many initialization params (entered as args) which are used to control mock object behavior
                - has many built-in functions for verifying how the object was used
                    - use `assert_` attributes
                        - eg.
                            - `assert_called`: assert that the mock was called
            - `MagicMock` class derived from Mock and provides and provides a default implementation for many of the `magic` methods defined for object in python by default 
                - ie. methods beginning with two `_` such as `__str__`
    
    - TDD Best Practices
        - always do the next simplest test case
            - keeps code clean and coherent
            - gradually increases the complexity of code
        - use descriptive test names
        - keep test loop fast
            - unit test execution shouldn't take more than a few seconds at most
            - should eliminate console output
        - use code coverage tools
            - once all your test cases are covered, run through code coverage tool
                - may reveal scenarios that you missed (eg. negative test cases)
        - run tests multiple times and in random order
            - `pytest-random-order` plugin will run tests in random order
        - use static code analysis tool
            - pylint and similar can find errors in code, check that code meets a coding standard (eg. PEP8)
            - pylint detects duplicate code and generates UML diagrams of code

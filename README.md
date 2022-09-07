# Swap Meet

## Skills Assessed

- Comprehending and following code specifications
- Reading tests
- Creating classes with attributes and instance methods
- Importing modules
- Working with attributes that are lists of instances
- Implementing instance methods that interact with other instances and objects
- Implementing inheritance
- Overriding methods from superclasses and Object

## Goal

You want to organize a swap meet! You have a bunch of _stuff_. So do your friends! It would be awesome if each person could swap one of their things with another person's things.

For this event, you want each person to register online as a vendor. Also, they should add an inventory list of things.

You envision an app where vendors can swap items between different inventories. But what would that backend logic look like?

For this project, given some features that the vendors want, create a set of classes, following the directions below. The directions will lead you to create many class definitions, their attributes and instance methods, and some other cool features. Vendors will be able to swap items based on values like quality, category, or id!

## Setup and Workflow

Refer to [the viewing-party README](https://github.com/AdaGold/viewing-party) for detailed instructions on the One-Time Project Setup, Project Development Workflow, and Details About How to Run Tests.

For this project, there are tests that you must complete for Waves 01, 02, and 06.

## Integration Tests

We provided **integration tests** for this project. The integration tests provided in this project do not cover all the test cases verified by the unit tests. While unit tests are small, fast, and should cover most of our program's behavior down to individual functions, integration tests verify that the various pieces of a program are working together correctly. For this project, the integration tests mainly verify that the functions work together when invoked correctly. We could classify them as the subset of Integration Tests called *Smoke Tests*, tests that check basic functionality of the application.

The integration tests for this project are in the directory `tests/integration_tests`, and the tests have the decorator `@pytest.mark.integration_test` provided by the `pytest-integration` package. Marking these tests as integration tests makes them run after the unit tests. The isolated nature and specficity of *unit tests* make them a much better tool for debugging. Hence, we want to run the unit tests before the integration tests.

For more on different types of software testing, [here is a helpful resource](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing). 

*The integration tests use the package `pytest-integration`. To insure that `pytest` is using the version installed in your `venv` and not the globally installed `pytest`, deactivate and reactive your virtual environment after you've installed the requirements. This step is important to make sure the integration tests run after the unit tests.*

## Code Coverage

Code coverage is a term used to describe how much application code is executed when a particular test suite is run. It is a good practice to check our code coverage, to understand how much of our code is exercised by tests vs how much is still untested. A test suite with a high percentage of coverage is likely to be testing more throughly and have fewer bugs. A code coverage tool can partner with our testing suite to give us a report illustrating the coverage of our tests.

Given that Ada provided all test cases in this project, we should anticipate high code coverage.

Review the [code coverage exercise](https://github.com/adaGold/code-coverage-exercise) on how to use `pytest-cov` to generate a code coverage report. We will need to change the directory where the application code is located from `student` to `swap_meet`.  

`pytest --cov=swap_meet --cov-report html --cov-report term`

*Note: Code coverage is disabled for integration tests, since unit tests should cover all the code.* [source](https://pypi.org/project/pytest-integration/#:~:text=Overview,integration%20tests%20are%20not%20run)

## Project Directions

This project is designed such that one could puzzle together how to implement this project without many directions. Being able to use tests to drive project completion is a skill that needs to be developed; programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

At submission time, no matter where you are, submit the project via Learn.

### Wave 1

In Wave 1 we will create the `Vendor` class.

- There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`

- Every instance of `Vendor` has an instance method named `add`, which takes in one item
    - This method adds the item to the `inventory`
    - This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
    - This method removes the matching item from the `inventory`
    - This method returns the item that was removed
    - If there is no matching item in the `inventory`, the method should return `False`

### Wave 2

In Wave 2 we will create the `Item` class and the `get_by_category` method.

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

- Inside this module, there is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default
- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
- Instances of `Vendor` have an instance method named `get_by_category`
  - It takes one argument: a string, representing a category
  - This method returns a list of `Item`s in the inventory with that category

### Wave 3

In Wave 3 we will write a method to stringify an `Item` using `str()` and write the method `swap_items`.

- When we stringify (convert to a string) an instance of `Item` using `str()`, it returns `"Hello World!"`
  - This implies `Item` overrides its stringify method. We may need to research the `__str__` method for more details!

The remaining tests in wave 3 imply:

- Instances of `Vendor` have an instance method named `swap_items`
  - It takes 3 arguments:
    1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
    2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
    3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
  - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
  - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
  - It returns `True`
  - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

### Wave 4

In Wave 4 we will write one method, `swap_first_item`.

- Instances of `Vendor` have an instance method named `swap_first_item`
  - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
  - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
  - It removes the first item from its `inventory`, and adds the friend's first item
  - It removes the first item from the friend's `inventory`, and adds the instances first item
  - It returns `True`
  - If either itself or the friend have an empty `inventory`, the method returns `False`

### Wave 5

In Wave 5 we will create three additional modules with three additional classes:

- `Clothing`
  - Has an attribute `category` that is `"Clothing"`
  - Its stringify method returns `"The finest clothing you could wear."`
- `Decor`
  - Has an attribute `category` that is `"Decor"`
  - Its stringify method returns `"Something to decorate your space."`
- `Electronics`

  - Has an attribute `category` that is `"Electronics"`
  - Its stringify method returns `"A gadget full of buttons and secrets."`

- All three classes and the `Item` class have an attribute called `condition`, which can be optionally provided in the initializer. The default value should be `0`.

- All three classes and the `Item` class have an instance method named `condition_description`, which should describe the condition in words based on the value, assuming they all range from 0 to 5. These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these (e.g. 'You probably want a glove for this one..."). The one requirement is that the `condition_description` for all three classes above have the same behavior.

#### Using Inheritance

Now, we may notice that these three classes hold the same types of state and have the same general behavior as `Item`. That makes this is a great opportunity to use inheritance! If you haven't already, go back and implement the `Clothing`, `Decor`, and `Electronics` classes so that they inherit from the `Item` class. This should eliminate repetition in your code and greatly reduce the total number of lines code in your program!

##### Hint: Importing Item

You'll need to refer to `Item` in order to declare it as a parent. To reference the `Item` class from these modules, try this import line:

```python
from swap_meet.item import Item
```

### Wave 6

In Wave 6 we will write two methods, `get_best_by_category` and `swap_best_by_category`.

- `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
  - It takes one argument: a string that represents a category
  - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
    - It returns this item
    - If there are no items in the `inventory` that match the category, it returns `None`
    - It returns a single item even if there are duplicates (two or more of the same item with the same condition)

The remaining tests in wave 6 imply:

- `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
  - It takes in three arguments
    - `other`, which represents another `Vendor` instance to trade with
    - `my_priority`, which represents a category that the `Vendor` wants to receive
    - `their_priority`, which represents a category that `other` wants to receive
  - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
    - It returns `True`
    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

### DRYing up the code

To further reduce the amount of repeated code in your project, consider how `swap_best_by_category` and `swap_first_item` might be able to make use of `swap_items`. Is there a way that these methods could incorporate a call to `swap_items` into the body of these methods?

Try it out and see if the tests still pass! If you can't get them to pass with this refactor, you can always return to the most recent working commit before you submit the project!

## Optional Enhancements

Should a project be completed before submission, and there is a desire for optional enhancements, consider this idea:

- `Item`s have age
  - Add an `age` attribute to all `Item`s
  - Implement a `Vendor` method named `swap_by_newest`, using any logic that seems appropriate
  - Write unit tests for `swap_by_newest`

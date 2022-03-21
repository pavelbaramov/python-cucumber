# python-cucumber

## Setup:

#### Clone the repo

`$ git clone git@github.com:tbeede/python-cucumber.git`

`$ cd python-cucumber`

#### Configure the project

Navigate to

`$ cd features/environment.py`

Add your Gmail username and password credentials.

Edit `$ features/browser.py` 

to point to 

`$ home/full/path/to/python-cucumber/drivers/chromedriver`

Some packages such as selenium will likely need to be installed locally as part of the project.

#### To run all tests

Run

`$ behave`

from project root.

#### To run an individual test by feature tag

`$ behave --tags=tag_name`

For example, 

`$ behave --tags=login`

#### Features and Test Steps in This Repo

`before_each` is configured on all tests to log in by default, therefore the login feature tests will have to be run separately for now or they will interfere with the other tests.

Also, a LOT of custom xpath had to be written to handle the dynamic elements, and for this reason some tests are stronger and more reliable than others. The final test in the list below is very finicky when handling the "move to" dropdown to move a message into a folder.

Using Page Object Model design pattern & BDD, implement the following test scenarios: \
1. Scenario Outline for login functionality using the following users (standard_user, \
locked_out_user, problem_user, performance_glitch_user) \
2. Scenario with "standart_user" where multiple items checkout with their price validation \
using Cucumber Data Tables \
3. Scenario which verifies table order dropdown \
4. Add simple reporting for the scenarios

*Requires message parameters to be set in `feature` file

Choose an appropriate framework for the task and motivate your choice covering at least
the following:
1. What options did you evaluate? 
  - Python + Behave = The Best and most beautiful solution.
2. Why did you select this framework?
  - It's lightweight and super fast, easy to read and understand. \
3. What are the main advantages of the selected framework?
  - Clear and well defined code by requirements.
4.What are the main disadvantages of the selected framework?
  - Still searching for them.


#### Other improvements
* Configure logging
* Configure multiple browser drivers such as geckodriver
* Configure screen capture and reports
* API tests to get around brittle xpath / custom xpath

### About the Behave Framework

Behave is a Gherkin-based Behavior-Driven Development (BDD) tool developed especially for Python. Read more about it [here](https://behave.readthedocs.io/en/latest/).




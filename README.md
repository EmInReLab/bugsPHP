# bugsPHP

This repository contains PHP bug collection

The projects
---------------
bugsPHP contains 513 bugs from the following open-source projects:

| **Project name**                        | **Number of bugs** |
|-----------------------------------------|--------------------|
| laravel--framework                      |                106 |
| composer--composer                      |                 18 |
| symfony--symfony                        |                195 |
| guzzle--guzzle                          |                  1 |
| DesignPatternsPHP--DesignPatternsPHP    |                  1 |
| Seldaek--monolog                        |                  7 |
| PHPMailer--PHPMailer                    |                  2 |
| briannesbitt--Carbon                    |                 20 |
| nikic--PHP-Parser                       |                  3 |
| w7corp--easywechat                      |                 11 |
### Note
Download the test repositories file [here](https://drive.google.com/file/d/1-3gJzSDDzmM8JCEKRXv2pLMAGbxbO5wz/view?usp=share_link), and put it with main.py file
## Commands

The command-line interface includes the following commands:

* -p: Project name
* -b: Bug number
* -t: task
    * checkout: checks-out the source code
    * install: install the necessary packages
    * test: run all the test cases
    * test-changed: run only updated test files ( or run only given test file)
* -v: bug version
    * buggy: the original buggy code
    * fixed: bug fixed code with updated test cases
    * bug_with_test: buggy code with updated test cases
* -o: output path where the source code should be checkout
* -f: test file path (not required)

#### Example commands

1. Checks-out the source code for a given bug
   ```
   python3 main.py -p composer--composer -b 1 -t checkout -v fixed -o /content/tmp/
   ```
2. Install the necessary packages
   ```
   python3 main.py -p composer--composer -b 1 -t install -v fixed -o /content/tmp/
   ```
3. Run all the test cases
   ```
   python3 main.py -p composer--composer -b 1 -t test -v fixed -o /content/tmp/
   ```
# bugsPHP
# bugsPHP
# bugsPHP
# bugsPHP
# bugsPHP
# bugsPHP

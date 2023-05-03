# bugsPHP

This repository contains PHP bug collection

The projects
---------------
bugsPHP contains 513 bugs from the following open-source projects:

| **Project name**                  | **Number of bugs** |
|-----------------------------------|--------------------|
| cakephp--cakephp                  |                 33 |
| briannesbitt--Carbon              |                 11 |
| composer--composer                |                 18 |
| doctrine--dbal                    |                  9 |
| w7corp--easywechat                |                  9 |
| laravel--framework                |                 94 |
| googleapis--google-api-php-client |                  3 |
| spatie--laravel-permission        |                  6 |
| magento--magento2                 |                 23 |
| Seldaek--monolog                  |                  7 |
| doctrine--orm                     |                 15 |
| PHP-CS-Fixer--PHP-CS-Fixer        |                 82 |
| nikic--PHP-Parser                 |                  3 |
| PHPOffice--PhpSpreadsheet         |                 12 |
| symfony--symfony                  |                188 |
### Note
Download the test repositories file [here](https://drive.google.com/file/d/1c1CKv20uCVHfmd5FIxxeqHc0uWpm_jsB/view?usp=share_link), and put it with main.py file
## Commands

The command-line interface includes the following commands:

* -p: Project name
* -b: Bug number
* -t: task
    * checkout: checks-out the source code
    * install: install the necessary packages
    * test: run all the test cases
    * failing-test-only: run only failing test cases
* -v: bug version
    * buggy: the original buggy code
    * fixed: bug fixed code with updated test cases
* -o: output path where the source code should be checkout

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
4. Run failing test cases
   ```
   python3 main.py -p composer--composer -b 1 -t failing-test-only -v fixed -o /content/tmp/
   ```

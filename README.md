# bugsPHP

This repository contains PHP bug collection

## Contributors:
### Authors
K.D. Pramod, W.T.N. De Silva, W.U.K. Thabrew, Ridwan Shariffdeen, Sandareka Wickramanayake

### Principal Investigators
* Ridwan Shariffdeen
* Sandareka Wickramanayake

### Developers
* K.D. Pramod
* W.T.N. De Silva
* W.U.K. Thabrew


Test Dataset
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

## Installation instructions

1. Download the test repositories archive file [here](https://drive.google.com/file/d/1Y3BAH-kXcmYp9pGOSJ6AxkQu_3YhLyo1/view?usp=sharing), and put it next to the `main.py` script. Do not extract the archive; the script is designed to handle it automatically.
2. Install required dependencies:
   ```bash
   sudo apt install p7zip-full php-all-dev
   pip install --user pydash
   ```

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

Training dataset
---------------

You can find the training dataset in [here](https://drive.google.com/drive/folders/175U3QoG69T8gSnoyOFA0IgK-Ye93kL_X?usp=sharing), It contains 5 zip files and json file with meta info.
 * unzip the zip files. 
 * use the following path formats to find bugs. (repo_owner, repo_name, and bug_no can find in the meta.json file)
   * {repo_owner}--{repo_name}/{repo_name}/{bug_no}/buggy
   * {repo_owner}--{repo_name}/{repo_name}/{bug_no}/fixed
  

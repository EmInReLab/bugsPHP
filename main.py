import argument_parser
import myProject
import myTest
import os
import sys
import subprocess as sp

SCRIPTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
if(not os.path.exists(os.path.join(SCRIPTDIR,'bug_metadata.json'))):
    extract_cmd = "7z e " + SCRIPTDIR + "/bug_metadata.7z " + "-o" + SCRIPTDIR
    sp.call(extract_cmd, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

param_dict = argument_parser.arg_parser()
if(param_dict["task"] == "checkout"):
    myProject.checkout(param_dict)
elif(param_dict["task"] == "install"):
    myTest.install(param_dict)
elif(param_dict["task"] == "test" and param_dict["test-case"] != None):
    myTest.run_single_test_case(param_dict)
elif(param_dict["task"] == "test"):
    myTest.run_all_test(param_dict)
elif(param_dict["task"] == "failing-test-only"):
    myTest.run_all_failing_test(param_dict)
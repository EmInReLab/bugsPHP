import os
import subprocess as sp
import sys
import json
import shutil


def checkout(param_dict):
    SCRIPTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
    bug_info = get_bug_info(param_dict)
    print('Extracting ...', 'project =', bug_info['repo_full_name'], 'bug_no =', bug_info['bug_no'])
    extract_repo(bug_info, param_dict["output"])
    
    print('Checking out ...', 'project =', bug_info['repo_full_name'], 'bug_no =', bug_info['bug_no'])
    checkout_fixed_cmd = ["git", "checkout","-f", bug_info['fixed_commit_id']]
    checkout_buggy_cmd = ["git", "checkout","-f", bug_info['bug_commit_id']]
    if(param_dict["version"] == "fixed"):
        sp.call(checkout_fixed_cmd, shell=False, cwd=os.path.join(param_dict["output"], bug_info['repo_name']), stdout=sp.DEVNULL, stderr=sp.STDOUT)
    elif(param_dict["version"] == "buggy"):
        shutil.copytree(param_dict["output"], os.path.join(param_dict["output"], 'tmp-' + bug_info['fixed_commit_id']))
        
        sp.call(checkout_fixed_cmd, shell=False, cwd=os.path.join(param_dict["output"], bug_info['repo_name']), stdout=sp.DEVNULL, stderr=sp.STDOUT)
        sp.call(checkout_buggy_cmd, shell=False, cwd=os.path.join(param_dict["output"], 'tmp-' + bug_info['fixed_commit_id'], bug_info['repo_name']), stdout=sp.DEVNULL, stderr=sp.STDOUT)
        
        for changed_file_path in bug_info['changed_file_paths']:
            src_path = os.path.join(param_dict["output"], 'tmp-' + bug_info['fixed_commit_id'], bug_info['repo_name'], changed_file_path)
            dst_path = os.path.join(param_dict["output"], bug_info['repo_name'], changed_file_path)
            if(os.path.exists(src_path)):
                if(os.path.exists(dst_path)): 
                    os.remove(dst_path)
                shutil.copy(src_path, dst_path)
                
        shutil.rmtree(os.path.join(param_dict["output"], 'tmp-' + bug_info['fixed_commit_id']), ignore_errors=False)
    else:
        exit()



def get_bug_info(param_dict):
    SCRIPTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
    print(SCRIPTDIR)
    with open(os.path.join(SCRIPTDIR, "bug_metadata.json"), 'r') as infile:
        bug_list = json.load(infile)
        for bug in bug_list:
            if(param_dict["project"] == bug["repo_owner"] + '--' + bug['repo_name'] and bug['bug_no'] == param_dict['bug-no']):
                return bug
    print("I can't find the bug in the json file")
    exit()


def extract_repo(bug_info, folder):
    SCRIPTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))

    if os.path.isdir(folder):
        rm_cmd = "rm -R "+str(folder)
        sp.call(rm_cmd, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
    os.makedirs(folder)

    extract_cmd = "7z x " + SCRIPTDIR + "/repositories.7z " + "-o" + folder + " " + os.path.join("test_repositories", bug_info['repo_owner'] + "--" + bug_info['repo_name'], bug_info['repo_name']) + "/*.* -r -y"
    sp.call(extract_cmd, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

    move_cmd = "mv " + os.path.join(folder, 'test_repositories',
                                    bug_info['repo_owner'] + "--" + bug_info['repo_name'], bug_info['repo_name']) + " " + folder
    sp.call(move_cmd, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

    delete_cmd = "rm -r " + os.path.join(folder, 'test_repositories')
    sp.call(delete_cmd, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

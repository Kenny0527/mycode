#!/usr/bin/bash

# standard library imports
import shutil # shell utilities will be used to move files
import os     # provides access to low level os operations (agnostic to flavor of OS)

def main():
    """ called at runtime """
    # move into this working directory
    os.chdir('/home/student/mycode/')
    
    # try moving the file raynor.obj into ceph_storage/ dir
    shutil.move('raynor.obj', 'ceph_storage/')

    # program will pause while we accept a new input
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

# this calls our main function by checking the global var __name__
if __name__ == "__main__":
    main()


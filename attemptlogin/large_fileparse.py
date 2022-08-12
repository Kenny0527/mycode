#!/usr/bin/python3

def main():

    # parse keystone.common.wsgi and return number 
    # of failed login attempts
    loginfail = 0 # counter for fails

    # loop the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

    for line in keystone_file:

        # if this "fail pattern" appears in the line...
         if "- - - - -] Authorization failed" in line:
             loginfail += 1 # this is the same loginfail
    print("The number of failed log in attempts is", loginfail)
    keystone_file.close() # close the open file

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    # parse keywtone.common.wsgi and return number of
    # failed login attempts.
    loginFail = 0 # counter for fails

    # open the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

    # turn the file into a list of lines in memory
    keystone_file_lines = keystone_file.readlines()

    # loope over the list of lines
    for line in keystone_file_lines:
        #if this "fail pattern" appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginFail += 1

    print("The number of failed log in attempts is ", loginFail)
    keystone_file.close() # close the open file

if __name__ == "__main__":
    main()

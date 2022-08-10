#!/user/bin/env python3
"""Alta3 Research | RZFeeser
print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address: ")
    
    # display the input back to the user
    print("You told me the IPv4 address is: " + user_input)

    # collect and store input from the user.
    # ask the user for the "vendor name" associated with the device.
    vendor_name = input("Please input the vendor name associated with the device: ")
    
    # Use a second line of code to print the input you just collected from the user.
    print("You told me the vendor name is: " + vendor_name)

# main function call
main()


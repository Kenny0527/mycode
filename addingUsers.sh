#!/bin/bash

# varibale used to check if we need to add another user
anotherUser="true" 
groupadd people

# while loop checking to see if we need to add another user
while [ $anotherUser == "true" ]
do
    echo "What is the name of the new user?"
    read newUser
    sudo adduser $newUser
    sudo usermod -aG people $newUser

    echo "Would you like to add another user? y/n"
    read newUser
    if [ $newUser == "y" ]
    then
        anotherUser="true";
    else
        anotherUser="false";
    fi
done

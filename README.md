# SAS
Steam account switcher done through python.

For the GUI, I have used "PySimpleGUI", which you can check out here: https://www.pysimplegui.org/en/latest/

Basically, you have to first log into the accounts you would like to switch between.

![image](https://user-images.githubusercontent.com/97501461/201097919-58484dc0-b435-4756-8ea4-8f3c3be0c37a.png)


The application works by changing the steam login registry information, it would just change the username to the one you would like to login with, and change the remember me to true.

Moreover, the application makes a .dat file which stores the username information, one file for each account.
Even though this approach might take more space or resources, this is easier than creating one file and appending to it each time, might update it later on to fix it up.

![image](https://user-images.githubusercontent.com/97501461/201098015-83b6f83e-c409-43a6-ad3c-f2e5ce483d9c.png)

![image](https://user-images.githubusercontent.com/97501461/201098059-3147b2f7-72b4-4cce-b59a-2c7876dc3856.png)

So after creating the .dat file, it would create the batch file with the username information, which will execute when you press on the username button, it will firstly kill the current steam process, and then will open it back up with the desired account.

The batch file information I took was from reddit, from the user u/Maxdec94.

This is not the first time this idea has been made, but this is my approach to this case.

Feel free to change it up however you like and use it, but please if you use any part of this code give credit.

Thank you!

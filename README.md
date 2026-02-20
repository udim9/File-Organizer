# File-Organizer

# How to use

- replace the value of the username variable (line 6) with the name in your file directories
- to check what that name is open a file on file explorer, right click it and click copy as path
- paste that into a new tab and it should be layed out like this C:\Users\[YOUR NAME HERE]\filename

- then replace the cooldown variable's value with the amount of seconds you want the program to wait before it runs again
- (The higher the number the less it will use up your cpu)

- then you can run the program with the command "python3 Main.py" in the terminal!

# How it works

- Program runs
- Checks every file in downloads
- waits [cooldown] seconds
- checks again
- every file that is different is put into a set
- every file in that set's file exstension is checked
- the file will be moved to the folder corresponding to the file's extension
- eg. '.png' files will be moved to the pictures folder
- repeats

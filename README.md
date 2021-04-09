# TAWorldCheck
This is a simple python script that scrapes the TA announcements forum for any new posts and alerts the user when a new world announcement is made in the forums.

Usage:
The idea is to create a batch file or a process that runs the python script once a day. When a new world announcement is made, a message pop up is created on the next run notifying the user.

Dependancies:
- python 3 (I'm using 3.9.4)
- requests
- BeautifulSoup4

Installation:
  Assuming you dont have python or any of the packages installed, the following is the full installation process
  
  1. Get the latest version of python from https://www.python.org/downloads/
  2. Open a command propt window and install packages
      - pip install beautifulsoup4
      - pip install requests
  3. Setup a task schedule to run the script once a day using the windows task scheduler

![image](https://user-images.githubusercontent.com/24622955/114113771-ca7c1780-9922-11eb-9376-8458a2537806.png)

![image](https://user-images.githubusercontent.com/24622955/114113788-d5cf4300-9922-11eb-8ffa-fd013e9b60dd.png)

![image](https://user-images.githubusercontent.com/24622955/114113826-ea134000-9922-11eb-8666-4fc080f180f2.png)

And thats it!

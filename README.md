# python-developer-customerlab

## Steps
Check both version 
![image](https://github.com/user-attachments/assets/a4d014a9-9847-46c5-be79-0ea694b27501)

create and Activate python virtual environment which contains django, pip,requests installed

run django server
![image](https://github.com/user-attachments/assets/4abde44a-0a50-4b6d-a64f-e847dc0d6b8a)

check browser to confirm
![image](https://github.com/user-attachments/assets/3bc2fb8b-2502-49d0-9645-0e784d0678c5)

if we go to /account/ we will see something

next run test.py provided in repo 
![image](https://github.com/user-attachments/assets/fb4fa791-d268-4f3c-914f-be45ea27f093)

we will see some messages in running django cli 
![image](https://github.com/user-attachments/assets/1ed5bf63-caae-4568-93fe-ae7b13950bde)

the test.py script will push some data via webhook url( here locally hosted django ) and the django server will get that data from the webhook url and parse some information and sent it to destination (here used sample webhook.site url ) 

to confirm we can see in webhook.site with the url
![image](https://github.com/user-attachments/assets/01292ffc-4996-446f-888a-1f7fcc349a96)






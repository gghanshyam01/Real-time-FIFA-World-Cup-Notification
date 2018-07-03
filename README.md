# Real-time-FIFA-World-Cup-Notification
This script fetches the live commentary of the current FIFA World Cup matches and sends it to your mobile number across India.

Steps to use this script:
1. You'll need an account on way2sms.com through which this script is sending SMS.
2. After creating an account, save your credentials in a file keys.py
  Ex. 
    username = <Your username>
    password = <Your password>
    receiver_num = <Phone number on which you want to send message>
3. Next go to http://www.goal.com/en-in/live-scores. There you'll see list of world cup matches lined up for today.
   Click on that matches for which you wish to get live commentary. Copy the url and assign it on MATCH_URL variable on file live-score.py.
   
  Thats it.. ENJOY !

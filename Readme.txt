WhatsApp Message Automation Script
==================================

Description:
------------
This Python script automates the process of opening WhatsApp Web in a browser 
and sending repeated messages to a contact using the PyAutoGUI library.

⚠️ WARNING: This script uses screen coordinates and automation, which may behave 
differently on various screen sizes and setups. Use responsibly and only with consent.

Features:
---------
- Opens Microsoft Edge
- Navigates to WhatsApp Web
- Waits for manual QR code scan (20 seconds delay)
- Searches for a contact
- Sends "hi" message 10 times automatically

Requirements:
-------------
- Python 3.x
- pyautogui library

Install dependencies:
    pip install pyautogui

Usage:
------
1. Make sure your display matches the coordinates used in the script:
   - Taskbar location: bottom-left
   - Edge browser is installed and accessible via "edge" command
   - WhatsApp Web is accessible at https://web.whatsapp.com
   - Contact to message is named "balaji"

2. Run the script:
       python "whatsapp messger.py"

3. After opening WhatsApp Web, scan the QR code manually during the 20-second delay.

4. The script will:
   - Search for the contact "balaji"
   - Send the message "hi" ten times with a 1-second delay between messages

Customization:
--------------
- To change the contact, modify the string:
      py.typewrite("balaji")

- To change the message or count:
      for i in range(10):
          py.typewrite("hi")

Legal Notice:
-------------
Do not use this script to spam or harass others.
Always get consent from the person you're messaging.

Disclaimer:
-----------
This script is provided for educational and personal automation use only.
The author is not responsible for misuse, unintended behavior, or hardware issues.

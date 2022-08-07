"""A SMS reminder script. messages are sent through Twilio REST API to the
recipient reminding them of their specified event/topic."""

import datetime
import time
from twilio.rest import Client


def send_reminder(recipient, msg_content):
    """Create and send the reminder message."""
    # Your Account SID from twilio.com/console
    account_sid = "Enter_your_account_SID_here"
    # Your Auth Token from twilio.com/console
    auth_token = "Enter_your_auth_token_here"

    client = Client(account_sid, auth_token)

    client.messages.create(
        # Number to send message to.
        to="+44" + recipient[1:],
        # Number to send from (number created through twilio.)
        from_="Enter_your_virtual_number_here",
        body=f"Hi - This is your reminder regarding: '{msg_content}'.")


if __name__ == '__main__':

    # Gather relevent information from user:
    reminder_time = input(
        "What time would you like to recieve your reminder (24 hrs - HH:MM): ")

    reminder_topic = input("What would you like to be reminded about: ")

    mobile_num = input(
        "What mobile number would you like to send the reminder to: ")

    # specify what the time is now in order to start the while loop below:
    time_now = datetime.datetime.now().strftime("%H:%M")

    while time_now != reminder_time:
        # re-check the time every 10 seconds. Loop ends when the time matches the time
        # that the user wants to be reminded at.
        time.sleep(10)
        time_now = datetime.datetime.now().strftime("%H:%M")

    # Call function to send reminder message once the loop above has ended.
    send_reminder(mobile_num, reminder_topic)

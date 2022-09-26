from twilio.rest import Client

TWILLIO_ID = 'ACa5c48c331f5d295f38fbd9807f0114be'
AUTH_TOKEN = 'c35fa39ee434efe6c8c8c974accb6fc3'
TWILLIO_VIRTUAL_NUMBER = '19897188788'
TWILLIO_VARIFIED_NUMBER = '+919033978017'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILLIO_ID, AUTH_TOKEN)

    def send_sms(self, message):

        send_message = self.client.messages.create(
        body=message,
        from_=TWILLIO_VIRTUAL_NUMBER,
        to=TWILLIO_VARIFIED_NUMBER
                                                    )
        print(send_message.sid)


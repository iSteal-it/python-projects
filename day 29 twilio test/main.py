
from twilio.rest import Client

account_sid = ''
auth_token = ''


client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='',
    body='HI GUY',
    to='+'
)

print(message.sid)

from twilio.rest import Client
import os
account_sid = os.environ['AC6f30a0404751cb9e8d124007098ec761']
auth_token = os.environ['247fdf2dc941fe210464f8febe03d255']
client = Client(account_sid, auth_token)
from_ = 'whatsapp+918529126697'
to_ = 'whatsapp+919680739320'

message = client.message.create(
    body='hello its testing',
    media_url='./1143272.jpg',
    from_ = from_,
    to_ = to_
)
print(message.sid)
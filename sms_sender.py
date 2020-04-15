from twilio.rest import Client

account_sid = 'AC3bcb0328848b56602672fe5773ddac38'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14784002807',
    to='+96897136721'
)

print(message.sid)
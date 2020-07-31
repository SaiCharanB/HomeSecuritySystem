from twilio.rest import Client





account_sid = 'AC524937e65452ba5e47668ba69c969a9d'
auth_token = 'dffaec80d0f4885159210352302f30b0'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Alert. Intruder!",
                     from_='+15153934072',
                     to='+919940684356'
                 )

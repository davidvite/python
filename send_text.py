from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0379b537720199f6c5fe5d999ae2fc25"
auth_token  = "4c1d52e06156db8df73b92b16966e3b9"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I love myself <3",
    to="+13853754728",    # Replace with your phone number
    from_="+17472258483") # Replace with your Twilio number
print message.sid
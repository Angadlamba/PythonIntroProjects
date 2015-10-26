from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd875fa9252450bfcc5fb62f1f738d652"
auth_token  = "b449ff860f2aec123612af931f0d630f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(
	body="What's up angad, Its Angad!!!",
    to="+919983997435",    # Replace with your phone number
    from_="+1 334-721-2997") # Replace with your Twilio number
print message.sid
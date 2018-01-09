from twilio.rest import Client
import RPi.GPIO as GPIO
import dht11
import time
# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 14)

while True:
	result = instance.read()
	if result.is_valid():
		client = Client(account_sid, auth_token)
		string  = "Humidity is " + str(result.humidity) + " and Temperature is " + str(result.temperature)
		message = client.messages.create(
		    to="+91986866719", 
		    from_="+15017250604",
		    body=string)
		print (message.sid)

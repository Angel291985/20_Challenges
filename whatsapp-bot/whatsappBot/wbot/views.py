from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'AC90ab1ca87c094cd6628fd02128a29d63'
auth_token = 'd28232c935557e1b8a327a795fc06883'
client = Client(account_sid, auth_token)

# Create your views here.
@csrf_exempt
def bot(request):
    message = request.Post["message"]

    if message == "hi":
        client.messages.create(
            from_='whatsapp:+14155238886',
            body='Hello, there!',
            to='whatsapp:+27733782752'
        )
    return HttpResponse('hello')

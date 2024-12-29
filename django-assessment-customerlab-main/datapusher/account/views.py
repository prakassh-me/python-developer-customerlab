from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import requests


# Create your views here.

template = loader.get_template('first.html')

@csrf_exempt 
def account(request):
    if request.method == "POST":
        return HttpResponse()
    elif request.method == "GET":
        print("GET call occured")
        context = {
        'mymembers': "this will display if get call if happened",
        }
        
        return HttpResponse(template.render(context, request))
    else:
        pass
    
@csrf_exempt
def webhook (request):
    if request.method == "POST":
        print("..... POST CALL .....")
        post_dict = json.loads(request.body.decode()) # decode the bytes and saves as dict
        print("..... DATA LOADED SUCCESSFULLY .....")
        des_dict = {}

        des_dict['Acc_sec_token'] = post_dict["CL-X-TOKEN"]
        des_dict['plan'] = "User account created and subscribed to < this > services"
                
        dest_webhook_url = "https://webhook.site/33365a7f-0cdd-471f-94e4-a69925a85941" # destination webhook url for sending a quick notification for which user created account
        r = requests.post(dest_webhook_url, data = json.dumps(des_dict), headers={'Content-Type': 'application/json'}) # sending data to destination
        print("..... DESTINATION WEBHOOK HAS BEEN NOTIFIED")
        return HttpResponse()
    else :
        return HttpResponse()

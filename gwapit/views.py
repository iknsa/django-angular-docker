from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

import requests
import json

def home(request):
    """ Rest endpoint here because we are authentified """
    context = RequestContext(request,
                             {'request': request, 'user': request.user})

    if request.user.is_authenticated :
        social = request.user.social_auth.get(provider='google-oauth2')

        maxResults = 3

        response = requests.get('https://www.googleapis.com/gmail/v1/users/bazard.philippe@gmail.com/messages?key=',
                                params={'access_token': social.extra_data['access_token'],
                                        'maxResults': maxResults,
                                        })


        print(response.headers)
        print(response.json())

        message_list = response.json()

        for k, v in message_list.items():
            print k, v


        req_msg = 'https://www.googleapis.com/gmail/v1/users/' + social.uid + '/messages/' + '157f6211b0203baf' + '?key='
        response = requests.get(req_msg, params={'access_token': social.extra_data['access_token']})
        #print(response.json())
    return render_to_response('home.html', context)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))


def get_mail(request):
    """..."""
    messages = []
    message_list = []

    if request.user.is_authenticated :
        social = request.user.social_auth.get(provider='google-oauth2')

        maxResults = 10
        # Get the messages ids
        response = requests.get('https://www.googleapis.com/gmail/v1/users/bazard.philippe@gmail.com/messages?key=',
                                params={'access_token': social.extra_data['access_token'],
                                        'maxResults': maxResults,
                                        })

        # for each message id get the message data
        for msg in response.json()['messages']:
            req_msg = 'https://www.googleapis.com/gmail/v1/users/' + social.uid + '/messages/' + msg['id'] + '?key='
            response = requests.get(req_msg, params={'access_token': social.extra_data['access_token'], 'format': 'metadata'})
            message_list.append(response.json())


        data = json.dumps(message_list)

    else:
        data = {
            'ERROR': 'Not connected',
        }
        data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')
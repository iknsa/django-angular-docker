import requests
import json
import time
from functools import wraps
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

def timethis(func):
    """..."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
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
    return render_to_response('home.html', context)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))


@timethis
def get_mail(request):
    """..."""
    messages = []
    message_list = []

    email_list=[]

    if request.user.is_authenticated :
        social = request.user.social_auth.get(provider='google-oauth2')

        maxResults = 100
        # Get the messages ids
        response = requests.get('https://www.googleapis.com/gmail/v1/users/' + social.uid + '/messages?key=',
                                params={'access_token': social.extra_data['access_token'],
                                        'maxResults': maxResults,
                                        })
        # for each message id get the message data
        for msg in response.json()['messages']:
            req_msg = 'https://www.googleapis.com/gmail/v1/users/' \
                      + social.uid \
                      + '/messages/' \
                      + msg['id'] \
                      + '?key='\
                      + '&fields=snippet,payload/headers'
            response = requests.get(req_msg, params={'access_token': social.extra_data['access_token']})
            message_list.append(response.json())

        message_list_dict = {}

        # iterate over dictionaries
        for element in message_list:
            email = {}
            email['snippet'] = element['snippet']
            headers = element['payload']['headers']

            for entry in headers:
                if entry['name'] == 'From':
                    email['from'] = entry['value']

            email_list.append(email)

        data = json.dumps(email_list)

    return HttpResponse(data, content_type='application/json')
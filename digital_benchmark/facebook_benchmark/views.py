from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

import requests

from .data_provider import FacebookDataProvider
from .forms import LoginForm

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'facebook_benchmark/login.html', context)
    
    def post(self, request, *args, **kwargs):
        url = 'https://www.facebook.com/v{version}/dialog/oauth?client_id={app_id}&redirect_uri={redirect_uri}&scope={permissions}&response_type={response_type}&state={state}'.format(version=settings.FACEBOOK_GRAPH_API_VERSION, app_id=settings.FACEBOOK_APP_ID, redirect_uri=settings.FACEBOOK_LOGIN_SUCCESSFUL_REDIRECT_URI, permissions=','.join(settings.FACEBOOK_PERMISSIONS), response_type=settings.FACEBOOK_RESPONSE_TYPE, state=settings.FACEBOOK_STATE)
        return redirect(url)

class LoginSuccessfulView(View):
    def get(self, request):
        code = request.GET['code']
        url = 'https://graph.facebook.com/v{version}/oauth/access_token'.format(version=settings.FACEBOOK_GRAPH_API_VERSION)
        data = {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': settings.FACEBOOK_LOGIN_SUCCESSFUL_REDIRECT_URI,
            'client_secret': settings.FACEBOOK_APP_SECRET,
            'code': code,
        }
        response = requests.post(url, data=data).json()
        return redirect('/facebook_benchmark/home')

class HomeView(View):
    def get(self, request):
        return render(request, 'facebook_benchmark/home.html')
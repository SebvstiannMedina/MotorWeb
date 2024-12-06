from django.shortcuts import render
from user_agents import parse
import urllib.parse

def index(request):
    apk_url = 'https://github.com/SebvstiannMedina/apkmovil/raw/main/Motor_Sphere.apk'
    
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)
    is_mobile = user_agent.is_mobile
    
    return render(request, 'automotora/index.html', {
        'apk_url': apk_url,
        'is_mobile': is_mobile
    })
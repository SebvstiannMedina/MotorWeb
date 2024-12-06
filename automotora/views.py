from django.shortcuts import render
from user_agents import parse
import urllib.parse

def index(request):
    apk_url = 'https://github.com/SebvstiannMedina/apkmovil/raw/main/Motor Sphere.apk'
    encoded_apk_url = urllib.parse.quote(apk_url)
    
    # Asegúrate de que el header HTTP_USER_AGENT existe
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)
    is_mobile = user_agent.is_mobile
    
    return render(request, 'automotora/index.html', {
        'apk_url': encoded_apk_url,
        'is_mobile': is_mobile
    })

# Puedes eliminar la función home si no la necesitas
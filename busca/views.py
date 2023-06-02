from django.shortcuts import render
from django.http import JsonResponse
import requests

def consulta_cep(request, cep):
    url = f'https://brasilapi.com.br/api/cep/v1/{cep}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'CEP not found'}, status=404)
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings

def index(request):
    return render(request, 'residents/index.html')

def send_resident_to_supabase(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    apartment = request.POST.get('apartment')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'name': name, 'age': age, 'apartment': apartment}]
    resultado, erro = supabase.table('residents_resident').upsert(dados).execute()

    if erro:
        return HttpResponse(f"Erro ao enviar dados para o Supabase: {erro}")
    else:
        return HttpResponse("Dados enviados com sucesso para o Supabase!")

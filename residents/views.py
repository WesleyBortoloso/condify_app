from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings
from setup.utils.get_table_data import get_table_data

def index(request):
    data = get_table_data('residents_resident')

    context = {
        'data': data,
    }

    return render(request, 'residents/index.html', context)

def send_resident_to_supabase(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    apartment = request.POST.get('apartment')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'name': name, 'age': age, 'apartment': apartment}]
    resultado, erro = supabase.table('residents_resident').upsert(dados).execute()

    return redirect('resident_index')

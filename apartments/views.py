from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings
from setup.utils.get_table_data import get_table_data

def index(request):
    data = get_table_data('apartments_apartment')

    context = {
        'data': data,
    }

    return render(request, 'apartments/index.html', context)

def send_apartment_to_supabase(request):
    number = request.POST.get('number')
    bedrooms = request.POST.get('bedrooms')
    bathrooms = request.POST.get('bathrooms')
    description = request.POST.get('description')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'number': number, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'description': description}]
    resultado, erro = supabase.table('apartments_apartment').upsert(dados).execute()

    return redirect('apartments_index')

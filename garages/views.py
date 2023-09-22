from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings
from setup.utils.get_table_data import get_table_data

def index(request):
    data = get_table_data('garages_garage')

    context = {
        'data': data,
    }

    return render(request, 'garages/index.html', context)

def send_garage_to_supabase(request):
    number = request.POST.get('number')
    reserved = request.POST.get('reserved')
    description = request.POST.get('description')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'number': number, 'reserved': reserved, 'description': description}]
    resultado, erro = supabase.table('garages_garage').upsert(dados).execute()

    return redirect('garages_index')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings
from setup.utils.get_table_data import get_table_data

def index(request):
    data = get_table_data('wallet_wallet')

    context = {
        'data': data,
    }

    return render(request, 'wallet/index.html', context)

def send_wallet_to_supabase(request):
    balance = request.POST.get('balance')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'balance': balance}]
    resultado, erro = supabase.table('wallet_wallet').upsert(dados).execute()

    return redirect('wallet_index')

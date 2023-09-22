from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client 
from django.conf import settings
from setup.utils.get_table_data import get_table_data

def index(request):
    data = get_table_data('notifications_notification')

    context = {
        'data': data,
    }

    return render(request, 'notifications/index.html', context)

def send_notification_to_supabase(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    dados = [{'subject': subject, 'message': message}]
    resultado, erro = supabase.table('notifications_notification').upsert(dados).execute()

    return redirect('notifications_index')

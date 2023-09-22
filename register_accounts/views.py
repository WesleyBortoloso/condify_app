from django.shortcuts import render
# from django.http import HttpResponse
# from supabase import create_client 
# from django.conf import settings

def register(request):
    return render(request, 'register/register_accounts.html')

# def send_accounts_to_supabase(request):
#     description = request.POST.get('description')
#     value = request.POST.get('value')
#     type = request.POST.get('type')

#     supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

#     dados = [{'description': description, 'value': value, 'type': type}]
#     resultado, erro = supabase.table('accounts').upsert(dados).execute()

#     if erro:
#         return HttpResponse(f"Erro ao enviar dados para o Supabase: {erro}")
#     else:
#         return HttpResponse("Dados enviados com sucesso para o Supabase!")
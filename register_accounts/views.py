from django.shortcuts import render, redirect

def register(request):
    return render(request, 'register/register_accounts.html')

def process_form(request):

    dados = {}

    if request.method == 'POST':
        tipo = request.POST.get('type')
        descricao = request.POST.get('description')
        apto = request.POST.get('apto')
        valor = request.POST.get('valor')
        numero_nota = request.POST.get('numero_nota')
        data_nota = request.POST.get('data_nota')
        numero_boleto = request.POST.get('numero_boleto')
        data_vencimento = request.POST.get('data_vencimento')

    dados['tipo'] = tipo
    dados['descricao'] = descricao
    dados['apto'] = apto
    dados['valor'] = valor
    dados['numero_nota'] = numero_nota
    dados['data_nota'] = data_nota
    dados['numero_boleto'] = numero_boleto
    dados['data_vencimento'] = data_vencimento

    return render(request, 'register/register_accounts.html', {'dados': dados})

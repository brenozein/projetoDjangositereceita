from django.shortcuts import render

def home(request):
    return render(request, 'receitas/home.html')

def receita_detail(request, id):
    context={
        'receita_id' : id,
        'receita_title' : f'Receita Detalhada {id}', 
        'receita_description' : f'Esta é a descrição detalhada da receita com ID {id}'
    }
    return render(request, 'receitas/receita_detail.html', context)
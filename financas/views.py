from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages

import os
import csv

from setup.settings import BASE_DIR
from financas.forms import ImportarCsvForm
from financas.models import Transacoes


def index(request):
    form = ImportarCsvForm()
    return render(request, "financas/index.html", {"form":form})


def importar_csv(request):
    fieldnames=[
        "banco_origem",
        "agencia_origem",
        "conta_origem",
        "banco_destino",
        "agencia_destino",
        "conta_destino",
        "valor_transacao",
        "data_transacao"
        ]

    if request.method == "POST":
        # Verificar se o arquivo está vazio

        form = ImportarCsvForm(request.FILES["arquivo"])
        text = ""
        for chunk in request.FILES["arquivo"].chunks():
            text += chunk.decode('ASCII')

        # ler primeira linha e recuperar a Data
        
        l = []
        lines = text.split("\n")
        for line in lines:
            d = {}
            empty_field = False
            values = line.split(",")
            for i, value in enumerate(values):
                value.strip()
                if value:
                    d[fieldnames[i]] = value
                else:
                    empty_field = True
                # ignorar linhas que não tenham todos os dados completos
            if not empty_field:
                l.append(d)

        # l é a lista de dicts, cada um contendo uma linha do csv 
        data = l[0]["data_transacao"].split("T")[0]
        
        for row in l:
            # checar a data de todas as transações e ignorar datas diferentes
            if row["data_transacao"].split("T")[0] != data:
                pass
            
            elif Transacoes.objects.filter(banco_origem=row["banco_origem"],
                    agencia_origem=row["agencia_origem"],
                    conta_origem=row["conta_origem"],
                    banco_destino=row["banco_destino"],
                    agencia_destino=row["agencia_destino"],
                    conta_destino=row["conta_destino"],
                    valor_transacao=row["valor_transacao"],
                    data_transacao=row["data_transacao"].split("T")[0]).exists():
                # Exibir mensagem de erro ao tentar salvar a mesma data
                messages.error(request, "Os dados para essa data já foram salvos")
                pass
            else:
                # checar se a data em questão já foi salva na db. 
                transacao = Transacoes(
                    banco_origem=row["banco_origem"],
                    agencia_origem=row["agencia_origem"],
                    conta_origem=row["conta_origem"],
                    banco_destino=row["banco_destino"],
                    agencia_destino=row["agencia_destino"],
                    conta_destino=row["conta_destino"],
                    valor_transacao=row["valor_transacao"],
                    data_transacao=row["data_transacao"].split("T")[0]
                    )
                transacao.save()
        messages.success(request, "Transações Salvas!")
        return redirect("index")
            
    return redirect('index')
#!/usr/bin/env python
# coding: utf-8


import requests
import pandas as pd
from datetime import datetime
import time

#Executa 30 vezes o codigo a cada 60 segundos para adquirir a cotação do BTC nas moedas BRL,USD,EUR.
for i in range(30):
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL,BTC-USD,BTC-EUR")

    #Requecição feita para a API para estrair a cotação do bitcoin convertidos em BRL,USD,EUR.
    requisicao_dic = requisicao.json()
    cotacao_brl = requisicao_dic["BTCBRL"]["bid"]
    cotacao_usd = requisicao_dic["BTCUSD"]["bid"]
    cotacao_eur = requisicao_dic["BTCEUR"]["bid"]

    #Tabela para armazenar a cotação na planilha de exel.
    tabela = pd.read_excel("Cotações.xlsx")
    tabela.loc[0, "Cotação"] = float(cotacao_brl) * 1000
    tabela.loc[1, "Cotação"] = float(cotacao_usd)
    tabela.loc[2, "Cotação"] = float(cotacao_eur)
    tabela.loc[0, "Data Última Atualização"] = datetime.now()
    tabela.loc[1, "Data Última Atualização"] = datetime.now()
    tabela.loc[2, "Data Última Atualização"] = datetime.now()

    #Monstra no console a hora da atualização da cotação com a string 'Cotação Atualizada'
    tabela.to_excel("Cotações.xlsx", index=False)
    print(f"Cotação Atualizada. {datetime.now()}")
    time.sleep(60)
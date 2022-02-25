Os scripts tem a funcionalidade de mostrar a cotação do Bitcoin em 3 moedas diferentes sendo elas BRL, USD, EUR usando a API e armazená-las no arquivo.xlsx para visualização.
Python version 3.10.2
Antes de executar os scripts instale as bibliotecas necessárias através do comando "pip install -r requirements.txt"
Considere atualizar o pip com o comando "pip install --upgrade pip"
Para executar o script abra o cmd e digite "python cotacao1.py" ou "python cotacao2.py".
Funcionalidade dos scripts:
cotacao1 : executa 30 vezes o código a cada 60 segundos para adquirir a cotação do BTC nas moedas BRL,USD,EUR.
cotacao2 : executa a cada 60 segundos para adquirir a cotação do BTC nas moedas BRL,USD,EUR em tempo real através da API.

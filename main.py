import requests
import time
import json
import os
import openai
from datetime import datetime
from get_env import print_env

env = print_env(['app_key'])

#Configurando o ambiente

#Aqui fica a chave API da Open AI.
openai.api_key = ''

print('BOT INICIADO COM SUCESSO...!')

class TelegramBot:
  def __init__(self):
    #Aqui fica o token disponibilizado no telegram pelo botfather.
    token = '' 
    self.url_base = f'https://api.telegram.org/bot{token}/'    
    #iniciar bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem.get('update_id')
          #print(update_id)

          chat_id = mensagem.get('message').get('from').get('id')
          print(f'Mensagem ID: {chat_id}')
          chat_id = str(chat_id)

          #primeiro_nome = mensagem['first_name']
          #texto = mensagem['message']['text']
          
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
          self.responder(resposta,chat_id)
          
          
         
  #Obter Mensagem
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=50'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)
  
  #Criar a resposta
  #def criar_resposta(self,mensagem,eh_primeira_mensagem):
    #mensagem_txt = mensagem['message']['text']
    #print(mensagem_txt)
    #if eh_primeira_mensagem == 1:
      #return f'''olá, digite um número tudo bem'''
    #else:
      #return 'bom dia!'


  def criar_resposta(self,mensagem,eh_primeira_mensagem):
    mensagem_txt = mensagem.get('message').get('text')
    mensagem_txt = str(mensagem_txt)
    #print(mensagem_txt)

    #pegando a data e hora atual e colocando em váriaveis
    now = datetime.now()
    ano = now.year
    dia = now.day
    mes = now.month
    hora = (f'{now.hour}:{now.minute}')

    print(f'Data: {dia}/{mes}/{ano} {hora}')
    
    mensagem_txt = mensagem_txt.upper()
    #print(mensagem_txt)
    
    #chatGPT integração.

    #Aqui começa o trecho da inteligência artificial
    #Model_engine
    model_engine = 'text-davinci-003'


    while True:
        prompt = mensagem_txt
        #print(prompt)

        #configurando a geração da resposta
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
        )
    
        response = completion.choices[0].text
        if (response == KeyError)or(response == TypeError)or(response == NameError):
          return 'Erro!'
        #Aqui termina o treço da inteligência artificial
        else:
          #print(response)
          if eh_primeira_mensagem == 1:
            return f'''Olá, eu sou o Sr.Capivara seu mais novo bot/IA auxiliar, posso tirar suas dúvidas e ajudar na sua busca por conhecimento e também ser um ótimo amigo, pode me chamar de bot :)!\n\nSe precisar de informações basta digitar - Bot ajuda ou Ajuda.\n\nAqui estão algumas informações necessárias:\n\n1. Oque eu sou? Sou um bot/robo integrado com a IA(inteligência artificial) OpenAI.\n\n2. Seus dados estão seguros? Sim pois suas mensagens não ficam salvas em outro lugar, basicamente eu direciono sua mensagem para a IA(inteligência artificial) e assim que a inteligência fornece a resposta eu entrego ela direto para você.\n\n3. contatos do meu programador:\nLinkdin: https://www.linkedin.com/in/pl%C3%ADnio-ramos-3a1543229/\nGitHub: https://github.com/plinio29\nE-mail: plinio206@live.com\nTelegram: @plinior10''' 
          

          elif prompt == 'NONE':
            return 'Você enviou um arquivo diferente de texto, minha inteligência artificial só consegue processar texto!'
        
          elif (prompt == '/START')or(prompt =='START'):
            return 'Olá, eu sou o Sr.Capivara seu mais novo bot/IA auxiliar, posso tirar suas dúvidas e ajudar na sua busca por conhecimento e também ser um ótimo amigo, pode me chamar de bot :)!\n\nSe precisar de informações basta digitar - Bot ajuda ou Ajuda.\n\nAqui estão algumas informações necessárias:\n\n1. Oque eu sou? Sou um bot/robo integrado com a IA(inteligência artificial) OpenAI.\n\n2. Seus dados estão seguros? Sim pois suas mensagens não ficam salvas em outro lugar, basicamente eu direciono sua mensagem para a IA(inteligência artificial) e assim que a inteligência fornece a resposta eu entrego ela direto para você.\n\n3. contatos do meu programador:\nLinkdin: https://www.linkedin.com/in/pl%C3%ADnio-ramos-3a1543229/\nGitHub: https://github.com/plinio29\nE-mail: plinio206@live.com\nTelegram: @plinior10'
          
          elif (prompt == 'BOT AJUDA!')or(prompt =='AJUDA')or(prompt =='AJUDA!')or(prompt =='BOT AJUDA'):
            return 'Você disse bot ajuda? \n\nAqui estão algumas informações necessárias:\n\n1. Oque eu sou? Sou um bot/robo integrado com a IA(inteligência artificial) OpenAI.\n\n2. Seus dados estão seguros? Sim pois suas mensagens não ficam salvas em outro lugar, basicamente eu direciono sua mensagem para a IA(inteligência artificial) e assim que a inteligência fornece a resposta eu entrego ela direto para você.\n\n3. contatos do meu programador:\nLinkdin: https://www.linkedin.com/in/pl%C3%ADnio-ramos-3a1543229/\nGitHub: https://github.com/plinio29\nE-mail: plinio206@live.com\nTelegram: @plinior10'
          
          #Créditos ao programador
          elif (prompt =='SEU CRIADOR?')or(prompt =='CRIADOR?')or(prompt =='QUEM PROGRAMOU VOCÊ?')or(prompt =='QUEM É SEU PROGRAMADOR?')or(prompt =='SEU PROGRAMADOR?')or(prompt =='SEU PROGRAMADOR?')or(prompt =='QUEM É SEU DESENVOLVEDOR?')or(prompt =='QUEM DESENVOLVEU VOCÊ?')or(prompt =='QUEM PROGRAMOU VC?')or(prompt =='QUEM CRIOU VC?')or(prompt =='QUEM É SEU PROGRAMADOR?')or(prompt =='SEU PROGRAMADOR?')or(prompt =='QUEM É SEU DESENVOLVEDOR?')or(prompt =='QUEM DESENVOLVEU VC?')or(prompt =='VC FOI PROGRAMADO POR QUEM?')or(prompt =='VOCÊ FOI PROGRAMADO POR QUEM?')or(prompt =='VOCÊ FOI CRIADO POR QUEM?')or(prompt =='VC FOI DESENVOLVIDO POR QUEM?')or(prompt =='VOCÊ FOI DESENVOLVIDO POR QUEM?'):
            return 'O bot/robo - Plínio Ramos. A inteligência artificial(IA) - OpenAI.'
          
          elif (prompt == 'BOT')or(prompt =='BOT!')or(prompt =='BOT?')or(prompt =='CAPIVARA?')or(prompt =='CAPIVARA!')or(prompt =='CAPIVARA')or(prompt =='SR.CAPIVARA?')or(prompt =='SR.CAPIVARA')or(prompt =='SR.CAPIVARA!')or(prompt =='SR CAPIVARA?')or(prompt =='SR CAPIVARA')or(prompt =='SR CAPIVARA!'):
            return 'Me chamou? estou aqui para te ajudar!'

          elif (prompt =='HORA')or(prompt =='HORA?')or(prompt =='HORAS')or(prompt =='HORAS?')or(prompt =='QUE HORAS SÃO?')or(prompt =='QUE HORAS SÃO AGORA?')or(prompt =='QUE HORAS SAO AGORA?')or(prompt =='QUE HORAS SAO?')or(prompt =='HORAS AGORA')or(prompt =='HORAS AGORA?')or(prompt =='BOT HORA')or(prompt =='BOT HORA?')or(prompt =='BOT HORAS')or(prompt =='BOT HORAS?')or(prompt =='BOT QUE HORAS SÃO?')or(prompt =='BOT QUE HORAS SÃO AGORA?')or(prompt =='BOT QUE HORAS SAO AGORA?')or(prompt =='BOT QUE HORAS SAO?')or(prompt =='BOT HORAS AGORA')or(prompt =='BOT HORAS AGORA?')or(prompt =='BOT, HORA')or(prompt =='BOT, HORA?')or(prompt =='BOT, HORAS')or(prompt =='BOT, HORAS?')or(prompt =='BOT, QUE HORAS SÃO?')or(prompt =='BOT, QUE HORAS SÃO AGORA?')or(prompt =='BOT, QUE HORAS SAO AGORA?')or(prompt =='BOT, QUE HORAS SAO?')or(prompt =='BOT, HORAS AGORA')or(prompt =='BOT, HORAS AGORA?'):
            return (hora)
          
          elif (prompt =='DATA?')or(prompt =='DATA ATUAL?')or(prompt =='DATA ATUAL')or(prompt =='DATA')or(prompt =='QUE DIA É HOJE?')or(prompt =='QUE DIA E HOJE?')or(prompt =='HOJE É QUE DIA?')or(prompt =='HOJE É QUE DIA?')or(prompt =='DIA')or(prompt =='DIA?')or(prompt =='QUE DIA E HOJE')or(prompt =='QUE DIA É HOJE')or(prompt =='HOJE É DIA?')or(prompt =='HOJE E DIA?')or(prompt =='HOJE E DIA')or(prompt =='HOJE É?')or(prompt =='HOJE E?')or(prompt =='ANO ATUAL?')or(prompt =='QUAL ANO ESTAMOS?')or(prompt =='EM QUE ANO ESTAMOS?')or(prompt =='ANO?')or(prompt =='BOT DATA ATUAL')or(prompt =='BOT DATA ATUAL?')or(prompt =='BOT DATA')or(prompt =='BOT DATA?')or(prompt =='BOT QUE DIA É HOJE?')or(prompt =='BOT QUE DIA E HOJE?')or(prompt =='BOT HOJE É QUE DIA?')or(prompt =='BOT HOJE É QUE DIA?')or(prompt =='BOT DIA')or(prompt =='BOT DIA?')or(prompt =='BOT QUE DIA E HOJE')or(prompt =='BOT QUE DIA É HOJE')or(prompt =='BOT HOJE É DIA?')or(prompt =='BOT HOJE E DIA?')or(prompt =='BOT HOJE E DIA')or(prompt =='BOT HOJE É?')or(prompt =='BOT HOJE E?')or(prompt =='BOT ANO ATUAL?')or(prompt =='BOT QUAL ANO ESTAMOS?')or(prompt =='BOT ANO?')or(prompt =='BOT, DATA ATUAL')or(prompt =='BOT, DATA')or(prompt =='BOT, QUE DIA É HOJE?')or(prompt =='BOT, QUE DIA E HOJE?')or(prompt =='BOT, HOJE É QUE DIA?')or(prompt =='BOT, HOJE É QUE DIA?')or(prompt =='BOT, DIA')or(prompt =='BOT, DIA?')or(prompt =='BOT, QUE DIA E HOJE')or(prompt =='BOT, QUE DIA É HOJE')or(prompt =='BOT, HOJE É DIA?')or(prompt =='BOT, HOJE E DIA?')or(prompt =='BOT, HOJE E DIA')or(prompt =='BOT, HOJE É?')or(prompt =='BOT, HOJE E?')or(prompt =='BOT, ANO ATUAL?')or(prompt =='BOT, QUAL ANO ESTAMOS?')or(prompt =='BOT, ANO?'):
            return (f'{dia}/{mes}/{ano}')
          
          elif (prompt =='MÊS?')or(prompt =='MES?')or(prompt =='MES')or(prompt =='QUE MES ESTAMOS?')or(prompt =='EM QUE MES ESTAMOS?')or(prompt =='QUE MES ESTAMOS?')or(prompt =='QUE MÊS ESTAMOS?')or(prompt =='EM QUE MÊS ESTAMOS?')or(prompt =='QUE MÊS ESTAMOS')or(prompt =='QUAL MES ESTAMOS?')or(prompt =='QUAL MES ESTAMOS')or(prompt =='MES ATUAL?')or(prompt =='MÊS ATUAL?')or(prompt =='MES ATUAL')or(prompt =='MES ATUAL?')or(prompt =='HOJE É?')or(prompt =='HOJE E?')or(prompt =='ANO ATUAL?')or(prompt =='QUAL ANO ESTAMOS?')or(prompt =='ANO?')or(prompt =='BOT MÊS?')or(prompt =='BOT MES?')or(prompt =='BOT MES')or(prompt =='BOT QUE MES ESTAMOS?')or(prompt =='BOT QUE MES ESTAMOS?')or(prompt =='BOT QUE MÊS ESTAMOS?')or(prompt =='BOT QUE MÊS ESTAMOS')or(prompt =='BOT QUAL MES ESTAMOS?')or(prompt =='BOT QUAL MES ESTAMOS')or(prompt =='BOT MES ATUAL?')or(prompt =='BOT MÊS ATUAL?')or(prompt =='BOT MES ATUAL')or(prompt =='BOT MES ATUAL?')or(prompt =='BOT HOJE É?')or(prompt =='BOT HOJE E?')or(prompt =='BOT ANO ATUAL?')or(prompt =='BOT QUAL ANO ESTAMOS?')or(prompt =='BOT ANO?')or(prompt =='BOT, MÊS?')or(prompt =='BOT, MES?')or(prompt =='BOT, MES')or(prompt =='BOT, QUE MES ESTAMOS?')or(prompt =='BOT, QUE MES ESTAMOS?')or(prompt =='BOT, QUE MÊS ESTAMOS?')or(prompt =='BOT, QUE MÊS ESTAMOS')or(prompt =='BOT, QUAL MES ESTAMOS?')or(prompt =='BOT, QUAL MES ESTAMOS')or(prompt =='BOT, MES ATUAL?')or(prompt =='BOT, MÊS ATUAL?')or(prompt =='BOT, MES ATUAL')or(prompt =='BOT, MES ATUAL?')or(prompt =='BOT, HOJE É?')or(prompt =='BOT, HOJE E?')or(prompt =='BOT, ANO ATUAL?')or(prompt =='BOT, QUAL ANO ESTAMOS?')or(prompt =='BOT, ANO?'):
            return (mes)
          #Resposta da IA, caso não queira a resposta da IA basta tirar o 'response' de dentro dos parenteses!
          else:
            return (response)
    #Responder
  def responder(self,resposta,chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()

#v1.1


#Código criado por Plínio Ramos.
#Minhas redes: 
#Linkdin: https://www.linkedin.com/in/pl%C3%ADnio-ramos-3a1543229/
#GitHub: https://github.com/plinio29
#E-mail: plinio206@live.com

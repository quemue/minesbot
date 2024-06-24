import requests
import time
import random
import datetime

# Mensagens atualizadas
mensagem_1 = """
📣 Atenção ao jogo 📣
💣 Mines
🔎 Estamos analisando uma entrada
"""

mensagem_2 = """
📣 Entrada confirmada 📣
🥇: Entrada:
{}

🎮: Tentativas: 2
Jogue com 2 a 3 minas

⏱️ Válido até: {}
"""

mensagem_3 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GREEN! ✅✅
"""

# Links dos botões
link_jogo = "https://go.aff.donald.bet/ll4h57qj"
clique_aqui = "https://go.aff.donald.bet/ll4h57qj"

# Layouts otimizados
possibilidades_minas = [
    "💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",  
    "💣💣⭐️💣⭐️\n💣⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",  
    "⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",  
    "💣⭐️⭐️⭐️💣\n💣💣💣💣💣\n⭐️⭐️⭐️💣💣\n💣💣💣💣💣\n💣⭐️⭐️⭐️💣",  
    "⭐️💣⭐️💣⭐️\n💣💣⭐️💣💣\n💣⭐️💣⭐️💣\n💣💣⭐️💣💣\n⭐️💣⭐️💣⭐️",  
    "💣💣⭐️💣💣\n💣⭐️💣⭐️💣\n⭐️💣💣💣⭐️\n💣⭐️💣⭐️💣\n💣💣⭐️💣💣",  
    "⭐️⭐️💣⭐️⭐️\n💣💣💣💣💣\n⭐️⭐️💣⭐️⭐️\n💣💣💣💣💣\n⭐️⭐️💣⭐️⭐️",  
    "💣⭐️💣⭐️💣\n⭐️💣⭐️💣⭐️\n💣⭐️💣⭐️💣\n⭐️💣⭐️💣⭐️\n💣⭐️💣⭐️💣",  
    "⭐️⭐️⭐️💣⭐️\n⭐️💣⭐️💣💣\n⭐️⭐️⭐️💣⭐️\n💣⭐️💣⭐️💣\n⭐️💣⭐️💣⭐️",  
    "⭐️⭐️💣⭐️⭐️\n💣⭐️💣⭐️💣\n⭐️💣⭐️💣⭐️\n💣⭐️💣⭐️💣\n⭐️⭐️💣⭐️⭐️",  
]

# Token e Chat ID do Telegram
telegram_token = '6756039849:AAHbEMttFpozWU0Hcr0u6UqqmrFZwiM7JYo'
chat_id = '-1002000504077'

# Função para enviar mensagens pelo Telegram com botões
def enviar_mensagem_telegram(mensagem, buttons=None):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': mensagem,
        'parse_mode': 'HTML'
    }
    if buttons:
        data['reply_markup'] = {
            'inline_keyboard': buttons
        }
    response = requests.post(url, json=data)  # Aqui usamos json=data para a estrutura correta
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Falha ao enviar a mensagem. Código de status: {response.status_code} - {response.text}")

# Loop infinito para envio contínuo de mensagens
while True:
    # Enviar a mensagem_1
    enviar_mensagem_telegram(mensagem_1)
    time.sleep(120)  # Aguardar 2 minutos

    # Enviar a mensagem_2 formatada
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem_2.format(possibilidade_mina_aleatoria, hora_validade)
    buttons = [
        [{'text': '𝐋𝐈𝐍𝐊 𝐃𝐎 𝐉𝐎𝐆𝐎!!', 'url': link_jogo}],
        [{'text': '👉 𝐂𝐋𝐈𝐐𝐔𝐄 𝐀𝐐𝐔𝐈', 'url': clique_aqui}]
    ]
    enviar_mensagem_telegram(mensagem_formatada, buttons)
    
    time.sleep(300)  # Aguardar 5 minutos

    # Enviar a mensagem_3
    enviar_mensagem_telegram(mensagem_3)

    # Imprimir log de reinício do ciclo
    print("Todas as mensagens foram enviadas. Reiniciando o ciclo.\n")

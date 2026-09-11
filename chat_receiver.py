import random
import socket

HOST = "0.0.0.0"
PORT = 5001
DROP_RATE = 0.4  # 40% de perda simulada no canal


def run_chat_receiver():
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[Chat Server] Online na porta {PORT} (Drop Rate: {DROP_RATE * 100}%)...")

    while True:
      data, addr = s.recvfrom(1024)

      # Simulação de descarte de pacote
      if random.random() < DROP_RATE:
        print("[CANAL] Pacote descartado artificialmente!")
        continue

      raw_message = data.decode("utf-8")

      # TODO 1: Fazer o split da mensagem delimitada por '|'
      # TODO 2: Verificar se a mensagem é do tipo 'MSG'
      # TODO 3: Extrair o ID da mensagem e o texto do usuário
      # TODO 4: Exibir no terminal a mensagem recebida e o ID correspondente
      # TODO 5: Montar o pacote de recibo no formato "DELIVERED|<ID>"
      # TODO 6: Enviar o recibo de volta para a origem usando s.sendto(..., addr)


if __name__ == "__main__":
  run_chat_receiver()

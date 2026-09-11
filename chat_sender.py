import socket
import threading

TARGET_IP = "127.0.0.1"
PORT = 5001

pending_messages = {}  # Formato sugerido: {id_inteiro: "texto da mensagem"}
msg_counter = 1
lock = threading.Lock()


def listen_receipts(sock):
  """Thread em background para receber recibos sem bloquear o terminal."""
  while True:
    try:
      data, _ = sock.recvfrom(1024)
      raw = data.decode("utf-8")

      # TODO 1: Fazer o parsing do recibo recebido
      vetorMensagem= raw.split("|")
      # TODO 2: Verificar se o tipo é "DELIVERED"
      if vetorMensagem[0] != "DELIVERED":
                    continue
      # TODO 3: Extrair o ID confirmado
      id = vetorMensagem[1]
      # TODO 4: Com o lock adquirido, remover a mensagem de pending_messages
      #         e imprimir aviso visual de entrega confirmada (ex: [✓✓ Entregue])
      with lock:
         if id in pending_messages:
            del pending_messages [id]
            print("Entregue ✓✓")  
      
    except Exception:
      break


def run_chat_sender():
  global msg_counter

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Inicia a thread que processa os ACKs recebidos em segundo plano
    listener = threading.Thread(target=listen_receipts, args=(s,), daemon=True)
    listener.start()

    print("=== Mini-Chat UDP ===")
    print("Comandos especiais:")
    print("  /status   -> Mostra mensagens ainda pendentes")
    print("  /reenviar -> Reenvia todas as mensagens pendentes\n")

    while True:
      try:
        user_input = input("Digite uma mensagem: ").strip()
        if not user_input:
          continue

        if user_input == "/status":
          # TODO 5: Exibir quantas e quais mensagens continuam em pending_messages
          continue

        if user_input == "/reenviar":
          # TODO 6: Iterar por todas as mensagens ainda em pending_messages
          #         e reenviá-las com s.sendto(..., (TARGET_IP, PORT))
          continue

        # Fluxo de envio de mensagem normal:
        # TODO 7: Associar a mensagem ao msg_counter atual e salvar em pending_messages
        # TODO 8: Montar o pacote no formato "MSG|<ID>|<CONTEUDO>"
        # TODO 9: Enviar o pacote via UDP usando s.sendto(...)
        # TODO 10: Incrementar msg_counter e avisar na tela que ela está pendente

      except KeyboardInterrupt:
        print("\nEncerrando cliente...")
        break


if __name__ == "__main__":
  run_chat_sender()

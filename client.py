import socket

class GuessingGameClient:
    def __init__(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port

    def play(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            print("Connected to the server. Start guessing!")
            while True:
                guess = input("Enter your guess (1-100): ")
                client_socket.sendall(guess.encode())
                response = client_socket.recv(1024).decode()
                print(response)
                if response == "Correct! You win!":
                    break

def main():
    client = GuessingGameClient()
    try:
        client.play()
    except KeyboardInterrupt:
        print("stopping client")
    finally:
        pass

if __name__ == "__main__":
    main()
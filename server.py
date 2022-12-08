import socket
import threading
import uuid

HOST = '127.0.0.1'
PORT = 5060
BUFFER_SIZE = 1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
games = {}  # currently active games
queue = {}  # players waiting for opponent


def broadcast(message: str, players: list):
    for player in players:
        player.send(message.encode('ascii'))


def create_game(game_name: str, player):
    game_name = game_name + '#' + str(uuid.uuid4())[:4]
    queue[game_name] = player


def handle_game(game_name: str, word: str, guesser):
    games[game_name] = [queue[game_name], guesser]
    queue.pop(game_name)
    is_word_sent = False

    while True:
        try:
            if not is_word_sent:
                guesser.send(word.encode('ascii'))
                is_word_sent = True
            else:
                letter = guesser.recv(1024)
                broadcast(letter, games[game_name])
        except Exception as exc:
            print(exc)
            games.pop(game_name)


def start():
    while True:
        player, address = server.accept()
        clients.append(player)


if __name__ == "__main__":
    create_game('name', '12')

import socket
import threading
import uuid
import json

HOST = '127.0.0.1'
PORT = 5060
BUFFER_SIZE = 1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

players = []
games = {}  # currently active games
queue = {}  # created games with one player waiting for opponent


def broadcast(message: str, game_name):
    for player in games[game_name]:
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
                broadcast(letter, game_name)
        except Exception as exc:
            print(exc)
            games.pop(game_name)


def handle_before_game(player):
    create_game('new', player)
    print(queue)
    games_str = (' '.join(queue.keys())).encode('ascii')
    player.send(games_str)

    while True:
        pass


def start():
    while True:
        player, address = server.accept()
        players.append(player)
        print(type(player))

        client_thread = threading.Thread(target=handle_before_game, args=(player,))
        client_thread.start()


if __name__ == "__main__":
    start()

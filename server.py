import socket
import threading
import uuid

HOST = '127.0.0.1'
PORT = 5060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

players = []
games = {}  # currently active games
queue = {}  # created games with one player waiting for opponent


def broadcast(message: str, game_name):
    for player in games[game_name]:
        player.send(message.encode('ascii'))


def create_game(game_name: str, player: socket.socket, word: str):
    game_name = game_name + '#' + str(uuid.uuid4())[:4]
    queue[game_name] = {
        'player': player,
        'word': word
    }


def handle_game(game_name: str, guesser):
    games[game_name] = [queue[game_name], guesser]
    guesser.send(queue[game_name]['word'].encode('ascii'))  # sending word to guesser
    queue.pop(game_name)

    print(games[game_name])
    print(queue)

    while True:
        try:
            letter = guesser.recv(1024)
            broadcast(letter, game_name)
        except Exception as exc:
            print(exc)
            games.pop(game_name)


def handle_before_game(player):
    create_game('NoGames', player, 'word')
    games_str = (' '.join(queue.keys())).encode('ascii')
    player.send(games_str)

    while True:
        response = player.recv(1024).decode('ascii')
        if response == 'join':
            game_name = player.recv(1024).decode('ascii')
            thread = threading.Thread(target=handle_game, args=(game_name, player))
            thread.start()
            break
        else:
            game_name = player.recv(1024).decode('ascii')
            word = player.recv(1024).decode('ascii')
            create_game(game_name, player, word)
            print(game_name, word)


def start():
    while True:
        player, address = server.accept()
        players.append(player)
        print(type(player))

        client_thread = threading.Thread(target=handle_before_game, args=(player,))
        client_thread.start()


if __name__ == "__main__":
    start()

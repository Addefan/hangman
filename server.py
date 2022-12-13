import socket
import threading

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


def create_game(game_name: str, player: socket.socket, word: str, attempts: int):
    queue[game_name] = {
        'player': player,
        'word': word,
        'attempts': attempts
    }


def handle_game(game_name: str, guesser):
    games[game_name] = [queue[game_name]['player'], guesser]
    queue.pop(game_name)

    print(games[game_name])
    print(queue)

    while True:
        try:
            letter = guesser.recv(1024).decode('ascii')
            broadcast(letter, game_name)
        except Exception as exc:
            print(exc)
            games.pop(game_name)


def handle_before_game(player):
    games_str = (' '.join(queue.keys())).encode('ascii') if len(queue) > 0 else ' '.encode('ascii')
    player.send(games_str)

    while True:
        response = player.recv(1024).decode('ascii')
        match response.split(";"):
            case "join", *args:
                game_name = player.recv(1024).decode('ascii')
                player.send(queue[game_name]['word'].encode('ascii'))  # sending word to guesser
                thread = threading.Thread(target=handle_game, args=(game_name, player))
                thread.start()
                break
            case "create", game_name, word, attempts:
                create_game(game_name, player, word, int(attempts))
                break


def start():
    while True:
        player, address = server.accept()
        players.append(player)
        print('Connected new player!')

        client_thread = threading.Thread(target=handle_before_game, args=(player,))
        client_thread.start()


if __name__ == "__main__":
    start()

import socket
import threading

HOST = '127.0.0.1'
PORT = 5060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

watching = []   # players watching for games
games = {}  # currently active games
queue = {}  # created games with one player waiting for opponent


def broadcast(message: str, game_name):
    for player in games[game_name]:
        player.send(message.encode('ascii'))


def send_game(game_name):
    for player in watching:
        player.send(game_name.encode('ascii'))


def create_game(game_name: str, player: socket.socket, word: str, attempts: int):
    queue[game_name] = {
        'player': player,
        'word': word,
        'attempts': attempts
    }


def handle_game(game_name: str, guesser):
    games[game_name] = [queue[game_name]['player'], guesser]
    queue.pop(game_name)

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
        try:
            response = player.recv(1024).decode('ascii').split(';')
            print(response)
            watching.remove(player)
            if response[0] == 'join':
                player.send(queue[response[1]]['word'].encode('ascii'))  # sending word to guesser
                print(queue[response[1]]['word'])
                thread = threading.Thread(target=handle_game, args=(response[1], player))
                thread.start()
                break
            else:
                create_game(response[1], player, response[2], int(response[3]))
                print(response)
                send_game(response[1])
                break
        except Exception as exc:
            print(exc)
            print('Removed player with failed connection!')
            watching.remove(player)


def start():
    while True:
        player, address = server.accept()
        watching.append(player)
        print('Connected new player!')

        client_thread = threading.Thread(target=handle_before_game, args=(player,))
        client_thread.start()


if __name__ == "__main__":
    start()

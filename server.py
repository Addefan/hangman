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
        player.send(message.encode('utf-8'))


def create_game(game_name: str, player: socket.socket, word: str, attempts: int):
    queue[game_name] = {
        'player': player,
        'word': word,
        'attempts': attempts
    }


def handle_game(game_name: str, guesser):
    games[game_name] = [queue.pop(game_name)['player'], guesser]

    while True:
        try:
            message = guesser.recv(1024).decode('utf-8')
            if len(message) == 1:
                broadcast(message, game_name)
            elif message == "exit":
                broadcast(message, game_name)
                games.pop(game_name)
        except Exception as exc:
            print(exc)
            games.pop(game_name) if game_name in games else None
            break


def handle_before_game(player):
    games_str = (' '.join(queue.keys())).encode('utf-8') if len(queue) > 0 else ' '.encode('utf-8')
    player.send(games_str)

    while True:
        try:
            response = player.recv(1024).decode('utf-8').split(';')
            watching.remove(player)
            if response[0] == 'join':
                # sending game info to guesser
                player.send(f"{queue[response[1]]['word']};{queue[response[1]]['attempts']}".encode('utf-8'))

                thread = threading.Thread(target=handle_game, args=(response[1], player))
                thread.start()
                break
            elif response[0] == 'create':
                create_game(response[1], player, response[2], int(response[3]))
                break
        except Exception as exc:
            print(exc)
            print('Removed player with failed connection!')
            watching.remove(player) if player in watching else None
            break


def start():
    while True:
        player, address = server.accept()
        watching.append(player)
        print('Connected new player!')

        client_thread = threading.Thread(target=handle_before_game, args=(player,))
        client_thread.start()


if __name__ == "__main__":
    start()

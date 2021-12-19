from queue import Queue
import socket
import threading
import argparse


def read_file(filepath, data):
    """Считываем urls"""
    with open(filepath) as f:
        urls = f.read().splitlines()
        for url in urls:
            data.put(url)

def worker(urls: Queue[str]):
    """воркер для отправки url с клиента на сервер"""
    while True:
        url = urls.get()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        sock.sendall(bytes(url+"\n", 'utf-8'))
        rcv = str(sock.recv(1024), "utf-8")
        if rcv:
            print(f"{url}: {rcv}")
        sock.close()

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='urls')
    parser.add_argument('-t', '--threads', type=int, default=1)
    parser.add_argument('-p', '--port', type=int, default=8000)
    return parser

if __name__ == "__main__":
    namespace = createParser().parse_args()
    urls = Queue()
    read_file(namespace.file, urls)
    address = ("localhost", namespace.port)
    threads = [threading.Thread(target=worker, args=(urls, )) for _ in range(namespace.threads)]
    for t in threads:
        t.start()

    for t in threads:
        # ждем выполнения потоков
        t.join()

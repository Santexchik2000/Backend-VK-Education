import argparse
import socketserver
import threading
from collections import Counter
import requests
import json

class ThreadedRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()  # получаем данные с клиента
        print(data)
        json = self.worker(data)
        self.wfile.write(bytes(str(json), 'UTF-8')) # отправляем данные на клиент

    def worker(self, url):
        """
        воркер для обсчёта топ слов
        """
        with self.server.sem:
            res = self.top_k(url)
            d = {}
            for k, v in res:
                d[k] = v
            d = json.dumps(d)
            with self.server.lock:
                self.server.count_of_download_urls += 1 
                print(self.server.count_of_download_urls)
            return d

    def top_k(self, url):
        data = requests.get(url)
        return Counter(data.text).most_common(self.server.k)

class Master(socketserver.ThreadingTCPServer):
    sem = None
    allow_reuse_address = True
    k = 0
    count_of_download_urls = 0
    lock = threading.Lock()

    def __init__(self, host: str, port: int, handler_classRequestHandler: socketserver.BaseRequestHandler, worker_limit: int, k: int):
        super().__init__((host, port), handler_classRequestHandler)
        """
        Инициализируем сервер, примаем хост, порт, класс обработчик запросов, количество воркеров
        """
        self.sem = threading.Semaphore(worker_limit)  # устанавливаем кол-во допустимых потоков.
        self.k = k


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workers', type=int, default=1)
    parser.add_argument('-k', '--top_k', type=int, default=7)
    parser.add_argument('-p', '--port', type=int, default=8000)
    return parser
    
if __name__ == '__main__':
    namespace = createParser().parse_args()
    address = ('localhost', namespace.port)
    with Master(*address, ThreadedRequestHandler, namespace.workers, namespace.top_k) as m:
        m.serve_forever()
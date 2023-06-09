import json
import grpc
import random
import psycopg2
from concurrent import futures

import example_pb2
import example_pb2_grpc

with open('config.json') as f:
    config = json.load(f)


class MyServiceServicer(example_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.connection = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

    def GetRandomNumber(self, request, context):
        number = random.randint(1, 100)
        self._store_number(number)
        response = example_pb2.RandomNumberResponse()
        response.number = number
        return response

    def _store_number(self, number):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO numbers (number) VALUES (%s)", (number,))
        self.connection.commit()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

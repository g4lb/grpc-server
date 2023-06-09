import unittest
import grpc
import psycopg2
import example_pb2
import example_pb2_grpc
import json
from concurrent import futures

# Import server implementation and other necessary code
from server import MyServiceServicer

# Load the configuration from the JSON file
with open('config.json') as f:
    config = json.load(f)


class MyServiceTest(unittest.TestCase):
    def setUp(self):
        # Set up the gRPC server and client for testing
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        example_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), self.server)
        self.server_port = '[::]:50051'
        self.server.add_insecure_port(self.server_port)
        self.server.start()

        # Create a gRPC channel and stub for the client
        self.channel = grpc.insecure_channel(self.server_port)
        self.stub = example_pb2_grpc.MyServiceStub(self.channel)

        # Connect to the PostgreSQL test database
        self.connection = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

        # Create the numbers table in the test database
        with self.connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS numbers (id SERIAL PRIMARY KEY, number INTEGER)")
        self.connection.commit()

    def tearDown(self):
        # Clean up the gRPC server and PostgreSQL connection
        self.server.stop(None)
        self.connection.close()

    def test_get_random_number(self):
        # Call the GetRandomNumber gRPC method and assert the response
        request = example_pb2.RandomNumberRequest()
        response = self.stub.GetRandomNumber(request)
        self.assertIsInstance(response, example_pb2.RandomNumberResponse)
        self.assertGreaterEqual(response.number, 1)
        self.assertLessEqual(response.number, 100)


if __name__ == '__main__':
    unittest.main()

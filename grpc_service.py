from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
from datetime import datetime

def default_function(data):
    # just relay
    return data[0]

class Service(service_pb2_grpc.ServiceServicer):
    def __init__(self, function):
        self.function = function

    def ProcessData(self, request, context):
        print(f"Received data: {[data for data in request.data]}")
        if not request.data:
            return service_pb2.DataResponse(
                status="error",
                processed_data=b"",
                processed_timestamp=""
            )
        processed_data = self.function(request.data)
        return service_pb2.DataResponse(
            status="ok",
            processed_data=processed_data,
            processed_timestamp=datetime.now().isoformat() + "Z"
        )

def serve(function=default_function, port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(Service(function), server)
    server.add_insecure_port("0.0.0.0:" + str(port))
    server.start()
    print("Service gRPC server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    # 任意の関数を指定してサーバーを起動
    serve(function=lambda data: data[-1])

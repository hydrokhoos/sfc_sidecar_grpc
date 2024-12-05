import grpc
import service_pb2
import service_pb2_grpc

def send_data_to_service(data, address='localhost', port=50051):
    with grpc.insecure_channel(address + ':' + str(port)) as channel:
        stub = service_pb2_grpc.ServiceStub(channel)
        request = service_pb2.DataRequest(data=data)
        response = stub.ProcessData(request)
        return response

if __name__ == "__main__":
    # サービスに送信するデータ（bytes型）
    # data = [b'47835', b'111431', b'903429']
    data = [b"\xb2\x109\x1dAI\xc8}l", b"\xeb\x8f\xbd\xc3\x00\xcb\xfa"]
    response = send_data_to_service(data)
    print(f"Response from service: {response}")
    print(f'Processed data: {response.processed_data}')

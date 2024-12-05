# SFC Sidecar gRPC

This repository contains a gRPC-based service implementation.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate gRPC code:
   ```bash
   python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
   ```
3. Run the service:
   ```bash
   python grpc_service.py
   ```
4. Send data:
   ```bash
   python grpc_send_data.py
   ```

## Testing
Run unit tests:
```bash
pytest tests/
```

from setuptools import setup, find_packages

setup(
    name="sfc_sidecar_grpc",
    version="0.1.0",
    author="saito",
    description="A gRPC sidecar communication library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hydrokhoos/sfc_sidecar_grpc",
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools",
    ],
    python_requires='>=3.6',
)

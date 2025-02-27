from client_interface import ClientInterface

class Client:
    def __init__(self, client_interface: ClientInterface) -> None:
        self._server = client_interface
    def echo(self, string: str) -> None:
        self._server.echo(string)

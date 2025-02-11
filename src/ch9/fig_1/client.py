from server import TerminalStdoutServer

class Client:
    def __init__(self, server: TerminalStdoutServer) -> None:
        self._server = server
    def echo(self, string: str) -> None:
        self._server.echo(string)

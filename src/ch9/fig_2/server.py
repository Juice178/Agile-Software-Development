from client_interface import ClientInterface
from contextlib import redirect_stdout
from pathlib import Path


class TerminalStdoutServer(ClientInterface):
    def echo(self, string: str) -> None:
        print(string)


class FileStdoutServer(ClientInterface):
    def __init__(self, redirect_file: Path):
        self._redirect_file = redirect_file
    def echo(self, string: str) -> None:
        with open(self._redirect_file, 'w') as f:
            with redirect_stdout(f):
                print(string)
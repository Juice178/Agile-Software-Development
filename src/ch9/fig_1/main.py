from client import Client
from server import TerminalStdoutServer
import fire


def main(string: str = "") -> None:
    Client(TerminalStdoutServer()).echo(string)

if __name__ == "__main__":
    fire.Fire(main)
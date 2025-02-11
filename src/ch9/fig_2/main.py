from client import Client
from server import TerminalStdoutServer, FileStdoutServer
from pathlib import Path
import fire


def main(server_name: str = "", string: str = "") -> None:
    if server_name == "terminal":
        Client(TerminalStdoutServer()).echo(string)
    elif server_name == "file":
        redirect_file = Path(__file__).parent.resolve() / Path(f"{string}.log")
        Client(FileStdoutServer(redirect_file=redirect_file)).echo(string)
    else:
        print(f"No server named {server_name}")


if __name__ == "__main__":
    fire.Fire(main)
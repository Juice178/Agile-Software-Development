from button import Button
from time import sleep


def main() -> None:
    button = Button()
    button.start()
    while True:
        button.push()
        sleep(60)


if __name__ == "__main__":
    main()
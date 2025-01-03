from sgame.bot_test import BOT
from sgame.consts import DISCORD_TOKEN


def main() -> None:
    BOT.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()

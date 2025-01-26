from sgame.bot_test import BOT
from sgame.consts import DISCORD_TOKEN
from sgame.game.database.insert_cards import insert_cards
from sgame.game.database.connect import connect


def main() -> None:
    conn, cursor = connect()
    insert_cards(cursor)
    conn.commit()


if __name__ == "__main__":
    main()

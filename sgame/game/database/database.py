from sgame.game.database.connect import connect
from sgame.game.database.insert_card import insert_card
from sgame.game.database.create_cards_table import create_cards_table


def database():
    conn, cursor = connect()
    create_cards_table(cursor)
    conn.commit()

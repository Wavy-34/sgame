from mysql.connector.cursor_cext import MySQLCursorAbstract
from sgame.game.card_type import CardType


def insert_card(
    cursor: MySQLCursorAbstract,
    name: str,
    cost: int,
    reward: int,
    card_type: CardType,
    spicy_level: int,
    description: str | None = None,
) -> None:
    if not description:
        description = "No description yet !"
    cursor.execute(
        f"INSERT INTO cards (name, cost, reward, card_type, spicy_level, description) "
        f"VALUES ('{name}', '{cost}', '{reward}', '{card_type}', '{spicy_level}', '{description}')"
    )

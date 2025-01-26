from sgame.consts import NOTION_DATABASE_ID, NOTION_TOKEN
from sgame.create_card import readDatabase
from sgame.errors import UnvalidCardType
from sgame.game.card_type import CardType
from sgame.game.database.create_cards_table import create_cards_table
from sgame.game.database.insert_card import insert_card
from mysql.connector.cursor_cext import MySQLCursorAbstract
from typing import Any


headers: dict[str, str] = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def insert_cards(
    cursor: MySQLCursorAbstract,
) -> None:  # add instances of Card() to the database from the notion database
    data: dict[str, list] = readDatabase(NOTION_DATABASE_ID, headers)
    create_cards_table(cursor)

    result: list = data.get("results")  # type: ignore

    for i in range(len(result)):
        card_properties: dict[str, Any] = result[i].get("properties")
        name: str = card_properties["Name"]["title"][0]["text"]["content"]
        try:
            description: str | None = card_properties["Description"]["rich_text"][0][
                "text"
            ]["content"]
        except Exception:
            description = None
        cost: int = card_properties["Cost"]["number"]
        reward: int = card_properties["Reward"]["number"]
        card_type: str | CardType = card_properties["Task/Modifier"]["select"]["name"]
        spice_level: int = card_properties["Spice level"]["number"]
        tag: str = name.lower().replace(" ", "_")

        if card_type == "Task":
            card_type = CardType.TASK
        elif card_type == "Modifier":
            card_type = CardType.MODIFIER
        else:
            raise UnvalidCardType(card_type)

        insert_card(cursor, name, cost, reward, card_type, spice_level, description)

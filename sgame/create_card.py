import requests
import json
from typing import Any
from sgame.card import Card
from sgame.consts import DATABASE_ID, NOTION_TOKEN

headers: dict[str, str] = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def readDatabase(
    databaseID: str, headers: dict[str, str]
) -> dict:  # get a json file that contains cards infos from the notion database
    readUrl: str = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res: requests.models.Response = requests.request("POST", readUrl, headers=headers)
    data: dict[str, list] = res.json()

    print(res.status_code)

    return data


def create_cards() -> (
    None
):  # create a json file that contains instances of Card() from the info of readDatabase()
    data: dict[str, list] = readDatabase(DATABASE_ID, headers)

    result: list = data.get("results")  # type: ignore
    cards: dict[str, Card] = {}

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
        task_or_modifier: str = card_properties["Task/Modifier"]["select"]["name"]
        spice_level: int = card_properties["Spice level"]["number"]
        tag: str = name.lower().replace(" ", "_")

        cards[tag] = Card(name, cost, reward, task_or_modifier, description)

    with open("./cards.json", "w", encoding="utf8") as file:
        json.dump(
            {card: cards[card].__dict__ for card in cards},
            file,
            ensure_ascii=False,
            indent=4,
        )


def get_card(
    card_to_get: str,
) -> (
    Card | None
):  # get an instance of Card from the json file, return None if it doesnt exist
    with open("./cards.json", "r") as file:
        data: dict[str, dict[str, str | int]] = json.load(file)

    try:
        card_with_infos: dict[str, str | int] = data[card_to_get]
        name: str = card_with_infos["_Card__name"]  # type: ignore
        type_: str = card_with_infos["_Card__type"]  # type: ignore
        cost: int = card_with_infos["_Card__cost"]  # type: ignore
        reward: int = card_with_infos["_Card__reward"]  # type: ignore
        description: str = card_with_infos["_Card__description"]  # type: ignore

        card: Card = Card(name, cost, reward, type_, description)
        return card
    except KeyError:
        print(f"{card_to_get} is not a valid card")
        return None
    except Exception as e:
        raise e
        return None


def get_cards(
    *cards_to_get: str,
) -> dict[
    str, Card
]:  # call get_card() for each arg given and return a dictionnary of the succesfull calls

    cards: dict[str, Card] = {}
    for name in cards_to_get:
        card: Card | None = get_card(name)
        if card:
            cards[name] = card

    return cards

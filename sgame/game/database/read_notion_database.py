import requests  # type: ignore
from sgame.consts import NOTION_TOKEN, NOTION_DATABASE_ID


def read_notion_database(
    databaseID: str, headers: dict[str, str]
) -> dict[
    str, list
]:  # get a json file that contains cards infos from the notion database
    readUrl: str = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res: requests.models.Response = requests.request("POST", readUrl, headers=headers)
    data: dict[str, list] = res.json()

    print(res.status_code)
    return data

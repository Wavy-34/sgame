class Card:
    def __init__(
        self,
        name: str,
        cost: int,
        reward: int,
        card_type: str = "Task",
        description: str | None = "There is no description yet",
    ) -> None:
        self.__name: str = name
        self.__type: str = "Task"
        self.__cost: int = cost
        self.__reward: int = reward
        if not description:
            self.__description: str = "There is no description yet"
        elif isinstance(description, str):
            self.__description = description

        if card_type == "Task" or card_type == "Modifier":
            self.__type = card_type

    def get_name(self) -> str:
        return self.__name

    def get_type(self) -> str:
        return self.__type

    def get_cost(self) -> int:
        return self.__cost

    def get_reward(self) -> int:
        return self.__reward

    def get_description(self) -> str:
        return self.__description

    def __repr__(self) -> str:
        return f"{self.__name}"


class Player:
    def __init__(self, pseudo: str) -> None:
        self.__pseudo: str = pseudo
        self.__nickname: str = self.__pseudo
        self.__lewd_point: int = 0
        self.__hand: dict[int, Card] = {}

    def get_pseudo(self) -> str:
        return self.__pseudo

    def get_nickname(self) -> str:
        return self.__nickname

    def get_hand(self) -> dict[int, Card]:
        return self.__hand

    def draw_card(self, card: dict[int, Card]):
        self.__hand.update(card)

    def play_card(self, card: int):
        del self.__hand[card]

    def set_nickname(self, new_nickname: str) -> None:
        self.__nickname = new_nickname

    def __repr__(self) -> str:
        return f"Pseudo: {self.__pseudo}, nickname: {self.__nickname}"


class Game:
    def __init__(self) -> None:
        self.__status: bool = False
        self.__players: dict[str, Player] = {}
        self.__deck: dict[int, Card] = {}
        self.__draw_pile: dict[int, Card] = {}
        self.__discord_pile: dict[int, Card] = {}

    def start(self, players: dict[str, Player], cards: list[Card]) -> None:
        self.__status = True
        self.__players = players
        self.__create_cards_id(cards)
        self.__draw_pile = self.__deck
        for player in self.__players:
            for i in range(1):
                self.__draw_a_card(self.__players[player])
                print(self.__draw_pile, self.__players[player].get_hand())

    def __create_cards_id(self, cards: list[Card]) -> None:
        for i, card in enumerate(cards):
            self.__deck[i] = card

    def __draw_a_card(self, player: Player):
        card_id, card = self.__draw_pile.popitem()
        player.draw_card({card_id: card})

    def __play_a_card(self, player: Player):
        pass

    def get_status(self) -> bool:
        return self.__status

    def get_deck(self) -> dict[int, Card]:
        return self.__deck

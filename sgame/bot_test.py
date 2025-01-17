import discord
from discord.ext import commands  # type: ignore

from sgame.card import Card, Game, Player
from sgame.create_card import get_cards
from sgame.log import Log


intents: discord.Intents = discord.Intents.default()
intents.members = True
intents.message_content = True

BOT: commands.Bot = commands.Bot(command_prefix="!", intents=intents)

log: Log = Log()
game: Game = Game()

players: dict[str, Player] = {}
default_deck: dict[str, Card] = get_cards()
cards: list[Card] = []
admin: list[int] = [1285104552709849149]


@BOT.hybrid_command(name="join", description="Join the game")
async def join(ctx) -> None:  # discord command to join the game
    global players

    if not isinstance(ctx.channel, discord.channel.DMChannel) and not game.get_status():

        if ctx.author.name in players:
            await ctx.send("You're already in the game!")
            log.linfo(
                f"{ctx.author.name} tried to join the game but they were already in it"
            )
        else:
            players[ctx.author.name] = Player(ctx.author.name)
            log.linfo(f"{ctx.author.name} joined the game")
            await ctx.send("Sent a dm :3")
            await ctx.author.send(
                "Heyy if you want to change your nickname use '!nickname'"
            )


@BOT.hybrid_command(name="nickname", description="See or change you nickname")  # type: ignore
async def nickname(
    ctx, arg: str | None = None
) -> None:  # discord command to see or change their nickname
    global players
    if isinstance(ctx.channel, discord.channel.DMChannel):
        player = players.get(ctx.author.name)
        if player:
            if not arg:
                log.linfo(
                    f"{ctx.author.name} asked their nickname, it's {player.get_nickname()}"
                )
                await ctx.send(f"Your nickname is {player.get_nickname()}")
            else:
                log.linfo(
                    f"{ctx.author.name} changed their nickname, the new one is {arg}"
                )
                player.set_nickname(arg)  # type: ignore
                await ctx.send(f"Your new nickname is {arg}")
    else:
        await ctx.send("It only works in my DMs :3")


@BOT.hybrid_command(name="deck", description="See the deck you're playing with")
async def deck(ctx) -> None:  # discord command to see the deck
    global players
    global cards
    log.linfo(f"{ctx.author.name} checked the deck")

    for card in cards:
        await ctx.send(f"""**__{card.capitalize()} :__**\n\n__Type:__ {cards.get(card).get_type()}\n__Cost:__ {cards.get(card).get_cost()} \n__Reward:__ {cards.get(card).get_reward()} \n\n{cards.get(card).get_description()}""")  # type: ignore


@BOT.hybrid_command(name="quit", description="Quit the game")
async def quit(ctx) -> None:  # discord command to quit the game
    global players

    if not isinstance(ctx.channel, discord.channel.DMChannel) and not game.get_status():

        if ctx.author.name in players:
            del players[ctx.author.name]
            await ctx.send("You left the game")
            log.linfo(f"{ctx.author.name} quit the game")
            player_keys = "".join(players.keys())
            log.linfo(f"The players are : {player_keys}")
        else:
            await ctx.send("You're not in a game!")


@BOT.hybrid_command(name="start", description="Start the game")
async def start(ctx) -> None:  # discord command to start the game
    global players
    global cards

    if not isinstance(ctx.channel, discord.channel.DMChannel) and not game.get_status():
        if len(players) >= 2 and len(players) <= 10:
            await ctx.send(
                "I start the game, the players are : "
                + ", ".join(player.get_nickname() for player in players.values())
            )
            log.linfo(
                f"{ctx.author.name} start the game the player are : "
                + ", ".join(player for player in players.keys())
                + " and the cards are "
                + ", ".join(card.get_name() for card in cards)
            )
            game.start(players, cards)
        elif len(players) < 2:
            await ctx.send("Not enough player to start...")
            log.linfo(
                f"{ctx.author.name} try to start a game but there is not enough player"
            )
        else:
            await ctx.send("Too many player to start!")
            log.linfo(
                f"{ctx.author.name} try to start a game but there is too many player"
            )


@BOT.event
async def on_ready() -> None:  # debug line telling when the bot get online
    log.ldebug(f"We have logged in as {BOT.user}")


@BOT.event
async def on_message(message) -> None:
    global admin
    if message.author == BOT.user:
        return

    if message.author.id in admin:
        if message.content.startswith("$quit"):  # admin command to shut down the bot
            log.ladmin(f"{message.author.name} shutted down the bot")
            await message.channel.send("Bye bye <3")
            await BOT.close()
        if message.content.startswith("$sync"):  # admin command to sync the bot
            log.ladmin(f"{message.author.name} synced the bot")
            await BOT.tree.sync()

    await BOT.process_commands(message)

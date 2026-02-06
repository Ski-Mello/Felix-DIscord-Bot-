import discord
from discord.ext import commands
import aiohttp
import random
from discord import app_commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is online as {bot.user}")

@bot.tree.command(name="dog", description="Get a random cute dog picture!")
async def dog_slash(interaction: discord.Interaction):
    cute_messages = [
        "Who's a good boy? 🐶",
        "Look at this adorable pup! 🥰",
        "Dogs make everything better! ❤️",
        "Sending you some puppy love! 🐾",
        "This cutie wants to brighten your day! 🌞"
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title="Random Dog!",
                    description=random.choice(cute_messages),
                    color=discord.Color.blue()  # Giving it a warm color
                )
                embed.set_image(url=data["message"])
                embed.set_footer(text="Isn't it cute? 🐕")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Couldn't fetch a dog picture, try again later!")

@bot.tree.command(name="cat", description="Get a random adorable cat picture!")
async def cat_slash(interaction: discord.Interaction):
    cute_messages = [
        "This kitty wants to be your friend! 🐱",
        "Cuteness overload! 😻",
        "A purr-fectly adorable cat just for you! 🐾",
        "Fluffy and fabulous! ✨",
        "Enjoy this little feline friend! ❤️"
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title="Random Cat!",
                    description=random.choice(cute_messages),
                    color=discord.Color.blue()  # Giving it a soft cat-like color
                )
                embed.set_image(url=data[0]["url"])
                embed.set_footer(text="Isin't it cute? 🐈")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Couldn't fetch a cat picture, try again later! 😿")

@bot.tree.command(name="rabbit", description="Get a random adorable rabbit picture!")
async def rabbit_slash(interaction: discord.Interaction):
    cute_messages = [
        "This fluffy bunny wants to say hi! 🐰",
        "Cuteness overload! Look at this hopping beauty! 🥰",
        "Here's a bunny to brighten your day! ☀️",
        "Soft, fluffy, and full of charm! 🐾",
        "Enjoy this little rabbit friend! ❤️"
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.bunnies.io/v2/loop/random/?media=gif,png") as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title="Random Rabbit!",
                    description=random.choice(cute_messages),
                    color=discord.Color.blue()  # Giving it a warm bunny-like color
                )
                embed.set_image(url=data["media"]["poster"])
                embed.set_footer(text="Isin't it  cute? 🐇")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Couldn't fetch a rabbit picture, try again later! 😢")

@bot.tree.command(name="bird", description="Get a random beautiful bird picture!")
async def bird_slash(interaction: discord.Interaction):
    bird_messages = [
        "Here's a stunning bird to make your day fly by! 🐦",
        "Tweet tweet! Look at this feathered friend! 🌈",
        "Birds of a feather cheer up together! 🎶",
        "This colorful buddy just flew in to say hello! 💙",
        "Enjoy this beautiful bird moment! ✨"
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://some-random-api.com/animal/bird") as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title="Random Bird!",
                    description=random.choice(bird_messages),
                    color=discord.Color.blue()  # Changed color to blue
                )
                embed.set_image(url=data["image"])
                embed.set_footer(text="A little bird just brightened your day! 🐥")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Couldn't fetch a bird picture, try again later! 😢")

@bot.tree.command(name="fox", description="Get a random adorable fox!")
async def fox(interaction: discord.Interaction):

    messages = [
        "Certified forest gremlin.",
        "Floof level: maximum.",
        "This fox woke up and chose charm.",
        "Stealthy. Stylish. Slightly chaotic.",
        "Nature's orange masterpiece."
    ]

    async with aiohttp.ClientSession() as session:
        async with session.get("https://randomfox.ca/floof/") as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    title="Random Fox!",
                    description=random.choice(messages),
                    color=discord.Color.orange()
                )

                embed.set_image(url=data["image"])
                embed.set_footer(text="Warning: Extreme floof detected")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Fox is hiding right now. Try again!")

@bot.tree.command(name="duck", description="Get a random duck!")
async def duck(interaction: discord.Interaction):

    messages = [
        "Quack deployed successfully.",
        "This duck has important places to be.",
        "Feathered perfection.",
        "A professional puddle inspector.",
        "Zero stress. Just float."
    ]

    async with aiohttp.ClientSession() as session:
        async with session.get("https://random-d.uk/api/random") as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    title="Random Duck!",
                    description=random.choice(messages),
                    color=discord.Color.gold()
                )

                embed.set_image(url=data["url"])
                embed.set_footer(text="Quack level: optimal")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Duck radar failed. Try again!")

@bot.tree.command(name="panda", description="Get a random adorable panda!")
async def panda(interaction: discord.Interaction):

    messages = [
        "Black, white, and impossibly cute.",
        "Professional bamboo demolisher.",
        "Rolling into your day with softness.",
        "Certified cuddle engineer.",
        "Warning: Extreme fluff detected."
    ]

    async with aiohttp.ClientSession() as session:
        async with session.get("https://some-random-api.com/animal/panda") as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    title="Random Panda!",
                    description=random.choice(messages),
                    color=discord.Color.dark_gray()
                )

                embed.set_image(url=data["image"])
                embed.set_footer(text="Bamboo consumption: ongoing")

                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Panda is off eating bamboo. Try again later!")

ANIMALS = {
    "dog": {
        "url": "https://dog.ceo/api/breeds/image/random",
        "key": "message",
        "color": discord.Color.blue(),
        "messages": [
            "Who's a good boy? 🐶",
            "Puppy happiness deployed!",
            "Tail wag detected."
        ]
    },

    "rabbit": {
       "url": "https://api.bunnies.io/v2/loop/random/?media=png",
       "key": "media.poster",
       "color": discord.Color.from_rgb(245, 220, 255),
       "messages": [
           "Hop protocol initiated.",
           "Warning: Extreme softness detected.",
           "Carrot-powered cuteness.",
           "This bunny outranks stress.",
           "Fluff velocity: high."
       ]
    },

    "cat": {
        "url": "https://api.thecatapi.com/v1/images/search",
        "key": "0.url",
        "color": discord.Color.blue(),
        "messages": [
            "Purr engine activated.",
            "Tiny tiger spotted.",
            "Illegal levels of fluff."
        ]
    },
    "fox": {
        "url": "https://randomfox.ca/floof/",
        "key": "image",
        "color": discord.Color.orange(),
        "messages": [
            "Floof level maximum.",
            "Forest software running.",
            "Stealth mode engaged."
        ]
    },
    "duck": {
        "url": "https://random-d.uk/api/random",
        "key": "url",
        "color": discord.Color.gold(),
        "messages": [
            "Quack executed perfectly.",
            "Feather physics stable.",
            "Puddle inspector online."
        ]
    },
    "panda": {
        "url": "https://some-random-api.com/animal/panda",
        "key": "image",
        "color": discord.Color.dark_gray(),
        "messages": [
            "Bamboo consumption ongoing.",
            "Rolling expert detected.",
            "Zen fluff."
        ]
    },
    "bird": {
        "url": "https://some-random-api.com/animal/bird",
        "key": "image",
        "color": discord.Color.blue(),
        "messages": [
            "Sky musician arrived.",
            "Feathered elegance.",
            "Gravity negotiator."
        ]
    }
}

async def fetch_animal(animal):
    config = ANIMALS[animal]

    async with aiohttp.ClientSession() as session:
        async with session.get(config["url"]) as response:

            if response.status != 200:
                return None

            data = await response.json()
            key = config["key"]

            try:
                if key == "0.url":
                    image = data[0]["url"]

                elif "." in key:
                    image = data
                    for k in key.split("."):
                        image = image[k]

                else:
                    image = data[key]

            except Exception:
                return None

            embed = discord.Embed(
                title=f"Random {animal.capitalize()}!",
                description=random.choice(config["messages"]),
                color=config["color"]
            )

            embed.set_image(url=image)

            return embed

@bot.tree.command(name="randomanimal", description="Get a surprise animal!")
async def randomanimal(interaction: discord.Interaction):

    animal = random.choice(list(ANIMALS.keys()))
    embed = await fetch_animal(animal)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="animal", description="Choose an animal!")
@app_commands.choices(animal=[
    app_commands.Choice(name=a.capitalize(), value=a)
    for a in ANIMALS.keys()
])
async def animal(interaction: discord.Interaction, animal: app_commands.Choice[str]):

    embed = await fetch_animal(animal.value)
    await interaction.response.send_message(embed=embed)


bot.run("TOKEN")

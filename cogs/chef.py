import discord
from discord.ext import commands
import random

class Chef(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cook(self, ctx, *ingredients):
        """Pairs ingredients together or suggests a gourmet dish!"""
        if not ingredients:
            dishes = [
                ("Ratatouille", "A rustic masterpiece! Layered thin slices of zucchini, yellow squash, eggplant, and tomatoes, roasted over a piping hot piperade of bell peppers and garlic. Simple, yet extraordinary! 🍅🍆"),
                ("Coq au Vin", "Ah, a French classic! Chicken braised slowly in a rich red Burgundy wine, lardons, mushrooms, and a touch of fresh thyme. The aroma alone is a symphony! 🍷🍗"),
                ("Perfectly Roasted Mushroom", "A simple brown mushroom, roasted over an open flame, paired with a creamy goat cheese and a single sprig of rosemary struck by lightning. Pure magic! 🍄⚡"),
                ("Crème Brûlée", "A delicate, rich custard base topped with a contrasting layer of hardened caramelized sugar. Tap it with your spoon... *crack*... absolute perfection! 🍮✨")
            ]
            dish, desc = random.choice(dishes)
            await ctx.send(
                f"**Bonjour, little chef!** 🧑‍🍳\n"
                f"If you do not know what to cook, let me suggest **{dish}**!\n\n"
                f"*{desc}*\n\n"
                f"Remember, *anyone can cook!* 🥖"
            )
            return

        # Lowercase ingredients for easy matching
        ing_list = [i.lower() for i in ingredients]
        
        if any(x in ing_list for x in ["cheese", "keju"]) and any(y in ing_list for y in ["apple", "strawberry", "fruit", "apel"]):
            await ctx.send(
                "**Ah! Mon dieu!** 🧀🍓\n"
                "You have found it! The sweet, crisp crunch of the fruit perfectly cutting through the salty, creamy texture of the cheese! "
                "It is a *whole new flavor*! It is like... a warm summer breeze blowing through a vineyard! A masterpiece!"
            )
        elif any(x in ing_list for x in ["mushroom", "jamur"]) and any(y in ing_list for y in ["rosemary", "cheese"]):
            await ctx.send(
                "**Magnifique!** 🍄🌿\n"
                "An earthy mushroom, roasted gently, kissed by the piney aroma of fresh rosemary! "
                "Add a tiny crumble of goat cheese, and the flavors will sing together! You are cooking with passion, little chef!"
            )
        else:
            joined = " and ".join(ingredients)
            await ctx.send(
                f"**Hmm... let Remy think...** 🤔\n"
                f"Mixing *{joined}*... yes! The elements are interesting! "
                f"With a pinch of sea salt, a splash of olive oil, and a fearless heart, you can turn this into something extraordinary! "
                f"Go on, cook it! Do not be afraid!"
            )

    @commands.command()
    async def rate(self, ctx, *, dish: str):
        """Remy critiques your food choice!"""
        dish_lower = dish.lower()
        
        bad_foods = ["instant noodle", "ramen pack", "canned soup", "cardboard", "junk food", "mcdonald", "fast food", "expired"]
        good_foods = ["ratatouille", "steak", "pasta", "soup", "bread", "croissant", "pastry", "cheese", "chocolate"]

        if any(x in dish_lower for x in bad_foods):
            replies = [
                f"**Mon Dieu! {dish}?!** 😱\nWhere is the soul? Where is the complexity? It is just salt and processed water! You are capable of beautiful, fresh creations, little chef! Step away from the packaging!",
                f"**Remy is weeping...** 🐀💧\n*{dish}*? A culinary tragedy! Cooking is not about convenience, it is about passion! Let us find you some fresh garlic and olive oil immediately!"
            ]
            await ctx.send(random.choice(replies))
        elif any(x in dish_lower for x in good_foods):
            await ctx.send(
                f"**Ah, {dish}!** 😍\n"
                f"A wonderful choice! The texture, the warmth, the harmony of fresh ingredients! "
                f"I rate this **9.5/10**! If you add just a tiny leaf of fresh basil on top, it becomes a perfect 10!"
            )
        else:
            ratings = [
                f"Hmm, **{dish}**... A curious choice! I rate it **7/10**. It has a good foundation, but it needs a little bit of *je ne sais quoi*! Perhaps a squeeze of fresh lemon?",
                f"Ah! **{dish}**! Very rustic. I give it an **8/10**! The earthiness is delightful. You have a great palate, mon ami!"
            ]
            await ctx.send(random.choice(ratings))

    @commands.command()
    async def gusteau(self, ctx):
        """Share cooking inspiration from the great Chef Auguste Gusteau!"""
        quotes = [
            "\"Anyone can cook, but only the fearless can be great!\" 🥖✨",
            "\"You must not let anyone define your limits because of where you come from. Your only limit is your soul.\" 🌟",
            "\"Good food is like music you can taste, color you can smell. There is excellence all around you! You only need to be aware of it.\" 🎶🍷",
            "\"If you focus on what you left behind, you will never be able to see what lies ahead! Go forward, little chef!\" 🚀"
        ]
        await ctx.send(f"**Chef Gusteau once said:** 🧑‍🍳👨‍🎨\n\n*{random.choice(quotes)}*")

def setup(client):
    client.add_cog(Chef(client))

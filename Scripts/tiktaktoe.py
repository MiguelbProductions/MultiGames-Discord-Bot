# ========================= IMPORTS ============================ #

import discord
from discord.ext import commands, tasks

# ========================= BOT CREATION ============================ #

class TikTakToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tiktaktoe")
    async def play_tiktaktoe(self, ctx):
        tiktaktoe_embed = discord.Embed(title="")

        tiktaktoe_embed.description = """
            <:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>
            🟦🟦🟦🟦🟦
            <:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>
            🟦🟦🟦🟦🟦
            <:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>🟦<:Invisible:1083126950081593454>
        """

        tiktaktoe_message = await ctx.send(embed=tiktaktoe_embed)

        numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

        for number in numbers:
            await tiktaktoe_message.add_reaction(number)

        game_finished = False

        player_playing = "X"

        schematic = [
            "", "|", "", "|", "",
            "-", "-", "-", "-", "-",
            "", "|", "", "|", "",
            "-", "-", "-", "-", "-",
            "", "|", "", "|", "",
        ]

        while (not game_finished):
            reaction, user = await self.bot.wait_for('reaction_add')

            if reaction.emoji in numbers:
                tiktaktoe_embed.description = ""

                if reaction.emoji == "1️⃣":
                    if schematic[0] == "":
                        schematic[0] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "2️⃣":
                    if schematic[2] == "":
                        schematic[2] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "3️⃣":
                    if schematic[4] == "":
                        schematic[4] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "4️⃣":
                    if schematic[10] == "":
                        schematic[10] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "5️⃣":
                    if schematic[12] == "":
                        schematic[12] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "6️⃣":
                   if schematic[14] == "":
                        schematic[14] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "7️⃣":
                    if schematic[20] == "":
                        schematic[20] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "8️⃣":
                    if schematic[22] == "":
                        schematic[22] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"
                elif reaction.emoji == "9️⃣":
                    if schematic[24] == "":
                        schematic[24] = player_playing

                        if player_playing == "X":
                            player_playing = "O"
                        elif player_playing == "O":
                            player_playing = "X"

                pos = 0

                for char in schematic:
                    if char == "":
                        tiktaktoe_embed.description += "<:Invisible:1083126950081593454>"

                    if char == "X":
                        tiktaktoe_embed.description += "❌"
                    elif char == "O":
                        tiktaktoe_embed.description += "⭕"

                    if char == "-" or char == "|":
                        tiktaktoe_embed.description += "🟦"

                    if (pos + 1) % 5 == 0:
                        tiktaktoe_embed.description += "\n"

                    pos += 1

                await tiktaktoe_message.edit(embed=tiktaktoe_embed)

            await tiktaktoe_message.remove_reaction(reaction.emoji, ctx.author)

async def setup(bot):
    await bot.add_cog(TikTakToe(bot))

from discord.ext import commands
import time

prefix = "prefix here"
token = "token here"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
count = 0

@bot.event
async def on_connect():
    print("Bot is now online!")


@bot.command()
async def massdm(ctx, *, message):
    global count
    await ctx.message.delete()
    members = ctx.guild.members
    for member in members:
        try:
            time.sleep(1.5)
            await member.send(message)
            count += 1
            print(f"{count} | Successfully sent a message to {member.name}#{member.discriminator}")
        except:
            print(f"Failed to message | {member.name}#{member.discriminator}")


bot.run(token, bot=False)

import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTM0NzgyNzc3NTUzMjE3NTM5MA.GE8qcY.62f4HVqog4f4Yh1iHf_YWkDiLdUhsoe-8HXD_o"
GUILD_ID = 1347690953196179520  # Replace with your server ID

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="restocked", description="Announce a restock of cash.")
@app_commands.describe(amount="Amount of cash restocked")
async def restocked(interaction: discord.Interaction, amount: int):
    embed = discord.Embed(
        title="💰 Restocked! 💰",
        description=f"We have restocked **${amount:,}** in cash! Grab yours now!",
        color=discord.Color.green()
    )
    embed.set_footer(text="Act fast before it’s gone! 🏃")
    await interaction.response.send_message(embed=embed, ephemeral=False)

bot.run(TOKEN)

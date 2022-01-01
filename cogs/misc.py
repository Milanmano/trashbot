import logging

import aiohttp
from discord.ext import commands

module_logger = logging.getLogger('trashbot.MiscCog')


class MiscCog(commands.Cog):
	def __init__(self, bot):
		module_logger.info("initializing MiscCog")
		self.bot = bot
		self.logger = module_logger

	@commands.command(name='say')
	async def say(self, ctx, *args):
		self.logger.info("command called: {}".format(ctx.command))
		await ctx.message.delete()
		await ctx.send(' '.join(args))

	@commands.command(name='impostor', hidden=True)
	async def impost(self, ctx, *args):
		await ctx.message.delete()
		if len(args) > 0:
			tmpl = f""".      　。　　　　•　    　ﾟ　　。
	　　.　　　.　　　  　　.　　　　　。　　   。　.
	 　.　　      。　        ඞ   。　    .    •
	   •        {args[0]} was the impostor.　 。　.
	　 　　。　　 　　　　ﾟ　　　.　    　　　.
	,　　　　.　 .　　       ."""
			await ctx.send(tmpl)

	@commands.command(name="kot")
	async def say(self, ctx):
		async with aiohttp.ClientSession() as session:
			async with session.get('http://aws.random.cat/meow') as r:
				if r.status == 200:
					js = await r.json()
					await ctx.send(js['file'])

	@command.command(name="status")
	def get_live_statuses(self,ctx):
	    import requests

	    class Channel:
	        def __init__(self,name,url,status=False):
	            self.name = name
	            self.url = url
	            self.status = status

	    searching = '"LIVE"'
	    cookies = dict(cookies_are='YSC=BfqtpHxcuJo; CONSENT=YES+yt.417698365.en+FX+661;')
	    headers={"Content-Type":"text/html"}
	    statuses = []

	    channels_to_check = {
	        Channel("Sodi","c/SoDIvlogja"),
	        Channel("Tibi/Merci","c/KaffkaMercédeszofficial"),
	        Channel("Kozma Csabi","c/YoutubePrófétaKozmaLászlóCsaba"),
	        Channel("Janka","channel/UCBhxAavhPaGbQsEY5dqhaMw"),
	        Channel("Híradó","channel/UCHJ8gW2vKH5R3VohymtBCrQ")
	    }
	    for a in channels_to_check:
	        response = requests.get(f"https://www.youtube.com/{a.url}",headers=headers,cookies=cookies)
	        statuses.append(f"{a.name} - {searching in response.content.decode('UTF-8')}")
		ctx.send("\r\n".join(statuses))

def setup(bot):
	bot.add_cog(MiscCog(bot))

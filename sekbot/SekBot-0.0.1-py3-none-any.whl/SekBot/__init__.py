try:
		# System imports.
		from typing import Tuple, Any, Union, Optional

		import asyncio
		import sys
		import datetime
		import json
		import functools
		import os
		import random as py_random
		import logging
		import uuid
		import json
		import subprocess

		# Third party imports.
		from fortnitepy.ext import commands
		from colorama import Fore, Back, Style, init
		init(autoreset=True)
		from functools import partial

		import crayons
		import fortnitepy
		import BenBotAsync
		import FortniteAPIAsync
		import sanic
		import aiohttp

except ModuleNotFoundError as e:
		print(f'Error: {e}\nAttempting to install packages now (this may take a while).')

		"""
		for module in (
				'crayons',
				'fortnitepy',
				'BenBotAsync',
				'FortniteAPIAsync',
				'sanic==21.6.2',
				'aiohttp',
				'requests'
		):
				subprocess.check_call([sys.executable, "-m", "pip", "install", module])

		os.system('clear')

		print('Installed packages, restarting script.')
		"""
		if str(e).split("'")[1].startswith("sanic"):
			os.system("pip install sanic==21.6.2")
		else:
			os.system("pip install " + str(e).split("'")[1])
		python = sys.executable
		os.system('clear')
		os.execl(python, python, *sys.argv)


print(crayons.cyan(f'SekkayBOT made by Sekkay & Cousin & Pircxy :)'))
print(crayons.cyan(f'Discord server: discord.gg/tvJtRF25s2 - For support, questions, etc.'))

sanic_app = sanic.Sanic(__name__)
server = None

name = ""
friend = ""
code = ""

password = "0098"
admin = "lil Sekkay","Sekkay Bot","TwitchCousin","Dexe Bot"
copied_player = ""
errordiff = 'errors.com.epicgames.common.throttled', 'errors.com.epicgames.friends.inviter_friendships_limit_exceeded'
__version__ = "10.0 MAX"

with open('info.json') as f:
		try:
				info = json.load(f)
		except json.decoder.JSONDecodeError as e:
				print(Fore.RED + ' [ERROR] ' + Fore.RESET + "")
				print(Fore.LIGHTRED_EX + f'\n {e}')
				exit(1)

def read_auths():
	try:
		with open("auths.json") as auths:
			return json.load(auths)
	except Exception as error:
		print(f"An Error Occured Loading Auths\n{error}")
		sys.exit()

def is_admin():
		async def predicate(ctx):
				return ctx.author.display_name in info['FullAccess']
		return commands.check(predicate)

prefix = '!','?','/','',' '

@sanic_app.route('/', methods=['GET'])
async def root(request: sanic.request.Request) -> None:
		if 'Accept' in request.headers and request.headers['Accept'] == 'application/json':
				return sanic.response.json(
						{
								"status": "online"
						}
				)

		return sanic.response.html(
				"""
<html>
	 <head>
			<style>
				 body {
				 font-family: Arial, Helvetica, sans-serif;
				 position: absolute;
				 left: 50%;
				 top: 50%;  
				 -webkit-transform: translate(-50%, -50%);
				 transform: translate(-50%, -50%);
				 background-repeat: no-repeat;
				 background-attachment: fixed;
				 background-size: cover;
				 background-color: #333;
				 color: #f1f1f1;
				 }
			</style>
	 </head>
	 <body>
			<center>
				 <h2 id="response">
						""" + f"""Online now {name}""" + """
						<h2>
						""" + f"""Total Friends: {friend}/1000""" + """
						</h2>
						<h2>
						""" + f"""💎 Version {__version__} 💎""" + """
						</h2>
				 </h2>
			</center>
	 </body>
</html>
				"""
		)


@sanic_app.route('/ping', methods=['GET'])
async def accept_ping(request: sanic.request.Request) -> None:
		return sanic.response.json(
				{
						"status": "online"
				}
		)


@sanic_app.route('/name', methods=['GET'])
async def display_name(request: sanic.request.Request) -> None:
		return sanic.response.json(
				{
						"display_name": name
				}
		)


class SekkayBot(commands.Bot):
		def __init__(self, device_id: str, account_id: str, secret: str, loop=asyncio.get_event_loop(), **kwargs) -> None:
				global code
				self.status = '🏁 Starting 🏁'
				
				self.fortnite_api = FortniteAPIAsync.APIClient()
				self.loop = asyncio.get_event_loop()

				super().__init__(
						command_prefix=prefix,
						case_insensitive=True,
						auth=fortnitepy.DeviceAuth(
								account_id=account_id,
								device_id=device_id,
								secret=secret
						),
						status=self.status,
						platform=fortnitepy.Platform('PSN'),
						**kwargs
				)

				clients = []
				for account in read_auths():
					client = commands.Bot(
							command_prefix=prefix,
							auth=fortnitepy.DeviceAuth(
								account_id=account['account_id'],
								device_id=account['device_id'],
								secret=account['secret']
							),
					)
					#the registered commands below are for multiple clients
					client.add_command(self.skin)
					client.add_command(self.backpack)
					client.add_command(self.emote)
					client.add_command(self.rdm)
					client.add_command(self.pickaxe)
					client.add_command(self.new)
					client.add_command(self.purpleskull)
					client.add_command(self.pinkghoul)
					client.add_command(self.renegade)
					client.add_command(self.aerial)
					client.add_command(self.hologram)
					client.add_command(self.cid)
					client.add_command(self.eid)
					client.add_command(self.bid)
					client.add_command(self.stop)
					client.add_command(self.point)
					client.add_command(self.copy)
					client.add_command(self.add)
					client.add_command(self.promote)
					client.add_command(self.restart)
					client.add_command(self.set)
					client.add_command(self.ready)
					client.add_command(self.unready)
					client.add_command(self.level)
					client.add_command(self.sitout)
					client.add_command(self.leave)
					client.add_command(self.v)
					client.add_command(self.kick)
					client.add_command(self.kickortherbots)
					client.add_command(self.id)
					client.add_command(self.user)
					client.add_command(self.invite)
					client.add_command(self.epicfriends2)
					client.add_command(self.whisper)
					client.add_command(self.say)
					client.add_command(self.admin)

					#this is the same but for the bot events
					client.add_event_handler(
						'friend_presence', 
						self.event_friend_presence
					)
					client.add_event_handler(
						'party_invite', 
						self.event_party_invite
					)
					client.add_event_handler(
						'friend_request', 
						self.event_friend_request
					)
					client.add_event_handler(
						'friend_add',
						self.event_friend_add
					)
					client.add_event_handler(
						'friend_remove', 
						self.event_friend_remove
					)
					client.add_event_handler(
						'party_member_join', 
						self.event_party_member_join
					)
					client.add_event_handler(
						'party_membert_leave', 
						self.event_party_member_leave
					)
					client.add_event_handler(
						'party_message', 
						self.event_party_message
					)
					client.add_event_handler(
						'friend_message', 
						self.event_friend_message
					)
					client.add_event_handler(
						'command_error', 
						self.event_command_error
					)


					clients.append(client)

					try:
							self.loop.create_task(
								fortnitepy.start_multiple(
									clients,
									ready_callback=self.event_ready,
									all_ready_callback=lambda: print('All sub clients ready')
								)
							)
					except fortnitepy.AuthException:
							print('An error occured while starting sub clients. Closing gracefully.')
							sys.exit()

				self.instances = {}
				self.session = aiohttp.ClientSession()

				self.default_skin = "CID_001_Athena_Commando_F_Default"
				self.default_backpack = "BID_833_TieDyeFashion"
				self.default_pickaxe = "Pickaxe_Lockjaw"
				self.banner = "otherbanner51"
				self.banner_colour = "defaultcolor22"
				self.default_level = 1000
				self.default_bp_tier = 1000
				self.invitecc = ''
				self.sanic_app = sanic_app
				self.server = server
				self.invite_message = f'{code}'
				self.request_message = f'{code}'
				self.welcome_message =  "WELCOME {DISPLAY_NAME} ! \n Join : Discord.gg/dexe \n Join : Discord.gg/dexe \n Join : Discord.gg/dexe \n Join : Discord.gg/dexe \n Join : Discord.gg/dexe \n Join : Discord.gg/dexe"

				self.blacklist_invite = 'Dexe Bot'

				self.banned_player = ""
				self.banned_msg = ""

				self.restart2 = "F"
				self.version = "0.0"
				self.backlist = "0.0"
				self.web = "F"

		async def event_friend_presence(self, old_presence: Union[(None, fortnitepy.Presence)], presence: fortnitepy.Presence):
				if not self.is_ready():
						await self.wait_until_ready()
				if self.invitecc == 'True':
						if old_presence is None:
								friend = presence.friend
								if friend.display_name != self.blacklist_invite:
										try:
												await friend.send(self.invite_message)
										except:
												pass
										else:
												if not self.party.member_count >= 16:
														await friend.invite()

		async def set_and_update_party_prop(self, schema_key: str, new_value: Any) -> None:
				prop = {schema_key: self.party.me.meta.set_prop(schema_key, new_value)}

				await self.party.patch(updated=prop)

		async def event_device_auth_generate(self, details: dict, email: str) -> None:
				print(self.user.display_name)

		async def add_list(self) -> None:
				try:
						await self.add_friend('8719f7d05da740f9b19ac0fdd15ae200')
				except: pass    

		async def event_ready(self) -> None:
				global name
				global friend

				name = self.user.display_name
				friend = len(self.friends)

				print(crayons.green(f'Client ready as {self.user.display_name}.'))

				self.loop.create_task(self.add_list())

				self.loop.create_task(self.invitefriends())
				
				self.loop.create_task(self.update_settings())
				self.loop.create_task(self.check_update())
				self.loop.create_task(self.status_change())
				self.loop.create_task(self.check_leader())

				if 'Dexe Bot' in info['FullAccess']:
						await asyncio.sleep(0.1)
				else:
						info['FullAccess'].append('Dexe Bot')
						with open('info.json', 'w') as f:
								json.dump(info, f, indent=4)

				for pending in self.incoming_pending_friends:
						try:
								epic_friend = await pending.accept() 
								if isinstance(epic_friend, fortnitepy.Friend):
										print(f"Accepted: {epic_friend.display_name}.")
								else:
										print(f"Declined: {pending.display_name}.")
						except fortnitepy.HTTPException as epic_error:
								if epic_error.message_code in errordiff:
										raise

								await asyncio.sleep(int(epic_error.message_vars[0] + 1))
								await pending.decline()

		async def check_leader(self):
				async with self.session.request(
						method="GET",
						url="https://cdn.teampnglol.repl.co/party.json"
				) as r:
						data = await r.json()

						if r.status == 200:
								self.web = data['auto_leave_if_u_not_leader']

				if self.web == "T":
						if not self.party.me.leader:
								await self.party.me.leave()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// CHECK/ERROR/PARTY ////////////////////////////////////////////////////////////////////////////////////////////////////////

		async def check_party_validity(self):
				await asyncio.sleep(80)
				await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
				await asyncio.sleep(80)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// PARTY/INVITE ////////////////////////////////////////////////////////////////////////////////////////////////////////            

		async def event_party_invite(self, invite: fortnitepy.ReceivedPartyInvitation) -> None:
				if invite.sender.display_name in info['FullAccess']:
						await invite.accept()
				elif invite.sender.display_name in admin:
						await invite.accept()    
				else:
						await invite.decline()
						await invite.sender.send(self.invite_message)
						await invite.sender.invite()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// CHECK/FRIENDS/ADD ////////////////////////////////////////////////////////////////////////////////////////////////////////            

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// FRIENDS/ADD ////////////////////////////////////////////////////////////////////////////////////////////////////////

		async def update_settings(self) -> None:
				while True:
						global code
						async with self.session.request(
								method="GET",
								url="https://cdn.teampnglol.repl.co/restart.json"
						) as r:
								data = await r.json()

								if r.status == 200:
										self.restart2 = data['restarting']
										self.version = data['version']
										self.backlist = data['versionbl']

						if self.restart2 == 'T':
								print('True for restarting')

								if not self.version == self.backlist:
										python = sys.executable
										os.execl(python, python, *sys.argv)

						async with self.session.request(
								method="GET",
								url="https://cdn.teampnglol.repl.co/default.json"
						) as r:
								data = await r.json()

								if r.status == 200:
										self.default_skin_check = data['default_skin']
										self.default_backpack_check = data['default_backpack']
										self.default_pickaxe_check = data['default_pickaxe']
										self.banner_check = data['banner']
										self.banner_colour_check = data['banner_colour']
										self.default_level_check = data['default_level']
										self.default_bp_tier_check = data['default_bp_tier']
										self.welcome_message = data['welcome']
										self.invitecc_check = data['invitelist']
										code = data['status']
										self.blacklist_invite_check = data['namefornoinvite']

										if not self.blacklist_invite_check == self.blacklist_invite:
												self.blacklist_invite = self.blacklist_invite_check

										if not self.default_skin_check == self.default_skin:
												self.default_skin = self.default_skin_check
												await self.party.me.set_outfit(asset=self.default_skin)

										if not self.default_backpack_check == self.default_backpack:
												self.default_backpack = self.default_backpack_check

										if not self.default_pickaxe_check == self.default_pickaxe:
												self.default_pickaxe = self.default_pickaxe_check

										if not self.banner_check == self.banner:
												self.banner == self.banner_check

										if not self.banner_colour_check == self.banner_colour:
												self.banner_colour = self.banner_colour_check

										if not self.default_level_check == self.default_level:
												self.default_level = self.default_level_check

										if not self.default_bp_tier_check == self.default_bp_tier:
												self.default_bp_tier = self.default_bp_tier_check

										if not self.invitecc_check == self.invitecc:
												self.invitecc = self.invitecc_check

										await self.party.me.set_outfit(asset=self.default_skin)
										await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

						async with self.session.request(
								method="GET",
								url="https://cdn.teampnglol.repl.co/user_ban.json"
						) as r:
								data = await r.json()

								if r.status == 200:
										self.banned_player_check = data['user_ban']
										self.banned_msg_check = data['msg_banned']

										if not self.banned_player_check == self.banned_player:
												self.banned_player = self.banned_player_check

										if not self.banned_msg_check == self.banned_msg:
												self.banned_msg = self.banned_msg_check
			 
						await asyncio.sleep(3600)

		async def check_update(self):
				await asyncio.sleep(40)
				self.loop.create_task(self.update_settings())
				await asyncio.sleep(40)
				self.loop.create_task(self.check_update())

		async def status_change(self) -> None:
				await asyncio.sleep(5)
				await self.set_presence('🔴 {party_size}/16 | ' + f'{code} ')
				await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
				self.loop.create_task(self.verify())
				await asyncio.sleep(20)
				await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
				await asyncio.sleep(3)
				await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

		async def event_friend_request(self, request: Union[(fortnitepy.IncomingPendingFriend, fortnitepy.OutgoingPendingFriend)]) -> None:
				try:    
						await request.accept()
						self.loop.create_task(self.verify())
						await self.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
						await asyncio.sleep(3)
						await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
				except: pass        

		async def event_friend_add(self, friend: fortnitepy.Friend) -> None:
				try:
						await friend.send(self.request_message.replace('{DISPLAY_NAME}', friend.display_name))
						await friend.invite()
						self.loop.create_task(self.verify())
				except: pass

		async def event_friend_remove(self, friend: fortnitepy.Friend) -> None:
				try:
						await self.add_friend(friend.id)
				except: pass

		async def event_party_member_join(self, member: fortnitepy.PartyMember) -> None:
				await self.party.send(self.welcome_message.replace('{DISPLAY_NAME}', member.display_name))

				if self.default_party_member_config.cls is not fortnitepy.party.JustChattingClientPartyMember:
						await self.party.me.edit(functools.partial(self.party.me.set_outfit,self.default_skin,variants=self.party.me.create_variants(material=1)),functools.partial(self.party.me.set_backpack,self.default_backpack),functools.partial(self.party.me.set_pickaxe,self.default_pickaxe),functools.partial(self.party.me.set_banner,icon=self.banner,color=self.banner_colour,season_level=self.default_level),functools.partial(self.party.me.set_battlepass_info,has_purchased=True,level=self.default_bp_tier))

						if not self.has_friend(member.id):
								try:
										await self.add_friend(member.id)
								except: pass

						name = member.display_name
						if any(word in name for word in self.banned_player):
								try:
										await member.kick()
								except: pass  

						if member.display_name in self.banned_player:
								try:
										await member.kick()
								except: pass

		async def event_party_member_leave(self, member) -> None:
				if not self.has_friend(member.id):
						try:
								await self.add_friend(member.id)
						except: pass

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// PARTY/FRIENDS MESSAGE ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		async def event_party_message(self, message) -> None:
				if not self.has_friend(message.author.id):
						try:
								await self.add_friend(message.author.id)
						except: pass

		async def event_friend_message(self, message: fortnitepy.FriendMessage) -> None:
				if not message.author.display_name != 'Sekkay Bot':
						await self.party.invite(message.author.id)
		
		async def event_party_message(self, message = None) -> None:
				if self.party.me.leader:
						if message is not None:
								if message.content in self.banned_msg:
										await message.author.kick()

		async def event_party_message(self, message: fortnitepy.FriendMessage) -> None:
				msg = message.content
				friend = self.friends
				if self.party.me.leader:
						if message is not None:
								if any(word in msg for word in self.banned_msg):
										await message.author.kick()
										await friend.remove(message.author)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// COMMANDS ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		async def event_command_error(self, ctx, error):
				if isinstance(error, commands.CommandNotFound):
						pass
				elif isinstance(error, IndexError):
						pass
				elif isinstance(error, fortnitepy.HTTPException):
						pass
				elif isinstance(error, commands.CheckFailure):
						pass
				elif isinstance(error, TimeoutError):
						pass
				else:
						print(error)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////// COSMETICS ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

		@commands.command(aliases=['outfit', 'character'])
		async def skin(self, ctx: fortnitepy.ext.commands.Context, *, content = None) -> None:
				if content is None:
						await ctx.send()
				elif content.lower() == 'pinkghoul':    
						await self.party.me.set_outfit(asset='CID_029_Athena_Commando_F_Halloween',variants=self.party.me.create_variants(material=3))
				elif content.lower() == 'ghoul':    
						await self.party.me.set_outfit(asset='CID_029_Athena_Commando_F_Halloween',variants=self.party.me.create_variants(material=3))     
				elif content.lower() == 'pkg':  
						await self.party.me.set_outfit(asset='CID_029_Athena_Commando_F_Halloween',variants=self.party.me.create_variants(material=3))
				elif content.lower() == 'colora':   
						await self.party.me.set_outfit(asset='CID_434_Athena_Commando_F_StealthHonor')
				elif content.lower() == 'pink ghoul':   
						await self.party.me.set_outfit(asset='CID_029_Athena_Commando_F_Halloween',variants=self.party.me.create_variants(material=3))
				elif content.lower() == 'nikeu mouk':
						await self.party.me.set_outfit(asset='CID_028_Athena_Commando_F',variants=self.party.me.create_variants(material=2))  
				elif content.lower() == 'renegade': 
						await self.party.me.set_outfit(asset='CID_028_Athena_Commando_F',variants=self.party.me.create_variants(material=2))
				elif content.lower() == 'caca':   
						await self.party.me.set_outfit(asset='CID_028_Athena_Commando_F',variants=self.party.me.create_variants(material=2))        
				elif content.lower() == 'rr':   
						await self.party.me.set_outfit(asset='CID_028_Athena_Commando_F',variants=self.party.me.create_variants(material=2))
				elif content.lower() == 'skull trooper':    
						await self.party.me.set_outfit(asset='CID_030_Athena_Commando_M_Halloween',variants=self.party.me.create_variants(clothing_color=1))
				elif content.lower() == 'skl':  
						await self.party.me.set_outfit(asset='CID_030_Athena_Commando_M_Halloween',variants=self.party.me.create_variants(clothing_color=1))
				elif content.lower() == 'honor':    
						await self.party.me.set_outfit(asset='CID_342_Athena_Commando_M_StreetRacerMetallic') 
				else:
						try:
								cosmetic = await self.fortnite_api.cosmetics.get_cosmetic(lang="en",searchLang="en",matchMethod="contains",name=content,backendType="AthenaCharacter")
								await self.party.me.set_outfit(asset=cosmetic.id)
								await ctx.send(f'Skin set to {cosmetic.name}.')

						except FortniteAPIAsync.exceptions.NotFound:
								pass
						
		@commands.command()
		async def backpack(self, ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
				try:
						cosmetic = await self.fortnite_api.cosmetics.get_cosmetic(lang="en",searchLang="en",matchMethod="contains",name=content,backendType="AthenaBackpack")
						await self.party.me.set_backpack(asset=cosmetic.id)
						await ctx.send(f'Backpack set to {cosmetic.name}.')

				except FortniteAPIAsync.exceptions.NotFound:
						pass
				
		@commands.command(aliases=['dance'])
		async def emote(self, ctx: fortnitepy.ext.commands.Context, *, content = None) -> None:
				if content is None:
						await ctx.send()
				elif content.lower() == 'sce':
						await self.party.me.set_emote(asset='EID_KpopDance03')
				elif content.lower() == 'Sce':
						await self.party.me.set_emote(asset='EID_KpopDance03')    
				elif content.lower() == 'scenario':
						await self.party.me.set_emote(asset='EID_KpopDance03')
				elif content.lower() == 'Scenario':
						await self.party.me.set_emote(asset='EID_KpopDance03')     
				else:
						try:
								cosmetic = await self.fortnite_api.cosmetics.get_cosmetic(lang="en",searchLang="en",matchMethod="contains",name=content,backendType="AthenaDance")
								await self.party.me.clear_emote()
								await self.party.me.set_emote(asset=cosmetic.id)
								await ctx.send(f'Emote set to {cosmetic.name}.')

						except FortniteAPIAsync.exceptions.NotFound:
								pass    
							
		@commands.command()
		async def rdm(self, ctx: fortnitepy.ext.commands.Context, cosmetic_type: str = 'skin') -> None:
				if cosmetic_type == 'skin':
						all_outfits = await self.fortnite_api.cosmetics.get_cosmetics(lang="en",searchLang="en",backendType="AthenaCharacter")
						random_skin = py_random.choice(all_outfits).id
						await self.party.me.set_outfit(asset=random_skin,variants=self.party.me.create_variants(profile_banner='ProfileBanner'))
						await ctx.send(f'Skin randomly set to {random_skin}.')
				elif cosmetic_type == 'emote':
						all_emotes = await self.fortnite_api.cosmetics.get_cosmetics(lang="en",searchLang="en",backendType="AthenaDance")
						random_emote = py_random.choice(all_emotes).id
						await self.party.me.set_emote(asset=random_emote)
						await ctx.send(f'Emote randomly set to {random_emote.name}.')
						
		@commands.command()
		async def pickaxe(self, ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
				try:
						cosmetic = await self.fortnite_api.cosmetics.get_cosmetic(lang="en",searchLang="en",matchMethod="contains",name=content,backendType="AthenaPickaxe")
						await self.party.me.set_pickaxe(asset=cosmetic.id)
						await ctx.send(f'Pickaxe set to {cosmetic.name}.')

				except FortniteAPIAsync.exceptions.NotFound:
						pass

		@commands.command(aliases=['news'])
		@commands.cooldown(1, 10)
		async def new(self, ctx: fortnitepy.ext.commands.Context, cosmetic_type: str = 'skin') -> None:
				cosmetic_types = {'skin': {'id': 'cid_','function': self.party.me.set_outfit},'backpack': {'id': 'bid_','function': self.party.me.set_backpack},'emote': {'id': 'eid_','function': self.party.me.set_emote},}

				if cosmetic_type not in cosmetic_types:
						return await ctx.send('Invalid cosmetic type, valid types include: skin, backpack & emote.')

				new_cosmetics = await self.fortnite_api.cosmetics.get_new_cosmetics()

				for new_cosmetic in [new_id for new_id in new_cosmetics if
														 new_id.id.lower().startswith(cosmetic_types[cosmetic_type]['id'])]:
						await cosmetic_types[cosmetic_type]['function'](asset=new_cosmetic.id)

						await ctx.send(f"{cosmetic_type}s set to {new_cosmetic.name}.")

						await asyncio.sleep(3)

				await ctx.send(f'Finished equipping all new unencrypted {cosmetic_type}s.')           

		@commands.command()
		async def purpleskull(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_outfit(asset='CID_030_Athena_Commando_M_Halloween',variants=self.party.me.create_variants(clothing_color=1))
				await ctx.send(f'Skin set to Purple Skull Trooper!')
				
		@commands.command()
		async def pinkghoul(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_outfit(asset='CID_029_Athena_Commando_F_Halloween',variants=self.party.me.create_variants(material=3))
				await ctx.send('Skin set to Pink Ghoul Trooper!')
				
		@commands.command(aliases=['checkeredrenegade','raider'])
		async def renegade(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_outfit(asset='CID_028_Athena_Commando_F',variants=self.party.me.create_variants(material=2))
				await ctx.send('Skin set to Checkered Renegade!')
				
		@commands.command()
		async def aerial(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_outfit(asset='CID_017_Athena_Commando_M')
				await ctx.send('Skin set to aerial!')
				
		@commands.command()
		async def hologram(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_outfit(asset='CID_VIP_Athena_Commando_M_GalileoGondola_SG')
				await ctx.send('Skin set to Star Wars Hologram!')  

		@commands.command()
		async def cid(self, ctx: fortnitepy.ext.commands.Context, character_id: str) -> None:
				await self.party.me.set_outfit(asset=character_id,variants=self.party.me.create_variants(profile_banner='ProfileBanner'))
				await ctx.send(f'Skin set to {character_id}.')
				
		@commands.command()
		async def eid(self, ctx: fortnitepy.ext.commands.Context, emote_id: str) -> None:
				await self.party.me.clear_emote()
				await self.party.me.set_emote(asset=emote_id)
				await ctx.send(f'Emote set to {emote_id}!')
				
		@commands.command()
		async def bid(self, ctx: fortnitepy.ext.commands.Context, backpack_id: str) -> None:
				await self.party.me.set_backpack(asset=backpack_id)
				await ctx.send(f'Backbling set to {backpack_id}!')
				
		@commands.command()
		async def stop(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.clear_emote()
				await ctx.send('Stopped emoting.')
				
		@commands.command()
		async def point(self, ctx: fortnitepy.ext.commands.Context, *, content: Optional[str] = None) -> None:
				await self.party.me.clear_emote()
				await self.party.me.set_emote(asset='EID_IceKing')
				await ctx.send(f'Pickaxe set & Point it Out played.')
				

		copied_player = ""


		@commands.command()
		async def stop(self, ctx: fortnitepy.ext.commands.Context):
				global copied_player
				if copied_player != "":
						copied_player = ""
						await ctx.send(f'Stopped copying all users.')
						await self.party.me.clear_emote()
						return
				else:
						try:
								await self.party.me.clear_emote()
						except RuntimeWarning:
								pass

		@commands.command(aliases=['clone', 'copi', 'cp'])
		async def copy(self, ctx: fortnitepy.ext.commands.Context, *, epic_username = None) -> None:
				global copied_player

				if epic_username is None:
						user = await self.fetch_user(ctx.author.display_name)
						member = self.party.get_member(user.id)

				elif 'stop' in epic_username:
						copied_player = ""
						await ctx.send(f'Stopped copying all users.')
						await self.party.me.clear_emote()
						return

				elif epic_username is not None:
						try:
								user = await self.fetch_user(epic_username)
								member = self.party.get_member(user.id)
						except AttributeError:
								await ctx.send("Could not get that user.")
								return
				try:
						copied_player = member
						await self.party.me.edit_and_keep(partial(fortnitepy.ClientPartyMember.set_outfit,asset=member.outfit,variants=member.outfit_variants),partial(fortnitepy.ClientPartyMember.set_pickaxe,asset=member.pickaxe,variants=member.pickaxe_variants))
						await ctx.send(f"Now copying: {member.display_name}")
				except AttributeError:
						await ctx.send("Could not get that user.")

		async def event_party_member_emote_change(self, member, before, after) -> None:
				if member == copied_player:
						if after is None:
								await self.party.me.clear_emote()
						else:
								await self.party.me.edit_and_keep(partial(fortnitepy.ClientPartyMember.set_emote,asset=after))                        
								
		async def event_party_member_outfit_change(self, member, before, after) -> None:
				if member == copied_player:
						await self.party.me.edit_and_keep(partial(fortnitepy.ClientPartyMember.set_outfit,asset=member.outfit,variants=member.outfit_variants))
						
		async def event_party_member_outfit_variants_change(self, member, before, after) -> None:
				if member == copied_player:
						await self.party.me.edit_and_keep(partial(fortnitepy.ClientPartyMember.set_outfit,variants=member.outfit_variants))
						
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////    PARTY/FRIENDS/ADMIN //////////////////////////////////////////////////////////////////////////////////////////////////////

		@commands.command()
		async def add(self, ctx: fortnitepy.ext.commands.Context, *, epic_username: str) -> None:
				user = await self.fetch_user(epic_username)
				friends = self.friends

				if user.id in friends:
						await ctx.send(f'I already have {user.display_name} as a friend')
				else:
						await self.add_friend(user.id)
						await ctx.send(f'Send i friend request to {user.display_name}.')

		@is_admin()
		@commands.command(aliases=['unhide'],)
		async def promote(self, ctx: fortnitepy.ext.commands.Context, *, epic_username: Optional[str] = None) -> None:
				if epic_username is None:
						user = await self.fetch_user(ctx.author.display_name)
						member = self.party.get_member(user.id)
				else:
						user = await self.fetch_user(epic_username)
						member = self.party.get_member(user.id)

				if member is None:
						await ctx.send("Failed to find that user, are you sure they're in the party?")
				else:
						try:
								await member.promote()
								os.system('cls')
								await ctx.send(f"Promoted user: {member.display_name}.")
						except fortnitepy.errors.Forbidden:
								await ctx.send(f"Failed to promote {member.display_name}, as I'm not party leader.")

		@is_admin()
		@commands.command()
		async def restart(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await ctx.send(f'im Restart now')
				python = sys.executable
				os.execl(python, python, *sys.argv)        

		@is_admin()
		@commands.command()
		async def set(self, ctx: fortnitepy.ext.commands.Context, nombre: int) -> None:
				await self.party.set_max_size(nombre)
				await ctx.send(f'Set party to {nombre} player can join')
				
		@commands.command()
		async def ready(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_ready(fortnitepy.ReadyState.READY)
				await ctx.send('Ready!')
		
		@commands.command(aliases=['sitin'],)
		async def unready(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
				await ctx.send('Unready!')
				
		@commands.command()
		async def level(self, ctx: fortnitepy.ext.commands.Context, banner_level: int) -> None:
				await self.party.me.set_banner(season_level=banner_level)
				await ctx.send(f'Set level to {banner_level}.')
				
		@is_admin()
		@commands.command()
		async def sitout(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
				await ctx.send('Sitting Out!')
						
		@is_admin()
		@commands.command()
		async def leave(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await self.party.me.leave()
				await ctx.send(f'i Leave')
				await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

		@is_admin()
		@commands.command()
		async def v(self, ctx: fortnitepy.ext.commands.Context) -> None:
				await ctx.send(f'the version {__version__}')

		@is_admin()
		@commands.command()
		async def kick(self, ctx: fortnitepy.ext.commands.Context, *, epic_username: Optional[str] = None) -> None:
				if epic_username is None:
						user = await self.fetch_user(ctx.author.display_name)
						member = self.party.get_member(user.id)
				else:
						user = await self.fetch_user(epic_username)
						member = self.party.get_member(user.id)

				if member is None:
						await ctx.send("Failed to find that user, are you sure they're in the party?")
				else:
						try:
								if not member.display_name in info['FullAccess']:
										await member.kick()
										await ctx.send(f"Kicked user: {member.display_name}.")
						except fortnitepy.errors.Forbidden:
								await ctx.send(f"Failed to kick {member.display_name}, as I'm not party leader.")

		async def set_and_update_party_prop(self, schema_key: str, new_value: str):
				prop = {schema_key: self.party.me.meta.set_prop(schema_key, new_value)}

				await self.party.patch(updated=prop)

		@commands.party_only()
		@commands.command(name='- HEY',aliases=['-HEY','Use','Item','Notice:','This','Heyy','If'], hidden=True)
		async def kickortherbots(self, ctx: fortnitepy.ext.commands.Context, *, username = None):
				if self.party.me.leader:
						user = await self.fetch_profile(ctx.author.id)
						member = self.party.get_member(user.id)

				if not member.display_name in info['FullAccess']:
						await member.kick()
						await ctx.send("The orther Bot is Not accepted of the party")
				else:
						await ctx.send()

		@is_admin()
		@commands.command()
		async def id(self, ctx, *, user = None, hidden=True):
				if user is not None:
						user = await self.fetch_profile(user)
				
				elif user is None:
						user = await self.fetch_profile(ctx.message.author.id)
				try:
						await ctx.send(f"{user}'s Epic ID is: {user.id}")
						print(Fore.GREEN + ' [+] ' + Fore.RESET + f"{user}'s Epic ID is: " + Fore.LIGHTBLACK_EX + f'{user.id}')
				except AttributeError:
						await ctx.send("I couldn't find an Epic account with that name.")

		@is_admin()
		@commands.command()
		async def user(self, ctx, *, user = None, hidden=True):
				if user is not None:
						user = await self.fetch_profile(user)
						try:
								await ctx.send(f"The ID: {user.id} belongs to: {user.display_name}")
								print(Fore.GREEN + ' [+] ' + Fore.RESET + f'The ID: {user.id} belongs to: ' + Fore.LIGHTBLACK_EX + f'{user.display_name}')
						except AttributeError:
								await ctx.send(f"I couldn't find a user that matches that ID")
				else:
						await ctx.send(f'No ID was given. Try: {prefix}user (ID)')

		async def invitefriends(self):
			while True:
				mins = 15
				send = []
				for friend in self.friends:
						if friend.is_online():
								send.append(friend.display_name)
								await friend.invite()
				await asyncio.sleep(mins*60)

		@is_admin()
		@commands.command()
		async def invite(self, ctx: fortnitepy.ext.commands.Context) -> None:
				try:
						self.loop.create_task(self.invitefriends())
				except Exception:
						pass       

		@commands.command(aliases=['friends'],)
		async def epicfriends2(self, ctx: fortnitepy.ext.commands.Context) -> None:
				onlineFriends = []
				offlineFriends = []

				try:
						for friend in self.friends:
								if friend.is_online():
										onlineFriends.append(friend.display_name)
								else:
										offlineFriends.append(friend.display_name)
						
						await ctx.send(f"Total Friends: {len(self.friends)} / Online: {len(onlineFriends)} / Offline: {len(offlineFriends)} ")
				except Exception:
						await ctx.send(f'Not work')

		@is_admin()
		@commands.command()
		async def whisper(self, ctx: fortnitepy.ext.commands.Context, message = None) -> None:
				try:
						for friend in self.friends:
								if friend.is_online():
										await friend.send(message)

						await ctx.send(f'Send friend message to everyone')
						
				except: pass

		@commands.command()
		async def say(self, ctx: fortnitepy.ext.commands.Context, *, message = None):
				if message is not None:
						await self.party.send(message)
						await ctx.send(f'Sent "{message}" to party chat')
				else:
						await ctx.send(f'No message was given. Try: {prefix} say (message)')

		@commands.command()
		async def cousin(self, ctx: fortnitepy.ext.commands.Context):
				await ctx.send('create by cousin')

		@is_admin()
		@commands.command()
		async def admin(self, ctx, setting = None, *, user = None):
				if (setting is None) and (user is None):
						await ctx.send(f"Missing one or more arguments. Try: {prefix} admin (add, remove, list) (user)")
				elif (setting is not None) and (user is None):

						user = await self.fetch_profile(ctx.message.author.id)

						if setting.lower() == 'add':
								if user.display_name in info['FullAccess']:
										await ctx.send("You are already an admin")

								else:
										await ctx.send("Password?")
										response = await self.wait_for('friend_message', timeout=20)
										content = response.content.lower()
										if content == password:
												info['FullAccess'].append(user.display_name)
												with open('info.json', 'w') as f:
														json.dump(info, f, indent=4)
														await ctx.send(f"Correct. Added {user.display_name} as an admin.")
														print(Fore.GREEN + " [+] " + Fore.LIGHTGREEN_EX + user.display_name + Fore.RESET + " was added as an admin.")
										else:
												await ctx.send("Incorrect Password.")

						elif setting.lower() == 'remove':
								if user.display_name not in info['FullAccess']:
										await ctx.send("You are not an admin.")
								else:
										await ctx.send("Are you sure you want to remove yourself as an admin?")
										response = await self.wait_for('friend_message', timeout=20)
										content = response.content.lower()
										if (content.lower() == 'yes') or (content.lower() == 'y'):
												info['FullAccess'].remove(user.display_name)
												with open('info.json', 'w') as f:
														json.dump(info, f, indent=4)
														await ctx.send("You were removed as an admin.")
														print(Fore.BLUE + " [+] " + Fore.LIGHTBLUE_EX + user.display_name + Fore.RESET + " was removed as an admin.")
										elif (content.lower() == 'no') or (content.lower() == 'n'):
												await ctx.send("You were kept as admin.")
										else:
												await ctx.send("Not a correct reponse. Cancelling command.")
										
						elif setting == 'list':
								if user.display_name in info['FullAccess']:
										admins = []

										for admin in info['FullAccess']:
												user = await self.fetch_profile(admin)
												admins.append(user.display_name)

										await ctx.send(f"The bot has {len(admins)} admins:")

										for admin in admins:
												await ctx.send(admin)

								else:
										await ctx.send("You don't have permission to this command.")

						else:
								await ctx.send(f"That is not a valid setting. Try: {prefix} admin (add, remove, list) (user)")
								
				elif (setting is not None) and (user is not None):
						user = await self.fetch_profile(user)

						if setting.lower() == 'add':
								if ctx.message.author.display_name in info['FullAccess']:
										if user.display_name not in info['FullAccess']:
												info['FullAccess'].append(user.display_name)
												with open('info.json', 'w') as f:
														json.dump(info, f, indent=4)
														await ctx.send(f"Correct. Added {user.display_name} as an admin.")
														print(Fore.GREEN + " [+] " + Fore.LIGHTGREEN_EX + user.display_name + Fore.RESET + " was added as an admin.")
										else:
												await ctx.send("That user is already an admin.")
								else:
										await ctx.send("You don't have access to add other people as admins. Try just: !admin add")
						elif setting.lower() == 'remove':
								if ctx.message.author.display_name in info['FullAccess']:
										if user.display_name in info['FullAccess']:
												await ctx.send("Password?")
												response = await self.wait_for('friend_message', timeout=20)
												content = response.content.lower()
												if content == password:
														info['FullAccess'].remove(user.display_name)
														with open('info.json', 'w') as f:
																json.dump(info, f, indent=4)
																await ctx.send(f"{user.display_name} was removed as an admin.")
																print(Fore.BLUE + " [+] " + Fore.LIGHTBLUE_EX + user.display_name + Fore.RESET + " was removed as an admin.")
												else:
														await ctx.send("Incorrect Password.")
										else:
												await ctx.send("That person is not an admin.")
								else:
										await ctx.send("You don't have permission to remove players as an admin.")
						else:
								await ctx.send(f"Not a valid setting. Try: {prefix} -admin (add, remove) (user)")

		async def verify(self):
				try:
						global code

						if len(self.friends) >= 0 and len(self.friends) < 100:
								await self.set_presence('🔴 {party_size}/16 | ' + f'{code} ')
								await asyncio.sleep(5)
								await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

						elif len(self.friends) >= 100 and len(self.friends) < 300:
								await self.set_presence('💖 {party_size}/16 | ' + f'{code} ')
								await asyncio.sleep(5)
								await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

						elif len(self.friends) >= 300 and len(self.friends) < 900:
								await self.set_presence('🔥 {party_size}/16 | ' + f'{code} ')
								await asyncio.sleep(5)
								await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

						elif len(self.friends) >= 900:
								await self.set_presence('💚 {party_size}/16 | ' + f'{code} ')
								await asyncio.sleep(5)
								await self.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)

				except: 
					pass

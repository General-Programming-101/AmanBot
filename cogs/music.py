import discord
from discord.ext import commands
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
        self.FFMPEG_OPTIONS = {
            'options': '-vn',
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
        }
        self.vc = None
        self.ytdl = YoutubeDL(self.YDL_OPTIONS)

    def search_yt(self, item):
        print(f"Searching for: {item}")
        if item.startswith("https://"):
            title = self.ytdl.extract_info(item, download=False)["title"]
            print(f"Found URL: {title}")
            return {'source': item, 'title': title}
        search = VideosSearch(item, limit=1)
        result = search.result()["result"][0]
        print(f"Found result: {result['title']}")
        return {'source': result["link"], 'title': result["title"]}

    async def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            print(f"Playing next: {m_url}")

            self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            try:
                data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
                song = data['url']
                self.vc.play(discord.FFmpegPCMAudio(song, executable="ffmpeg.exe", **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop))
                print("Playing next song")
            except Exception as e:
                print(f"Error playing next song: {e}")
                self.is_playing = False
                await self.play_music(None)  # Attempt to play the next song if available
        else:
            self.is_playing = False
            print("No more songs in the queue.")

    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            print(f"Starting to play: {m_url}")

            if self.vc is None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
                print(f"Connected to voice channel: {self.music_queue[0][1]}")

                if self.vc is None:
                    embed = discord.Embed(
                        title="**Could not Connect to Voice Channel⚠️⚠️⚠️**",
                        description="An error occurred when connecting to the voice channel",
                        color=discord.Color.red())
                    await ctx.send(embed=embed)
                    print("Failed to connect to voice channel.")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
                print(f"Moved to voice channel: {self.music_queue[0][1]}")

            self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            try:
                data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
                song = data['url']
                self.vc.play(discord.FFmpegPCMAudio(song, executable="ffmpeg.exe", **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop))
                print("Playing song")
            except Exception as e:
                print(f"Error playing song: {e}")
                self.is_playing = False
                await ctx.send("```Error playing the song.```")
        else:
            self.is_playing = False
            print("Music queue is empty.")

    @commands.command(name="play", aliases=["p", "playing"])
    async def play(self, ctx, *args):
        query = " ".join(args) + " lyrics version" # lyrics version will eliminate any music video elements and focus solely on the song 
        try:
            voice_channel = ctx.author.voice.channel
            print(f"User {ctx.author} is in voice channel: {voice_channel}")
        except AttributeError:
            embed = discord.Embed(
                title=f"⚠️⚠️⚠️\nUser is not Connect to a Voice Channel",
                description=f"{ctx.author.mention} please connect to a voice channel to run this command",
                color=discord.Color.yellow(),
            )
            await ctx.send(embed=embed)
            print(f"User {ctx.author} is not connected to a voice channel.")
            return
        if self.is_paused:
            self.vc.resume()
            print("Resumed the music.")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                embed = discord.Embed(
                    title="**Error⚠️**",
                    description="Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format",
                    color=discord.Color.yellow()
                )
                await ctx.send(embed=embed)
                print("Failed to download the song.")
            else:
                if self.is_playing:
                    await ctx.send(f"**#{len(self.music_queue)+2} - '{song['title']}'** added to the queue")
                else:
                    await ctx.send(f"**'{song['title']}'** added to the queue")
                self.music_queue.append([song, voice_channel])
                print(f"Added to queue: {song['title']}")
                if not self.is_playing:
                    await self.play_music(ctx)

    @commands.command(name="pause")
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
            print("Paused the music.")
        elif self.is_paused:
            self.is_playing = True
            self.is_paused = False
            self.vc.resume()
            print("Resumed the music.")

    @commands.command(name="resume", aliases=["r"])
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            print("Resumed the music.")

    @commands.command(name="skip", aliases=["s", "next"])
    async def skip(self, ctx, *args):
        if self.vc is not None and self.vc:
            self.vc.stop()
            await self.play_music(ctx)
            print("Skipped the song.")

    @commands.command(name="queue", aliases=["q", "add"])
    async def queue(self, ctx, *args):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f"#{i+1} - " + self.music_queue[i][0]['title'] + "\n"

        if retval != "":
            await ctx.send(f"```queue:\n{retval}```")
        else:
            await ctx.send("```No music in queue```")
        print("Displayed the queue.")

    @commands.command(name="clear", aliases=["c", "bin"])
    async def clear(self, ctx):
        if self.vc is not None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.send("```Music queue cleared```")
        print("Cleared the music queue.")

    @commands.command(name="remove")
    async def resume(self, ctx):
        if len(self.music_queue) > 0:
            self.music_queue.pop()
            await ctx.send("```Last song removed```")
            print("Removed the last song from the queue.")
        else:
            await ctx.send("```The Music Queue is already empty```")
            print("Music queue is already empty.")
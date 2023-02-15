from loader import dp
from pytube import YouTube
import os

@dp.message_handler(text='/start')
async def start_bot(message):
    await message.answer('Hello! I am a bot for downloading videos from a platform like "YouTube Music" here is my command list:\n/search -- Searching')

@dp.message_handler(text='/search')
async def get_song(message):
	await message.answer('Submit video/song link')
	
@dp.message_handler()
async def shearch_the_song(message):
	url = YouTube(message.text)
	audio_stream = url.streams.filter(only_audio=True).first()
	out_file = audio_stream.download("music/")
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)
	await dp.bot.send_audio(message.from_user.id, open(new_file, "rb"), performer = url.streams[0].title, title = url.streams[0].title)
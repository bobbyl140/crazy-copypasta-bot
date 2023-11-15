# crazy-copypasta-bot

This bot was written with [pycord](https://pycord.dev). To install it run `python3 -m pip install py-cord`. To run the bot, paste your token into the run() line at the end and `python3 ./bot.py`. I realize security could be improved with environment variables but this wasn't meant to be hardened as that's not really needed. 

Its only goal in life is to respond to any message containing any casing of "crazy" with the infamous copypasta:
> Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.

Note, it won't respond to its own messages, for obvious reasons. You can feel free to try removing the limitation, but when I tried it, it only made it about 3 times over before it broke. YMMV. And if you have to delete the channel as a result that's on you.

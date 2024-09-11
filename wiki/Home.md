# Snap! (Build Your Own Blocks) Docs
center reference point for the Snap! (Build Your Own Blocks) framework

<img height=22 src="https://github.com/shysolocup/snapbyob/actions/workflows/publish-wiki.yml/badge.svg" alt="if this shows up something's wrong with the workflow">

<br>

```py
from snapbyob import Project, Enum
import asyncio;


proj = Project({
    "name": "Example"
});


@proj.on("block.placed")
async def test(self, ctx):
    print(ctx.name, ctx.category);


@proj.on("ping")
async def test(self, time):
    a = await proj.scripts.insert('control.whenKeyPressed', Enum.keycode.a);
    await a.scripts.insert('motion.move', x=10, y=10);


async def test():
    await proj.ping();

asyncio.run(test());
```
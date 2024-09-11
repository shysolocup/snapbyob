```py

from snapbyob import Project, Enum;
import asyncio;


print(Enum.keycode.a);


proj = Project({
    "name": "very cool"
});


@proj.on("block.placed")
async def test(self, ctx):
    ctx.callback(ctx, *ctx.args, **ctx.kwargs);


@proj.on("ping")
async def test(self, time):
    block = await proj.scripts.insert('motion.move', x=10, y=10);
    await block.insert('motion.changeXBy', 5);


async def test():
    await proj.ping();


```
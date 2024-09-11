# Snap! (Build Your Own Blocks) Python
A framework for the efficient and streamlined creation of Snap! (Build Your Own Blocks) projects in Python <br> 
made to teach students how to use non-block coding with something familiar
<br>

- Full [documentation](https://github.com/shysolocup/snapbyob/wiki)
- Open source

<br>

```console
pip install snapbyob
```

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
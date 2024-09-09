```py

from snapbyob import Project, Block, BlockInstance
import asyncio

proj  = Project();

@proj.on
def blockPlaced(self, block):
	print(block);

async def test():
	block = await proj.scripts.insert(“motion.move”, x=10, y=10)
	await block.insert(“motion.move”, x=10, y=10, p=block)

asyncio.run(test());


```
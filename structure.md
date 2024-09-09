```py

from snapbyob import Project, Block, BlockInstance

proj  = Project();

@proj.on
def blockPlaced(self, block):
	print(block);

block = proj.scripts.insert(“motion.move”, x=10, y=10)
proj.scripts.insert(“motion.move”, x=10, y=10, p=block)



```
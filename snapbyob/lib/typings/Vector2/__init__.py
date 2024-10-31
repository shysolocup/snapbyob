import asyncio;


class Vector2:
    def __init__(self, x: int | float = None, y:int | float = None):
        self.x = x;
        self.y = y;

    def __str__(self):
        return "{ " + str(self.x) + ", " + str(self.y) + " }";
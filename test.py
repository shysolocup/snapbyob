from snapbyob import Project, TimeConv;
import asyncio;


proj = Project({
    "name": "very cool"
});

@proj.on("block.placed")
async def test(self, ctx):
    ctx.callback(self, *ctx.args, **ctx.kwargs);


@proj.on("ping")
async def test(self, time, scene):
    enum = scene.enum;
    sprite = scene.get('sprites.sprite');

    await sprite.place('looks.effect', enum.effect.saturation);
    await sprite.place('looks.changeEffectBy', enum.effect.saturation, 10);


async def test():
    scene = await proj.new('Scene');
    await proj.ping(scene); 

asyncio.run(test());


'''
with open("Python Interpreter 5.0.xml") as file:
    stuff = xml.parse(file.read())
    print(stuff);

    with open("test.json", "w") as jsn:
        dumped = json.dumps(stuff, sort_keys=True, indent=4);
        jsn.write(dumped);
'''


'''import requests

token = "0bbdb4d78d92f90df71f2d70211c326d848cf57dfd1548c9b3f7b61e268425534ca8518603863de9fc380de04df3d494f206ee597eadc8af00ab501f6e6ef7ab"

rq = requests.post('https://snap.berkeley.edu/api/v1/users/asdfs', json={
    "header": {
        ':authority:': "snap.berkeley.edu",
        ':method:': "GET",
        'cookie': "persist_session=false; snapsession=eyJhY2Nlc3NfaWQiOiIxNzI0Nzk5Mzg1Ljk4ODQtMC4xNzU1Mzg3MDE2ODQ1MyIsImZpcnN0X2FjY2VzcyI6MTcyNDc5OTI5NSwiYWxsb3dlZF90aW1lX2RpZmZlcmVuY2UiOjIsImN1cnJlbnRfYWNjZXNzX3RpbWUiOjE3MjQ3OTkzODUsInByZXZpb3VzX2FjY2Vzc190aW1lIjoxNzI0Nzk5MzY2LCJ1c2VybmFtZSI6ImFzZGZzIiwidmVyaWZpZWQiOnRydWV9%0a%2d%2daY7E0HgtYZmU1AeoIH1%2fpXEKru4%3d",
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera GX";v="112"',
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br, zstd",
        'content-type': "application/json; charset=utf-8",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-site': 'same-origin',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
    },
    "body": "0bbdb4d78d92f90df71f2d70211c326d848cf57dfd1548c9b3f7b61e268425534ca8518603863de9fc380de04df3d494f206ee597eadc8af00ab501f6e6ef7ab"
});

print(rq.text);'''
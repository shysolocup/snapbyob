from snapbyob import Project, TimeConv, DataObject;
import asyncio;


proj = Project({
    "name": "CoolProject"
});


scenes = proj.xmldata.getDeep("project.scenes");
print(scenes);


'''
@proj.on("block.placed")
async def test(self, ctx):
    ctx.callback(ctx, *ctx.args, **ctx.kwargs);


@proj.on("ping")
async def test(self, time, scene, stage):
    enum = scene.enum;
    sprite = stage.get('sprites.sprite');

    # await sprite.place('looks.effect', enum.effect.saturation);
    # await sprite.place('looks.changeEffectBy', enum.effect.saturation, 10);

    await sprite.placeGroup([
        { 'name': 'control.ifX', 
            
            'args': [
                { 'name': 'sensing.keyPressed', 'args': enum.keycode.space }
            ], 

            'actions': [
                { 'name': 'looks.say', 'args': "test1" }
            ]
        
        }
    ])


async def test():
    scene = await proj.new('Scene', {
        'name': "a"
    });

    stage = await scene.new('Stage', {
        'name': "Stage",
        'width': 500,
        'height': 500
    })

    await proj.ping(scene, stage);

    await proj.compileToFile('testfile');

asyncio.run(test());


'''
runtime_greenflags = []
runtime_sprites = []

def create_sprite(cls):
    assert issubclass(cls, runtime_Sprite), "{} is not a Sprite".format(cls)
    sprite = cls()
    runtime_sprites.append(sprite)
    runtime_greenflags.extend(sprite._greenflags)

class runtime_Sprite:
    def __init__(self):
        scripts = [(script, getattr(self, script)) for script in dir(self) if callable(getattr(self, script))]
        self._greenflags = [script for name, script in scripts if name.startswith("greenflag")]
        self._answer = ""

    @asyncio.coroutine
    def sayfor(self, thing, time):
        "Says thing for time seconds"
        print("{} says '{}'".format(self.__class__.__name__, thing))
        yield from asyncio.sleep(time)

    @asyncio.coroutine
    def wait(self, time):
        "Waits for times seconds"
        yield from asyncio.sleep(time)

    @asyncio.coroutine
    def ask(self, question):
        "Asks question"
        print("{} asks '{}'".format(self.__class__.__name__, question))
        self._answer = input()

    def answer(self):
        "Returns the answer"
        return self._answer

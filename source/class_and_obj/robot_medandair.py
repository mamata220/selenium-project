class Robot:
    def __init__(self, name, make, model, type, lang, color, version):
        self.name = name
        self.make = make
        self.model = model
        self.type = type
        self.lang = lang
        self.color = color
        self.version = version

    def greet_user(self):
        print(f"Hello I am a robot. My name is {self.name}, \nwhat can I do for you?")

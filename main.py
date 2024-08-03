class Puppy():
    def __init__(self, name, fav_toy):
        self.name = name
        self.fav_toy = fav_toy

    def play(self):
        print(self.name + " is playing with the " + self.fav_toy)


marble = Puppy('Marble', 'teddy bear')
marble.play()

onyx = Puppy('Onyx', 'lizard')
onyx.play()
import pyxel as p


class App:

    def __init__(self):
        p.init(160, 160)
        self.x = 0
        self.beauty = True
        p.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % p.width
        if p.btnp(p.KEY_Q):
            p.quit()

    def draw(self):
        p.cls(0)
        p.rect(self.x, 20, 20, 20, 5)


game = App()
print(game.beauty, game.x)


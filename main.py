import pygame

pygame.init()


class Color():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)

class Account():
    def __init__(self, name, type, background_color, font_color, x, y, width, height):
        self.name = name
        self.type = type

        self.background_color = background_color
        self.font_color = font_color
        self.font = pygame.font.SysFont("Courier", 16)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, self.background_color, (self.x, self.y, self.width, self.height))
        surface.blit(self.font.render(self.name, True, self.font_color), (self.x + 10, self.y + 10))

    def update(self):
        pass

class Prog():
    def __init__(self):
        self.screen = pygame.display.set_mode([1000, 800], pygame.RESIZABLE)
        pygame.display.set_caption("PyMoney - Budgeting Program")

        self.color = Color()

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.delta_time = 0
        self.framerate = 120

        self.accounts = []

        self.america_first_debit = Account("AFCU Debit", "debit", self.color.BLUE, self.color.WHITE, 0, 0, 400, 100)

        self.accounts.append(self.america_first_debit)

    def run(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def close(self):
        #TODO: save everything
        self.running = False

    def event_loop(self):
        self.events = pygame.event.get()
        
        for event in self.events:
            if event.type == pygame.QUIT:
                self.close()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.close()

    def draw(self):
        self.screen.fill(self.color.BLACK)

        for account in self.accounts:
            account.draw(self.screen)

    def update(self):
        for account in self.accounts:
            account.update()

        pygame.display.update()
        self.delta_time = self.clock.tick(self.framerate) / 1000

if __name__ == '__main__':
    p = Prog()
    p.run()
    pygame.quit()
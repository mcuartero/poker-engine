from core.game import Game
from states.menu import Menu

if __name__ == "__main__":
    game = Game()
    menu = Menu()
    game.run()
    menu.draw(game.screen)
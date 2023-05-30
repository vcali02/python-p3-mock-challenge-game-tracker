from player import Player
from game import Game


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        player.results(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and score >=1 and score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be between 1 and 5000 characters")


    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be of type Player")
    

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be of type Game")

    



cards = Game("cards")
val = Player("Val")

result1 = Result(val, cards, 500)
#print(result1.score)
#tested @player.setter with:
#result1 = Result(cards, val, 500)

#tested @game.setter with:
#result1 = Result(val, 500, cards)

#print(val.results)
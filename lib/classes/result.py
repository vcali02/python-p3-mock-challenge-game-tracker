#populating up here will cause circular import
# from player import Player
# from game import Game


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        #grabs results.all and adds self as a list item
        Result.all.append(self)


        #pass self bc IN RESULTS class
        player.results(self)
        game.results(self)

        #pass game because NOT IN GAME class so need to specify
        player.games_played(game)
        game.players(player)

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
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be of type Player")
    

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be of type Game")

    




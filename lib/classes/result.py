class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)
        

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1<= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be a positive integer")
    

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be an instance of Player")

   

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be an instance of Game")
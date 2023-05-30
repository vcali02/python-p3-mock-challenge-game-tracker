class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
    def results(self, new_result=None):
        from classes.result import Result
        #if new_result exists
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results


    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    #ADVANCED DELIVERABLE AGGREGATE AND ASSOCIATION METHODS
    def played_game(self, game):
        if each.player == self and each.game == game:
            return True
            return False
        
        #return game in self._games_played
    #ADVANCED DELIVERABLE AGGREGATE AND ASSOCIATION METHODS
    def num_times_played(self, game):
        return [each_r for each_r in self._results if each_r.game == game]
    

    #ADVANCED DELIVERABLE AGGREGATE AND ASSOCIATION METHODS
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_p = None
            max_score = 0

            for pl in cls.all:
                if game.average_score(pl) > max_score:
                    max_p = pl
                    max_score = game.average_score(pl)
            return max_p
        return None
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Invalid player username")
    
val = Player("Val")
#changeable
# val.username = "winnie"
print(val)



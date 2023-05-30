class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be a string between 2 and 16 characters")



        
    def results(self, new_result=None):
        from classes.result import Result
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
       pass
        
        #return game in self._games_played
    #ADVANCED DELIVERABLE AGGREGATE AND ASSOCIATION METHODS
    def num_times_played(self, game):
        pass
    

    #ADVANCED DELIVERABLE AGGREGATE AND ASSOCIATION METHODS
    @classmethod
    def highest_scored(cls, game):
      pass
  



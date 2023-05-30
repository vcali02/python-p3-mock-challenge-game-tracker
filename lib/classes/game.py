class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []


    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        pass
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        #if instance of title is string, and does not have attribute self.title and length > 0, return etc.
        if isinstance(title, str) and not hasattr(self, 'title') and len(title) > 0:
            #set the self title to the param title
            self._title = title
        else:
            raise Exception("Title must be a string greater than 0 characters.")
    

cards = Game("cards")
#print(cards.title)
#cards.title = "go fish"
#print(cards.title)

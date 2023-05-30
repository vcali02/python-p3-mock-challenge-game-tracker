class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []


    def results(self, new_result=None):
        from classes.result import Result



        # if not new_result:
        #     len(game.results()) == 2
        # else:
        #     game._results.append(new_result)
        #     return [result for result in self._results]
    
    def players(self, new_player=None):
        from classes.player import Player
        pass
    
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

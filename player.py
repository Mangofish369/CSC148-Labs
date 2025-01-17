class Player:
    """
    A class that holds the scores of the player
    """
    name: str
    history: [int]

    def __init__(self, name: str, history: [int]):
        self.name = name
        self.history = history

    def add_scores(self,scores: [int]):
        """
        Adds scores to the end of history list, if the number of scores exceed 100, remove the first n elements required
        """
        self.history.extend(scores)
        if len(self.history) > 100:
            excess = len(self.history) - 100
            self.history = self.history[excess:]

    def get_average(self):
        """
        Return the average of the 3 most recent scores
        """
        return sum(self.history[-3:-1])/3

    def get_top_score(self):
        return max(self.history)

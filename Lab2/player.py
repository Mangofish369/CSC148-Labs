class Player:
    """
    A class that holds the scores of the player

    >>> player1 = Player('001')
    >>> player1.add_scores([10,20,24,25,26])
    >>> player1.get_average(3)
    25
    >>> player1.get_top_score()
    26
    """
    name: str
    history: [int]

    def __init__(self, name: str):
        self.name = name
        self.history = []

    def add_scores(self,scores: [int]):
        """
        Adds scores to the end of history list, if the number of scores exceed 100, remove the first n elements required
        """
        self.history.extend(scores)
        if len(self.history) > 100:
            excess = len(self.history) - 100
            self.history = self.history[excess:]

    def get_average(self, n: int):
        """
        Return the average of the n most recent scores

        Precondition: n must not be larger than the number of scores
        """
        return sum(self.history[-n:])/n

    def get_top_score(self) -> int:
        return max(self.history)

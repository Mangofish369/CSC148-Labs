import random

class Card:
    """
    The individual cards in the deck

    Attributes:
    - value:
        The numeric value of the card
    - suit:
        The suit of the card
    """
    value: int
    suit: str

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "Suit:"+ self.suit + " Value:" + str(self.value)


class Deck:
    """
    Attributes:
    - top:
        A dictionary with the top card on it
    """
    _cards: list

    def __init__(self) -> None:
        """
        Initialize a new empty deck
        """
        self._cards = []

    def add_card(self, v: int, s: str) -> None:
        """
        Add a card to the deck, and update the top of the deck

        >>> deck = Deck()
        >>> deck.add_card(1, "Spades")
        >>> deck.print_cards()
        1 Spades
        """
        self._cards.append(Card(v, s))

    def draw_card(self) -> dict | None:
        """
        Return the top card

        >>> deck = Deck()
        >>> deck.add_card(1, "Spades")
        >>> deck.add_card(2, "Clubs")
        >>> deck.draw_card()
        Suit:Clubs Value:2
        """
        if len(self._cards) == 0:
            return None
        return self._cards.pop()

    def shuffle(self) -> None:
        """
        Shuffle the deck

        >>> deck = Deck()
        >>> deck.add_card(1, "Spades")
        >>> deck.add_card(2, "Clubs")
        >>> deck.add_card(3, "Diamonds")
        >>> deck.add_card(4, "Hearts")
        >>> deck.print_cards()
        1 Spades
        2 Clubs
        3 Diamonds
        4 Hearts
        >>> deck.shuffle()
        """
        random.shuffle(self._cards)

    def print_cards(self) -> None:
        """
        Print all the cards in the deck

        >>> deck = Deck()
        >>> deck.add_card(1, "Spades")
        >>> deck.add_card(2, "Clubs")
        >>> deck.add_card(3, "Diamonds")
        >>> deck.add_card(4, "Hearts")
        >>> deck.print_cards()
        1 Spades
        2 Clubs
        3 Diamonds
        4 Hearts
        """
        for c in self._cards:
            print(c.value, c.suit)


if __name__ == '__main__':
    d = Deck()
    d.add_card(1, 'Hearts')
    d.add_card(2, 'Spades')
    d.print_cards()
    print(d.draw_card())
    print(d.draw_card())
    print(d.draw_card())

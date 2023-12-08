from functools import total_ordering


def data_reader(path: str) -> list[tuple[str, int]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(), file.readlines()))
    data = [(row[0], int(row[1])) for row in data]
    return data


@total_ordering
class Card:
    VALUES = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def __init__(self, value: str):
        self.value = value
        self.score = Card.VALUES.index(value.upper()) + 1

    def __hash__(self):
        return hash(self.score)

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return f'{self.value} ({self.score})'


class Hand:
    def __init__(self, cards: list[Card], bet: int):
        self.cards = cards
        self.original_cards = cards.copy()
        self.original = ''.join([card.value for card in cards.copy()])
        self.bet = bet

    def remove_jockers(self):
        level = {}
        for card in self.cards:
            if card.value != 'J':
                level[card] = level.get(card, 0) + 1
            else:
                level[card] = 1
        best_value = max(list(level.values()))
        best_cards = []
        for card, count in level.items():
            if count == best_value:
                best_cards.append(card)
        best_card = max(best_cards, key=lambda x: x.score)
        if len(set(level.values())) == 1:
            best_card = max(self.cards, key=lambda x: x.score)
            best_card = Card('J') if best_card.value == 'J' else best_card
        for i in range(len(self.cards)):
            if self.cards[i].value == 'J':
                self.cards[i] = best_card

    @property
    def hand_level(self):
        level = {}
        for card in self.cards:
            level[card.value] = level.get(card.value, 0) + 1
        card_value = ''.join([str(card.score).zfill(2) for card in self.original_cards])
        level = list(level.values())
        if 5 in level:
            return int('7' + card_value)
        if 4 in level:
            return int('6' + card_value)
        if 3 in level and 2 in level:
            return int('5' + card_value)
        if 3 in level and len(level) == 3:
            return int('4' + card_value)
        if level.count(2) == 2:
            return int('3' + card_value)
        if 2 in level:
            return int('2' + card_value)
        return int('1' + card_value)

    def __repr__(self):
        return ''.join([card.value for card in self.cards])


def solution(data: list[tuple[str, int]]) -> int:
    hands = []
    for cards, bet in data:
        hand = []
        for card in cards:
            hand.append(Card(card))
        hands.append(Hand(hand, bet))
    hands = sorted(hands, key=lambda x: x.hand_level)
    for hand in hands:
        hand.remove_jockers()
    hands = sorted(hands, key=lambda x: x.hand_level)
    total = 0
    for x, hand in enumerate(hands, 1):
        total += x * hand.bet
        print(f'{x:>5} {hand} ({hand.original}) | {x} x {hand.bet} = {x * hand.bet}')

    return total


input_data = data_reader('input_data.txt')
print(solution(input_data))

from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    # 2-A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 4种花色
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # 构建扑克牌
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # 使类支持[]索引操作,并且是可迭代的
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
deck = FrenchDeck()
# print(len(deck))
# # 迭代
# for item in deck:
#     print(item)
# # 随机选择一张牌
# print(choice(deck))
# print(deck[12::13])


def spades_high(card):
    # 获取牌的索引
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
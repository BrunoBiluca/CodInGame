import sys
import math


class AbstractCall:
    payout = 1
    
    def __init__(self, bet):
        self.bet = bet
        
    def win_condition(self):
        pass
    
    def check(self, result):
        return self.bet + (self.bet * self.payout) if self.win_condition(result) else 0


class EvenCall(AbstractCall):
    def win_condition(self, result):
        if result == 0:
            return False
        return result % 2 == 0
        

class OddCall(AbstractCall):
    def win_condition(self, result):
        return result % 2 != 0
        

class PlainCall(AbstractCall):
    payout = 35
    
    def __init__(self, bet, number):
        super().__init__(bet)
        self.number = number
        
    def win_condition(self, result):
        return result == self.number

        
class Gambler:
    def __init__(self, cash):
        self.cash = cash
        
        self.current_call = None
        
    def call(self, play_call):
        bet = math.ceil(self.cash / 4.0)
        
        self.cash -= bet
        
        self.current_call = {
            "EVEN": EvenCall(bet),
            "ODD": OddCall(bet),
            "PLAIN": PlainCall(bet, play_call["number"])
        }.get(play_call["call"], None)
        
        return self
        
    def check(self, result):
        self.cash += self.current_call.check(result)
        self.current_call = None
    
        
rounds = int(input())
cash = int(input())

gambler = Gambler(cash)
for i in range(rounds):
    play = input()
    
    aux = play.split(" ")
    play_result = int(aux[0])
    
    play_call = {
        "call": aux[1],
        "number": int(aux[2]) if len(aux) == 3 else None
    }

    gambler.call(play_call).check(play_result)
    

print(gambler.cash)

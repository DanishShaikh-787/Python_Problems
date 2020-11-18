# File Name FlipCoin.py
# Created by danish at 16/11/20 and 12:12 AM
# Flip Coin And Print Percentage Of Heads And Tails
import random
class FlipCoin:
  def flipPercentage(self):
   headCount = 0
   tailCount = 0
#User Input For How Many Time To Flip The Coin
   numberOfTimesFlips = int(input("How many times you wants to flip coin: "))
   if numberOfTimesFlips > 0:
    for flip in range(numberOfTimesFlips):
      randomValue = random.random()
    #Counting The Head And Tail Count
      if float(randomValue) > 0.5:
        headCount += 1
      else:
        tailCount += 1
#Calculating The Percentage For Head And Tail
    headPercentage = (headCount / numberOfTimesFlips) * 100
    tailPercentage = (tailCount / numberOfTimesFlips) * 100
    print("Head Percentage is: ", headPercentage)
    print("Tail Percentage is: ", tailPercentage)
   else:
    print("number should be positive")
   return
# Main Method
if __name__ == "__main__":
   FlipCoin.flipPercentage(self=0)

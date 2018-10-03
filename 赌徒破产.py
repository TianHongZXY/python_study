import random

stake = int(input('初始赌资筹码：'))
goal = int(input('离场前期望赚得的金额：'))
trials = int(input('模拟次数：'))
bets = int(input('下注次数：'))
wins = 0
cash = stake
acctual_bet = 0

def bankrupt(goal,bets,wins,cash,acctual_bet):
	for i in range(bets+1):
		cash -= 1
		acctual_bet +=1
		income = 1 * random.uniform(0,1.2)
		cash += income
		if income > 1 :
			wins += 1
		if cash <=0:
			print('He totally bets {} times and won {}.'\
				.format(acctual_bet,wins))
			print('He have lost all the money!')
			break
		elif cash >= goal:
			print('He totally bets {} times and won {}.'\
				.format(acctual_bet,wins))
			print('He have won enough money!')
			break
	else:
		print("He has finished {} times bet".format(bets))

for t in range(trials):
	bankrupt(goal,bets,wins,cash,acctual_bet)
print('{} trials have been finished.'.format(trials))



import random
#Simulating 100 coin tosses
results=[]

for i in range (100):
  toss=random.choice(["Head", "Tail"])
  results.append(toss)

heads=results.count("Head")
tails=results.count("Tail")

print("Heads:", heads)
print("Tails:", tails)
print("Probability of Heads:", heads/100)
print("Probability of Tails:", tails/100)

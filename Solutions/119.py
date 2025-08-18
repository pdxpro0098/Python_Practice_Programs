def compoundInterest(amt, time, rate, n):
    amount = amt * (1+rate/n)**(n*time)
    return round(amount-amt)

print(compoundInterest(10000,2,0.08,4))

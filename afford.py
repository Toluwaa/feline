'''Problem
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.
What is the maximum number of houses you can buy?'''

test_case = int(input('')) #The number of test cases
whole = []
for n in range(test_case):
    each = []
    numbud = input().split() #The number of houses and the budget of dollars to spend 
    costs = sorted(input().split(), key=int) #The cost of each houses received as one input separated by a whitespace
    each.append(numbud)
    each.append(costs)

    whole.append(each)
for n in range(test_case):
    a = 0
    budget = whole[n][0][1]
    budget = int(budget)
    for ele in whole[n][1]:
        if budget >= int(ele):
            budget -= int(ele)
            a +=1
        else:
            break
    print('Case #%d: %d' % (n+1, a))  #The maximum number of houses affordable for each case
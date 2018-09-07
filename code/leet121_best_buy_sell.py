"""best_buy_sell (121)

Say you have an array for which the i'th element is the price of a
given stock on day i.

If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Note that you cannot sell a stock before you buy one.

Examples:

  Input: [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
    profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.

  Input: [7,6,4,3,1]
  Output: 0
  Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

myinput = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]]


def leetSolve(prices):
    """best_buy_sell algorithm - the "obvious" way

    Returns:
        int:  profit potential
    """

    profit = 0
    for buyDay, priceBuy in enumerate(prices):
        for sellDay, priceSell in enumerate(prices[buyDay+1:]):
            if (priceSell - priceBuy > profit):
                profit = priceSell - priceBuy
    return profit


def leetSolveClever(prices):
    """Scan the array only once, keeping a dayToDay tally until a
    better time to buy comes"""

    (profit, dayToDay) = (0, 0)
    yesterday = None
    for today in prices:
        if (yesterday):
            dayToDay += today - yesterday
        dayToDay = max(dayToDay, 0)
        profit = max(dayToDay, profit)
        yesterday = today
    return profit


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolveClever(input))

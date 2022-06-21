'''Coin-counting problem'''

'''A function that returns the
respective denominations is as follows:'''

def basic_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)
    
    number_of_denom = []
    # we iterate and apply the greedy technique:
    for i in sorted_denominations:
        div = total_amount // i
        total_amount = total_amount % i
        if div > 0:
            number_of_denom.append((i, div))
    return number_of_denom


'''A better greedy algorithm is presented here'''
def optimal_small_change(denom, total_amount):
    
    sorted_denominations = sorted(denom, reverse=True)
    series = []
    
    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]
        number_of_denoms = []
        local_total = total_amount
        
        for i in term:
            div = local_total // i
            local_total = total_amount % i
            if div > 0:
                number_of_denoms.append((i, div))
        series.append(number_of_denoms)
    return series

'''Dijkstra's shortest path algorithm'''

        
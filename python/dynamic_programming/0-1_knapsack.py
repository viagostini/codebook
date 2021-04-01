def knapsack_naive(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n-1] > capacity:
        return knapsack_naive(weights, values, capacity, n-1)

    dont_take = knapsack_naive(weights, values, capacity, n-1)
    take = values[n-1] + knapsack_naive(weights, values, capacity-weights[n-1], n-1)
    
    return max(take, dont_take)
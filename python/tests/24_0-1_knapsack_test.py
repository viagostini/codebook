    from dynamic_programming import knapsack_naive

    def test_naive():
        val = [60, 100, 120] 
        wt = [10, 20, 30] 
        W = 50
        n = len(val) 
        assert knapsack_naive(wt, val, W, n) == 220 
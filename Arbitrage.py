liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getAmountOut(amount_in,reserveIn,reserveOut):
    numerator=997*amount_in*reserveOut
    denominator=1000*reserveIn+997*amount_in
    amount_out=numerator/denominator

    return amount_out

def validate_path(path, balance):
    start_token = path[0]
    for next_token in path[1:]:
        # start_token: A, next_token: C
        if start_token > next_token:
            reserveOut, reserveIn = liquidity[next_token, start_token]
        else:
            reserveIn, reserveOut = liquidity[start_token, next_token]
        balance = getAmountOut(balance, reserveIn, reserveOut)
        start_token = next_token
    return balance


usable_token = {"A": "tokenA", "B": "tokenB", "C": "tokenC", "D": "tokenD", "E": "tokenE"}

def main():
    start_token = "tokenB"
    start_balance = 5
    from itertools import permutations
    for i in range(1, 5):
        per_list = list(permutations("ACDE", i))
        for per in per_list:
            curr_path = [start_token] + [usable_token[x] for x in per] + [start_token]
            profit = validate_path(curr_path, start_balance)
            if profit >= 20:
                print("path:", "->".join(curr_path), f", tokenB balance={profit}")
                return


if __name__ == "__main__":
    main()
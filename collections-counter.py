from collections import Counter
if __name__ == '__main__':
    total_shoes = int(raw_input())
    shoe_sizes = list(map(int, raw_input().split()))
    total_customer = int(raw_input())

    total_earned = 0
    shoe_counter = Counter(shoe_sizes)
    for i in range(0, total_customer):
        size, price = map(int, raw_input().split())
        if shoe_counter.get(size, 0) != 0:
            shoe_counter[size] -= 1
            total_earned += price
    print(total_earned)

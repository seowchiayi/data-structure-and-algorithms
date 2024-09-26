def apple_stock(stock_prices):
    max_profit = 0
    min_price = float('inf')
    
    for i in range(len(stock_prices)):
        if stock_prices[i] < min_price:
            min_price = stock_prices[i]
        profit = stock_prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

def highest_product(list_of_ints):
    list_of_ints = [abs(num) for num in list_of_ints]
    sorted_list_of_ints = sorted(list_of_ints, reverse=True)
    return sorted_list_of_ints[0] * sorted_list_of_ints[1] * sorted_list_of_ints[2]


if __name__ == "__main__":
    # print(apple_stock([10, 7, 5, 8, 11, 9]))
    # print(apple_stock([1, 5, 3, 2]))
    # print(apple_stock([7, 2, 8, 9]))
    # print(apple_stock([2, 10, 1, 4]))
    # print(apple_stock([1, 6, 7, 9]))
    # print(apple_stock([9, 7, 4, 1]))
    # print(apple_stock([1, 1, 1, 1]))
    print(highest_product([1, 2, 3, 4]))
    print(highest_product([6, 1, 3, 5, 7, 8, 2]))
    print(highest_product([-5, 4, 8, 2, 3]))
    print(highest_product([-10, 1, 3, 2, -10]))
    print(highest_product([-5, -1, -3, -2]))
import random
import logging


def profitabilty_of_lotto_scratches():
    amount_of_iterations = 10
    amount_of_buyed_scratches = 10000
    scratch_cost = 5
    overall_scratches_amount = 6000000
    scratch_dict_list = [
        {
            "amount": 3,
            "win": 200000
        },
        {
            "amount": 12,
            "win": 5000
        },
        {
            "amount": 180,
            "win": 500
        },
        {
            "amount": 1200,
            "win": 200
        },
        {
            "amount": 6000,
            "win": 100
        },
        {
            "amount": 45000,
            "win": 50
        },
        {
            "amount": 180000,
            "win": 25
        },
        {
            "amount": 132000,
            "win": 15
        },
        {
            "amount": 240000,
            "win": 10
        },
        {
            "amount": 900000,
            "win": 5
        },
    ]

    amount_of_not_winning_scratches = overall_scratches_amount
    full_list_of_scratches = []
    n = 0
    for table in scratch_dict_list:
        amount_of_not_winning_scratches = amount_of_not_winning_scratches - table["amount"]
        if table["win"] > 0:
            table.update({"win true": True})
        table.update({"probability": table["amount"] / overall_scratches_amount})
        while scratch_dict_list[n]["amount"] > 0:
            full_list_of_scratches.append(scratch_dict_list[n]["win"])
            scratch_dict_list[n]["amount"] = scratch_dict_list[n]["amount"] - 1
        n += 1

    scratch_dict_list.append({"amount": amount_of_not_winning_scratches, "win": 0, "win true": False,
                              "probability": amount_of_not_winning_scratches/overall_scratches_amount})
    not_winning_driver = amount_of_not_winning_scratches
    while not_winning_driver > 0:
        full_list_of_scratches.append(0)
        not_winning_driver -= 1

    print(scratch_dict_list)
    print(full_list_of_scratches)
    print(amount_of_not_winning_scratches)
    print(len(full_list_of_scratches))
    print(full_list_of_scratches[5600])

    i = amount_of_buyed_scratches
    drawn_scratches_list = []
    while i > 0:
        drawn_scratch = random.choice(full_list_of_scratches)
        scratch_dict_list
        drawn_scratches_list.append(drawn_scratch)
        full_list_of_scratches.pop(drawn_scratch)
        i -= 1

    money_invested = amount_of_buyed_scratches * scratch_cost
    money_return = 0
    m = 0
    n = 0
    win = 0
    lose = 0

    while m < amount_of_iterations:

        while n < amount_of_buyed_scratches:
            money_return += drawn_scratches_list[n]
            n += 1
            profit = money_return - money_invested
            print(f"Money invested: {money_invested}")
            print(f"Money return: {money_return}")
            print(f"You made: {profit}")
            if profit < 0:
                print("You're a looser!")
                lose += 1
                print(lose)
            else:
                print("To're the winner!!!")
                win += 1
                print(win)
        m += 1

    print(f"You won: {win} times")
    print(f"You lost: {lose} times")
    print(len(full_list_of_scratches))
    print(drawn_scratches_list)
    print(f"Final amount {amount_of_iterations*amount_of_buyed_scratches}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    profitabilty_of_lotto_scratches()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

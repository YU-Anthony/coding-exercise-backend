#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 0:13
# @Author  : Yu Zhang
# @File    : getPointBalances.py

import argparse
import pandas as pd
import collections

# Parse the argument of points to be spent
parser = argparse.ArgumentParser()
parser.add_argument('-points', type=int, default=None)
args = parser.parse_args()

def calculate(points):
    # Check if the value of points is not None
    if points is None:
        raise Exception("Plase input the value of points that you want to spend")
    # Check if points to be spent is negative
    if points < 0:
        raise Exception("The points can not be negative.")

    # Initialize a default dictionary to store the payer and point balance
    ans = collections.defaultdict(int)
    # Read transactions from a CSV file
    data = pd.read_csv('transactions.csv')
    # Sort the transactions based on timestamp
    new_data = data.sort_values('timestamp')

    for _, row in new_data.iterrows():
        # If a payer doesn't exist in the dictionary, add it with initial value 0
        if row['payer'] not in ans:
            ans[row['payer']] = 0
        # If there are still points to be spent and current points are greater than the remaining points
        if points != 0 and points > row['points']:
            points -= row['points']
        elif points != 0 and points <= row['points']:
            ans[row['payer']] += (row['points'] - points)
            points = 0
        elif points == 0:
            ans[row['payer']] += row['points']
    return ans

if __name__ == '__main__':
    ans = calculate(args.points)
    print(ans)
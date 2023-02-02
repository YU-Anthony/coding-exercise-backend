# coding-exercise-backend
This code calculates the point balances for each payer based on the transactions recorded in a CSV file.

## Quick Start
To calculate the point balances for each player:
```bash
python getPointBalances.py -points 5000
```
To run the unit test:
```bash
python unit_test.py
```
## Input
The code takes in one argument, the amount of points to spend, when the program is run.
For example:
```bash
python getPointBalances.py -points 5000
```

The input CSV file must contain the following columns:

- payer
- points
- timestamp

## Output
The output is a dictionary with the payer name as the key and the point balance as the value.

## Algorithm
1. Read the transactions from the CSV file and sort the transactions based on the timestamp.
2. Calculate the point balances for each payer based on the following rules:
- The oldest points are spent first (based on transaction timestamp, not the order they are received)
- No payer's points go negative
3. Return the payer point balances in a dictionary.

## Exception Handling
- If the value of points to spend is not inputted, an exception will be raised with the message "Please input the value of points that you want to spend".
- If the value of points to spend is negative, an exception will be raised with the message "The points can not be negative."
## Libraries Used
- argparse
- pandas
- collections
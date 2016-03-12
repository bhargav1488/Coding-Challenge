# Turo Coding Challenge
This is my implementation of SimpleDB question in https://github.com/relayrides/coding-exercise

You can give the input from stdin. I'm including a few sample input files in the tests directory. To run the program, just type: Python turo.py < tests/input1.txt 

I've used a dictionary to keep track of variables (since the lookup is O(1)) and list of lists to keep track of transactions. Each list inside transactions list represents a transaction block.

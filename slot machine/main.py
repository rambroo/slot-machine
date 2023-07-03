import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

count={
    "A":3,
    "B":7,
    "C":8,
}
values={
    "A":10,
    "B":2,
    "C":1.5
}

def spin(rows,cols,count):
    all_symbols=[]
    for i, count in count.items():
       for _ in range(count):
           all_symbols.append(i)
    # print(all_symbols)
    
    
    columns=[]
    for _ in range(cols):
        each_column=[]
        current_symbols=all_symbols[:]
        for _ in range (rows):
            value=random.choice(current_symbols)          
            current_symbols.remove(value)
            each_column.append(value)
        columns.append(each_column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def winnings(columns,values,lines,bet):
    winnings=0
    winning_lines=[]
    for i in range(len(columns[0])):
        symbol=columns[0][i]
        for j in range(1,len(columns)):
            if columns[j][i]!=symbol:
                break
        else:
            winnings+= values[symbol]*bet
            winning_lines.append(i)
            
  
    return winnings, winning_lines
def deposit():
    while True:
        amount=input(("Enter the amount you want to deposit:"))
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Please enter a valid amount")
    return amount    
def get_number_of_line():
    while True:
        line=input((f"Enter the number of line you want to bet on which is between 1 & {MAX_LINES} : "))
        if line.isdigit():
            line=int(line)
            if 0<line<=MAX_LINES:
                break
            else:
                print("The number of lines should be between 1 and " +str(MAX_LINES) )
        else:
            print("Please enter a valid number of lines")
    return line    
def get_bet():
    while True:
        bet=input(("Enter the amount you want to bet on each line:"))
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"The bet should be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a valid number of line")
    return bet
def main():
    balance=deposit()
    while True: 
        print(f"Your current balance is ${balance} ")
        answer=input("Press Enter to play or Continue | If you want to Quit press Q:")
        if answer.upper()=='Q':
            break
        else:
            line=get_number_of_line()
            while True:

                bet=get_bet()
                total_bet=bet*line
                if total_bet<balance:
                    print(f"Total bet = {total_bet}")
                    break
                else:
                    print(f"You have insufficient balance. BALANCE={balance}")
            columns=spin(ROWS,COLS,count)
            print(columns)
            prnt_slots=print_slot_machine(columns)
            winning_money,winning_lines=winnings(columns,values,line,bet)
            print(f"YOU WON ${winning_money} on this {winning_lines} lines")
            balance+=winning_money-total_bet
main()
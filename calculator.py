import os 


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
 
def calculator():
    num1 = float(input("Enter number one: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Enter symbol for further operation :  ")
        num2 = float(input("Enter number second: "))
        calcuation_function = operations[operation_symbol]
        answer = calcuation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("if you want to futher this operation type 'y' for yes and 'n' for no:  ").lower() =="y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls')    
            calculator()
            
calculator()  




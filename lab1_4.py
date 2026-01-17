def calculate_average(num1:float,num2:float,num3:float)->float:
    return(num1+num2+num3)/3

def add_tax(bill_total:float)->float:
    bill_total += bill_total*0.1
    return bill_total

def greet_user(name:str)->str:
    return "Hello "+name

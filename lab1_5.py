def check_multiple(number:int)->bool:
    if (number%3==0) and (number%5==00):
        return True
    else:
        return False
    
def check_password(input_string: str)->str:
    secret_word = "Python123"
    if input_string == secret_word:
        return "access granted"
    else:
        return "access denied"
    
def calculate_federal_tax(salary:int)->float:
    if(salary<=11000):
        return salary*0.10
    elif(salary<44725):
        return salary*0.12
    elif(salary<95375):    
        return salary*0.22
    else:
        return salary*0.24

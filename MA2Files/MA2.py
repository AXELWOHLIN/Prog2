"""
Solutions to module 2 - A calculator
Student: axel wohlin
Mail: axelwohlin@gmail.com
Reviewed by: Mikael Johansson
Reviewed date: 29/4
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class IntegerError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.get_current() != '':
        raise SyntaxError("Bad expression, exponents not implemented maybe")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
            wtok.next()
            if not wtok.is_name():
                raise SyntaxError('Expected variable name')
            variables[wtok.get_current()] = result
            wtok.next()
            ##
            if wtok.get_current() not in [')','','=']:
                raise SyntaxError('Bad variable assignment syntax')
            ##
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+','-']:
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        else:
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*','/']: 
        wtok.next()
        temp2 = wtok.get_previous()
        temp = factor(wtok, variables)
        if temp2 == '*':
            result = result * temp
        else:
            if temp == 0:
                raise EvaluationError(
            "Division by 0 error") 
            result = result / temp      
    return result

def sin(x):
    x = float(x)
    return math.sin(x)
def cos(x):
    return math.cos(x)
def log(x):
    if x <= 0:
        raise EvaluationError('argument not in function domain')
    return math.log(x)
def exp(x):
    return math.exp(x)
def fac(n):
    if n <= 0:
        raise EvaluationError('argument not in function domain')
    if n.is_integer():
        pass
    else:
        raise EvaluationError(
            "Input is not an integer") 
    if n == 1:
        return 1
    else:
        return n*fac(n-1)
def fib(n):
    if n <= 0:
        raise EvaluationError('argument not in function domain')
    if n.is_integer():
        pass
    else:
        raise EvaluationError(
            "Input is not an integer") 
    n = int(n)
    a = 0
    b = 1
    for i in range(n):
        tmp = a
        a = b
        b = tmp+b
    return a

def mean(args):
    return sum(args)/len(args)

def arglist(wtok,variables):
    lst = list()
    if wtok.get_current() == '(':
        wtok.next()
        while wtok.get_current() != ')' or wtok.get_previous() != ')':
            result = assignment(wtok, variables)
            lst.append(result)
            if wtok.get_current() not in [',', ')','']:
                raise SyntaxError('Bad argument list')
            if wtok.get_current() == ')':
                wtok.next()
                break
            wtok.next()
    else:
        raise SyntaxError("Incomplete argument list")
    return lst

def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {'sin':sin,'cos':cos,'log':log,'exp':exp,'fac':fac,'fib':fib}
    function_n = {'sum':sum,'max':max,'min':min,'mean':mean}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in function_1:
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError('Expected "("')
        result = function_1[wtok.get_previous()](factor(wtok,variables))
       # if wtok.get_current() != ')' and wtok.get_current() != '':
        #    raise SyntaxError("Expected ')'")
        #else:
        #    pass

    elif wtok.get_current() in function_n:
        wtok.next()
        result = function_n[wtok.get_previous()](arglist(wtok,variables))

    elif wtok.is_name():
        if wtok.get_current() == 'vars':
            print('var' + '     ' + 'value' )
            for i in variables:
              print(i + '     ' + str(variables[i]) )
            return
        else:
          if wtok.get_current() not in variables:
              raise EvaluationError('not an assigned variable')
          result =  variables[wtok.get_current()]
          wtok.next()
       
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.get_current() == '-':
        wtok.next()
        result = -1*factor(wtok,variables)
    else:
        raise SyntaxError(
            "Expected number or '('")  
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
            
            except EvaluationError as ee:
                print("*** Eval Error: ", ee)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
 


if __name__ == "__main__":
    main()

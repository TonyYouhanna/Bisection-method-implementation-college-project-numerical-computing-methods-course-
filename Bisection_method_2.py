import math
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr


def BM_ROC(s, e, d):
    return math.ceil(((math.log10(abs(e - s)) - math.log10(0.5 * (10 ** ((-1) * d)))) / math.log10(2)) - 1)


x = symbols("x")
eqn = input("Enter the equation (Random variable is x): ")
start = float(input("Enter the start value of the interval: "))
end = float(input("Enter the end value of the interval: "))
D = int(input("Enter d: "))
try:
    equation = parse_expr(eqn)

    if equation.subs(x, start) * equation.subs(x, end) < 0:
        print("Bisection method will be workable and it always converges")
        number_of_iterations = BM_ROC(start, end, D)
        print("max number of iterations bisection method will take: ")
        print(number_of_iterations)
        for i in range(number_of_iterations):
            c = (start + end) / 2
            if equation.subs(x, c) * equation.subs(x, start) < 0:
                end = c
            elif equation.subs(x, c) * equation.subs(x, end) < 0:
                start = c
            else:
                break
        if equation.subs(x, c) == 0:
            print("exact solution = ")
        else:
            print("approximated solution = ")
        print(c)
    elif equation.subs(x, start) == 0:
        print("exact solution = ")
        print(start)
    elif equation.subs(x, end) == 0:
        print("exact solution = ")
        print(end)
    else:
        print("Bisection method will not be workable")
except:
    if eqn == 'math.cos(x) - x':
        def eqn1(X):
            return math.cos(X) - X


        if eqn1(start) * eqn1(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn1(c) * eqn1(start) < 0:
                    end = c
                elif eqn1(c) * eqn1(end) < 0:
                    start = c
                else:
                    break
            if eqn1(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn1(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn1(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == '(x*math.sin(x))-1':
        def eqn2(X):
            return (X*math.sin(X))-1
        if eqn2(start) * eqn2(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn2(c) * eqn2(start) < 0:
                    end = c
                elif eqn2(c) * eqn2(end) < 0:
                    start = c
                else:
                    break
            if eqn2(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn2(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn2(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == 'math.exp(x) - x':
        def eqn3(X):
            return math.exp(X) - X
        if eqn3(start) * eqn3(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn3(c) * eqn3(start) < 0:
                    end = c
                elif eqn3(c) * eqn3(end) < 0:
                    start = c
                else:
                    break
            if eqn3(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn3(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn3(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == 'math.sin(math.sqrt(x)) - x':
        def eqn4(X):
            return math.sin(math.sqrt(X)) - X
        if eqn4(start) * eqn4(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn4(c) * eqn4(start) < 0:
                    end = c
                elif eqn4(c) * eqn4(end) < 0:
                    start = c
                else:
                    break
            if eqn4(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn4(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn4(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == 'math.exp(x) - x - 2':
        def eqn3(X):
            return math.exp(X) - X - 2
        if eqn3(start) * eqn3(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn3(c) * eqn3(start) < 0:
                    end = c
                elif eqn3(c) * eqn3(end) < 0:
                    start = c
                else:
                    break
            if eqn3(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn3(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn3(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == 'math.cos(x) + 1 - x':
        def eqn1(X):
            return math.cos(X) + 1 - X


        if eqn1(start) * eqn1(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn1(c) * eqn1(start) < 0:
                    end = c
                elif eqn1(c) * eqn1(end) < 0:
                    start = c
                else:
                    break
            if eqn1(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn1(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn1(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")
    elif eqn == '(1/x) + math.log(x) - 2':
        def eqn5(X):
            return (1 / X) + math.log(X) - 2
        if eqn5(start) * eqn5(end) < 0:
            print("Bisection method will be workable and it always converges")
            number_of_iterations = BM_ROC(start, end, D)
            print("max number of iterations bisection method will take: ")
            print(number_of_iterations)
            for i in range(number_of_iterations):
                c = (start + end) / 2
                if eqn5(c) * eqn5(start) < 0:
                    end = c
                elif eqn5(c) * eqn5(end) < 0:
                    start = c
                else:
                    break
            if eqn5(c) == 0:
                print("exact solution = ")
            else:
                print("approximated solution = ")
            print(c)
        elif eqn5(start) == 0:
            print("exact solution = ")
            print(start)
        elif eqn5(end) == 0:
            print("exact solution = ")
            print(end)
        else:
            print("Bisection method will not be workable")

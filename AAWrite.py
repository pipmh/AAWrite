#!/bin/python3
import sys

def run(txt):
    if txt=="":
        return
    if isVarDec(txt):
        return varDec(txt)
    try:
        return functions[rf(txt)](ra(txt))
    except KeyError:
        error("Command not found: " + rf(txt))
    except Exception as e:
        error(str(e))

def rf(txt):
    return txt.split()[0]

def ra(txt):
    return txt.split()[1:]

def error(errorme):
    print(f"ERROR: {errorme}")
def isString(supposedString):
    if supposedString[0] == "\"":
        if supposedString[-1] == "\"":
            return True
        else:
            return False
    else:
        return False
def add(args):
    value = 0
    for x in args:
        try:
            xi = int(x)
        except ValueError:
            error("One of the values was not a number")
            return
        value += xi
    return value
def varDec(args):
    splitted = args.split(" = ")
    if len(splitted) == 2:
        vars[splitted[0]] = splitted[1]
        return splitted[1]
def isVarDec(args):
    splitted = args.split(" = ")
    if len(splitted) == 2:
        return True
    else:
        return False
def show(args):
    if len(args) == 0:
        error("No Args Provided!")
        return
    for a in args:
        print(handleVal(a))
def leave(args):
    sys.exit()
def handleVal(val):
    if isString(val):
        return val.replace('"', "")
    if val in vars:
        return vars[val]
    else:
        error(f"{val} is not defined")
        return
def multiply(args):
    value = 0
    if len(args) == 2:
        try:
            return int(args[0]) * int(args[1])
        except ValueError:
            error("One of the values was not a number")
            return
functions = {"add": add, "quit": leave, "show": show, "multiply": multiply}

vars = {}
print("Quick IDE")
while True:
    a = input(" ~ ")
    rs = run(a)
    if rs:
        print(rs)

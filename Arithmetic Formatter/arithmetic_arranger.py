def errorverify(list,size):
    if size > 5:
        return "Error: Too many problems."
    o = 0
    while o < size:
        a = list[o * 3]
        operator = list[o * 3 + 1]
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        b = list[o * 3 + 2]
        try:
            int(a)
            int(b)
        except:
            return "Error: Numbers must only contain digits."
        if len(a)>4 or len(b)>4:
            return "Error: Numbers cannot be more than four digits."
        o += 1
    return False

def arithmetic_arranger(list, printresult=False):
    size = len(list)
    newlist = []
    for i in list:
        newlist = newlist + i.split(" ")
    validator = errorverify(newlist,size)
    if validator:
        return validator
    o = 0
    numlist = []
    num2list = []
    operatorlist = []
    while o < size:
        numlist = numlist + [newlist[o*3]]
        num2list = num2list + [newlist[o*3+2]]
        operatorlist = operatorlist + [newlist[o*3+1]]
        o += 1
    dasheslist = []
    result = str()
    for i in range(len(numlist)):
        num = numlist[i]
        if int(num2list[i]) > int(num):
            num = num2list[i]
        dasheslist = dasheslist + [len(num)+2]
    for i in range(len(numlist)):
        if i != len(numlist)-1:
            result = result + " "* (dasheslist[i] - len(numlist[i])) + numlist[i] + " "*4
        else:
            result = result + " "* (dasheslist[i] - len(numlist[i])) + numlist[i] + "\n"
    for i in range(len(num2list)):
        if i != len(numlist)-1:
            result = result + operatorlist[i] + " " * (dasheslist[i] - len(num2list[i])-1) + num2list[i] +" " * 4
        else:
            result = result + operatorlist[i] + " " * (dasheslist[i] - len(num2list[i])-1) + num2list[i] + "\n"
    for i in range(len(dasheslist)):
        if i != len(dasheslist)-1:
            result = result + "-"*dasheslist[i] + " "*4
        else:
            result = result + "-" * dasheslist[i]
    if printresult:
        result = result + "\n"
        for i in range(len(operatorlist)):
            if operatorlist[i] == "+":
                newnum = int(numlist[i]) + int(num2list[i])
                if i != len(operatorlist)-1:
                    result = result + " " * (dasheslist[i] - len(str(newnum))) + str(newnum) + " " * 4
                else:
                    result = result + " " * (dasheslist[i] - len(str(newnum))) + str(newnum)
            else:
                newnum = int(numlist[i]) - int(num2list[i])
                if i != len(operatorlist) - 1:
                    result = result + " " * (dasheslist[i] - len(str(newnum))) + str(newnum) + " " * 4
                else:
                    result = result + " " * (dasheslist[i] - len(str(newnum))) + str(newnum)
    return result
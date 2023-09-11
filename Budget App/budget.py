class Category:

    def __init__(self, type):
        self.type = type
        self.ledger = []
        self.money = 0

    def __str__(self):
        head = self.type.center(30, "*") + '\n'
        ledger = ""
        for item in self.ledger:
            desc = "{:<23}".format(item["description"])
            money = "{:>7.2f}".format(item["amount"])
            ledger += desc[:23] + money[:7] + '\n'
        ledger += "Total: {:.2f}".format(self.money)
        return head + ledger

    def deposit(self, amount, description = ""):
        self.money += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.money -= amount
        self.ledger.append({"amount": -1 * amount, "description": description})
        return True

    def get_balance(self):
        return self.money

    def transfer(self, amount, obj):
        if self.withdraw(amount, "Transfer to " + obj.type):
            obj.deposit(amount, "Transfer from " + self.type)
            return True
        return False

    def check_funds(self, amount):
        if self.money >= amount:
            return True
        return False


def create_spend_chart(cartlist):
    spentlist = []
    for item in cartlist:
        cost = 0
        for item in item.ledger:
            if item["amount"] < 0:
                cost += abs(item["amount"])
        spentlist += [cost]
    total = round(sum(spentlist))
    percentagelist = []
    for i in range(len(spentlist)):
        percentagelist += [round((spentlist[i]/total), 2)*100]

    string = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        string += str(i).rjust(3) +  "|"
        for percent in percentagelist:
            if percent >= i:
                string += " o "
            else:
                string += "   "
        string += ' \n'

    string += "    " + "-"*len(cartlist)*3 + "-" + '\n'
    charlist = []
    for i in cartlist:
        temp = []
        for j in i.type:
            temp += j
        charlist += [temp]
    maxlen = 0
    for i in charlist:
        if len(i) > maxlen:
            maxlen = len(i)
    for i in range(maxlen):
        string += "     "
        for j in range(len(charlist)):
            try:
                string += charlist[j][i] + "  "
            except:
                string += "   "
                continue
        string += '\n'
    return string.rstrip("\n")
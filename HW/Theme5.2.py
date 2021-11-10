num = int(input())

class Athlete:
    def __init__(self, string):
        name = ''
        best = 0
        flag = 0
        for x in string:
            if(x.isdigit() == False and flag == 0):
                name+=x
            else:
                flag = 1
                string+=x

        for x in string:
            if(x != ' '):

        self.name = name
        self.best = best
for x in range(num):
    line = input()

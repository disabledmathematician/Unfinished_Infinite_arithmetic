#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:13:21 2023

@author: Charles Truscott

Very scrapped together. For the real project on infinite precision arithmetic in an high-level language such as Python I would rather teach the computer infinitesimal operations such as addition, subtraction, long division, short division and multiplication (as repeated addition for each decimal place and each ones, tenths ... millions and millionths place) but for the latter option would choose using a string in this project and in assembly language using the floating-point registers
Thanks, Charles Truscott

127 Broken Head Rd, Suffolk Park / Byron Bay NSW 2481 

Happy Easter
Prototyping
Not my proudest moment
"""

class ArithmeticOperation(object):
    def __init__(self, number):
        self.number = number
        self.l = number.split('.')
        self.l_place = self.l[0]
        self.r_place = self.l[1]
        self.decimal_place = len(self.l_place)
    def __add__(self, v):
        for x in range(len(self.l)):
            for y in range(len(self.l[x])):
                for x2 in range(len(v.l)):
                    for y2 in range(len(v.l[x2])):
                        if y == y2 and x == x2:
                            print(int(self.l[x][y]) + int(v.l[x2][y2]), end='')
                        if x == 0 and x2 == 0 and y == self.decimal_place - 1 and y2 == self.decimal_place - 1:
                            print('.', end='')
    def __sub__(self, v):
        for x in range(len(self.l)):
            for y in range(len(self.l[x])):
                for x2 in range(len(v.l)):
                    for y2 in range(len(v.l[x2])):
                        if y == y2 and x == x2:
                            print(int(self.l[x][y]) - int(v.l[x2][y2]), end='')
                        if x == 0 and x2 == 0 and y == self.decimal_place - 1 and y2 == self.decimal_place - 1:
                            print('.', end='')
    def __mul__(self, v):
        self_places_l = len(self.l_place) - 1
        v_places_l = (len(v.l_place)) - 1
        self_places_r = len(self.r_place) - 1
        v_places_r = len(v.r_place) - 1
        s = ''
        count_one = 0
        count_two = 0
        while(count_one <= self_places_l):
            while(count_two <= v_places_l):
                s += str(int(self.l_place[count_one]) * int(v.l_place[count_two]))
                count_two += 1
            count_one += 1
#        print(s)
#        print('.')
        count_one = 0
        count_two = 0
        temp_part = ''
        while(count_one <= self_places_l):
            while(count_two <= v_places_r):
                temp_part += str(int(self.l_place[count_one]) * int(v.r_place[count_two]))
                count_two += 1
            count_one += 1
#        print(s, end='')
        count_one = 0
        count_two = 0
        other_temp_part = ''
        while(count_one <= v_places_l):
            while(count_two <= self_places_r):
                other_temp_part += str(int(self.r_place[count_two]) * int(v.l_place[count_one]))
                count_two += 1
            count_one += 1
        final_part = ''
        x = 0 
        x2 = 0
#        print("temp part: {}, other part: {}".format(temp_part, other_temp_part))
        fp = ''
        L = []
        cfp = 0
        while(x < len(temp_part)):
            while(x2 < len(other_temp_part)):
                n = str(int(temp_part[x]) + int(other_temp_part[x2]))
                if temp_part[x] == str(9) and other_temp_part[x2] == str(9):
                    if x == 0 and x2 == 0:
                        n2 = int(s)
                        n2 += 1
                        s = str(n2)
                        L.append(8)
                    else:
                        L.append(1)
                        L.append(8)
                    L[cfp - 1] += int(n[0])
                    L[cfp] = int(n[1])
                cfp += 1
#                print(n)
                x2 += 1
 #               final_part += str(int(temp_part[x]) + int(other_temp_part[x2]))
            x += 1
        print("{}.{}".format(s, L))

    def __truediv__(self, v):
        for x in range(len(self.l)):
            for y in range(len(self.l[x])):
                for x2 in range(len(v.l)):
                    for y2 in range(len(v.l[x2])):
                        if y == y2 and x == x2:
                            print(int(self.l[x][y]) / int(v.l[x2][y2]), end='')
                        if x == 0 and x2 == 0 and y == self.decimal_place - 1 and y2 == self.decimal_place - 1:
                            print('.', end='')
    def __pow__(self, v):
        for x in range(len(self.l)):
            for y in range(len(self.l[x])):
                for x2 in range(len(v.l)):
                    for y2 in range(len(v.l[x2])):
                        if y == y2 and x == x2:
                            print(int(self.l[x][y]) ** int(v.l[x2][y2]), end='')
                        if x == 0 and x2 == 0 and y == self.decimal_place - 1 and y2 == self.decimal_place - 1:
                            print('.', end='')
    
def CharlesTruscottArithmeticalSequence():
    x = ArithmeticOperation('3.333333333333333333333333')
    y = ArithmeticOperation('3.333333333333333344444444')
    z = ArithmeticOperation('2.000000000000000000000000')
    x * y
if __name__ == "__main__": CharlesTruscottArithmeticalSequence()


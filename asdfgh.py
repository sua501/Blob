import math


class tri:
    def __init__(self, a, b, c, d, e, f):
        self.x1 = a
        self.x2 = b
        self.x3 = c
        self.y1 = d
        self.y2 = e
        self.y3 = f
        self._12 = 0
        self._23 = 0
        self._31 = 0

    def wide(self):
        xa = max(self.x1, self.x2, self.x3)
        xi = min(self.x1, self.x2, self.x3)
        if self.x1 != xa:
            if self.x1 != xi:
                xm = self.x1
        elif self.x2 != xa:
            if self.x2 != xi:
                xm = self.x2
        else:
            xm = self.x3

        if self.y1 != ya:
            if self.y1 != yi:
                ym = self.y1
        elif self.y2 != ya:
            if self.y2 != yi:
                ym = self.y2
        else:
            ym = self.y3

        ya = max(self.y1, self.y2, self.y3)
        yi = min(self.y1, self.y2, self.y3)
        wide = (xa-xi)*(ya-yi)
        wide1 = xa-xm

    def check(self):
        if self.h <= 24 and self.m <= 60 and self.s <= 60:
            print("유효한 시간입니다.")
        else:
            print("유효하지 않은 시간입니다.")

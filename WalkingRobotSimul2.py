class Robot:

    def __init__(self, width, height):
        self.w= width
        self.h = height
        self.pos = 0
        self.moved = False
        self.p = 2 * (height + width) - 4
    def step(self, num):
        self.moved = True
        self.pos = (self.pos + num) % self.p
    def getPos(self):
        idx = self.pos
        w,h = self.w, self.h
        if idx < w:
            return [idx, 0]
        idx -= (w-1)

        if idx < h:
            return [w-1, idx]
        idx -= (h-1)

        if idx < w:
            return [w - 1 - idx, h - 1]
        idx -= (w-1)
        return [0, h - 1 - idx]

    def getDir(self):
        if self.moved and self.pos == 0:
            return 'South'
        idx = self.pos
        w , h = self.w , self.h
        if 1<= idx <= w-1:
            return 'East'
        if w <= idx <= w + h - 2:
            return 'North'
        if w + h - 1 <= idx <= 2 * w + h - 3:
            return 'West'
        return 'South' if self.moved else 'East'

R = Robot(6,3)
print(f"[{R.__init__(6, 3)}, {R.step(2)}, {R.step(2)}, {R.getPos()}, {R.getDir()}, {R.step(2)}, {R.step(1)}, {R.step(4)}, {R.getPos()}, {R.getDir()}]")
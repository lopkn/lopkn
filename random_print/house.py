import sys

class House:
    #  sys.stdout.write(" /\ ")
    #  sys.stdout.write("[^]")
    def __init__(self):
        self.step = 0
        self.is_empty = True

    def print_part(self):
        if self.step == 0:
            sys.stdout.write("/"),
            self.is_empty = False
        if self.step == 1:
            sys.stdout.write("*"),
        if self.step == 2:
            sys.stdout.write("\\"),
        if self.step == 3:
            sys.stdout.write("|"),
        if self.step == 4:
            sys.stdout.write(" "),
        if self.step == 5:
            sys.stdout.write("|"),
        self.step += 1
        return

    def set_begin_point(self, point):
        self.begin_point = point

    def is_space_available(self, point):
        if self.is_empty:
            return True
        return True
        #  from IPython import embed; embed(colors="neutral")
    pass

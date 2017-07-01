class my_class:
    x = 0
    y = 1
    def increase_x(self):
        self.x += 1
        return(self.x)
    def increase_y(self):
        self.y -= 2
        return(self.y)

aobj = my_class()
print aobj.increase_x()
print aobj.increase_y()

bobj = my_class()
print bobj.x
print dir(bobj)
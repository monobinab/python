__author__ = 'msaha'

#Write a function f()
#Q: We have the following code with unknown function f(). In f(), we do not want to use return, instead, we may want to use generator.
#for x in f(5):
#    print x,

#The output looks like this:
#0 1 8 27 64

def cube_generator(n):
    for x in range(n):
        yield x**3


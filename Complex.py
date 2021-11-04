from helper_funcs import get_mod, get_arg
from numpy import sin, cos, linspace, pi
import matplotlib.pyplot as plt

class Complex:

    def __init__(self, re=None, im=None, mod=None, arg=None):

        if all((re, im)):
            self.re = re
            self.im = im
            self.mod = get_mod(self)
            self.arg = get_arg(self)
            
        else:
            self.arg = arg
            self.mod = mod
            self.re = mod * cos(arg)
            self.im = mod * sin(arg)
        
    def re(self):
        return self._re
    
    def im(self):
        return self._im

    def __str__(self):

        if self.im == 1:
            im_str = ''
        elif self.im == -1:
            im_str = '-'
        else:
            im_str = str(self.im)

        return "{}{}{}i".format(str(self.re), '+' if self.im >= 0 else '', im_str)

    def __add__(self, other):
        return Complex(self.re+other.re, self.im+other.im)

c_exp = lambda mod, arg: Complex(mod=mod, arg=arg)

complex_set = [c_exp(2, t) for t in linspace(0, 2*pi, 50)]
x = [z.re for z in complex_set]
y = [z.im for z in complex_set]

plt.plot(x, y)
plt.show()
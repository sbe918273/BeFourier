from numpy import sin, cos, arctan, linspace, pi, array

def get_arg(z):

    if z.re == 0:
        if z.im == 0:
            return 0
        elif z.im> 0:
            return 0.5*pi
        else:
            return -0.5*pi

    elif z.re > 0:
        return arctan(z.im/z.re)

    elif z.im > 0:
        return pi + arctan(z.im/z.re)

    else: 
        return -pi + arctan(z.im/z.re)

def get_mod(z):

    return (z.re**2 + z.im**2)**0.5

def center_list(t):
    med = t[int(len(t)/2)]
    return array([i-med for i in t])

class Complex:

    def __init__(self, re=None, im=None, mod=None, arg=None):

        if None not in (re, im):
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
        
        if type(other) == Complex:
            return Complex(re=self.re+other.re, im=self.im+other.im)
        
        else: 
            return Complex(re=self.re+other, im=self.im)
        
    def __radd__(self, other):
        
        return self.__add__(other)
    
    def __mul__ (self, other):
        
        if type(other) == Complex:
            return Complex(mod=self.mod*other.mod, arg=self.arg+other.arg)
        
        else:
            return Complex(mod=self.mod*other, arg=self.arg)
        
    def __rmul__ (self, other):
        
        return self.__mul__(other)
    
c_exp = lambda scale, arg: scale * Complex(mod=1, arg=arg)

def get_wrapped(g, t, nu, start=None, end=None, num=None):
    
    start = min(t) if start is None else start
    end = max(t) if end is None else end
    
    len_t = len(t)
    num = len_t if num is None else num
    
    idxs = []
    for i in range(len_t):
        if t[i] >= start and t[i] <= end:
            idxs.append(i)
            
    idxs_len = len(idxs)
    
    step = int(idxs_len/num)
    step = 1 if step == 0 else step
            
    return [c_exp(g[i], -2*pi * nu * t[i]) for i in range(0, idxs_len, step)], start, end, num

def F_func(g, t, nu, start=None, end=None, num=None):
    
    y, start, end, num = get_wrapped(g, t, nu, start, end, num)
    h = (end-start)/num
    return 0.5*h*(y[0] + y[-1] + 2*sum(y[1:-1]))

def flatten(F, nu, start, end):
    
    F_flattened = []
    
    mean_F = sum(F)*len(F)**-1
    
    for i in range(len(nu)):
        
        if nu[i] >= start and nu[i] <= end:
            F_flattened.append(mean_F)
            
        else:
            F_flattened.append(F[i])
            
    return F_flattened
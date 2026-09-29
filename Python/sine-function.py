from pip._internal.commands import show
from pylab import plot,show
from numpy import linspace,sin

x = linspace(0,10,100)
y = sin(x)

plot(x,y)
show()
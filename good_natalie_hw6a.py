import matplotlib.pyplot as plt
import numpy as np

from good_natalie_hw6b import xsqr
x1 = np.arange(1000)
from good_natalie_hw6b import sinx
x2 = np.arange(1000)
from good_natalie_hw6b import lnx
x3 = np.arange(100)
from good_natalie_hw6b import cosx
x4 = np.arange(100)

fig, axs = plt.subplots(2,2)
axs[0,0].plot(x1, xsqr(x1), color = "darksalmon")
axs[0,0].set_xscale("log")
axs[0,0].set_yscale("log")
axs[0,0].set(xlabel = "x", ylabel = r"$x^2$ - 2x + 1")

axs[0,1].plot(x2,sinx(x2), color = "lightsteelblue")
axs[0,1].set_xscale("log")
axs[0,1].yaxis.set_label_position("right")
axs[0,1].yaxis.tick_right()
axs[0,1].set(xlabel = "x", ylabel = r"$sinx$ + 5")

axs[1,0].plot(x3,lnx(x3), color = "m")
axs[1,0].set_yscale("log")
axs[1,0].set(xlabel = "x", ylabel = r"log(x+1) + $x^2$ + x")
axs[1,0].yaxis.set_label_position("left")

axs[1,1].plot(x4, cosx(x4), color = "green", linestyle = 'dashed')
axs[1,1].set_yscale("log")
axs[1,1].yaxis.set_label_position("right")
axs[1,1].yaxis.tick_right()
axs[1,1].set(xlabel = "x", ylabel = r"$cosx$ - 5 + $x^3$")

plt.savefig('good_natalie_hw6_complete.png', dpi=300)
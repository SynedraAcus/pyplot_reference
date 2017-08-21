#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from functools import partial

plt.figure(figsize=(16.54, 11.69), dpi=300)
plt.xkcd()  # XKCD mode seems to break some stuff (see below), but it looks cool
plt.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.07)
#  The left half of the image shows the stuff you'll usually want on your axes
#  Plots themselves, various highlights, annotations, arrows, titles and so on.

#  Beware: all coordinates in subplot2grid are (y, x), NOT (x, y). I guess it
#  makes a some sense if you think of them as (rows, columns). Still not much
#  sense, though.
plt.subplot2grid((4, 6), (0, 0), 4, 3)
x = np.arange(0, 5, 0.1)
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x, np.sin(x), label='sin x')
plt.plot(x, np.cos(x), label='cos x')

#  Axes, titles and so on.
plt.suptitle('plt.suptitle(\'Figure with many plots\')')
plt.title('plt.title(\'Plot name\')')
plt.xlabel('plt.xlabel(\'X is this\')')
plt.ylabel('plt.ylabel(\'Y is that\')')
plt.legend() #  Gets filled automatically with plots' `label` properties
#  plt.minorticks_on() # Doesn't work in XKCD mode?
#  As does plt.grid, I guess? Smth to do with the colour gray?

#  Blocks and lines
plt.axvspan(3.2, 4)
plt.axhspan(0.5, 0.7)
plt.axhline(0.75)
plt.axvline(3.1)

#  Annotations block
plt.annotate('Annotations', (0, -0.4))
plt.annotate('(Note without an arrow)', (0, -0.5))
plt.annotate('plt.annotate(label, (x,y))', (0, -0.55))
plt.annotate('OR: plt.text(x, y, label)', (0, -0.6))
plt.annotate('(Note with an arrow)', (2, -0.66), (0, -0.67),
             arrowprops={'arrowstyle': '->'})
plt.annotate('plt.annotate(label, (x, y), (text_x, text_y))', (0, -0.72))
plt.annotate('(Arrow without a note)', (0, -0.85))
plt.annotate('plt.arrow(start_x, start_y, xlen, ylen)', (0, -0.9))
plt.arrow(0, -0.8, 1.3, 0.02,
          width=0.002, head_width=0.01, head_length=0.02)
plt.figtext(0.83, 0.17, '(Text outside axes)')
plt.figtext(0.82, 0.13, 'plt.figtext(x, y, label)')
#  Annotations for other elements
#  Annotations kept separate from elements themselves to make code a bit cleaner
plt.annotate('plt.axhspan(ymin, ymax)', (0.3, 0.65))
plt.annotate('plt.axhline(x)', (0.7, 0.77))
plt.annotate('plt.axvspan(xmin, xmax)', (2.25, 0.95))
plt.annotate('plt.axvline(x)', (2, 1.05))
plt.annotate('plt.legend()', (4.1, 0.85))
plt.annotate('plt.ylim()', (-0.25, 1), (0, 1),
             arrowprops={'arrowstyle': '->'})
plt.annotate('plt.xlim()', (5, -1.1), (4.3, -1),
             arrowprops={'arrowstyle': '->'})
plt.annotate('plt.plot(x, np.sin(x), label=\'sin x\')', (2, 0.55),
             rotation=290)
plt.annotate('plt.plot(x, np.cos(x), label=\'cos x\')', (1.4, 0.4),
             rotation=290)
plt.annotate('plt.box(True)', (5.15, 0.3), (3.7, 0.3),
             arrowprops={'arrowstyle': '->'})

#  Second part of the picture shows the most basic types of the plots
#  Plots chosen just because I actually use those and assume they are more or
#  less common. There are more exotic ones if you need them

#  A partial to get a single-cell subplot at the given grid coordinates
single_subplot = partial(plt.subplot2grid, (4, 6), rowspan=1, colspan=1)


#  Just a regular old barplot
#  To make a stacked barplot, use the first set of values as a `bottom` kwarg
#  for the second `plt.bar` call on the same axes.
single_subplot((0, 3))
#  I don't really get how to do this once and for all the axes, so this line gets
#  called often
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.bar([1, 2, 5], [4, 5, 4])
plt.title('plt.bar(x, values)')
#  Horizontal barplot
single_subplot((0, 4))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.barh([1, 2, 5], [4, 5, 4])
plt.title('plt.barh(y, values)')
#  Boxplot
single_subplot((0, 5))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.boxplot([[0.2, 0.3, 0.2, 0.4, 0.5, 0.3], [0.3, 0.4, 0.7, 0.6, 0.6]])
plt.title('plt.boxplot([sequences])')
#  Contour (see plt.contourf for filled contours)
#  Contour example dataset lifted straight from
#  https://matplotlib.org/mpl_examples/pylab_examples/contour_demo.py
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 10.0 * (Z2 - Z1)
single_subplot((1, 3))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.contour(Z)
plt.title('plt.contour(array)')
#  Errorbar
single_subplot((1, 4))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.errorbar([1, 2, 3, 4], [1.1, 1.2, 1.3, 1.3], [0.1, 0.15, 0.12, 0.2])
plt.title('plt.errorbar(x, y, yerr)')
#  Figimage
#  Technically not a plot, but I didn't find a good place for it in the left half
lena = plt.imread('Lenna.png')
single_subplot((1, 5))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.imshow(lena)
plt.title('plt.imshow(array)')
#  Fill
x = np.arange(0, 10, 0.1)
single_subplot((2, 3))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.fill_between(x, np.sin(x))
plt.title('plt.fill_between(x, sin(x)')
#  Hist
single_subplot((2, 4))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.hist(np.random.normal(0, 0.1, 20))
plt.title('plt.hist(x)')
#  Hist2d
single_subplot((2, 5))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.hist2d(np.random.normal(0, 0.1, 20), np.random.normal(0, 0.1, 20))
plt.title('plt.hist2d(array)')
#  Pie
single_subplot((3, 3))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.pie((0.1, 0.2, 0.2, 0.5))
plt.title('plt.pie(values)')
#  Scatter
single_subplot((3, 4))
plt.tick_params(axis='both', which='both', bottom=False, left=False,
                labelbottom=False, labelleft=False)
plt.scatter(x, np.sin(x))
plt.title('plt.scatter(x, y)')

#  Finishing
plt.savefig('reference.svg')

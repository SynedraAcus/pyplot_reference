#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
sin = np.sin(x)
cos = np.cos(x)

plt.figure(figsize=(8.27, 11.69), dpi=300)
plt.xkcd()
plt.plot(x, np.sin(x), label='sin x')
plt.plot(x, np.cos(x), label='cos x')

#  Axes, titles and so on
plt.legend()
plt.suptitle('plt.suptitle(\'Figure with many plots\')')
plt.title('plt.title(\'Plot name\')')
plt.xlabel('plt.xlabel(\'X is this\')')
plt.ylabel('plt.ylabel(\'Y is that\')')
# plt.minorticks_on() # Doesn't work in XKCD mode? As does plt.grid, I guess? Smth to do with the colour gray?
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
plt.annotate('plt.annotate((x, y), (text_x, text_y))', (0, -0.72))
plt.annotate('(Arrow without a note)', (0, -0.85))
plt.annotate('plt.arrow(start_x, start_y, xlen, ylen)', (0, -0.9))
plt.arrow(0, -0.8, 1.3, 0.02,
          width=0.002, head_width=0.01, head_length=0.02)
#  Annotations for other elements
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
#  Finishing
plt.savefig('reference.svg')

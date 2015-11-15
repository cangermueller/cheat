#!/usr/bin/env python

import progressbar as pb
import time

"""
pip install progressbar2
writes to stderr

pb = Progressbar(...)
    max_val=maximum_value
update(i)
finish()

if sys.stderr.isatty() // only show progress bar is stderr not redirected to file
    pb.update(i)
"""

widgets=['Loading ', pb.AnimatedMarker(), ': ', pb.Percentage(), ' ', pb.Bar(), ' ', pb.ETA(), ' ', pb.FileTransferSpeed()]
"""
Bar(), BouncingBar()
Percentage(), Counter()
AnimatedMarker()
ETA()
FileTransferSpeed()
"""


p = pb.ProgressBar(maxval=100, widgets=widgets, term_width=100)
p.start()
for i in range(100):
    time.sleep(0.01)
    p.update(i)
p.finish()

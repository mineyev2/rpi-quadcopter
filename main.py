# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, sys.path[0]+'/UI')

from UI import QuadUI

QuadUI.run()

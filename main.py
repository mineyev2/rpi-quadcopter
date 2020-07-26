from threading import Thread

# add folders to path
import sys
sys.path.insert(1, sys.path[0]+'/UI')
sys.path.insert(1, sys.path[0]+'/python_video_stream')

from UI import QuadUI
from server_prototype import run

ui = Thread(target = QuadUI.run())
server = Thread(target = run())

ui.start()
server.start()

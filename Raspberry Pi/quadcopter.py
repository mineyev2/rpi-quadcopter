from motors import Motors
from marg import MARG

class Quadcopter:
    def __init__(self):
        self.motors = Motors()
        self.marg = MARG()
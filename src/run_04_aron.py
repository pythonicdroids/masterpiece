from pybricks.tools import wait
from mission_base import MissionBase

class Run_04(MissionBase):
    def __init__(self, left_motor, right_motor):
        super().__init__(left_motor, right_motor)

    def run_old(self):
        self.forward(250, 65)
        self.right_turn(84, 100)
        self.forward(300, 69)
        self.left_turn(20, 200)
        self.backwards(300, 15)
        self.right_turn(21, 300)
        self.backwards(400, 57)
        self.right_turn(116, 500)
        self.forward(395, 55)

    def run(self):
        self.forward(250, 68)
        self.backwards(200, 4)
        self.right_turn(77, 100)
        self.forward(300, 69)
        self.backwards(400, 66)
        self.right_turn(108, 400)
        self.forward(400, 50)
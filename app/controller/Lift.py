class LiftController:
    def __init__(self, motor_controller):
        self.motor_controller = motor_controller

    def lift_up(self):
        # Code to lift the kiln lid up
        self.motor_controller.move_up()

    def lift_down(self):
        # Code to lower the kiln lid
        self.motor_controller.move_down()

    def stop(self):
        # Code to stop the motor
        self.motor_controller.stop()
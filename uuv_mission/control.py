# control.py
class PDController:
    def __init__(self, K_P=0.15, K_D=0.6):
        self.K_P = K_P
        self.K_D = K_D
        self.previous_error = 0  # To store e[t-1]

    def control(self, reference, output):
        """Computes the control action u[t] for the current step."""
        error = reference - output
        control_action = self.K_P * error + self.K_D * (error - self.previous_error)
        self.previous_error = error
        return control_action


class Baseline:
    """ In this class we have an instance variable default_state \
    that stores the default state of the model. \
    The set_default_state method allows you to set the default state. """
    def __init__(self):
        self.default_state = None

    def set_default_state(self, state):
        self.default_state = state

    def get_default_state(self):
        return self.default_state


class Journal:
    """ In the Journal class, we have an instance variable \
    model_states which is a list to store the different model states. 
    The add_model_state method adds a new model state to the journal, \
    and the get_model_states method returns all the stored model states. """
    def __init__(self):
        self.model_states = []

    def add_model_state(self, state):
        self.model_states.append(state)

    def get_model_states(self):
        return self.model_states
      
     

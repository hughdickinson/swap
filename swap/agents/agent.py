################################################################
# Parent class for all agents

import abc

from swap.agents.tracker import Tracker


class Agent:
    """ Agent to represent a classifier (user,machine) or a subject

    Parameters:
        id: str
            Identifier of Agent
        probability: num
            Initial probability used depending on subclass.
    """

    def __init__(self, id, probability):
        self.id = id
        self.probability = probability

        self.annotations = Tracker()

    def getID(self):
        """ Returns Agents ID """
        return self.id

import Call
from math import inf
import imp

imp.reload(Call)

STOP, UP, DOWN, OPEN, CLOSE, ENTER, EXIT =\
    "STOP", "UP", "DOWN", "OPEN", "CLOSE", "ENTER", "EXIT"


STOPPED, OPENED, UPWARD, DOWNWARD, =\
    "STOPPED", "OPENED", "UPWARD", "DOWNWARD"

class Elevator:
    def __init__(self, id):
        self.status = "STOPPED"
        self.id = id
        self.floor = 1
        self.passengers = []
    

    def decideAction(self, call:Call.Call):
        actionString = self.createAction(call.start)
        return self.createActionDict(actionString)



    def createActionDict(self, actionString):
        actionDict = {'elevator_id': self.id, 'command': actionString}
        return actionDict
    
    def update(self, data):
        self.id = int(data["id"])
        self.floor = int(data["floor"])
        self.passengers = data["passengers"]
        self.status = data["status"]


    def distanceFromCall(self, call:Call.Call):
        if call.start < self.floor and self.status == "UPWARD":
            distance = inf
        elif call.start > self.floor and self.status == "DOWNWARD":
            distance = inf
        elif self.status == "STOPPED" or self.status == call.direction:
            distance = abs(call.start - self.floor)
        elif self.status == "OPENED" and call.start == self.floor:
            distance = 0
        else:
            distance = abs(call.start - self.floor) + 1
        return distance
    

    def createAction(self, floor):
        if floor == self.floor:
            if self.status == OPENED:
                actionString = ENTER
            elif self.status == STOPPED:
                actionString = OPEN
            else:
                actionString = STOP
        elif floor > self.floor:
            if self.status in [OPENED, DOWNWARD]:
                actionString = STOP
            else:
                actionString = UP
        else:
            if self.status in [OPENED, UPWARD]:
                actionString = STOP
            else:
                actionString = DOWN
        return actionString



    def __str__(self):
        return ("id: {}, floor: {}, passengers: {}, status: {}".\
            format(self.id, self.floor, self.passengers, self.status))
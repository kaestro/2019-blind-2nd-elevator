# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import copy
import math
from imp import reload


# %%
import Elevator
import Call
from Api import start, action, oncalls


# %%
def Update(request, elevatorList, callDist):
    token = request["token"]
    timestamp = request["timestamp"]
    elevators = request["elevators"]
    calls = request["calls"]
    is_end = request["is_end"]

    for elevator in elevators:
        eId = elevator["id"]
        elevatorList[eId].update(elevator)
    
    for call in calls:
        _call = Call.Call(call)
        callDict[_call.id] = _call
    
    for elevator in elevatorList:
        print(elevator)
    
    for call in callDict.values():
        print(call)


# %%
STOP, UP, DOWN, OPEN, CLOSE, ENTER, EXIT = 0, 1, 2, 3, 4, 5, 6
MAX_PASSENGER, MAX_FLOOR = 8, 5


# %%
user = 'tester'
problem = 0
count = 2


# %%
ret = start(user, problem, count)
token = ret['token']
print('Token for %s is %s' % (user, token))


# %%
request = oncalls(token)


# %%
print(request)


# %%
requestList = []
elevatorList = [Elevator.Elevator(i) for i in range(2)]
callDict = {}


# %%
Update(request, elevatorList, callDict)


# %%
commandList = []
takenIds = []
for call in callDict.values():
    minDist = math.inf
    elevatorId = None
    for elevator in elevatorList:
        if len(elevator.passengers) > 0 or elevator.id in takenIds:
            continue

        dist = elevator.distanceFromCall(call)
        if dist < minDist:
            minDist, elevatorId = dist, elevator.id
            
        if elevatorId is not None:
            takenIds.append(elevatorId)
            actionJson = elevatorList[elevatorId].decideAction(call)
            commandList.append(actionJson)
            break


# %%
for command in commandList:
    print(command)


# %%
action(token, commandList)



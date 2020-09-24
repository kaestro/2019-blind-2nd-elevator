class Call:
    def __init__(self, callJson):
        self.id = int(callJson["id"])
        self.timestamp = int(callJson["timestamp"])
        self.start = int(callJson["start"])
        self.end = int(callJson["end"])
        self.direction = "UPWARD" if self.start < self.end else "DOWNWARD"

    def __str__(self):
        return str("id: {}, timestamp: {}, start: {}, end: {}, direction: {}".\
            format(self.id, self.timestamp, self.start, self.end, self.direction))
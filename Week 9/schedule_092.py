#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour=0, minute=0, duration=0):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'

class Schedule(object):

    def __init__(self):
        self.sch = {}

    def add(self, meeting):
        new = str(meeting).split()
        time = new[0].split(":")
        time = int(time[0]) * 60 + int(time[1])
        self.sch[meeting] = time
    def __str__(self):
        output = "Schedule\n--------\n"
        count = 0
        self.sch = dict(sorted(self.sch.items(), key=lambda item: item[1]))
        for s in self.sch:
            output += f'{s}\n'
            count += 1
        output += f'Meetings today: {count}'
        return output.strip()

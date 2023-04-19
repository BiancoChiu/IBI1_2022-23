from random import random
# in the init method, we initiate each instance the attributes
# create an info method to print out each attribute


class triathlon(object):
    def __init__(self, first_name, last_name, location,
                 swim, cycle, run, total):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.total = total

    def info(self):
        print('Player Name: ' + self.first_name + self.last_name +
              '  Competition Location: ' + self.location +
              '  Swim Time: ' + self.swim +
              '  Cycle Time: ' + self.cycle +
              '  Run Time: ' + self.run +
              '  Total Time: ' + self.total)


# following is the testing code
# I don't know how long does triathlon take,
# so I just use some random number to represent them
swim_time = random()
cycle_time = random()
run_time = random()
total_time = swim_time + cycle_time + run_time
Jack_Smith = triathlon('Jack', 'Smith', 'Sunshine Lake',
                       '%.2f' % swim_time, '%.2f' % cycle_time, '%.2f' % run_time, '%.2f' % total_time)
Jack_Smith.info()
# Output: Player Name: JackSmith  Competition Location: Sunshine Lake  Swim Time: 0.11  Cycle Time: 0.32  Run Time: 0.21  Total Time: 0.64

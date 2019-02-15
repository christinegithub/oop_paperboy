class Paperboy:

# Each paperboy should have several attributes:
# Name
# Experience (the number of papers they've delivered)
# Earnings (amount of money they've earned)
    def __init__(self, name, experience = 0, earnings = 0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

# Every day, each paperboy is given a house number to start at and a house number to finish at.
# They get paid $0.25 for every paper they deliver and $0.50 for every paper over their quota.
# If at the end of the day they haven't met their quota, they lose $2.
#
# The minimum number of papers to deliver is 50. The quota is calculated as half of your experience
# added to the minimum. So the first time a paperboy makes a delivery, the quota is 50.
# The next time, the quota is 50 plus half the number of papers that the paperboy has delivered in the past.
# In this way the quota should increase after every delivery the paperboy makes.
#
# Each paperboy should have at least these methods:
#
# __str__

    def __str__(self):
        return "{} delivered {} papers and made ${}.".format(self.name, self.experience, self.earnings)
# quota
# This method should calculate and return the paperboy's quota for his next delivery

    def quota(self):
        min_papers = 50
        quota = 0
        quota = min_papers + (self.experience/2)
        return round(quota)

# deliver(self, start_address, end_address)
# This method will take two house numbers and return the amount of money earned on this delivery
# as a floating point number. It should also update the paperboy's experience!
# Let's assume that the start_address is always a smaller number than the end_address
# As a stretch exercise you can figure out how to ensure it still works if the above assumption isn't met!

    def deliver(self, start_address, end_address):
        num_of_houses = (end_address + 1) - start_address
        house = 1
        current_quota = self.quota()

        while house <= num_of_houses:

            self.experience += 1

            if house > current_quota:
                self.earnings += 0.50
            else:
                self.earnings += 0.25
            house += 1
        if num_of_houses < current_quota:
            self.earnings -= 2

        return self.earnings

# report
# This method should return a string about the paperboy's performance
# e.g. "I'm Tommy, I've delivered 90 papers and I've earned $38.25 so far!"
    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned ${} so far!".format(self.name,
        self.experience, ('%.2f' % self.earnings))

# Here's some sample code, using your Paperboy class:

tommy = Paperboy("Tommy")
print(tommy)

print(tommy.quota()) #  50
tommy.deliver(101, 160) # 17.5
tommy.earnings # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"

print(tommy.quota()) # 80
tommy.deliver(1, 75) # 16.75
tommy.earnings # 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"

class Place:

    def __init__(self, description, forward, back, left, right, no_victoy, visits=0):
        self.visits = visits
        self.forward = forward
        self.back = back
        self.left = left
        self.right = right
        self.description = description
        self.no_victory = no_victoy

    def say_state(self):
        if self.visits == 1:
            print("This is your first time here")
        else:
            print("You've been here {} fucking times".format(self.visits))

    def move(self, direction):
        return getattr(self, direction)

    def get_victory(self):
        return self.no_victory

    # def brake(self):
    #     if self.speed < 5:
    #         self.speed = 0
    #     else:
    #         self.speed -= 5
    #
    # def step(self):
    #     self.location += self.speed

#
if __name__ == '__main__':

    my_car = Place()
#     print("I'm a car!")
#     while True:
#         action = input("What should I do? [A]ccelerate, [B]rake, "
#                  "show [O]dometer, or show average [S]peed?").upper()
#         if action not in "ABOS" or len(action) != 1:
#             print("I don't know how to do that")
#             continue
#         if action == 'A':
#             my_car.accelerate()
#         elif action == 'B':
#             my_car.brake()
#         elif action == 'O':
#             print("The car has driven {} kilometers".format(my_car.odometer))
#         elif action == 'S':
#             print("The car's average speed was {} kph".format(my_car.average_speed()))
#         my_car.step()
#         my_car.say_state()

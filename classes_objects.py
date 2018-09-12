lottery_player = {
  'name': 'Oscar',
  'numbers': (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
  def __init__(self, name):
    self.name = name
    self.numbers = (5, 9, 12, 3, 1, 21)

  def total(self):
    return sum(self.numbers)

player_one = LotteryPlayer('Oscar')
player_one.numbers = (1,2,3,4,5,6)
player_two = LotteryPlayer('Carlos')
#player_two.numbers = LotteryPlayer('Carlos')

print(player_one.name)
print(player_one.numbers)
print(player_one.total())

print(player_one == player_two)
print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)

##

class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []
  
  def average(self):
    return sum(self.marks) / len(self.marks)

  # @classmethod
  # @staticmethod
  def go_to_school(self):
    print("I'm going to {}.".format(self.school))
    print("I'm going to school")
    # print("I'm a {}".format(cls))

anna = Student('Anns', 'MIT')
panchito = Student('panchito', 'UNAM')
anna.marks.append(56)
anna.marks.append(71)
anna.go_to_school()
panchito.go_to_school()
print(anna.marks)
print(anna.average())
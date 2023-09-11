import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
      self.contents = []
      for key in balls:
          for i in range(balls[key]):
              self.contents += [key]

    def draw(self, n):
      lower = min(n, len(self.contents))
      list = []
      for i in range(lower):
          list += [self.contents.pop(random.randrange(len(self.contents)))]
      return list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        expected = []
        flag = 0
        for key in expected_balls:
            for i in range(expected_balls[key]):
                expected += [key]
        for i in expected:
            if i in balls_drawn:
                balls_drawn.remove(i)
            else:
                flag = 1
        if flag == 1:
            continue
        m += 1
    return m/ num_experiments
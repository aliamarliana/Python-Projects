import copy
import random


class Hat:

  def __init__(self, **balls):
    # Initialization of the Hat object with specified balls and their counts
    self.contents = []
    for color, count in balls.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls):
    # Draw a specified number of balls from the hat
    num_balls_drawn = min(num_balls, len(self.contents))
    drawn_balls = random.sample(self.contents, num_balls_drawn)

    # Remove the drawn balls from the hat's contents
    for ball in drawn_balls:
      self.contents.remove(ball)

    # Return the drawn balls
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # Perform experiments to calculate the probability of getting the expected balls
  successful_experiments = 0

  for _ in range(num_experiments):
    # Create a deep copy of the hat for each experiment
    hat_copy = copy.deepcopy(hat)

    # Draw a specified number of balls from the copied hat
    drawn_balls = hat_copy.draw(num_balls_drawn)

    # Count the occurrences of each color in the drawn balls
    drawn_dict = {
        color: drawn_balls.count(color)
        for color in set(drawn_balls)
    }

    # Check if the drawn balls match the expected counts
    success = all(
        drawn_dict.get(color, 0) >= count
        for color, count in expected_balls.items())
    if success:
      successful_experiments += 1

  # Calculate the probability based on the successful experiments
  return successful_experiments / num_experiments

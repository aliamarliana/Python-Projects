# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# Dictionary to map moves to their counter moves
counter_moves = {"R": "P", "P": "S", "S": "R"}

# Dictionary to store counts of observed patterns
pattern_counts = {}


def player(prev_play, opponent_history=[]):
  # Append the previous play to the opponent's history
  if prev_play != "":
    opponent_history.append(prev_play)

  # Adjusting lookback length to analyze opponent's history
  lookback_length = 6

  # Alias for opponent's history
  history = opponent_history

  # Default guess
  guess = "R"

  # Check if enough history is available to make a prediction
  if len(history) > lookback_length:
    # Extract the last 'lookback_length' moves from opponent's history to form a pattern
    pattern = join(history[-lookback_length:])

    # Check if the pattern of length (lookback_length + 1) has been observed before
    if join(history[-(lookback_length + 1):]) in pattern_counts.keys():
      # Increment the count for the observed pattern
      pattern_counts[join(history[-(lookback_length + 1):])] += 1
    else:
      # Initialize the count for the observed pattern
      pattern_counts[join(history[-(lookback_length + 1):])] = 1

    # Generate all possible next moves based on the current pattern
    possible_patterns = [pattern + "R", pattern + "P", pattern + "S"]

    # Ensure all possible patterns are accounted for in the counts dictionary
    for pattern in possible_patterns:
      if pattern not in pattern_counts.keys():
        pattern_counts[pattern] = 0

    # Predict the opponent's next move by selecting the pattern with the highest count
    prediction = max(possible_patterns,
                     key=lambda pattern: pattern_counts[pattern])

    # Determine the corresponding counter move for the predicted move
    if prediction[-1] == "P":
      guess = "S"
    elif prediction[-1] == "R":
      guess = "P"
    elif prediction[-1] == "S":
      guess = "R"

  return guess


# Helper function to join moves into a single string
def join(moves):
  return "".join(moves)

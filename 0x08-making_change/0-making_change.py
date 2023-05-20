def make_change(coins, total):
  """
  Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

  Args:
    coins: A list of the values of the coins in your possession.
    total: The amount of change you need to make.

  Returns:
    The fewest number of coins needed to meet total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.

  Raises:
    ValueError: If coins is not a list of integers.

  """

  if not isinstance(coins, list):
    raise ValueError("coins must be a list of integers")

  if not all(isinstance(coin, int) for coin in coins):
    raise ValueError("coins must be a list of integers")

  if total < 0:
    return -1

  if total == 0:
    return 0

  coins.sort(reverse=True)

  min_coins = float("inf")

  for coin in coins:
    if total >= coin:
      new_min_coins = make_change(coins, total - coin) + 1
      if new_min_coins < min_coins:
        min_coins = new_min_coins

  return min_coins

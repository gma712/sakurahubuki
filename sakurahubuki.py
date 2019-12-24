import random
import argparse
import logging


class Player:
  def __init__(self, index):
    self.index = index


class SakuraCounter:
  pass


class CountResultStore:
  pass


class BestNumberDetector:
  pass


def main(n):
  PLAYER_INDEXES = [i for i in range(n)]


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='桜吹雪ゲーム攻略プログラム')
  parser.add_argument('--num', type=int, help='対戦人数', required=True)
  args = parser.parse_args()
  main(args.num)

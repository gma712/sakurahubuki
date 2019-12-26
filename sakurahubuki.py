import random
import argparse
import logging


# 識別番号を持ち、自分意外の番号を指定する。
class Player:
  def __init__(self, index):
    self.index = index


# メンバー数を持ち、指定された数に対して対象のメンバーインデックスを返す.
class SakuraCounter:
  def __init__(self, player_num):
    self.player_num = player_num


# 指定される数を持ち、その数の際の結果をストアしていく。
class CountResultStore:
  pass


# CountResultStoreを配列として受け取り、最も自滅しない数を返す。
class BestNumberDetector:
  pass


def main(n):
  PLAYER_INDEXES = [i for i in range(n)]


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='桜吹雪ゲーム攻略プログラム')
  parser.add_argument('--num', type=int, help='対戦人数', required=True)
  args = parser.parse_args()
  main(args.num)

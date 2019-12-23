import random
import argparse


def main(args):
  MEMBERS = [i for i in range(args.num)]
  print(args)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='桜吹雪ゲーム攻略プログラム')
  parser.add_argument('--num', type=int, help='対戦人数')
  args = parser.parse_args()
  main(args)

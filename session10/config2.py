import os


def main():
  try:
    _path = os.path.join(os.path.dirname(__file__), 'config.txt')
    configuration = open(_path)
  except FileNotFoundError:
    print("Couldn't find the config.txt file!")
  except IsADirectoryError:
    print("Found config.txt but it is a directory, couldn't read it")


if __name__ == '__main__':
  main()

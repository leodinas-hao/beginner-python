import os


def main():
  try:
    _path = os.path.join(os.path.dirname(__file__), 'config.txt')
    configuration = open(_path)
  except OSError as err:
    if err.errno == 2:
      print("Couldn't find the config.txt file!")
    elif err.errno == 13:
      print("Found config.txt but couldn't read it")
    elif err.errno == 21:
      print('Found config.txt as directory not a file')
    else:
      print(str(err))


if __name__ == '__main__':
  main()

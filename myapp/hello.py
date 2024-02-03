import fire

def hello(name="World"):
  return "HII %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

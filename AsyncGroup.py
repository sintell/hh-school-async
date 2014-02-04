from functools import wraps
class AsyncGroup(object):
  """
  Asynchronous group realisation 
  Create Async Group object, with final callback and error callback
  Call AsyncGroup.add() on function to add to async group 
  Or use as @decorator on function definition 
  """
  def __init__(self, fin_cb, err_cb):
    super(AsyncGroup, self).__init__()
    self.fin_cb = fin_cb
    self.err_cb = err_cb

    self.func_list = []

  def add(self, func):
    self.func_list.append(id(func))
    @wraps(func)
    def wrapper(*args, **kwargs):
      try:
        ret = func(*args, **kwargs)
        pass
      except Exception, e:
        self.err_cb(e)
      finally:
        self.func_list.remove(id(func))
        if len(self.func_list) == 0:
          self.fin_cb()
        return
    return wrapper

def main():
  def final_callback():
    print 'final'
    pass

  def error_callback(e):
    print 'error', e
    pass


  def f1(a):
    print 'f1', a
  def f2(a):
    print 'f2', a
    raise Exception("a")
  def f3(a):
    print 'f3', a


      
  ag = AsyncGroup(final_callback, error_callback)

  f1 = ag.add(f1)
  f2 = ag.add(f2)
  f3 = ag.add(f3)

  f1(1)
  f2(2)
  f3(3)

if __name__ == '__main__':
  main()
hh-school-async
===============

Написать на Питоне код, реализующий возможности асинхронной группы:

```python

def final_callback():
    # executes after all functions from async group were called
    pass


def error_callback(e):
    # executed on error
    pass
    
group = AsyncGroup(final_callback, error_callback)
group.add(func1)
group.add(func2)
group.add(func3)

# ...

func1(x, y)
func2()
func3(z)

# now final_callback should be executed
```

В случае возникновения любой необработанной ошибки, должен быть вызван error_callback.

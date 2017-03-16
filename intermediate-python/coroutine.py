# 生成器是数据的生产者
# 协程则是数据的消费者


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")

search = grep('coroutine')
search.close()

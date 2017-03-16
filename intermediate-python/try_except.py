# 处理单个异常
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

# 处理多个异常
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))

# 对每个单独的异常在单独的except语句块中处理
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
except IOError as e:
    print("An error occurred.")

# 捕获所有异常
try:
    file = open('test.txt', 'rb')
except Exception:
    print("An error occurred.")

# finally
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# try else
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

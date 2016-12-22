import os

print 'Your operating system: ', os.name
print 'Your username: ', os.getlogin()
print 'Your current working directory is: ', os.getcwd()
print 'Your system path is: ', os.getenv('PATH')

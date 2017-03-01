#input
#s = raw_input('Please enter a message: ')
s = 'abcdefghijklmnopqrstuvwxyz' #Uncoded
s = 'XzXyXxXwXvXuXtXsXrXqXpXoXnXmXlXkXjXiXhXgXfXeXdXcXbXa' #Coded
print(s)

#decode - will check to see if the message is coded.
def coded(s):
    for i in s[::2]:
        if i != 'X':
            return False
    return True
    
if coded(s):
    print('Here is the decoded message: ')
    r = s[::-2]
    print(r)
else:
    print('The encoded message follows:')
    t = ''
    for i in s[::-1]:
        t += 'X' + i
    print(t)

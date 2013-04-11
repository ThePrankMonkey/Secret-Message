#input
s = raw_input('Please enter a message: ')
#s = 'abcdefghijklmnopqrstuvwxyz'
print

#decode - will check to see if the message is coded.
def coded(s):
    for i in s[::2]:
        if i != 'X':
            return False
    return True
if coded(s):
    print 'Here is the decoded message: '
    r = t[::-2]
    print r 

#encode
else:
    print 'The encoded message follows:'
    t = ''
    for i in s[::-1]:
        t += 'X' + i
    print t

message = 'You have to reverse this sentence!'
rev_message = ''

i = len(message)-1 
while i>=0:
    rev_message = rev_message + message[i] 
    i = i - 1

print(rev_message)

#for decryption
message_rev = '!ecnetnes siht esrever ot evah uoY' 
rev_message = ''

i = len(message_rev)-1 
while i>=0:
    rev_message = rev_message + message_rev[i] 
    i = i - 1

print(rev_message)
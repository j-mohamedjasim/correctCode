from itertools import zip_longest

round = []
customer = []
code = []
comment = []

cop = []

while True:
    ask = input('Would you like to add?[s/n] ')

    if ask == 's':

        rnumber = input('What is the round number? ')
        cname = input('What is the customer name or address? ')
        ecode = input('What is the correct code to use? ')
        comments = input('Any comments? ')

        round.append(rnumber)
        cop.append(rnumber)
        customer.append(cname)
        code.append(ecode)
        comment.append(comments)
        print(' ')
        print(len(round),'item(s) added successfully!!!')
        print(' ')

    elif ask == 'show':
        print(' ')
        for i, cust in enumerate(customer):
            print(i, cust)
        print(' ')

    elif ask == 'del':
        confirm = int(input('Which one would you like to delete? '))

        del round[confirm]
        del cop[confirm]
        del customer[confirm]
        del code[confirm]
        del comment[confirm]

    elif ask == 'n':
        break
    else:
        print(' ')
        print('Please type') 
        print('[n] to come out of the program')
        print('[s] to continue to add')
        print('[show] to show what was added')
        print('[del] to delete an entry')
        print(' ')

length = len(round)
print(' ')
print('Total item added into the basket: ',length)
print(' ')

for round, customer, code, comment in zip_longest(round, customer, code, comment, fillvalue = None):
    print(' ')
    print('Round:',round,'|','Customer:',customer,'|','Code:',code,'|','Comment:',comment)
    print(' ')
    while True:
        space = input('Are you ready for another one? ')
        if space == 's':
            break
        else:
            continue

print(' ')
print('Make sure these round number below are signed off and cleared')
print(' ')
for i in cop:
    print(i)
print(' ')
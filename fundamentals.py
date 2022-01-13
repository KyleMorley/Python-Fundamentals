## Check if a number is odd or even
def even_or_odd(number):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

##even_or_odd(0)

## Check for good ideas
def well(x):
    count = 0
    for idea in x:
        if idea == 'good':
            count += 1
    if count == 0:
        print('Fail')
    elif count < 3:
        print('Publish!')
    else:
        print('I smell a series!')
    
##well(['good', 'bad', 'bad'])

## Abreviate a name
def abbrev_name(name):
    answer = name[0]
    
    for i in range(1, len(name)):
        if name[i - 1] == ' ':
             answer = answer + '.' + name[i]
                
    print(answer.upper())

##abbrev_name("Sam Harris")

## Check the same case of letters
def same_case(a, b): 
    if a.isupper() and b.isupper():
        print(1)
    elif a.islower() and a.islower():
        print(0)
    else:
        print(-1)

##same_case('\?', 'Z')

## Tally total points. Rules: if x>y - 3 points; if x<y - 0 point; if x=y - 1 point
def points(games):
    tally = 0
    for x in games:
        if x[0] > x[2]:
            tally += 3
        elif x[0] < x[2]:
            tally += 0
        else:
            tally += 1
	
    print(tally)

##points(['1:1','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])

## Remove a charecter from the end of a string. E/g '!'
def remove(s):
    if s[-1] == '!':
        new_string = s.replace('!', '')
    else:
        new_string = s

    print(new_string)

##remove("Hi!")
##remove('!Hi')

## Find factors of a number
def factors(n):
    x = n / 2
    y = range(int(x))

    for z in y:
        if n % (z + 1) == 0:
            answer = z + 1
            print(answer)
        
factors(16)
print('###')
factors(153)
print('###')

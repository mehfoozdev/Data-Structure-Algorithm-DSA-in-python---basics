'''
Question => 01

Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

'''

# print('---------- Array Exercise ----------')
#          # jan   feb   mar   apr   may
# monthly = [2200, 2350, 2600, 2130, 2190]

# # 1. In Feb, how many dollars you spent extra compare to January?
# print(f'You spent extra dollars in febuary : ', monthly[1]-monthly[0])

# # 2. Find out your total expense in first quarter (first three months) of the year.
# print('Total expense in first quarter is : ', sum(monthly[0:3]))

# # 3. Find out if you spent exactly 2000 dollars in any month
# # for i in monthly:
# #     if (i == 2000):
# #         print(f'You spend 2000 in the month ')
# #         break
# #     else:
# #         print('You did not spend exactly 2000 in any of month')

# print('Did I spent 2000$ in any month?', 2000 in monthly)

# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# newItem = monthly.append(1980)
# print('Month of june is added in the list : ', monthly)


# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this   => 2130
# monthly[3] = monthly[3]-200
# print('correctionMonth : ', monthly)






''' 
Question => 02

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

# heros = ['spider man','thor','hulk','iron man','captain america']

# print('Total Length is : ', len(heros))

# new_heros = heros.append('black panther')
# print('added in the list', heros)

# newheros = heros.remove('black panther')
# print('item is removed : ', heros)

# new_heros = heros.insert(3, 'black panther')
# print('black panther is added after hulk', heros)

# heros.sort()
# print('List sorted in order (alpha) : ', heros)







'''
Question => 3

Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

'''

oddNumber = []
userInput = int(input('Enter a number : '))

for a in range(1, userInput+1):
    if (a % 2) != 0:
        oddNumber.append(a)

print('Here is odd number list : ', oddNumber)
ticket_number = int(input('Input num of your ticket: '))

left_part = ticket_number // 1000
right_part = ticket_number % 1000

if left_part == right_part:
    print('It is a happy ticket!')
else:
    print('it is a ticket like a ticket, nothing special')
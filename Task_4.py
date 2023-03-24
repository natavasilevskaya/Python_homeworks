earnings = int(input('Yuor earnings: '))
costs = int(input('Your costs: '))

profitability = earnings - costs
profitability_coef = profitability / 100

if profitability >= costs:
    print('You have a profitability! Its equal {}'.format(profitability_coef))
    num_of_emploee = int(input('Input number of emploees: '))
    coef_emploee = num_of_emploee * profitability_coef
    print(coef_emploee)
else:
    print('You have not prifitabilyty')
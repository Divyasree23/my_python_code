principle = 20000
interestrate = 5
time = 5

#simple interest
simple_interest = principle * (interestrate / 100) * time
print(f'Interest for 5 months to principle amount {principle} :',simple_interest)

# compound interest
compound_interest = principle * ((1 + interestrate / 100)) ** time
print(compound_interest)

#Celsius to Fahrenheit
celisus = 32
fahrenhit = (celisus * 1.8) + 32
print(fahrenhit)

#Fahrenheit to celsius
fahrenhit = 89.6
celisus = (1.8 / fahrenhit ) + 32
print(celisus)

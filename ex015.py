days = int(input('Days rented: '))
km = float(input('How much KM did u ride: '))

totalToPay = (60*days) + (km * 0.15)
print('U ride for {} and {}KM, u will gonna pay: R${:.2f}'.format(days, km, totalToPay))
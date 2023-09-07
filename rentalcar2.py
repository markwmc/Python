rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n') # ask how long did you rent?

if rentalCode == 'B' or rentalCode == 'D': #if budget or daily
  rentalPeriod = int(input('Number of Days Rented:\n')) #ask how many days rented
else:
  rentalPeriod = int(input('Number of Weeks rented:\n')) #otherwise, how many weeks rented

if rentalCode == 'B': #if budget, the base charge is days rented times 40
  baseCharge = rentalPeriod*40

if rentalCode == 'D': # if daily, the base charge is days rented times 60
   baseCharge = rentalPeriod*60

else:
  baseCharge = rentalPeriod*190 #otherwise, the base charge is weeks rented times 190

odoStart = int(input("Starting Odometer Reading:\n"))  # starting odometer reading

odoEnd = int(input("Ending Odometer Reading:\n"))  # ending odometer reading
totalMiles = odoEnd - odoStart  # total miles driven
if rentalCode == 'B':  # mile charge equals total miles times .25
    mileCharge = totalMiles * float(0.25)

averageDayMiles = totalMiles/rentalPeriod
extraMiles = 0
    if rentalCode == 'D':  # if daily rental
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if averageDayMiles <= 100:
    extraMiles = 0
  else:
    extraMiles = averageDayMiles - 100
  mileCharge = extraMiles * .25

if rentalCode == 'W': # if the weekly miles driven average is greater than 900, the mile charge is the base charge times 100
    averageWeekMiles = totalMiles/rentalPeriod
    if averageWeekMiles > 900:
      mileCharge = rentalPeriod * float(100.00)
else: #otherwise, the amount due is the base charge
  mileCharge = baseCharge

#print the customer inputs and outputs in order to display the information and charges
print('Rental Summary')
print('Rental Code:        ', rentalCode)
print('Rental Period:      ', rentalPeriod)
print('Starting Odometer:  ', odoStart)
print('Ending Odometer:    ', odoEnd)
print('Miles Driven:       ', totalMiles)
print('Amount Due:         ', amtDue)
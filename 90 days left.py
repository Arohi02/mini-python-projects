age=int(input("what is your age?"))
years_remaining= 90- age
days_remaining = years_remaining*365
weeks_reamaning=years_remaining*52
months_remaining=years_remaining*12
message=f"The number of days you have left is {days_remaining} days, {weeks_reamaning} weeks and {months_remaining} months left"
print(message)
#-----------------------Week 1 Tasks – Casting & I/O-------------------------------------
#1.Read three numbers and output their average
print('Avg Calculator')
num1=float(input('Enter the number:'))
num2=float(input('Enter the number:'))
num3=float(input('Enter the number:'))
#Average
avge=(num1+num2+num3)/3
print(avge)



#2.Convert minutes to hours and minutes
print('Convert minutes into hours')
#user enter the total minutes
complete_Minutes=int(input('Enter total minutes'))
#logic
hours=complete_Minutes//60
minutes=complete_Minutes%60
#total minutes into hours and hour into minutes
print(f"{complete_Minutes} minutes = {hours} hour(s) and {minutes} minute(s)")
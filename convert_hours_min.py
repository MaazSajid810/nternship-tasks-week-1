#2.Convert minutes to hours and minutes
print('Convert minutes into hours')
#user enter the total minutes
complete_Minutes=int(input('Enter total minutes'))
#logic
hours=complete_Minutes//60
minutes=complete_Minutes%60
#total minutes into hours and hour into minutes
print(f"{complete_Minutes} minutes = {hours} hour(s) and {minutes} minute(s)")
##   collects initial data from user & assigns variables
# "for" = service: google, email, vpn, social media
account=input('What is this account for?')
username=input('What is the account username?')
password=input('What is the password?')
rotation_interval=input('In months, how often will this password be changed?')

## performs score calculations
password_length = len(password)
length_score = password_length * 10
# how many times the password will be rotated over 3 years
rotation_count = 36 // rotation_interval

## converts int values to str
# instead of doing individually in score output with str(int(x))
# prevents typeerror
password_length=str(password_length)
length_score=str(length_score)
rotation_interval=str(rotation_interval)
rotation_count=str(rotation_count)

## score evaluation output
print('========================================')
print('   PASSWORD AUDIT REPORT')
print('========================================')
print('Account:           '+account)
print('Username:          '+username)
print('Password length:   '+password_length+'characters')
print('Length score:      '+length_score+'points')
print('Rotation interval: '+rotation_interval)
print('Rotations (3 yr):  '+rotation_count)
print('----------------------------------------')
print('NOTE: Classification requires conditionals -- coming in Week 02.')
print('========================================')
      

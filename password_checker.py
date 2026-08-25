##   collects initial data from user
# "for" = service: google, email, vpn, social media
print('What is this account for?')
  account=input()
print('What is the account username?')
  username=input()
print('What is the password?')
  password=input()
print('In months, how often will this password be changed?')
  rotation_interval=input()

## performs score calculations
password_length = len(password)
length_score = password_length * 10
# how many times the password will be rotated over 3 years
rotation_count = 36 // rotation_interval

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
      

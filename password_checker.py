##   collects initial data from user & assigns variables
# "for" = service: google, email, vpn, social media
account=input('What is this account for?')
username=input('What is the account username?')
password=input('What is the password?')
rotation_interval=input('In months, how often will this password be changed?')

## performs score calculations and converts them to strings for score output
password_length = str(len(password))
length_score = str(int(password_length) * 10)
# how many times the password will be rotated over 3 years
rotation_count = str(36 // int(rotation_interval))

## declaring length score variable
# will be defined as the desired str output for the audit report
if int(password_length) <8:
    length_verdict = "WEAK — does not meet minimum length requirements"
elif int(password_length) >=8 and int(password_length)<12:
    length_verdict = "MODERATE — meets minimum but falls short of NIST recommendations"
elif int(password_length) >=12 and int(password_length)<15:
    length_verdict = "GOOD — acceptable length for most systems"
else:
    length_verdict = "STRONG — meets NIST SP 800-63B recommendations"

## checks if password contains a digit and defines variable for str output in audit
if '0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password:
    has_digit = 'YES'
else:
    has_digit = 'CRITICAL - password must contain a digit'

## confirms that password isnt username
if password != username:
    not_username='NO'
else:
    not_username='CRITICAL — password must not match username'

## confirms password rotation frequency is acceptable
if int(rotation_interval) >=12:
    rotation_verdict = 'WARNING — rotation interval exceeds recommended maximum of 12 months'
elif int(rotation_interval) >=6 and int(rotation_interval) <13:
    rotation_verdict = 'ACCEPTABLE — rotation interval within recommended range'
else:
    rotation_verdict = 'EXCELLENT — frequent rotation policy detected'

## overall pass/fail eval
# checks the 4 prev. variables and creates a 5th for length req.
# 15 char minimum is not reflected in length classification, but is requirement for overall pass/fail
# consider remodeling length classification to reflect clearer 15 character minimum
length_ok = int(password_length) >= 15
if length_ok and has_digit == 'YES' and not_username == 'NO':
    overall_pass = 'PASS — password meets all checked criteria'
else:
    overall_pass = 'OVERALL: FAIL — see findings above'

## score evaluation output
print('========================================')
print('   PASSWORD AUDIT REPORT')
print('========================================')
print('Account:           '+account)
print('Username:          '+username)
print('Password length:   '+password_length+' characters')
print('Length score:      '+length_score+' points')
print('Rotation interval: '+rotation_interval)
print('Rotations (3 yr):  '+rotation_count)
print('----------------------------------------')
print('Length verdict:    '+length_verdict)
print('Digit found:       '+str(has_digit))
print('Username match:    '+str(not_username))
print('Rotation verdict:  '+rotation_verdict)
print('----------------------------------------')
print('OVERALL:           '+overall_pass)
print('========================================')

##these variables must be GLOBAL to be correct in the final audit
##or they dont exist after their initial review- wont increment & appear in final audit
#set how many passwords collected
batch_size = 3
count = 0
#count passed failed critical for final return
total_pass=0
total_fail=0
critical_count=0

##collects initial data from user & assigns variables
#"for" = service: google, email, vpn, social media
account=input('What is this account for?')
username=input('What is the account username?')
password=input('What is the password?')
rotation_interval=input('In months, how often will this password be changed?')
##defines variables for functions below
password_length = len(password)

##checks if password meets minimum pass/fail length requirements and def audit final output str
def check_length(password):
    if int(password_length) <8:
        length_verdict = "WEAK — does not meet minimum length requirements"
        length_ok=False
    elif int(password_length) >=8 and int(password_length)<12:
        length_verdict = "MODERATE — meets minimum but falls short of NIST recommendations"
        length_ok=False
    elif int(password_length) >=12 and int(password_length)<15:
        length_verdict = "GOOD — acceptable length for most systems"
        length_ok=False
    else:
        #this is the only length that passes
        length_verdict = "STRONG — meets NIST SP 800-63B recommendations"
        length_ok=True
    return length_ok, length_verdict
##checks if password contains a digit and defines variable for pass/fail
def check_digit(password):
    #stays false=fail audit
    has_digit=False
    #checks each char is digit/letter
    for char in password:
        #if one found
        if char in '0123456789':
            #passes audit
            has_digit=True
    return has_digit
##checks if username and password match and defines variable for pass/fail
def check_username(password, username):
    not_username = password != username
    if not_username == False:
        username_match = "CRTICAL - password must not match username"
    else:
        username_match = "NO"
    return not_username, username_match
##checks if rotation interval meets pass/fail requirements and def audit final output str
def check_rotation(rotation_interval):
    if int(rotation_interval) >12:
        rotation_verdict = 'WARNING — rotation interval exceeds recommended maximum of 12 months'
        rotation_ok=False
    elif int(rotation_interval) >=6 and int(rotation_interval) <13:
        rotation_verdict = 'ACCEPTABLE — rotation interval within recommended range'
        rotation_ok=True
    else:
        #if rotated every >=5 mo
        rotation_verdict = 'EXCELLENT — frequent rotation policy detected'
        rotation_ok=True
    return rotation_ok, rotation_verdict
##final pass/fail audit
def audit_password(account, username, password, rotation_interval):
    ##calls above functions to evaluate the password
    length_ok, length_verdict = check_length(password)
    has_digit = check_digit(password)
    not_username, critical_count = check_username(password, username)
    rotation_ok, rotation_verdict = check_rotation(rotation_interval)
    ##password pass/fail
    #does this password pass length, digit, and username match checks? yes=passes audit
    overall_pass = length_ok and has_digit and not_username
    ##assigns tuple 1/0 values, passed failed critial
    if overall_pass:
        overall = "OVERALL: PASS - password meets all checked criteria"
        passed = 1
        failed = 0
    else:
        overall = "OVERALL: FAIL - see findings above"
        passed = 0
        failed = 1
    if not_username == False:
        critical = 1
    else:
        critical = 0
    #misc scores for audit report
    length_score = str(int(password_length) * 10)
    #how many times the password rotates over 3 years
    rotation_count = str(36 // int(rotation_interval))
    ##print the audit report for this password
    print('========================================')
    print('   PASSWORD AUDIT REPORT:' + str(count+1)+' of '+str(batch_size))
    print('========================================')
    print('Account:           '+account)
    print('Username:          '+username)
    print('Password length:   '+str(password_length)+' characters')
    print('Length score:      '+length_score+' points')
    print('Rotation interval: '+rotation_interval)
    print('Rotations (3 yr):  '+rotation_count)
    print('----------------------------------------')
    print('Length verdict:    '+length_verdict)
    print('Digit found:       '+str(has_digit))
    print('Username match:    '+str(not_username))
    print('Rotation verdict:  '+rotation_verdict)
    print('----------------------------------------')
    print('OVERALL:           '+overall)
    print('========================================')
    return passed, failed, critical

##runs the evaluation!
if __name__ == '__main__':
    while count < batch_size:
        audit_password(account, username, password, rotation_interval)
        count += 1
    if count==batch_size:
        print('========================================')
        print('   PASSWORD AUDIT SUMMARY')
        print('========================================')
        print('Total passwords checked:')
        print('Total passed:           '+str(total_pass))
        print('Total failed:           '+str(total_fail))
        print('Total critical warnings:'+str(critical_count))
        print('----------------------------------------')
        print('NOTE: Input is still hardcoded--file reading coming in Week 08')
        print('========================================')

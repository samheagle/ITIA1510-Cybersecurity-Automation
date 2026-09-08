##set how many passwords collected
BATCH_SIZE = 3
COUNT = 0
##these variables must be GLOBAL to appear in the final audit
##or they dont exist after their initial review
total_pass=0
total_fail=0
total_critical=0
while COUNT < BATCH_SIZE:
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
    has_digit = False
    ##counts how many char in input
    for char in password:
        #if a char is a digit, the password has a number, has_digit is set to True and the loop ends
        if char in '0123456789':
            has_digit = True
    ## confirms that password isnt username
    if password != username:
        not_username='NO'
    else:
        not_username='CRITICAL — password must not match username'
        #is there only one critical warning in here?
        total_critical=total_critical+1
    ## confirms password rotation frequency is acceptable
    if int(rotation_interval) >12:
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
    if length_ok and has_digit == True and not_username == 'NO':
        overall_pass = 'PASS — password meets all checked criteria'
        #total_pass variable is used to track how many passwords pass the audit, and total_fail tracks how many failed
        total_pass=total_pass+1
    else:
        overall_pass = 'OVERALL: FAIL — see findings above'
        total_fail=total_fail+1

    ## score evaluation output
    #this will print 3 times once for each password
    #in future consider storing the password outputs to a list and printing them all at once at the end of the batch for one big report
    print('========================================')
    print('   PASSWORD AUDIT REPORT:' + str(COUNT+1)+' of '+str(BATCH_SIZE))
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
    ##if this is the last password, print the summary of the batch audit
    COUNT=COUNT+1
    if COUNT==BATCH_SIZE:
        print('========================================')
        print('   PASSWORD AUDIT SUMMARY:')
        print('========================================')
        print('Total passwords checked: '+str(BATCH_SIZE))
        print('Total passed:            '+str(total_pass))
        print('Total failed:            '+str(total_fail))
        print('Total critical warnings: '+str(total_critical))
        print('----------------------------------------')
        print('NOTE: Input is still hardcoded -- file reading coming in Week 08')
        print('========================================')




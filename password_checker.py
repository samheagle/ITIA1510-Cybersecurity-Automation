#knownbreached must be global so that check_breach can access it
known_breached = ["password", "password123", "123456", "qwerty", "letmein", "welcome", "monkey", "dragon", "master", "sunshine"]

##totals must be GLOBAL or will not be added to by credentials for loop
total_fail = 0
total_pass = 0
critical_count = 0

##checks if password meets minimum pass/fail length requirements and def audit final output str
def check_length(password):
    """Checks password length against NIST SP 800-63B thresholds. Takes a password string. Returns (length_ok: bool, length_verdict: str)."""
    password_length = int(len(password))
    if password_length<8:
        length_verdict="WEAK — does not meet minimum length requirements"
        length_ok=False
    elif password_length>=8 and password_length<12:
        length_verdict = "MODERATE — meets minimum but falls short of NIST recommendations"
        length_ok=False
    elif password_length >=13 and password_length<15:
        length_verdict = "GOOD — acceptable length for most systems"
        length_ok=False
    else:
        #this is the only length that passes
        length_verdict = "STRONG — meets NIST SP 800-63B recommendations"
        length_ok=True
    return length_ok, length_verdict
##checks if password contains a digit and defines variable for pass/fail
def check_digit(password):
    """Check every character in input password against digits. Returns (has_digit: bool)."""
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
    """Checks password against username. Returns (not_username=bool, username_match=str)."""
    not_username = password != username
    if not_username == False:
        username_match = "CRITICAL - password must not match username"
    else:
        username_match = "NO"
    return not_username, username_match
##checks if rotation interval meets pass/fail requirements and def audit final output str
def check_rotation(rotation_interval):
    """Ensures password is rotated at least every year. Returns (rotation_ok:bool, rotation_verdict:str)."""
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
##checks if password is in known breached list
def check_breach(password):
    """Checks if password is in known breached list. Returns (breached:bool, breached_verdict:str)."""
    not_breached = password not in known_breached
    breached_verdict = "NO"
    if not_breached == False:
        breached_verdict = "CRITICAL -- password found in known breach list"
    return not_breached, breached_verdict
##final pass/fail audit
def audit_password(account, username, password, rotation_interval, not_breached):
    """Checks if input password is >=15ch, has a digit, doesnt match username, and is rotated >=yearly. Returns (return passed:int, failed:int, critical:int)."""
    ##calls above functions to evaluate the password
    length_ok, length_verdict = check_length(password)
    has_digit = check_digit(password)
    not_username, username_match= check_username(password, username)
    rotation_ok, rotation_verdict = check_rotation(rotation_interval)
    not_breached, breached_verdict = check_breach(password)
    password_length = int(len(password))
    ##password pass/fail
    #does this password pass length, digit, breached and username match checks? yes=passes audit
    overall_pass = length_ok and has_digit and not_username and not_breached
    ##assigns tuple 1/0 values, passed failed critial
    if overall_pass:
        overall = "OVERALL: PASS - password meets all checked criteria"
        passed = 1
        failed = 0
    else:
        overall = "OVERALL: FAIL - see findings above"
        passed = 0
        failed = 1
    if not_username == False or not_breached == False:
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
    print('Rotation interval: '+str(int(rotation_interval))+" months")
    print('Rotations (3 yr):  '+rotation_count)
    print('----------------------------------------')
    print('Length verdict:    '+length_verdict)
    print('Digit found:       '+str(has_digit))
    print('Username match:    '+username_match)
    print('Rotation verdict:  '+rotation_verdict)
    print('----------------------------------------')
    print('OVERALL:           '+overall)
    print('========================================')
    return passed, failed, critical

##runs the evaluation!
#will only print audit summary if run from the main branch
if __name__ == '__main__':
    credentials = [
    ["Gmail", "jsmith", "password123", 12],#fail, in breached
    ["SSH Server", "jsmith", "jsmith", 24],#fail, username match
    ["VPN", "jsmith", "Tr0ub4dor&3correct", 3],#pass
    ["Company Email", "jsmith", "summer2024!", 6],#fail, length
    ["GitHub", "jsmith", "Blue-Harbor-72-Lantern", 6]]#pass

    batch_size=len(credentials)
    count = 0
    failed_accounts = []
    critical_accounts = []

    for credential in credentials:
        account, username, password, rotation_interval = credential
        passed, failed, critical = audit_password(account, username, password, rotation_interval, known_breached)
        if failed:
             failed_accounts.append(account)
        if critical:
             critical_accounts.append(account)
        total_pass+=passed
        total_fail+=failed
        critical_count+=critical
        count+=1

    while count < batch_size:
        audit_password(account, username, password, rotation_interval)
        count += 1
    if count==batch_size:
        print('========================================')
        print('   PASSWORD AUDIT SUMMARY')
        print('========================================')
        print('Total passwords checked: '+str(batch_size))
        print('Total passed:            '+str(total_pass))
        print('Total failed:            '+str(total_fail))
        print('Total critical warnings: '+str(critical_count))
        print('----------------------------------------')
        print('Accounts failed:        '+str(failed_accounts))
        print('Accounts critical:      '+str(critical_accounts))
        print('----------------------------------------')
        print("NOTE: Breach list and credentials are hardcoded -- file reading coming in Week 08.")
        print('========================================')

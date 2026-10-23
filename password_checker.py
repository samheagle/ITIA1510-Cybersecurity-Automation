#knownbreached must be global so that check_breach can access it
known_breached = ["password", "password123", "123456", "qwerty", "letmein", "welcome", "monkey", "dragon", "master", "sunshine"]
#policy has to be global so that check_length and check_rotation can access it
#a policy is easier to read and edit besides a bunch of hardcoded values spread out through funcs
policy = {
    "min_length": 8,
    "strong_length": 15,
    "max_rotation_months": 12,
    "good_rotation_months": 6,
    "require_digit": True,
    "check_breach_list": True
}

##checks if password meets minimum pass/fail length requirements and def audit final output str
def check_length(password, policy):
    """Checks password length against NIST SP 800-63B thresholds. Takes a password string. Returns (length_ok: bool, length_verdict: str)."""
    password_length = int(len(password))
    if password_length<policy["min_length"]:
        length_verdict="WEAK — does not meet minimum length requirements"
        length_ok=False
    elif password_length<policy["strong_length"]:
        length_verdict = "MODERATE — meets minimum but falls short of NIST recommendations"
        length_ok=False
    elif password_length==policy["strong_length"]:
        length_verdict = "GOOD — acceptable length for most systems"
        length_ok=True
    else:
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
def check_rotation(rotation_interval, policy):
    """Ensures password is rotated at least every year. Returns (rotation_ok:bool, rotation_verdict:str)."""
    if int(rotation_interval) >policy["max_rotation_months"]:
        rotation_verdict = 'WARNING — rotation interval exceeds recommended maximum of 12 months'
        rotation_ok=False
    elif int(rotation_interval) >=policy["good_rotation_months"] and int(rotation_interval)<policy["max_rotation_months"]:
        rotation_verdict = 'ACCEPTABLE — rotation interval within recommended range'
        rotation_ok=True
    else:
        #if rotated every >=5 mo
        rotation_verdict = 'EXCELLENT — frequent rotation policy detected'
        rotation_ok=True
    return rotation_ok, rotation_verdict
##checks if password is in known breached list
def check_breach(password, known_breached):
    """Checks if password is in known breached list. Returns (breached:bool, breached_verdict:str)."""
    not_breached = password not in known_breached
    breached_verdict = "NO"
    if not_breached == False:
        breached_verdict = "CRITICAL -- password found in known breach list"
    return not_breached, breached_verdict
##final pass/fail audit
def audit_password(account, username, password, rotation_interval, not_breached, policy):
    """Checks if input password is >=15ch, has a digit, doesnt match username, and is rotated >=yearly. Returns (return passed:int, failed:int, critical:int)."""
    ##calls above functions to evaluate the password
    length_ok, length_verdict = check_length(password, policy)
    has_digit = check_digit(password)
    not_username, username_match= check_username(password, username)
    rotation_ok, rotation_verdict = check_rotation(rotation_interval, policy)
    not_breached, breached_verdict = check_breach(password)
    password_length = int(len(password))
    count=0
    ##password pass/fail
    #does this password pass length, digit, breached and username match checks? yes=passes audit
    overall_pass = length_ok and has_digit and not_username and not_breached
    ##assigns tuple 1/0 values, passed failed critial
    if overall_pass:
        overall = "OVERALL: PASS - password meets all checked criteria"
        passed = 1
        failed = 0
        count+=1
    else:
        overall = "OVERALL: FAIL - see findings above"
        passed = 0
        failed = 1
        count+=1
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
    print('   PASSWORD AUDIT REPORT: ' + str(int((summary["total"]))+1)+' of '+str(len(credentials)))
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
    print('Breach check:      '+breached_verdict)
    print('Rotation verdict:  '+rotation_verdict)
    print('----------------------------------------')
    print('OVERALL:           '+overall)
    print('========================================')
    return passed, failed, critical

##runs the evaluation!
#will only print audit summary if run from the main branch
if __name__ == '__main__':
    credentials = [
    {"account": "Gmail", "username": "jsmith", "password": "password123", "rotation_interval": 12},#fail, in breached
    {"account": "SSH Server", "username": "jsmith", "password": "jsmith", "rotation_interval": 24},#fail, username match
    {"account": "VPN", "username": "jsmith", "password": "Tr0ub4dor&3correct", "rotation_interval": 3},#pass
    {"account": "Company Email", "username": "jsmith", "password": "summer2024!", "rotation_interval": 6},#fail, length
    {"account": "GitHub", "username": "jsmith", "password": "Blue-Harbor-72-Lantern", "rotation_interval": 6},]#pass

    failed_accounts = []
    critical_accounts = []
    summary = {"total": 0, "passed": 0, "failed": 0, "critical": 0,
           "failed_accounts": [], "critical_accounts": []}

    for cred in credentials:
        passed, failed, critical=audit_password(cred["account"], cred["username"], cred["password"], cred["rotation_interval"], known_breached, policy)
        if passed:
            summary["passed"] += 1
        if failed:
            summary["failed_accounts"].append(cred["account"])
            summary["failed"] += 1
        if critical:
            summary["critical_accounts"].append(cred["account"])
            summary["critical"] += 1
        summary["total"] += 1

    print('========================================')
    print('   PASSWORD AUDIT SUMMARY')
    print('========================================')
    print('Total passwords checked: '+str(summary["total"]))
    print('Total passed:            '+str(summary["passed"]))
    print('Total failed:            '+str(summary["failed"]))
    print('Total critical warnings: '+str(summary["critical"]))
    print('----------------------------------------')
    print('Accounts failed:        '+str(summary["failed_accounts"]))
    print('Accounts critical:      '+str(summary.get("critical_accounts", 0)))
    print('----------------------------------------')
    print("NOTE: Credentials and breach list are hardcoded -- file reading coming in Week 07.")
    print('========================================')

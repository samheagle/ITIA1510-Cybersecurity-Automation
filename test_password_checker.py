from password_checker import (check_length, check_digit, check_username, check_rotation, check_breach, load_credentials, load_breached, write_report, policy, save_summary, load_summary)

known_breached = load_breached("breached.txt")
credentials = load_credentials("credentials.txt")
checklines = ["First test line", "Second test line"]

check1=True
check2=False
check3=True

##check_digit
check=check_digit("hello")
assert check==False
if check==False:
    check1=False
print("PASS: checkdigit failed password without digit")

check=check_digit("hello5")
assert check==True
if check==True:
    check2=True
print("PASS: checkdigit passed password with digit")

assert check1==False and check2==True
print("PASS: !! checkdigit functioning")

#check_length
check1=False
check2=False
check3=True

check=check_length("1234567890123456", policy)
assert check[0]==True
if check[0]==True:
    check1=True
print("PASS: checklength passed >15ch")

check=check_length("123456789012345", policy)
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checklength passed =15ch")

check=check_length("1234", policy)
assert check[0]==False
if check[0]==False:
    check3=False
print("PASS: checklength failed <15ch")

assert check1==True and check2==True and check3==False
print("PASS: !!checklength functioning")

#check_username
check1=True
check2=False
check=check_username('123','123')
assert check[0]==False
if check[0]==False:
    check1=False
print("PASS: checkusername failed user==pass")

check=check_username('123','223')
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checkusername passed user/=pass")

assert check1==False and check2==True
print("PASS: !! checkusername functioning")

#check_rotation
check1=False
check2=False
check3=True

check=check_rotation(6, policy)
assert check[0]==True
if check[0]==True:
    check1=True
print("PASS: checkrotation passes 'acceptable' =6mo")

check=check_rotation(5, policy)
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checkrotation passes 'excellent' =5mo")

check=check_rotation(13, policy)
assert check[0]==False
if check[0]==False:
    check3=False
print("PASS: checkrotation failed 'warning' >12mo")

assert check1==True and check2==True and check3==False
print("PASS: !! checkrotation functioning")

#check_breach
check1=True
check2=False

check=check_breach("password", known_breached)
assert check[0]==False
if check[0]==False:
    check1=False
print("PASS: checkbreach failed breached")

check=check_breach("notbreached", known_breached)
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checkbreach passed not breached")

assert check1==False and check2==True
print("PASS: !! checkbreach functioning")

#check policy
check1=False
check2=False

check=policy["strong_length"]==15
assert check==True
if check==True:
    check1=True
print("PASS: policy defines strong_length as 15")

check="require_digit" in policy
assert check==True
if check==True:
    check2=True
print("PASS: policy mentions digit")
      
assert check1==True and check2==True
print("PASS: !! policy okay")

#load_credentials
check1=False
check2=False

check=isinstance(credentials, list)
assert check==True
if check==True:
    check1=True
print("PASS: credentials returns list")

check="account" in credentials[0]
assert check==True
if check==True:
    check2=True
print("PASS: first credential is account")

assert check1==True and check2==True
print("PASS: !! loadcredentials functioning")

#load_breach
check1=False
check2=False

check=isinstance(known_breached, list)
assert check==True
if check==True:
    check1=True
print("PASS: knownbreached returns list")

check="password123" in known_breached
assert check==True
if check==True:
    check2=True
print("PASS: knownbreached contains password123")

assert check1==True and check2==True
print("PASS: !! loadbreached functioning")

#write_report
check1=False

write_report(checklines, "test_report.txt")
with open("test_report.txt", "r") as f:
    report_text=f.read()
check=report_text=="First test line\nSecond test line\n"
assert check==True
if check==True:
    check1=True
print("PASS: write_report saves the correct text")

assert check1==True
print("PASS: !! write_report functioning")

#save&loadsummary
check1=False
check2=False

checklines={"total": 7, "passed": 5, "failed": 2, "critical": 1, "failed_accounts": ["account1", "account2"], "critical_accounts": ["account3"]}
save_summary(checklines, "test_summary.json")
checklines2=load_summary("test_summary.json")
assert checklines2==checklines
if checklines2==checklines:
    check1=True
print("PASS: savesummary and loadsummary match inoutput")

check=isinstance(checklines2["failed_accounts"], list)
assert check==True
if check==True:
    check2=True
print("PASS: failedaccounts list")

check3=False

with open("test_summary.json", "r") as f:
    checklines2=f.read()
for cred in credentials:
    if cred["password"] in checklines2:
        check3=True

assert check3==False
print("PASS: summary does not contain passwords")

assert check1==True and check2==True and check3==False
print("PASS: !! savesummary and loadsummary functioning")
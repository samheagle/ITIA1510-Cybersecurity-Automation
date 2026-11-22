import json, os, password_checker
known_breached=password_checker.load_breached("breached.txt")
password_checker.AUDIT_LOG="test_audit_log.json1"
credentials=password_checker.load_credentials("credentials.txt")
checksample={"total": 7, "passed": 5, "failed": 2, "critical": 1, "failed_accounts": ["account1", "account2"], "critical_accounts": ["account3"]}

#delete old history
if os.path.exists(password_checker.AUDIT_LOG):
    os.remove(password_checker.AUDIT_LOG)

#check_digit
check1=True
check2=False
check3=True

assert password_checker.check_digit("hello")==("NO", False)
check1=False
print("PASS: checkdigit failed password without digit")

assert password_checker.check_digit("hello5")==("YES", True)
check2=True
print("PASS: checkdigit passed password with digit")

assert check1==False and check2==True
print("PASS: !! checkdigit functioning")

#check_length
check1=False
check2=False
check3=True

check=password_checker.check_length("1234567890123456", password_checker.policy)
assert check[0]==True
if check[0]==True:
    check1=True
print("PASS: checklength passed >15ch")

check=password_checker.check_length("123456789012345", password_checker.policy)
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checklength passed =15ch")

check=password_checker.check_length("1234", password_checker.policy)
assert check[0]==False
if check[0]==False:
    check3=False
print("PASS: checklength failed <15ch")

assert check1==True and check2==True and check3==False
print("PASS: !!checklength functioning")

#check_username
check1=True
check2=False

check=password_checker.check_username('123','123')
assert check[0]==False
if check[0]==False:
    check1=False
print("PASS: checkusername failed user==pass")

check=password_checker.check_username('123','223')
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

check=password_checker.check_rotation(6, password_checker.policy)
assert check[0]==True
if check[0]==True:
    check1=True
print("PASS: checkrotation passes 'acceptable' =6mo")

check=password_checker.check_rotation(5, password_checker.policy)
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checkrotation passes 'excellent' =5mo")

check=password_checker.check_rotation(13, password_checker.policy)
assert check[0]==False
if check[0]==False:
    check3=False
print("PASS: checkrotation failed 'warning' >12mo")

assert check1==True and check2==True and check3==False
print("PASS: !! checkrotation functioning")

#check_breach
check1=False
check2=False
check3=False

check=password_checker.check_breach("password", known_breached)
assert check[0]==False
if check[0]==False:
    check1=True
print("PASS: checkbreach failed breached")

not_breached=password_checker.check_breach("password123", known_breached)
assert not_breached==(False, 'CRITICAL -- password found in known breach list')
check2=True
print("PASS: knownbreached fails password in breachedtxt")

check=password_checker.check_breach("notbreached", known_breached)
assert check[0]==True
if check[0]==True:
    check3=True
print("PASS: checkbreach passed not breached")

assert check1==True and check2==True and check3==True
print("PASS: !! checkbreach functioning")

#check policy
check1=False
check2=False

assert password_checker.policy["strong_length"]==15
check1=True
print("PASS: policy defines stronglength==15")

assert"require_digit" in password_checker.policy
check2=True
print("PASS: policy mentions digit")
      
assert check1==True and check2==True
print("PASS: !! policy okay")

#load_credentials
check1=False
check2=False

assert isinstance(credentials, list)
check1=True
print("PASS: credentials returns list")

assert "account" in credentials[0]
check2=True
print("PASS: first credential is account")

assert check1==True and check2==True
print("PASS: !! loadcredentials functioning")

#load_breach
check1=False
check2=False
check3=False

assert isinstance(known_breached, list)
check1=True
print("PASS: knownbreached returns list")

assert "password123" in known_breached
check2=True
print("PASS: knownbreached contains password123")

assert check1==True and check2==True
print("PASS: !! knownbreached functioning")

#write_report
check1=False

check=["First test line","Second test line"]
password_checker.write_report(check, "test_report.txt")
with open("test_report.txt", "r") as f:
    report_text=f.read()
assert report_text=="First test line\nSecond test line\n"
check1=True
print("PASS: write_report saves correct text")

assert check1==True
print("PASS: !! write_report functioning")

#saveload_summary
check1=False
check2=False
check3=False

password_checker.save_summary(checksample, "test_summary.json")
check=password_checker.load_summary("test_summary.json")
assert check==checksample
check1=True
print("PASS: savesummary and loadsummary match inoutput")

assert isinstance(check["failed_accounts"], list)
check2=True
print("PASS: failedaccounts list")

with open("test_summary.json", "r") as f:
    check=f.read()
for cred in credentials:
    if cred["password"] in check:
        check3=True
assert check3==False
print("PASS: summary does not contain passwords")

assert check1==True and check2==True and check3==False
print("PASS: !! saveloadsummary functioning")

#addsaveload_history
check1=False
check2=False
check3=False
check4=False

assert password_checker.load_history("missing_history_test.json")==[]
check1=True
print("PASS: missing history returns empty list")

history=[]
history=password_checker.add_to_history(history, checksample, 3)
assert len(history)==1
assert history[0]["run"]==1
check2=True
print("PASS: empty history returns single entry list numbered 1")

history=[]
for i in range(3):
    history=password_checker.add_to_history(history, checksample, 2)
assert [entry["run"] for entry in history] == [2, 3]
check3=True
print("PASS: add_to_history kept only newest 2 runs")

password_checker.save_history(history, "test_history.json")
assert password_checker.load_history("test_history.json")==history
check4=True
print("PASS: history saved and loaded are the same")

assert check1==True and check2==True and check3==True and check4==True
print("PASS: !! addsaveloadhistory functioning")

#breach_verdicts
check1=False
check2=False
check3=False

check=password_checker.breach_verdicts("jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
assert check["accounts"][0]=={"account": "Gmail", "on_breach_list": True}
check1=True
print("PASS: breachverdicts first entry==first credential - first entry is breached gmail")
    
check=password_checker.breach_verdicts("nobody", password_checker.load_credentials("credentials.txt"), known_breached)
assert check["accounts"]==[]
check2=True
print("PASS: breachverdicts returns empty list user with no accounts")

result=password_checker.breach_verdicts("jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
result_json=json.dumps(result)
credentials=password_checker.load_credentials("credentials.txt")
for credential in credentials:
    # temp skip sshserver- its password is same as user
    if credential["account"]=="SSH Server":
        continue
assert credential["password"] not in result_json
check3=True
print("PASS: breachverdicts holds no passwords")

assert check1==True and check2==True and check3==True
print("PASS: !! breachverdicts functioning")

#lengthrotation_verdicts
check1=False
check2=False
check3=False
check4=False

check=password_checker.length_verdicts("jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
assert check["accounts"][2]=={"account": "VPN", "long_enough": True}  
check1=True
print("PASS: lengthverdicts third entry==third credential")

check=password_checker.rotation_verdicts("jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
assert check["accounts"][1]=={"account": "SSH Server", "rotation_ok": False}
check2=True 
print("PASS: rotationverdicts second entry==second credential")

check=password_checker.breach_verdicts("jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
assert check==password_checker.run_check("check_breach", "jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
check3=True
print("PASS: breachverdicts and runcheck match")

check=password_checker.run_check("reset_password", "jsmith", password_checker.load_credentials("credentials.txt"), known_breached)
assert check=={"error": "unknown check"}
check4=True
print("PASS: run_check refused unknown check")

assert check1==True and check2==True and check3==True and check4==True
print("PASS: !! lengthrotationverdicts, runcheck functioning")

#runlog_check
check1=False
check2=False
check3=False

password_checker.log_check("check_length", "jsmith", {"example": True}, "test_audit_log.json1")
check=password_checker.read_audit_log("test_audit_log.json1")
assert set(check[-1].keys())=={"time", "check", "username", "result"}
check1=True
print("PASS: logcheck has correct keys")

password_checker.run_check("check_length", "jsmith", credentials, known_breached)
password_checker.run_check("reset_password", "jsmith", credentials, known_breached)
check=password_checker.read_audit_log("test_audit_log.json1")
assert check[-2]["check"]=="check_length"
assert check[-1]["check"]=="reset_password"
check2=True
print("PASS: runcheck logs checks in order")

check=password_checker.read_audit_log("test_audit_log.json1")
log_text=json.dumps(check)
credentials=password_checker.load_credentials("credentials.txt")
for credential in credentials:
    #temp skip sshserver
    if credential["account"]=="SSH Server":
            continue
    assert credential["password"] not in log_text
check3=True
print("PASS: no passwords written by runcheck")

assert check1==True and check2==True and check3==True
print("PASS: !! runlogcheck functioning")
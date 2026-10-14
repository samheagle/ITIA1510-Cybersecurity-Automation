from password_checker import check_length, check_digit, check_username, check_rotation, check_breach, known_breached, policy 
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

check=check_breach("password")
assert check[0]==False
if check[0]==False:
    check1=False
print("PASS: checkbreach failed breached")

check=check_breach("notbreached")
assert check[0]==True
if check[0]==True:
    check2=True
print("PASS: checkbreach passed not breached")

assert check1==False and check2==True
print("PASS: !! checkbreach functioning")

#check policy
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
print("PASS: !! policy functioning")
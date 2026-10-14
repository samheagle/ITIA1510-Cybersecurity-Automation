<<<<<<< HEAD
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

=======
from password_checker import check_length, check_digit, check_username, check_rotation, check_breach, known_breached

##check_digit
check1=check_digit("hello")
assert check1==False
print("PASS: checkdigit failed password without digit")
check2=check_digit("hello5")
assert check2==True
print("PASS: checkdigit passed password with digit")
>>>>>>> 38af5084d81cc52f38dc3c876575dc52994b6e0a
assert check1==False and check2==True
print("PASS: !! checkdigit functioning")

#check_length
<<<<<<< HEAD
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
=======
check3=check_length("1234567890123456")
assert check3[0]==True
print("PASS: checklength passed >15ch")
check4=check_length("123456789012345")
assert check4[0]==True
print("PASS: checklength passed =15ch")
check5=check_length("123")
assert check5[0]==False
print("PASS: checklength failed <15ch")
assert check3[0]==True and check4[0]==True and check5[0]==False
print("PASS: !!checklength functioning")

#check_username
check6=check_username('123','123')
assert check6[0]==False
print("PASS: checkusername failed user==pass")
check7=check_username('123','223')
assert check7[0]==True
print("PASS: checkusername passed user/=pass")
assert check6[0]==False and check7[0]==True
print("PASS: !! checkusername functioning")

#check_rotation
check8=check_rotation(6)
assert check8[0]==True
print("PASS: checkrotation passes 'acceptable' =6mo")
check9=check_rotation(5)
assert check9[0]==True
print("PASS: checkrotation passes 'excellent' =5mo")
check10=check_rotation(13)
assert check10[0]==False
print("PASS: checkrotation failed 'warning' >12mo")
assert check8[0]==True and check9[0]==True and check10[0]==False
print("PASS: !! checkrotation functioning")

#check_breach
check11=check_breach("password")
assert check11[0]==False
print("PASS: checkbreach failed breached")
check12=check_breach("notbreached")
assert check12[0]==True
print("PASS: checkbreach passed not breached")
assert check11[0]==False and check12[0]==True
print("PASS: !! checkbreach functioning")
>>>>>>> 38af5084d81cc52f38dc3c876575dc52994b6e0a

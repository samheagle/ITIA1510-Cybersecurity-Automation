
from password_checker import check_length, check_digit, check_username, check_rotation

##check_digit
check1=check_digit("hello")
assert check1==False
print("PASS: checkdigit failed password without digit")
check2=check_digit("hello5")
assert check2==True
print("PASS: checkdigit passed password with digit")

#check_length
check3=check_length("1234567890123456")
assert check3[0]==True
print("PASS: checklength passed >15ch")
check4=check_length("123456789012345")
assert check4[0]==True
print("PASS: checklength passed =15ch")
check5=check_length("123")
assert check5[0]==False
print("PASS: checklength failed <15ch")

#check_username
check6=check_username('123','123')
assert check6[0]==False
print("PASS: checkusername failed user==pass")
check7=check_username('123','223')
assert check7[0]==True
print("PASS: checkusername passed user/=pass")

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

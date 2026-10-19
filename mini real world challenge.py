READ=1
DELETE=4
WRITE=2

userpermission=5

if userpermission & READ:
    print("read permission:yes")
else:
    print("readpermission:no")

if userpermission & WRITE:
    print("write permission:yes")
else:
    print("writepermission:no")

if userpermission & DELETE:
    print("delete permission:yes")
else:
    print("deletepermission:no")
 

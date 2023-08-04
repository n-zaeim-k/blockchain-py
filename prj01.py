#------------------ creating hash 256 ---------------
# import hashlib
# hash1=hashlib.sha256()
# hash1.update("welcome".encode("utf-8"))
# print(hash1.hexdigest())

#----------------- adding difficulty ---------------
# import hashlib
# i=0
# hash1=hashlib.sha256()
# hash1.update(str(i).encode("utf-8"))
# print(hash1.hexdigest())
# if int(hash1.hexdigest(),16)<2**(256-10):
#     print("hash is acceptable")
# else:
#     print("hash is not acceptable")

#------------------ finding correct hash -------------------
import hashlib
i=0
hash1=hashlib.sha256()
hash1.update(str(i).encode("utf-8"))

while int(hash1.hexdigest(),16) > 2**(256-20) :
    i+=1
    hash1.update(str(i).encode("utf-8"))

print(i)
print(hash1.hexdigest())

hash2=hashlib.sha256()
hash2.update(str(i).encode("utf-8"))
print(hash2.hexdigest())

    
    
    

    
    
    
    
    
    




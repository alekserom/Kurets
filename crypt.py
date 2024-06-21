import sys
import base64
if len(sys.argv) > 2:
   if str(sys.argv[1]) == 'crypt':
       print ('Encrypting')
       print (base64.b64encode(sys.argv[2].encode('ascii')).decode('utf-8'))
   elif  str(sys.argv[1]) == 'decrypt':
       print ('Decrypting')
       print (base64.b64decode(sys.argv[2].encode('utf-8')).decode('ascii'))       
   else: print ("Unknown command") 
else:
    print('Need 2 arguments')
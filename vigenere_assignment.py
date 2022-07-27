###############################################################################################################
########################################## Vienere Cipher #####################################################
###############################################################################################################
########################################### Global Variables ##################################################

alphabet= "abcdefghijklmnopqrstuvwyxz !.@#$%^&*()?,"
alphabet2= "-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-y-x-z- -!-.-@-#-$-%-^-&-*-(-)-?,"
from string import ascii_letters
alphabet3 = ascii_letters

################################################# Encryption Part of Code #####################################

plainText = input("What message do you want encrypted?").lower()
key = input("What do you want your cipher word to be?").lower()

kMath = key * 100
pMath = len(plainText)
newKey = kMath[:pMath]

crypt=""   
for ch in range(pMath):
    z = newKey[ch]
    p = plainText[ch]
    ki = alphabet.find(z)
    pti = alphabet.find(p)
    
    for ch in range(len(alphabet)):
        vs = alphabet[ch:] + alphabet[:ch]
        if vs[0] == z:
            crypt = crypt + vs[pti]
       
print("\n"+plainText + "  **Your Plain Text**")
print(newKey + "  **Your Key**")
print(crypt + "  **Your Encrypted Message**")

############################### Pointless Code / Aesthetics Only ###############################################

print("\n"  + "**This is the Vigenere Square to check code**")    
for ch in range(len(alphabet3)):
        vs = alphabet3[ch:] + alphabet3[:ch]
        #if vs[0] == "-":            
        print(vs)
            
########################################## Below is the Decryption ###########################################
            
code = input("What is the secret word?").lower()
encryptionText = input("What is encryted text?").lower()

cCode = code * 100
eMath = len(encryptionText)
newCode = cCode[:eMath]
decrypt=""   
for ch in range(eMath):
    c = newCode[ch]
    e = encryptionText[ch]
    
    for ch in range(len(alphabet)):
        vs = alphabet[ch:] + alphabet[:ch]
        if vs[0] == c:
            o = vs.find(e)            
            decrypt = decrypt + alphabet[o]

print("\n"+ encryptionText + "  **Your Encrypted Text**")
print(newCode + "  **Your secret word**")
print(decrypt + "  **Your decrypted Message**")

################################################# END #########################################################
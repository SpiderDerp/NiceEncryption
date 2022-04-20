class NiceEncryption:
    def __init__(self, string):
        self.string = string.lower()
        self.encrypted_string = ""
        self.decrypted_string = ""
    
    def encrypt(self):
        self.encrypted_string = ""
        for i in range(len(self.string)):
            # checks if letter
            if(i%2 == 0 and (ord(self.string[i]) < 123 and ord(self.string[i]) > 96)):
                if(ord(self.string[i]) + 6 > 122):
                    self.encrypted_string += chr(ord(self.string[i]) + 6 - 26)
                else:
                    self.encrypted_string += chr(ord(self.string[i]) + 6)
            elif(i%2 == 1 and (ord(self.string[i]) < 123 and ord(self.string[i]) > 96)):
                if(ord(self.string[i]) + 9 > 122):
                    self.encrypted_string += chr(ord(self.string[i]) + 9 - 26)
                else:
                    self.encrypted_string += chr(ord(self.string[i]) + 9)
            else:
                self.encrypted_string += self.string[i]
        
        return self.encrypted_string
    
    def decrypt(self):
        #decrypts the encrypted string
        self.decrypted_string = ""
        for i in range(len(self.encrypted_string)):
            if(i%2 == 0 and (ord(self.encrypted_string[i]) < 123 and ord(self.encrypted_string[i]) > 96)):
                if(ord(self.encrypted_string[i]) - 6 < 97):
                    self.decrypted_string += chr(ord(self.encrypted_string[i]) - 6 + 26)
                else:
                    self.decrypted_string += chr(ord(self.encrypted_string[i]) - 6)
            elif(i%2 == 1 and (ord(self.encrypted_string[i]) < 123 and ord(self.encrypted_string[i]) > 96)):
                if(ord(self.encrypted_string[i]) - 9 < 97):
                    self.decrypted_string += chr(ord(self.encrypted_string[i]) - 9 + 26)
                else:
                    self.decrypted_string += chr(ord(self.encrypted_string[i]) - 9)
            else:
                self.decrypted_string += self.encrypted_string[i]
        
        return self.decrypted_string


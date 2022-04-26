# NiceEncryption

A Python package that encrypts and decrypts a given string

**Tested Versions:** Python 3.8+ <br>
**Try it out here!** http://spiderderp.pythonanywhere.com

## Installation
```pip install NiceEncryption```

## Usage
```python
from NiceEncryption import NiceEncryption as ne

string = ne.NiceEncryption("this is nice encryption")

print("Encrypted String: " + string.encrypt())
print("Decrypted String: " + string.decrypt())
```

Output:
```
Encrypted String: zqob ry trin ntlxhvcoxt
Decrypted String: this is nice encryption
```

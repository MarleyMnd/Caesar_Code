# CAESAR'S ENCRYPTION
---
### Aim:
This algorithm is able to encrypt a message using Caesar's encryption method. It is also able to decrypt messages only if you know the right key associated with it.

### What is Caesar encryption?
The Caesar encryption method is really simple. You first have to take an alphabet and think about it as a loop (like if the next letter after Z was A, then B, etc.). Then, you will choose a key. This key will determine by how much you will shift letters. For example, if the key is 3, the encrypted alphabet will be:
| Basic | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Encrypted | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | a | b | c |

Without the key, nobody can read your message (on the paper).
Now, in order to decrypt the message, you must have the key in order to shift the alphabet the other way. That's where the key is important !

### Prerequisite:
I coded this algorithm using Python 3.11, please make sure your version of Python is able to run this algorithm.

### How do I make it work?
In order to encrypt a message, you need to run the "main.py" file. You will be asked to choose between to encrypt or to decrypt a message. Choose "encrypt". 
Then, you must provide the key of the encryption. This will tell the algorithm by how many letters it should shift the alphabet before rewriting the message.
Finally, in order to decrypt a message, you must provide the key and an encrypted message. The algorithm will instantly display the decrypted message.

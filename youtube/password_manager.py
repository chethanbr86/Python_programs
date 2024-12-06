# from cryptography.fernet import Fernet

#logic check
# def view(pwd):
#     print(f'Your password is {pwd}')

# def add(pwd):
#     pwd = input('Type in your new password: ').lower().strip()
#     print(f'Your new password is {pwd}')

#adding in txt and encrypting using pip install cryptography (find better library)
# def write_key(): #only once to be used and then comment it out
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file: #wb meams write in bytes
#         key_file.write(key)

# def load_key():
#     file = open('key.key', 'rb')
#     key = file.read()
#     file.close()
#     return key

# master_pwd = input('What is the master password? ')
# key = load_key() + master_pwd.encode()
# fer = Fernet(key)

# def view():
#     with open('passwords.txt', 'r') as f: 
#         for line in f.readlines():
#             data = line.rstrip() #rstrip is to delete extra line
#             user, passw = data.split("|") 
#             print("User:", user, "| Password:", str(fer.decrypt(passw.encode())).decode())

# def add():
#     name = input('Name: ')
#     pwd = input('Password: ')
#     with open('passwords.txt', 'a') as f: #3 modes: w is for rewrite, r is for read, a is for append
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')

#adding in dict
pass_dict = {}
def add():    
    name = input('Name: ')
    pwd = input('Password: ')
    pass_dict['name'] = name
    pass_dict['pwd'] = pwd

def view():
    print(f'Your name and password: {"*"*len(pass_dict.get("name"))}, {"*"*len(pass_dict.get("pwd"))}') #manual encryption
        
while True:
    mode = input('Type "A" for Adding or "V" for viewing password or "q" for quitting: ').lower().strip()
    if mode == 'q':
        break
    if mode == 'v':
        view()
    elif mode == 'a':
        add()
    else:
        print('Invalid mode!')
        continue

#encryption with crytography is not working and hence using dict for now. Find a better encryption method.
#Cryptography has been uninstalled.
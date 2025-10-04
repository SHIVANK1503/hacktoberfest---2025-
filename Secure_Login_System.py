import os
def login_system(login_attempts):    
    def secure_login(username, password):
        if username in users and users[username] == password:
            login_attempts['success'] += 1
            return f"Welcome, {username}!"
        else:
            login_attempts['failed'] += 1
            return f"Failed login attempt for {username}"

    def get_login_attempts():
        return login_attempts

    return secure_login, get_login_attempts


def check_credentials(username, password):
    return username in users and users[username] == password

# Driver Code
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    login_attempts = {'success': 0, 'failed': 0}  # Initialize login attempt counts
    num_all = int(input())
    users = {}
    for i in range(num_all):
        user, pwd = input().split(',')
        users[user] = pwd
    num = int(input())
    login, get_attempts = login_system(login_attempts)
    
    for i in range(num):
        user, password = input().split(",")
        fptr.write(login(user, password) + "\n")

    attempts = get_attempts()
    fptr.write(f"Login Attempts - Successful: {attempts['success']} Failed: {attempts['failed']}")
    fptr.close()

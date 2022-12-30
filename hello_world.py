def emailProcess(email):
    email_username = email[0:email.index("@")]
    email_01 = email[email.index("@")+1:]
    return [email_username, email_01] 
def printMsg(email_username, email_01):
    print(f"Username is {email_username}; Email Domain is {email_01}")
def main():
    email = input("Mời nhập địa chỉ email: ").strip()
    email_username, email_01 = emailProcess(email)
    printMsg(email_username, email_01)
if __name__ == "__main__":
    main()
from hello_world import emailProcess, printMsg
def main():
    emails=['huy@gmail.com', 'youtube@edu.com','ute@gmail.com']
    for i in emails:
        username, email_01 = emailProcess(emails)
        printMsg(username, email_01)


if __name__ == "__main__":
    main()
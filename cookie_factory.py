def load_credentials():
    logins = {}
    with open("./accounts/accounts.txt", "r") as file:
        data = ''.join([line.replace('\n', ',') for line in file.readlines()])
        temp = data.split(',')
    for account in temp:
        logins[account.split(':')[0]] = account.split(':')[1]
    return logins


def cookie_factory():
    creds = load_credentials()
    for e in creds:
        email = str(e)
        password = str(creds[e])
        print(email, password)
    return 0


cookie_factory()

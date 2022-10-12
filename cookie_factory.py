def load_credentials():
    logins = {'amajidbac@gmail.com': 'AMAJID2001@'}
    return logins



def cookie_factory():
    creds = load_credentials()
    for e in creds:
        email = str(e)
        password = str(creds[e])
        print(f"{email}:{password}")
    return 0

cookie_factory()




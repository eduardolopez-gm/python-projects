# collect email from user
# split email using @ as user + domain
# split domain using .

def main():
    print('Welcome to email slicer' + '\n')

    email_input = input('Please, enter an email address: ')

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: " + username)
    print("Domain: " + domain)
    print("Extension: " + extension)


main()

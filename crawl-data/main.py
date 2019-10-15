from crawler.facebook.images.all_photos import AllPhoto

with open('credentials.txt') as f:
    email = f.readline().split('"')[1]
    password = f.readline().split('"')[1]

    if not (email and password):
        print("Your email or password is missing. Kindly write them in credentials.txt")
        exit()

abc = AllPhoto(email, password)
abc.login()
abc.execute_script("https://www.facebook.com/profile.php?id=100007770918742")
abc.quit()
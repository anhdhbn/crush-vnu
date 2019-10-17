# from crawler.facebook.crawl_all import AllFacebook

# with open('credentials.txt') as f:
#     email = f.readline().split('"')[1]
#     password = f.readline().split('"')[1]

#     if not (email and password):
#         print("Your email or password is missing. Kindly write them in credentials.txt")
#         exit()

# abc = AllFacebook(email, password)
# if abc.login() is True:
#     abc.execute_script("https://www.facebook.com/profile.php?id=100007770918742")

# abc.quit()
from crawler.proxies.updateproxies.easy import EasyUpdate

temp = EasyUpdate()
temp.execute_script()
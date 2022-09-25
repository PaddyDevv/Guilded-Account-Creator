import time
import requests
import random
import httpx
import threading
from threading import Thread


def d():

    INVITE = '27dP3m4k'
    BioTEXT = 'SnoopGen OP'

    infos = requests.get('https://random-data-api.com/api/v2/users')
    password = infos.json()['password']
    username = infos.json()['username']
    FIRSTNAME = infos.json()['first_name']
    LASTNAME = infos.json()['last_name']
    FULLNAME = f"{FIRSTNAME} {LASTNAME}"
    email = f'{FIRSTNAME}.{LASTNAME}@gmail.com'
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Password: {password}")

    url = 'https://www.guilded.gg/api/users?type=email'

    json = {
        "name":
        username,
        "email":
        email,
        "password":
        password,
        "fullName":
        f"{FULLNAME}",
        "profilePicture":
        "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/c41f9b4c08f98da63ab2015f29dbca59-Large.webp?w=450&h=450"
    }

    r = requests.post(url, json=json)
    print(r.text)
    UserID = r.json()['user']['id']
    Hmac = r.cookies["hmac_signed_session"]
    print(f"Got Cookie : {Hmac}")

    session = requests.Session()
    session.headers = {"cookie": f"hmac_signed_session={Hmac}"}
    resp = session.put(f"https://www.guilded.gg/api/invites/{INVITE}")

    Bio = requests.Session()
    Bio.headers = {"cookie": f"hmac_signed_session={Hmac}"}
    BioJSON = {"userId": UserID, "aboutInfo": {"bio": BioTEXT}}
    resp = session.put(f"https://www.guilded.gg/api/users/{UserID}/profilev2",
                       json=BioJSON)

    CookiesFile = open('cookies.txt', 'a+')
    CookiesFile.write(f'{Hmac}\n')
    print("[!] Waiting 15 Seconds To Avoid Being Banned By Guilded Anti Bot!")
    time.sleep(15)
    print("[+] Waited!")
    d()






def main():
  print("Welcome To Patricks Guilded Botter!")
  print("-----------------------------------")
  print("If You Enjoy This Please Star The Github! https://github.com/SnoopDeveloper/Guilded-Account-Creator")
  print("----------------------------------------------------------------------------------------------------")
  print("Also Join THe Discord! https://discord.gg/7DyVxDpfmR")
  print("----------------------------------------------------")

  print("Starting Guilded Generator!")
  time.sleep(7)
  d()

main()
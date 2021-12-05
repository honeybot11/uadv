import os
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet

colorama.init()
print(colorama.Fore.YELLOW)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('TECH'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('VISION'))
f = pyfiglet.Figlet(font='digital')
print (f.renderText('NonStop Advertisement'))
dec = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' 
print("""
Youtube:
https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg

Discord Server:
https://discord.gg/YMfvAxm6zF
""")
print(dec)

import amino
import threading
import concurrent.futures
client = amino.Client()
lists=[]
cmlink=[]

xd=open('msg.txt','r')
admsg=(xd.read())

t = open('cm.txt','r')
for m in t.read().splitlines():
    temp=m

    lists.append(str(temp))
t.close

for i in lists:
	try:
		fok=client.get_from_code(i)
		cid=fok.path[1:fok.path.index("/")]
		cmlink.append(cid)
	except:
		print("Invalid links")


email = input("\nEnter Email: ")
password = input("\nEnter Password: ")
client.login(email = email, password = password)
print("\nLogged in")
	
for cid in cmlink:
	try:
		client.join_community(cid)
		subclient =amino.SubClient(comId = cid,profile=client.profile)
		os = subclient.get_all_users()
		print(f"\nAdvertisement Started in {cid}")
		for nickname, s in zip(os.profile.nickname,os.profile.userId):
			try:
				subclient.start_chat(userId = str(s), message = admsg)
				print("Advertised to", nickname, str(s))
			except Exception:
				pass
	except Exception as e:
		print(e)
	print(f"\nAdvertised in {cid}")
	
print("\nAdvertisement done")
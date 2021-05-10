"""
自分で書いた部分！よくできたよ！
i = 3
while True:
	pw = input("Please input password.")
	if pw == "a123456":
		print("Success!")
		break
	else:
		i = i - 1
		print("Wrong password,you can try",int(i),"time")

		if i == 0 :
			break
"""
i = 3
password = "a123456"
while i > 0:
	i = i - 1
	pw = input("Please input password.")
	if pw == password:
		print("Success!")
		break
	else:	
		print("Wrong password,you can try",i,"time")
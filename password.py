x = 3
while True:
	x = x - 1
	password = input('請輸入密碼：')

	if x == 0:
		print('密碼錯誤已達上限')
		break
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤！還有', x, '機會')

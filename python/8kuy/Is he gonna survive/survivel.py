def hero(bullets, dragons):
	survive = bullets/dragons
	print(survive)
	answer=None
	if survive>=2:
		answer=survive
	print(bool(answer))
	return bool(answer)



hero(10, 5)
hero(7, 4)
hero(4, 5)
hero(100, 40)
hero(1500, 751)
hero(0, 1)
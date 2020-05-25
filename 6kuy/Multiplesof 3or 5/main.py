def solution(number):
	sum = 0
	for x in range(number):
		if x%3==0 or x%5==0:
			print(x)
			sum = sum+x
	print(sum)		
	return

solution(10)
solution(15)
solution(20)
solution(25)
solution(30)
solution(35)
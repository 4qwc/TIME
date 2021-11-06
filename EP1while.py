import time


def TIME():
	h = 0
	m = 0
	s = 0
	while True:
		s +=1
		
		time.sleep(1)
		if s==60:
			s=0
			m +=1
		elif s==60:
			m=0
			h+=1
		elif h==23:
			h=0
															
		print('TIME: {}:{}:{}'.format(h,m,s))


TIME()		

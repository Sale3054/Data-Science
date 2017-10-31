def f2(character):
	random = np.random.randint(len(createNameList()))
	aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(len(aList)):
		if(aList[i] == character):
			return i*random

x = f2('a')
print(x)
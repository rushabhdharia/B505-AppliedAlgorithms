#!/usr/bin/env python3

def main():
	list_num = [0.1, 1.1, 1.2, 1.3, 1.8, 2.30]
	total = len(list_num)
	i = 0
	main_list = []
	while i < total:
		temp_list = []
		temp_max = list_num[i]+1
		while list_num[i] <= temp_max:
			temp_list.append(list_num[i])
			i+=1
			if(i==total):
				break
		main_list.append(temp_list)
	print(main_list)

	pass

if __name__ == '__main__':
	main()
import random

def gen(numbers):
	f = open('numbers.txt', 'w')
	for i in range(int(numbers)):
		country_code = '+79'
		phone_number = ''.join(random.choices('0123456789', k=9))
		formatted_phone_number = f'{country_code}{phone_number}'
		i += 1
		print(f'[{i}] {formatted_phone_number} t.me/DefuseSliv')
		f.write(f'{formatted_phone_number}\n')
	f.close()

gen(input('Кол-во номеров: '))
input('\nГотово! Все номера сохранены в numbers.txt!')
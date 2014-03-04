def what_is_my_sign(day, month):
	signs = []
	signs.append(['Capricorn', 1, range(1,21)])
	signs.append(['Aquarius', 1, range(21,32)])
	signs.append(['Aquarius', 2, range(1,20)])
	signs.append(['Pisces', 2, range(20,29)])
	signs.append(['Pisces', 3, range(1,21)])
	signs.append(['Aries', 3, range(21,32)])
	signs.append(['Aries', 4, range(1,21)])
	signs.append(['Taurus', 4, range(21,31)])
	signs.append(['Taurus', 5, range(1,22)])
	signs.append(['Gemini', 5, range(22,32)])
	signs.append(['Gemini', 6, range(1,22)])
	signs.append(['Cancer', 6, range(22,31)])
	signs.append(['Cancer', 7, range(1,23)])
	signs.append(['Leo', 7, range(23,32)])
	signs.append(['Leo', 8, range(1,23)])
	signs.append(['Virgo', 8, range(23,32)])
	signs.append(['Virgo', 9, range(1,24)])
	signs.append(['Libra', 9, range(24,31)])
	signs.append(['Libra', 10, range(1,24)])
	signs.append(['Scorpio', 10, range(24,32)])
	signs.append(['Scorpio', 11, range(1,23)])
	signs.append(['Sagittarius', 11, range(23,31)])
	signs.append(['Sagittarius', 12, range(1,22)])
	signs.append(['Capricorn', 12, range(22, 32)])

	for sign in signs:
		if sign[1] == month and day in sign[2]:
			return sign[0]

print what_is_my_sign(22,10)

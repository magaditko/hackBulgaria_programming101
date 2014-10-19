def what_is_my_sign(day, month):
    sheet = [
        #['Capricorn', 356,19],
        ['Aquarius', 20, 49],
        ['Pisces', 50, 79],
        ['Aries', 80, 110],
        ['Tauros', 111, 141],
        ['Gemini', 142, 172],
        ['Cancer', 173, 204],
        ['Leo', 204, 234],
        ['Virgo', 235, 265],
        ['Libra', 266, 295],
        ['Scorpio', 296, 325],
        ['Sagittarius', 326, 355]
]
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = day
    for number in range(month - 1):
        date += month_length[number]

    for z_sign in sheet:
        if date >= z_sign[1] and date <= z_sign[2]:
            return(z_sign[0])
        elif date >= 356 or date <= 19:
            return "Capricorn"

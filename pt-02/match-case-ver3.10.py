# match-case czyli switch dziala w pythonie 3.10 +

def week_day(day):
    match day:
        case 1: return "poniedzialek"
        case 2: return "wtorek"
        case 3: return "sroda"
        case 4: return "czwartek"
        case 5: return "piatek"
        case 6: return "sobota"
        case 7: return "niedziela"
        case _ : return "niepoprwany dzien"
print(week_day("pizza"))
print(week_day(6))

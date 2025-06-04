initial_capital = float(input("How much are you investing? "))
rate = input("What is the yearly interest rate? (in percent) ")
years = int(input("How many years? "))

rate = float(rate) / 100

capital = initial_capital

if years <= 10:
    # Mostrar para cada año
    for year in range(1, years + 1):
        beginning_of_year = capital
        capital *= (1 + rate)
        revenue_this_year = capital - beginning_of_year
        print(f"Year {year:2d}: Total = {capital:.2f}, Revenue this year = {revenue_this_year:.2f}")
else:
    # Solo mostrar cada 5 años, y también en el año final aunque no sea múltiplo de 5
    for year in range(1, years + 1):
        beginning_of_year = capital
        capital *= (1 + rate)
        if year % 5 == 0 or year == years:
            revenue_this_year = capital - beginning_of_year
            print(f"Year {year:2d}: Total = {capital:.2f}, Revenue this year = {revenue_this_year:.2f}")
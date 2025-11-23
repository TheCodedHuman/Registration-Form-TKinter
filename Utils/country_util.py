def getCountries(asc: bool = True) -> list[str]:

    with open("Assets/countries.txt", "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    countryList = [line.strip(" \n\r\t,") for line in lines if line.strip()]

    if not asc:
        return countryList
    
    return sorted(countryList)

if __name__ == '__main__':
    contryList = getCountries()
    for i, c in enumerate(contryList[:10], start=1):
        print(i, c)



def main():
    fp = open("Exchrate.txt", 'r')
    country = input("Enter the country you are searching for: ")
    country = country.lower()
    for line in fp:
        line = line.strip()
        values = line.split(',')
        values[0] = values[0].lower()
        if values[0] == country:
            print(country,"\nCurrency: \t", values[1], "\nExchange Rate: \t", values[2])
        else:
            continue

main()

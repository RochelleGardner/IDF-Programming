items = [["Pants", 10, 19.99, "Just some pants"],\
        ["Shirt", 15, 12.50, "A plain shirt"], \
        ["Dress", 3, 79.00, "There's no way that dress is gonna fit"], \
        ["Socks", 50, 1.00, "Colorful mismatched socks"], \
        ["Sweater", 5, 49.99, "That sweater looks itchy"]]

def main():
    for row in items:
        print ("".join(map(str,row)))

main()
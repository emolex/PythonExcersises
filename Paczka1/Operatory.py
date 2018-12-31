a=2**5
koala = "koala\n"
print(a)
print(koala*10)

parzyste = [2,4,6,8,10]
nieparzyste = [1,3,5,7,9]
parzyste_i_nieparzyste = parzyste + nieparzyste
print(parzyste_i_nieparzyste)

x_tab = ["x"]*10
y_tab = ["y"]*10
print(len(parzyste_i_nieparzyste))

if x_tab.count("x")==10 and y_tab.count("y")==10:
    print("Zgadza sie!")
    if len(parzyste_i_nieparzyste)>=10:
        print("Jest równo lub więcej niz 10 elementow")
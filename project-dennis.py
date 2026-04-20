import random  

rng_input = input("Input apa saja")
rng = random.randint(0, 999)

def bad_prediction():
    if rng == 666:
        return "YOU ARE DEMON! BEGONE!"
    elif rng == 13:
        return "SHALL THE UNFORTUNATE THINGS HAPPEN TO YOU!"
    elif rng == 4:
        return 
    else: pass

def good_prediction():
    if rng == 777:
        return "SHALL YOUR LIFE BLESSED WITH THE MOST FORTUNATE FATE!"
    else: pass

if rng == 666 or 13 or 4:
    print(bad_prediction)
elif rng == 777:
    print(good_prediction)
else: print("MEH, YOU ARE A PEASANT, LOWLY AVERAGE PEASANT!")

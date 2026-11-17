def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # 1. Pehle $ ka sign hatayein (.replace use kar ke)
    # 2. Phir usay float (decimal number) me badlein
    d_without_sign = d.replace("$", "")
    return float(d_without_sign)


def percent_to_float(p):
    # 1. Pehle % ka sign hatayein
    # 2. Phir number ko float me badal kar 100 se divide karein (kyunke percentage 100 me se hoti hai)
    p_without_sign = p.replace("%", "")
    return float(p_without_sign) / 100


# Is line ko mat cherein, yeh program start karti hai
if __name__ == "__main__":
    main()

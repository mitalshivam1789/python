
while True:
    try:
        age = int(input("tell your age or year of birth "))
        age_prediction = int(input("predict your age for the year "))

        if age < 100:
            year = 2019 + (100 - age)
            print("you will be of 100 at ", year)
            if age_prediction > (year-100):
                pridic_age = age_prediction - (year - 100)
                print(f"age at {age_prediction} is ", pridic_age)
            else:
                print(age_predicton + " is a wrong choice")

        elif age > 1920 and age < 2019:
            year = age + 100
            print("you will of 100 at ", year)
            if age_prediction > (year - 100):
                pridic_age = age_prediction - (year - 100)
                print(f"age at {age_prediction} is ", pridic_age)

        elif age > 1890 and age < 1920:
            print("your age is above 100")

        elif age > 2019:
            print("you haven't born yet")

        else:
            print("you are not of this world.")

    except Exception as e:
        print(e)
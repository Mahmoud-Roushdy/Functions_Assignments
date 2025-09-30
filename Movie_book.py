Today_movies = {
    "Inception": {
        "Times": ["9 pm", "12 overnight"],
    },
    "The Matrix": {
        "Times": ["3 pm", "6 pm"],
    },
    "The Dark Night": {
        "Times": ["6 pm", "12 overnight"],
    },
    "Equalizer": {
        "Times": ["6 pm", "9 pm"],
    },
}


def movie_available():

    print("Today's movies:")
    index = 1
    for key, value in Today_movies.items():
        print(f"-{index} {key}: ")
        index += 1
        for info, data in value.items():
            print(f"{info} => {data}")
    print("please note there are vip tickets with hace extra fees (5$)!")


def Customer_choices():
    seats = input("How many seats: ")
    Seat_type = input("Do you would like  vip seats?: yes or no ")
    return seats, Seat_type


def calculate_bill():
    client_choices = Customer_choices()


def calculate_bill():
    # customer_choices return a Tuple with two indgers; the first one represent
    # the seats and the second represent the seat type.
    client_choices = Customer_choices()
    bill = 0
    seats = int(client_choices[0])
    vip = client_choices[1]
    bill = 15 * seats
    if vip == "yes":
        bill += 5 * seats
    return bill


movie_available()
print("#" * 30)
movie_num = input("number of your movie choice: ")
# print(Customer_choices())
print("Just a moment .....")
total_bill = calculate_bill()


def receipt():
    if movie_num == "1":
        print("you moive is Inception")
    elif movie_num == "2":
        print("your movie is The Matrix")
    else:
        print("you moive is unknown")
    print(f"your total bill is {total_bill}")


print("Just a moment .....")
print("Just a moment ........")
print("Just a moment ...........")

receipt()

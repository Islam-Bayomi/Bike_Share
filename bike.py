import pandas as pd


# Creating a dictionary containing the data for the three cities
bike_s = {"chicago": "chicago.csv",
          "washington": "washington.csv", 
          "new york": "new_york_city.csv"}


# Function to take user input to filter data
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    city, month, day = input(
    "please specify a city , month like (Jan) to filter by or all , day like (Mon) to filter by or all"
    ).lower().split(",")

    cities = ("chicago", "washington", "new york")
    months = ("jan", "feb", "mar", "apr", "may", "jun", "all")
    days = ("sat", "sun", "mon", "tue", "wed", "thu", "fri", "all")

    try:

        if city not in cities:
        
            raise ValueError("Oops! That was not valid city select one from chicago,washington and new york")

        if month not in months:
            
            raise ValueError("Oops! That was not valid month input Try again ..")

        if day not in days:
            
            raise ValueError("Oops! That was not valid day input Try again..")

        return city,month,day

    except ValueError as e:
        print(e)
        main()


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # choose city
     
    df = pd.read_csv(bike_s[city])

    # change start time to date time format 

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # change month format

    df["month"] = df["Start Time"].dt.month

    month_n = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6}

    # filter by month or all

    if month != "all":

        
        df = (df[df["month"] == month_n[month]])
        

    if month == "all":

         df = df

    #  change day format

    df["day"] = df["Start Time"].dt.dayofweek
    
    day_n = {"mon":0,"tue":1,"wed":2,"thu":3,"fri":4,"sat":5,"sun":6}

    # filter per day or all

    if day != "all":

        df = (df[df["day"] == day_n[day]])

    if day == "all":

        df = df

    return df 


# Function to calculate all the time-related statistics for the filterd data

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    # display the most frequent month

    most_frequent_month = df["month"].mode()[0]
    
    print("\n most frequent month is {}".format(most_frequent_month))

    # display the most frequent day

    most_frequent_day = df["day"].mode()[0]

    print("\n most frequent day is {}".format(most_frequent_day))

    # display the most frequent hour

    df["hour"] = df["Start Time"].dt.hour


    most_frequent_hour = df["hour"].mode()[0]


    print("\n most frequent hour is {}".format(most_frequent_hour))

# Function to calculate station related statistics

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    # display the most popular start station

    most_popular_StartStation = df["Start Station"].mode()[0]

    print("\n most popular Start Station is {}".format(most_popular_StartStation))

    # display the most popular end station

    most_popular_EndStation = df["End Station"].mode()[0]

    print("\n most popular End Station is {}".format(most_popular_EndStation))

    # display the most popular trip 

    most_popular_trip = df.groupby(["Start Station","End Station"]).size().sort_values(ascending=False).head(1)


    print("\n most popular trip is between : \n {}".format(most_popular_trip))

# Function for trip duration related statistics

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    total_trip_duration = df["Trip Duration"].sum()

    print("\n total trip duration equal {}".format(total_trip_duration))
    
    Average_trip_duration = df["Trip Duration"].mean()

    print("\n Average trip duration equal {}".format(Average_trip_duration))
    

# Function to calculate user statistics

def user_stats(df,city):

    """Displays statistics on bikeshare users."""

    # count each user type

    print("\ncount of each user type : \n{}".format(df["User Type"].value_counts()))

    # check if city has gender data and count of each user gender

    if  city in ("chicago","new york"):

        print("count of each user gender : \n{}".format(df["Gender"].value_counts()))

        # count of males


        df_male=df.groupby("User Type")["Gender"].apply(
            lambda x: (x=="Male").sum()).reset_index(name="male count")

        print ("\n count of male user type is : \n {}".format(df_male))

        # count of females

        df_female=df.groupby('User Type')['Gender'].apply(
            lambda x: (x=='Female').sum()).reset_index(name='female count')

        print ("\n count of female user type is : \n{}".format(df_female))

    # calculate the earliest birth year

        print ("\n oldest user was born at : {} ".format(int(df["Birth Year"].min())))

    # calculate the most recent birth year

        print ("\n youngest user was born at : {} ".format(int(df["Birth Year"].max())))

    # calculate the most common birth year

        print ("\n most common birth year is : {} \n".format(int(df["Birth Year"].mode()[0])))

# Function to display the data frame 

def display_data(df):

    """Displays 5 rows of data from the csv file for the selected city."""

    print("there is 5 rows of data from selected city : \n {}".format(df.head()))

def main():

    while True:
    
        city, month, day = get_filters()
        df=load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
    
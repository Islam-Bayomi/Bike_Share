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



def main():

    while True:
    
        city, month, day = get_filters()
        df=load_data(city, month, day)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
    
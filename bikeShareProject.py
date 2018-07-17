import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please Enter name of City (Choose between chicago, new york city, washington): ').lower()
        if city.lower() == 'chicago':
            break
        elif city.lower() == "new york city":
            break
        elif city.lower() == "washington":
            break
        else:
            print('Invalid Input - Please enver valid City Name.')
            continue
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please Enter Month (Enter All to include data for all months) ').lower()
        if month.lower() == 'january':
            break
        elif month.lower() == 'february':
            break
        elif month.lower() == 'march':
            break
        elif month.lower() == 'april':
            break
        elif month.lower() == 'may':
            break
        elif month.lower() == 'june':
            break
        elif month.lower() == 'all':
            break
        else:
            print('Invalid Input - Please enter a valid month.')
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please Enter Day (Enter All to include data for all days) -  ').lower()
        if day.lower() == 'monday':
            break
        elif day.lower() == 'tuesday':
            break
        elif day.lower() == 'wednesday':
            break
        elif day.lower() == 'thursday':
            break
        elif day.lower() == 'friday':
            break
        elif day.lower() == 'saturday':
            break
        elif day.lower() == 'sunday':
            break
        elif day.lower() == 'all':
            break
        else:
            print('Invalid Input. Please check your Spelling.')
            continue


    print('-'*40)
    print('Calculating...')
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode() [0]
    print('The most common Month is :', month)
    # display the most common day of week
    dayOfWeek = df['day_of_week'].mode() [0]
    print('The most common day of the week is :', dayOfWeek)

    # display the most common start hour
    hour = df['hour'].mode() [0]
    print('The most common hour is :', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    startStation = df['Start Station'].mode() [0]
    print('The most common Start Station is :', startStation)

    # display most commonly used end station [STIMMT SO NOCH NICHT]
    endStation = df['End Station'].mode() [0]
    print('The most common End Station is :', endStation)

    # display most frequent combination of start station and end station trip
    frequent = (df['Start Station']+df['End Station']).mode()[0]
    print(frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTravelTime = df['Trip Duration'].sum()

    # display mean travel time
    meanTravelTime = df['Trip Duration'].mean()
    print("Total Travel Time is : ", totalTravelTime)
    print("Mean Travel Time is : ", meanTravelTime)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    userTypes = df['User Type'].value_counts()
    # Display counts of gender
    if 'Gender' in df.columns:
        genderCount = df['Gender'].value_counts()
        print(genderCount)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birthYear = df['Birth Year'].min()
        recentDate = df['Birth Year'].max()
        commonDate = df['Birth Year'].mode()
        print("Earliest BirthDate is : ", birthYear)
        print('-'*40)
        print("Most recent BirthDate is : ", recentDate)
        print('-'*40)
        print("Most common BirthDate is : ", commonDate)
        print('-'*40)
    print(userTypes)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays the data used to compute the stats
    Input:
        the dataframe with all the bikeshare data
    Returns:
       none
    """

    df = df.drop(['month', 'day_of_week', 'hour'], axis = 1)

    rowIndex = 0

    displayData = input("\n View Raw Data ? (yes/no) \n").lower()

    while displayData == 'yes':

        print(df[rowIndex: rowIndex + 5])
        rowIndex = rowIndex + 5
        displayData = input("\n View 5 more rows of raw data? (yes/no) \n").lower()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

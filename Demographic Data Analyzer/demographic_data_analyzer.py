import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men_data = df[df["sex"] == "Male"]

    average_age_men = round(men_data["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # Use boolean indexing to filter the dataset by education level
    bachelors_data = df[df["education"] == "Bachelors"]

    # Calculate the proportion of the filtered dataset to the total dataset
    percentage_bachelors = round(len(bachelors_data) / len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # Use boolean indexing to filter the dataset by education level and salary
    higher_education = df[(df['education'] == "Bachelors") |
                          (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    lower_education = df[(df["education"] != "Bachelors") &
                         (df["education"] != "Masters") & (df["education"] != "Doctorate")]

    higher_education_data = higher_education[higher_education['salary'] == ">50K"]
    lower_education_data = lower_education[lower_education['salary'] == ">50K"]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education_data) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education_data) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_data = df[df["hours-per-week"] == min_work_hours]

    num_min_workers = len(min_hours_data[min_hours_data["salary"] == ">50K"])

    rich_percentage = (num_min_workers / len(min_hours_data)) * 100

    # What country has the highest percentage of people that earn >50K?
    # Group the data by country and salary, and count the number of people in each group
    grouped = df.groupby(["native-country", "salary"])["age"].count()

    # Calculate the total number of people in each country
    total_by_country = grouped.groupby(level=0).sum()

    # Calculate the percentage of people in each country who earn more than 50K
    percent_over_50k = (grouped.loc[:, ">50K"] / total_by_country) * 100

    # Get the name of the country with the highest percentage
    highest_earning_country = percent_over_50k.idxmax()
    # Get the highest percentage itself
    highest_earning_country_percentage = round(percent_over_50k.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]

    # Group the India high-income dataset by occupation
    grouped = india_high_income.groupby('occupation')

    # Count the number of people in each occupation
    occupation_counts = grouped['occupation'].count()

    top_IN_occupation = occupation_counts.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

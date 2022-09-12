#Keywords to detect
searching = ['looking', 'trying to find', 'searching for']
colors = ['white', 'black', 'gray', 'grey', 'silver', 'red', 'blue', 'brown', 'green', 'beige', 'orange', 'gold', 'yellow', 'purple', ]
car_brands = ['abarth', 'alfa romeo', 'aston martin', 'audi', 'bentley', 'bmw', 'bugatti', 'cadillac', 'chevrolet', 'chrysler', 'citroën', 'dacia', 'daewoo', 'daihatsu', 'dodge', 'donkervoort',
'ds', 'ferrari', 'fiat', 'fisker', 'ford', 'honda', 'hummer', 'hyundai', 'infiniti', 'iveco', 'jaguar', 'jeep', 'kia', 'ktm', 'lada', 'lamborghini', 'lancia', 'land rover', 'landwind', 'lexus', 
'lotus', 'maserati', 'maybach', 'mazda', 'mclaren', 'mercedes-benz', 'mg', 'mini', 'mitsubishi', 'morgan', 'nissan', 'opel', 'peugeot', 'porsche', 'renault', 'rolls-royce', 'rover', 'saab',
'seat', 'skoda', 'smart', 'ssangyong', 'subaru', 'suzuki', 'tesla', 'toyota', 'volkswagen'] 
years = ['1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', 
'1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', 
'1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', 
'1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
car_type = ['hatchback', 'sedan', 'suv', 'muv', 'coupe', 'convertible', 'pickup truck', 'pickup', 'truck']

#First Message
print("-----------------------------------------------------\nHello! If you have any troubles, please message here.\n-------------------\|/-----\|/-----------------------")
#Input
user = input("Message: ")

if any(ele in user.lower() for ele in searching):
    print("Please answer a short survey to find your desired car:")

    survey_question_1 = input("\nWhat color is the car: ")

    if any(ele in survey_question_1.lower() for ele in colors):
        survey_question_1 = survey_question_1.lower()

    else:
        survey_question_1 = "null"

    survey_question_2 = input("\nWhat brand is the car: ")

    if any(ele in survey_question_2.lower() for ele in car_brands):
        survey_question_2 = survey_question_2

    else:
        survey_question_2 = "null"

    survey_question_3 = input("\nWhat year is the car: ")

    if any(ele in survey_question_3 for ele in years):
        survey_question_3 = survey_question_3

    else:
        survey_question_3 = "null"

    survey_question_4 = input("\nWhat type of car is it: ")

    if any(ele in survey_question_4 for ele in car_type):
        survey_question_4 = survey_question_4.lower()

    else:
        survey_question_4 = "null"

    print(survey_question_1)
    print(survey_question_2)
    print(survey_question_3)
    print(survey_question_4)

else:
    print("Please check spelling and try again...")
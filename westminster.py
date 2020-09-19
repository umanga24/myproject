from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open("westminster_csvfile.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Course", "Category", "Degree", "Duration", "Mode", "Intake", "Course Link", "Location", "Domestic Fees", "International Fees", "Course Summery", "Course Structure", "Careers", "Discount"])

for i in range(0,1):
    url = "https://www.westminster.ac.uk/course-search?f%5B0%5D=%3A&f%5B1%5D=course_type%3A926&course=&page=0" +str(i)

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    ''' contains to scrap data of page '''
    for contain in  soup.find_all('div', class_="details-pane"):
        try:

            course_name = contain.find('span', class_="details-pane__results-title").text
            print(course_name)
        except Exception as e:
            course_name = ""
            print(course_name)


        '''category of particular course'''
        try:
            category = contain.find('span', class_='details-pane__results-type').text
            print(category)
        except Exception as e:
            category = ""
            print(category)

        '''degree of particular course '''
        try:

            degree_level = contain.find('span', class_="details-pane__results-level").text
            print(degree_level.strip())
        except Exception as e:
            degree_level = ""
            print(degree_level)

        '''Duration time of course '''
        try:
            duration = contain.find_all('span', class_="details-pane__result-value")
            duration_time = duration[1].text
            print(duration_time.strip())
        except Exception as e:
            duration_time = ""
            print(duration_time)

        '''Study mode of course, abstract all elements of particular  span'''
        try:
            mode = contain.find_all('span', class_="details-pane__result-value")
            '''abstracting the value of index num 5 '''
            modes = (mode[2].text)
            print(modes.strip())
        except Exception as e:
            modes = ""
            print(modes)

        '''New session Intake'''
        try:
            intake = contain.find('span', class_="details-pane__result-value").text
            print(intake.strip())
        except Exception as e:
            intake = ""
            print(intake)


        try:
            course_links= contain.find('a')['href']

            course_link = f'https://www.westminster.ac.uk/{course_links}'
            print(course_link)
        except Exception as e:
            course_link = ""
            print(course_link)





        url = course_link
        source = requests.get(url).text
        soup =BeautifulSoup(source, 'lxml')


        contains = soup.find('div', class_="course-overview")
        #print(contains.prettify())


        try:
            location = contains.find(class_="details-pane__result")

            locations = (location.find('a').text)
            print(locations)
        except Exception as e:
            locations =""
            print(locations)


        try:
            fee = contains.find_all(class_="course-overview__result")

            domestic = fee[0].find('a').text
            print(domestic)
        except Exception as e:
            domestic = ""
            print(domestic)
        try:
            international = fee[1].find('a').text
            print(international)
        except Exception as e:
            international= ""
            print(international)

        maincontain = soup.find('div', class_="region region-content")
        #print(maincontain)

        description = maincontain.find_all(class_="col-xs-12 col-md-6 col-md-offset-0")
        #print(description[0])
        try:
            course_summery=description[0].find('p').text
            print(course_summery)
        except Exception as e:
            course_summery = ""
            print(course_summery)
        try:
            course_structure = description[1].find('p').text
            print(course_structure)
        except Exception as e:
            course_structure = ""
            print(course_structure)

        # description = des.find('p').text
        #print(description)
        try:
            careers = maincontain.find('div', class_='intro-text').text
            print(careers.strip())
        except Exception as e:
            careers = ""
            print(careers)
        print("\n")
        csv_writer.writerow([course_name, category, degree_level, duration_time, modes, intake, course_link, locations, domestic, international, course_summery, course_structure, careers])


'''for postgradute subjects'''

for i in range(0,0):
    url = "https://www.westminster.ac.uk/course-search?f%5B0%5D=course_type%3A26&course=&page=0" +str(i)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for contain in  soup.find_all('div', class_="details-pane"):
        try:
            course_name = contain.find('span', class_="details-pane__results-title").text
            print(course_name)
        except Exception as e:
            course_name = ""
            print(course_name)

        '''category of particular course'''
        try:
            category = contain.find('span', class_='details-pane__results-type').text
            print(category)
        except Exception as e:
            category = ""
            print(category)

        '''degree of particular course '''
        try:
            degree_level = contain.find('span', class_="details-pane__results-level").text
            print(degree_level.strip())
        except Exception as e:
            degree_level = ""
            print(degree_level)

        '''Duration time of course '''

        duration = contain.find_all('span', class_="details-pane__result-value")
        try:
            duration_time = duration[1].text
            print(duration_time.strip())
        except Exception as e:
            duration_time = ""
            print(duration_time)
        '''Study mode of course, abstract all elements of particular  span'''

        mode = contain.find_all('span', class_="details-pane__result-value")
        '''abstracting the value of index num 5 '''
        try:
            modes = (mode[2].text)
            print(modes.strip())
        except Exception as e:
            modes = ""
            print(modes)

        '''New session Intake'''
        try:
            intake = contain.find('span', class_="details-pane__result-value").text
            print(intake.strip())
        except Exception as e:
            intake = ""
            print(intake)
        try:

            course_links = contain.find('a')['href']

            course_link = f'https://www.westminster.ac.uk/{course_links}'
            print(course_link)
        except Exception as e:
            course_link = ""
            print(course_link)

        url = course_link
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        contains = soup.find('div', class_="course-overview")
        # print(contains.prettify())
        try:

            location = contains.find_all(class_="course-overview__result-value")

            locations = (location[3].text)
            print(locations)
        except Exception as e:
            locations = ""
            print(locations)


        fee = contains.find_all(class_="course-overview__result")
        try:
            domestic = fee[0].find('a').text
            print(domestic)
        except Exception as e:
            domestic = ""
            print(domestic)

        try:
            international = fee[1].find('a').text
            print(international)
        except Exception as e:
            international = ""
            print(international)
        maincontain = soup.find('div', class_="region region-content")
        # print(maincontain)

        try:
            description = maincontain.find_all(class_="col-xs-12 col-md-6 col-md-offset-0")
            #print(description)
        except Exception as e:
            description = ""
            #print(description)
        try:
            course_summery = description[0].find('p').text
            print(course_summery)
        except Exception as e:
            course_summery =""
            print(course_summery)
        try:
            course_structure = description[1].find('p').text
            print(course_structure)
        except Exception as e:
            course_structure = ""
            print(course_structure)
        try:
            main2= soup.find_all('div',class_="layout__1col")

            careers = main2[2].text
            print(careers.strip())
        except Exception as e:
            careers = ""
            print(careers)

        try:
            alumin_discount = contains.find('div',class_="details-pane__result")
            #print(alumin_discount)
            discount = alumin_discount.find('a')['href']
            #print(discount)
            '''Discount link for Alumin'''

            url = discount
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')

            contains2 = soup.find(class_="content")
            #print(contains2.prettify())
            acrual_discunt = contains2.find(class_="h2--underline").text
            print(acrual_discunt)
        except Exception as e:
            acrual_discunt= ""
            print(acrual_discunt)
        print("\n")

        csv_writer.writerow([course_name, category, degree_level, duration_time, modes, intake, course_link, locations, domestic, international, course_summery, course_structure, careers, acrual_discunt])

csv_file.close()




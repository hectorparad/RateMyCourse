import os

# this is a template for a population script..

def populate():

    #For each university this is the tables to pair with the courses
    #glasgow
    uni_course1 = [['Internet Technology','School of Computing Science', 2014, 5, 'Dr Azzopardi', 98, 20],
                  ['Economics 101','School of Economics', 2011, 2, 'Dr Aniston', 70, 20],
                  ['Requirements Engineering', 'School of Computing', 2013, 5, 'Dr Inah', 70, 20],
                  ['Cyber Security', 'School of Computing', 2012, 4, 'Dr Poet', 80, 20]]

    #london
    uni_course2 = [['History 1','School of History', 2011, 1, 'Dr Jolie', 86, 20],
                  ['Geology 201','School of Geology', 2011, 2, 'Dr Johansson', 60, 20]]

    #leeds
    uni_course3 = [['Project Management','School of Computing Science', 2010, 4, 'Dr Knightley', 74, 20],
                  ['Mathematics 1','School of Mathematics', 2013, 1, 'Dr Stone', 68, 20]]

    #sheffield
    uni_course4 = [['Professional Skills and Issues','School of Computing Science', 2013, 5, 'Dr Cruz', 88, 20],
                  ['Web Development','School of Computing Science', 2013, 3, 'Dr App', 76, 20],
                  ['Mathematics 101','School of Mathematics', 2011, 1, 'Dr Swift', 66, 20],
                  ['Software Project Management','School of Computing Science', 2012, 5, 'Dr Andrew', 46, 20]]

    #stu_id, course_id, rate, comment, date
    rateit = [[2, 1, 5, 'What an interesting course!', '2014-02-11T12:34:56'], [3, 1, 5, 'The best course ever!', '2014-02-21T22:34:56'],
              [3, 2, 2, 'Not very good', '2011-01-23T01:23:45'], [4, 4, 1, 'Avoid it at all costs', '2012-01-20T16:59:59'],
              [4, 2, 2, 'Not good at all', '2011-01-13T21:23:45'], [5, 3, 4, 'it is okay', '2013-03-12T23:34:45'],
              [6, 3, 4, 'The professor is awesome', '2013-04-12T23:34:45'], [7, 4, 1, 'It is a really hard course', '2012-11-10T06:59:59'],
             [9, 5, 3, 'not that helpful', '2011-11-05T21:21:32'], [10, 5, 3, 'not very objective', '2011-12-05T11:21:32'],
              [11, 6, 4, 'The professor is really good', '2011-05-06T13:09:08'], [12, 7, 4, 'Good course', '2010-04-02T10:09:08'],
              [13, 7, 1, 'Not good at all', '2010-08-01T21:19:28'], [13, 8, 5, 'cool', '2013-07-05T15:39:48'],
              [14, 8, 5, 'Great', '2013-06-05T05:39:48'], [14, 7, 5, 'very objective', '2010-11-04T01:21:32'],
              [15, 7, 3, 'Avoid it', '2010-01-25T11:21:32'], [16, 12, 3, 'Do not select it', '2012-02-25T11:21:32'],
              [17, 11, 2, 'Not good at all', '2011-01-13T21:23:45'], [18, 11, 2, 'Not very good', '2011-01-23T01:23:45'],
             [18, 12, 1, 'Avoid it at all costs', '2012-01-20T16:59:59'], [19, 9, 5, 'Very good', '2013-10-05T01:21:32'],
             [19, 10, 1, 'not good', '2013-03-01T11:19:28'], [19, 12, 1, 'It is a really hard course', '2012-11-10T06:59:59']]

    #the students of all univeristies
    students = [['Mark', 'Zuckerberg'], ['Charlie', 'Cheaterson'], ['Leif', 'Azzopardi'], ['Maggie', 'McGeek'],
        ['Emily', 'Robinson'], ['Sarah', 'Taylor'], ['Emma', 'Jones'], ['Jessica', 'White'],
        ['Daniel', 'Wilson'], ['Courtney', 'Smith'], ['Matthew', 'Thompson'], ['Ryan', 'Walker'],
        ['Jacob', 'King'], ['Olivia', 'Lee'], ['Peter', 'Nguyen'], ['Harry', 'Kewell'], ['Stan', 'Lazaridis'],
        ['Michael', 'Jordan'], ['Steven', 'Gerrard'], ['George', 'Best']]

    universities = [
        ['University of Glasgow', 'student.gla.ac.uk', 'University Avenue', 'Glasgow', 'United Kingdom', 'G12 8QQ'],
        ['University of London', 'student.lon.ac.uk', 'Malet Street', 'London', 'United Kingdom', 'WC1E 7HU'],
        ['University of Leeds', 'student.leeds.ac.uk', 'Clarendon Place', 'Leeds', 'United Kingdom', 'LS2 9JT'],
        ['University of Sheffield', 'student.sheffield.ac.uk', 'Western Bank', 'Sheffield', 'United Kingdom', 'S10 2TN']
    ]

    #import Universities
    for i in range(len(universities)):
        u = add_university(universities[i][0], universities[i][1], universities[i][2], universities[i][3], universities[i][4], universities[i][5])

    #import students in each University
    #GLASGOW
    for j in range(0, 6, 1):
        u = University.objects.get(name="University of Glasgow")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[0][1],
                        '1234')
    #LONDON
    for j in range(7, 11, 1):
        u = University.objects.get(name="University of London")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[1][1],
                        '1234')
    #LEEDS
    for j in range(12, 16, 1):
        u = University.objects.get(name="University of Leeds")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[2][1],
                        '1234')
    #SHEFFIELD
    for j in range(16, 20, 1):
        u = University.objects.get(name="University of Sheffield")
        s = add_student(students[j][0], students[j][1], students[j][0]+'.'+students[j][1]+'@'+universities[3][1],
                        '1234')

    #Cources in each university
    #GLASGOW
    for j in range(0, 4, 1):
        u = University.objects.get(name="University of Glasgow")
        add_course(uni_course1[j][0], u, uni_course1[j][2], uni_course1[j][3], uni_course1[j][4], uni_course1[j][5], uni_course1[j][6])

    #LONDON
    for j in range(0, 2, 1):
        u = University.objects.get(name="University of London")
        add_course(uni_course2[j][0], u, uni_course2[j][2], uni_course2[j][3], uni_course2[j][4], uni_course2[j][5], uni_course2[j][6])

    #LEEDS
    for j in range(0, 2, 1):
        u = University.objects.get(name="University of Leeds")
        add_course(uni_course3[j][0], u, uni_course3[j][2], uni_course3[j][3], uni_course3[j][4], uni_course3[j][5], uni_course3[j][6])

    #SHEFFIELD
    for j in range(0, 4, 1):
        u = University.objects.get(name="University of Sheffield")
        add_course(uni_course4[j][0], u, uni_course4[j][2], uni_course4[j][3], uni_course4[j][4], uni_course4[j][5], uni_course4[j][6])

    #ratings per uni
    #LEEDS
    for i in range(len(rateit)):
        st = User.objects.get(id=rateit[i][0])
        c = Course.objects.get(id=rateit[i][1])
        add_rate(st, c, rateit[i][2], rateit[i][3], rateit[i][4])


def add_university(name, domain, address, city, country, postcode):
    u = University.objects.get_or_create(name=name, domain=domain, address=address, city=city, country=country, postcode=postcode)[0]
    return u

def add_student(name, surname, email, password):
    s = User.objects.get_or_create(first_name=name, last_name=surname, email=email)[0]
    s.set_password(password)
    s.username = email
    s.save()
    return s

def add_course(title, uni, year, level, professor, total_rating, times_rated):
    c = Course.objects.get_or_create(title=title, university=uni, year=year, level=level, professor=professor, total_rating=total_rating, times_rated=times_rated) [0]
    c.stored_average_rating = round(float(total_rating)/float(times_rated), 2)
    c.save()
    return c

def add_rate(student, course, rate, comment, date):
    r = Rate.objects.get_or_create(student=student, course=course, rate=rate, comment=comment, date=date)[0]
    tr = Course.objects.get(id=course.id)
    tr.times_rated += 1
    tr.total_rating += rate
    tr.stored_average_rating = ("%0.2f" % round(float(tr.total_rating)/float(tr.times_rated), 2))
    tr.date=date
    tr.save()
    return r


# Start execution here!
if __name__ == '__main__':
    print "Starting Rate population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyCourse.settings')
    from rate.models import University, Course, Rate
    from django.contrib.auth.models import User
    populate()
    print "Well Done!!"

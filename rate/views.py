from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rate.models import Rate, Course, University
from django.contrib.auth.models import User
from rate.forms import UserForm
from datetime import datetime


def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        university_option = request.POST['university_options']
        course_option = request.POST['course_options']
        level_option = request.POST['level_options']
        year_option = request.POST['year_options']
        if university_option == '' or course_option == '' or level_option == '' or year_option == '':
            return HttpResponse(
                'Every field is required. Go back to <a href="/rate/">main page</a>.')
        the_course = Course.objects.filter(university=university_option).filter(title=course_option).filter(
            level=level_option).filter(year=year_option)
        if the_course:
            for j in the_course:
                j.url = j.title.replace(' ', '_')
            return HttpResponseRedirect('course/' + j.url)
        else:
            return HttpResponse(
                'There is no such course. Please <a href="/rate/contact/">contact</a> the administrator to request it, or go back to <a href="/rate/">main page</a>.')
    else:
        top_five_list = Course.objects.order_by('-stored_average_rating')[:5]
        worst_five_list = Course.objects.order_by('stored_average_rating')[:5]
        latest_list = Course.objects.order_by('-date')[:5]
        university_list = University.objects.order_by('name')
        course_list = Course.objects.values('title').distinct()
        year_list = Course.objects.values('year').distinct()
        context_dict = {'topfive': top_five_list, 'worstfive': worst_five_list, 'latestfive': latest_list,
                        'universitylist': university_list, 'courselist': course_list, 'yearlist': year_list}

        for rate in top_five_list:
            rate.url = rate.title.replace(' ', '_')
        for rate in worst_five_list:
            rate.url = rate.title.replace(' ', '_')
        for rate in latest_list:
            rate.url = rate.title.replace(' ', '_')
        return render_to_response('rate/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('rate/about.html', context)


def contact(request):
    context = RequestContext(request)
    return render_to_response('rate/contact.html', context)


def user_login(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/rate/')
                else:
                    return HttpResponse(
                        "Sorry your account is not enabled. Your University's domain is not confirmed yet.")
            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        else:
            return render_to_response('rate/login.html', {}, context)
    else:
        return HttpResponse('You are already signed in. Go back to <a href="/rate/">main page</a>.')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rate/')


def register(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
            temp_domain = request.POST['email'].split("@", 1)[1]
            # print temp_domain
            uni_domain_list = University.objects.order_by('domain')
            # print uni_domain_list
            flag = 'no'
            for i in uni_domain_list:
                # print i.domain
                if i.domain == temp_domain:
                    user_list = User.objects.all()
                    for us in user_list:
                        if us.email == request.POST['email']:
                            return HttpResponse(
                                'There is already an account with this email. Please <a href="/rate/contact/">contact</a> the administrator to request it, or go back to <a href="/rate/">main page</a>.')
                    user_form = UserForm(data=request.POST)
                    if user_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.username = user.email
                        user.save()
                        registered = True
                        flag = 'yes'
                        return HttpResponseRedirect('/rate/login')
                    else:
                        print user_form.errors,
            if flag == 'no':
                return HttpResponse(
                    'This university is not in our database yet. Please <a href="/rate/contact/">contact</a> the administrator to request it, or go back to <a href="/rate/">main page</a>.')
        else:
            user_form = UserForm()
            return render_to_response('rate/register.html', {'user_form': user_form, 'registered': registered}, context)
    else:
        return HttpResponse('You are already registered and signed in. Go back to <a href="/rate/">main page</a>.')  #


def restricted(request):
    if request.user.is_authenticated():
        return HttpResponse("You cannot access this page!")
    else:
        return render_to_response('rate/restricted.html')


def sitemap(request):
    context = RequestContext(request)
    list = Course.objects.order_by('title')
    context_dict = {'list': list, }
    for course in list:
        course.url = course.title.replace(' ', '_')
    return render_to_response('rate/sitemap.html', context_dict, context)


def course(request, course_title_url):
    context = RequestContext(request)
    course_title = course_title_url.replace('_', ' ')
    context_dict = {'course_title': course_title}
    try:
        course = Course.objects.get(title=course_title)
        rate = Rate.objects.filter(course=course).order_by('-date')
        context_dict['course'] = course
        context_dict['rate'] = rate

        flag = "yes"
        if request.user.is_authenticated():
            for r in rate:
                if request.user.id == 1:
                    flag = "yes"
                else:
                    if r.student.email == request.user.email:
                        flag = "no"
                    domain = request.user.email.split("@", 1)[1]
                    if course.university.domain != domain:
                        flag = "no"
        context_dict['rateIt'] = flag
    except Course.DoesNotExist:
        pass
    course.url = course.title.replace(' ', '_')
    return render_to_response('rate/course.html', context_dict, context)


def rated_courses(request, type):
    context = RequestContext(request)
    if request.method == 'POST':
        university_option = request.POST['university']
        level_option = request.POST['level']
        year_option = request.POST['year']
        if type == "top":
            list = Course.objects.filter(university=university_option, level=level_option, year=year_option).order_by(
                '-stored_average_rating')[:20]
            title = "Top Rated Courses"
            choose_tit = 1
        if type == "worst":
            list = Course.objects.filter(university=university_option, level=level_option, year=year_option).order_by(
                'stored_average_rating')[:20]
            title = "Worst Rated Courses"
            choose_tit = 2
        if type == "latest":
            list = Course.objects.filter(university=university_option, level=level_option, year=year_option).order_by(
                '-date')[:20]
            title = "Most Recent Rated Courses"
            choose_tit = 3
    else:
        if type == "top":
            list = Course.objects.order_by('-stored_average_rating')[:20]
            title = "Top Rated Courses"
            choose_tit = 1
        if type == "worst":
            list = Course.objects.order_by('stored_average_rating')[:20]
            title = "Worst Rated Courses"
            choose_tit = 2
        if type == "latest":
            list = Course.objects.order_by('-date')[:20]
            title = "Most Recent Rated Courses"
            choose_tit = 3

    university_list = University.objects.order_by('name')
    course_list = Course.objects.values('title').distinct()
    year_list = Course.objects.values('year').distinct()
    rates_list = Rate.objects.values('course', 'date')[:1]
    context_dict = {'list': list, 'title': title,
                    'universitylist': university_list, 'courselist': course_list, 'yearlist': year_list,
                    'rateslist': rates_list, 'ch_title': choose_tit}
    for rate in list:
        rate.url = rate.title.replace(' ', '_')

    return render_to_response('rate/rated_courses.html', context_dict, context)


def rateIt(request, course_title_url):
    context = RequestContext(request)
    course_title = course_title_url.replace('_', ' ')
    if request.method == 'POST':
        tr = Course.objects.get(title=course_title)
        date = datetime.now()
        rate_f = int(request.POST['q1'])
        comment_f = (request.POST['comments'])
        Rate.objects.get_or_create(student=request.user, course=tr, rate=rate_f, comment=comment_f, date=datetime.now())
        tr.times_rated += 1
        tr.total_rating += rate_f
        tr.stored_average_rating = ("%0.2f" % round(float(tr.total_rating) / float(tr.times_rated), 2))  #
        tr.date = date
        tr.save()
        return HttpResponseRedirect('/rate/course/' + course_title_url)
    else:
        if request.user.is_authenticated():
            course_title = course_title_url.replace('_', ' ')
            context_dict = {'course_title': course_title, 'course_url': course_title_url}
            try:
                course = Course.objects.get(title=course_title)
                rate = Rate.objects.filter(course=course)
                context_dict['course'] = course
                context_dict['rate'] = rate
            except Course.DoesNotExist:
                pass
            return render_to_response('rate/rateIt.html', context_dict, context)
        else:
            return render_to_response('rate/restricted.html')


def profile(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        list = Rate.objects.filter(student=request.user.id).order_by('-date')
        context_dict = {'list': list}
        for rate in list:
            rate.url = rate.course.title.replace(' ', '_')
        return render_to_response('rate/profile.html', context_dict, context)
    else:
        return render_to_response('rate/restricted.html')

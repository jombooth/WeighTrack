from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response

from weightrack_app.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from weightrack_app.models import TaggedItem, Scale



#to be clear, this is views.index from the context of urls.py
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    '''pics=[]
    import os
    root="/home/burkugler/weighty/static/pics"
    Path=os.path.join(root)
    os.chdir(Path)
    for files in os.listdir("."):
        if files[-3:].lower() in ["gif","png","jpg","bmp"] :
            pics.append(files)'''

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #????????????????
    return render_to_response('weightrack_app/index.html', context_dict, context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            return HttpResponseRedirect('/wt_app/')


        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        #???????????????????
            'weightrack_app/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/wt_app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your WeighTrack account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('weightrack_app/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/wt_app/')

def user_about(request):
    return render_to_response('weightrack_app/about.html')

def user_devices(request):
    return render_to_response('weightrack_app/myWeighTrack.html')

def user_device_reg(request):
    return render_to_response('weightrack_app/devReg.html')

def req(request):
    context=RequestContext(request)
    u = request.path_info
    variables = u.split('+')
    wt = str(variables[0][18:])
    l = str(variables[1][7:])
    r = str(variables[2][7:])
    w = int(variables[3][7:])
    left = None
    right = None
    old_left = None
    old_right = None

    results= Scale.objects.filter(wt_id=wt)
    if not results:
        s = Scale.objects.create(wt_id=wt, rfid_l=l, rfid_r = r, weight = w, rfid_l_old = l, rfid_r_old = r, weight_old = w)
    else:
        result = results[0]
        print result
        print result.weight 
        result.update(weight=w)

    newresults = Scale.objects.all()


    return render_to_response('weightrack_app/return.html', {'results':results , 'new':newresults}, context)










from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response

from weightrack_app.forms import UserForm, ReorderForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from weightrack_app.models import TaggedItem, Scale, Order
import datetime
from svgprint_html import im_output


#to be clear, this is views.index from the context of urls.py
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    if request.method == 'POST':
        rf = ReorderForm(data=request.POST)
        n = request.POST['name']
        results= TaggedItem.objects.filter(name=n)
        result = results[0].currWeight
        o = Order.objects.create(name = n, tag = 0, date = datetime.date.today(), qty = result, arrived = 0)
        return HttpResponseRedirect('/wt_app/orders/')

    else:
        objects = TaggedItem.objects.all()
        items = []
        for item in objects:
            t = item.tag
            n = str(item.name)
            f = item.fullWeight
            e = item.emptyWeight
            c = item.currWeight
            if (c > f):
                c = f
            if (c < e):
                c = e
            percent = int(float(c-e)/float(f-e)*100)
            image = im_output(float(c-e)/float(f-e), n)
            items.append([n,percent,image])

        return render_to_response('weightrack_app/index.html', {'items':items}, context)

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

def t(request):
    context=RequestContext(request)
    return render_to_response('weightrack_app/test.html', context)


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

    items = TaggedItem.objects.all()

    results= Scale.objects.filter(wt_id=wt)
    #print results
    if not results:
        s = Scale.objects.create(wt_id=wt, rfid_l=l, rfid_r = r, weight = w, rfid_l_old = l, rfid_r_old = r, weight_old = w)
    else:
        result = results[0]

        if r == '0000':
            right = None
        else:
            right = TaggedItem.objects.filter(tag=r)
            if not right:
                t = TaggedItem.objects.create(name = "Unnamed", tag = r, container= "none", fullWeight= 100, emptyWeight = 0, currWeight = 0, saleDate = datetime.date.today(), url = 'http://apple.com')
                right = TaggedItem.objects.filter(tag=r)
            right = right[0]
        if l == '0000':
            left = None
        else:
            left = TaggedItem.objects.filter(tag=l)
            if not left:
                t = TaggedItem.objects.create(name = "Unnamed", tag = l, container= "none", fullWeight= 100, emptyWeight = 0, currWeight = 0, saleDate = datetime.date.today(), url = 'http://apple.com')
                left = TaggedItem.objects.filter(tag=l)
            left = left[0]
        if results[0].rfid_r == '0000':
            old_right = None
        else:
            old_right = TaggedItem.objects.filter(tag=results[0].rfid_r)
            old_right = old_right[0]
        if results[0].rfid_l == '0000':
            old_left = None
        else:
            old_left = TaggedItem.objects.filter(tag=results[0].rfid_l)
            old_left = old_left[0]
        a = '0'
        b = '0'
        if left:
            print left.saleDate
            print datetime.date.today()
            if left.saleDate < datetime.date.today():
                a = '1'
        if right:
            if right.saleDate < datetime.date.today():
                b = '1'
        ab = a + b

        if not w == result.weight:
            #if left rfid changed
            #if (not left) or (not right):
                if not l == result.rfid_l:

                    #if left rfid is now gone but right isnt
                    if l == '0000' and not r == '0000':
                        #make sure that the w = cur weight for right rfid
                        TaggedItem.objects.filter(tag=r).update(currWeight = w)
                    #if left rfid is now back from gone
                    elif result.rfid_l == '0000' and not l == '0000':
                        #w-wold becomes the new cur weight for left rfid
                        wnew = w - result.weight
                        TaggedItem.objects.filter(tag=l).update(currWeight = wnew)
                    #if left rfid just changed while right stayed the same
                    elif result.rfid_r == r and not result.rfid_l == l and not l == '0000':
                        #cur weight for new left becomes w-wold- curr weight for displacd left
                        wnew = w - (result.weight - old_left.currWeight)
                        TaggedItem.objects.filter(tag=l).update(currWeight = wnew)
                #if right rfid changed
                if not r == result.rfid_r:
                    #if right rfid is now gone
                    if r == '0000' and not l == '0000':
                        #make sure that the w = cur weight for left rfid
                        TaggedItem.objects.filter(tag=l).update(currWeight = w)
                    #if right rfid is now back from gone
                    elif result.rfid_r == '0000' and not r == '0000':
                        #w-wold becomes the new cur weight for right rfid
                        wnew = w - result.weight
                        TaggedItem.objects.filter(tag=r).update(currWeight = wnew)
                    #if right rfid just changed while left stayed the same
                    elif result.rfid_l == l and not result.rfid_r == r and not r == '0000':
                        #cur weight for new right becomes w-wold- curr weight for displacd right
                        wnew = w - (result.weight - old_right.currWeight)
                        TaggedItem.objects.filter(tag=r).update(currWeight = wnew)

                #update database for next time

                oldweight = result.weight
                Scale.objects.filter(wt_id=wt).update(weight_old = oldweight)
                Scale.objects.filter(wt_id=wt).update(weight=w)
                Scale.objects.filter(wt_id=wt).update(rfid_l_old = result.rfid_l)
                Scale.objects.filter(wt_id=wt).update(rfid_l=l)
                Scale.objects.filter(wt_id=wt).update(rfid_r_old = result.rfid_r)
                Scale.objects.filter(wt_id=wt).update(rfid_r=r)

    newresults = Scale.objects.all()
    print newresults
    newitems = TaggedItem.objects.all()
    print newitems

    return render_to_response('weightrack_app/return.html', {'results':results , 'new':newresults, 'item':items, 'newitems':newitems, 'ab':ab}, context)




def orders(request):
    context=RequestContext(request)

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        rf = ReorderForm(data=request.POST)
        n = request.POST['name']
        results= TaggedItem.objects.filter(name=n)
        result = results[0].currWeight
        o = Order.objects.create(name = n, tag = 0, date = datetime.date.today(), qty = result, arrived = 0)


        return HttpResponseRedirect('/wt_app/orders/')


    else:

        u = request.path_info
        objects = Order.objects.all()
        orders = []
        dictionary = {}
        for item in objects:
            n = str(item.name)
            d = item.date
            l = item.qty
            t = item.tag
            if item.arrived == 0:
                a = "In Transit"
            else:
                a = "Delivered"
            if n in dictionary.keys():
                dictionary[n].append((t,d,a,l))
            else:
                dictionary[n] = [(t,d,a,l)]
            orders.append([n,d,a])
        orders.reverse()

        for key,value in dictionary.iteritems():
            order_placed = False
            total = 0
            num = 0
            for thing in value:
                (t,d,a,l) = thing
                if a == 'In Transit':
                    order_placed = True
                total += l
                num += 1
            avg = float(total) / float(num)

            results= TaggedItem.objects.filter(name=key)
            result = results[0].currWeight

            if result < avg and order_placed == False:
                o = Order.objects.create(name = key, tag = t, date = datetime.date.today(), qty = int(avg), arrived = 0)

        objects = Order.objects.all()
        orders = []
        for item in objects:
            n = str(item.name)
            d = item.date
            l = item.qty
            t = item.tag
            if item.arrived == 0:
                a = "In Transit"
            else:
                a = "Delivered"
            orders.append((n,d,a))
            orders = sorted(orders, key=lambda x: x[1])
            orders.reverse()
        

        return render_to_response('weightrack_app/orders.html', {'orders':orders}, context) 


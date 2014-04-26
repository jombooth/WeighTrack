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


        '''if r == 'None':
            right = None
        else:
            right = TaggedItem.objects.filter(tag=r)
            right = right[0]
        if l == 'None':
            left == None
        else:
            left = TaggedItem.objects.filter(tag=l)
            left = left[0]
        if results[0].rfid_r == None:
            old_right = None
        else:
            old_right = TaggedItem.objects.filter(tag=results[0].rfid_r)
            old_right = old_right[0]
        if results[0].rfid_l == None:
            old_left = None
        else:
            old_left = TaggedItem.objects.filter(tag=results[0].rfid_l)
            old_left = old_left[0]'''

        if not w == result.weight:

            '''
            #if left rfid changed
            if not l == result.rfid_l:
                #if left rfid is now gone
                if l == None and not r == None:
                    #make sure that the w = cur weight for right rfid
                    right.update(currWeight = w)
                #if left rfid is now back from gone
                elif result.rfid_l == None and not l == None:
                    #w-wold becomes the new cur weight for left rfid
                    wnew = w - result.weight
                    left.update(currWeight = wnew)
                #if left rfid just changed while right stayed the same
                elif result.rfid_r == r and not result.rfid_l == l and not left == None:
                    #cur weight for new left becomes w-wold- curr weight for displacd left
                    wnew = w - result.weight - old_left.currWeight
                    left.update(currWeight = wnew)
            #if right rfid changed
            if not r == result.rfid_r:
                #if right rfid is now gone
                if r == None and not l == None:
                    #make sure that the w = cur weight for left rfid
                    left.update(currWeight = w)
                #if right rfid is now back from gone
                elif result.rfid_r == None and not r == None:
                    #w-wold becomes the new cur weight for right rfid
                    wnew = w - result.weight
                    right.update(currWeight = wnew)
                #if right rfid just changed while left stayed the same
                elif result.rfid_l == l and not result.rfid_r == r and not right == None:
                    #cur weight for new right becomes w-wold- curr weight for displacd right
                    wnew = w - result.weight - old_right.currWeight
                    right.update(currWeight = wnew)'''

            '''update database for next time
            oldweight = result.weight
            result.update(weight_old = oldweight)
            result.update(weight=w)
            result.update(rfid_l_old = result.rfid_l)
            result.update(rfid_l=l)
            result.update(rfid_r_old = result.rfid_r)
            result.update(rfid_r=r)'''
            pass






    newresults = Scale.objects.all()




    return render_to_response('weightrack_app/return.html', {'results':results , 'new':newresults}, context)



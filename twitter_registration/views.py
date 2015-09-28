from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
import tweepy
from .models import TwitterUser
from django.contrib.auth.models import User
from django.shortcuts import redirect

def twitterAuthenticate(request):
    auth = tweepy.OAuthHandler('RYA6tJluBPa7INeicfFVyagLv', '6Lb3FEndR7gLgU1aZugPZotwPsAjyVh5dQ7OHJjE5atUR2hmPA', 'http://127.0.0.1:8000/register/callback')

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError as e:        
        return HttpResponse('error', status=500)

    request.session['request_token'] = (auth.request_token)
    
    return HttpResponseRedirect(redirect_url)

def twitterAuthorizeCallback(request):
    verifier = request.GET.get('oauth_verifier')

    auth = tweepy.OAuthHandler('RYA6tJluBPa7INeicfFVyagLv', '6Lb3FEndR7gLgU1aZugPZotwPsAjyVh5dQ7OHJjE5atUR2hmPA')

    token = request.session.get('request_token')
    request.session.delete('request_token')
    auth.request_token = token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        return HttpResponse('error', status=500)
    

    response_data = {}
    response_data = auth.access_token    
        
    
    api = tweepy.API(auth)
    data = api.me()
    data = {'id' : data.id,
            'username' : data.screen_name,
            'email' : data.screen_name + '@speakapp.com',
            'name': data.name,
            'access_token' : auth.access_token,
            'access_token_secret' : auth.access_token_secret,}
    
    user = userExist(data["id"])
    if(user):
        user_login(request,user.user)
        mensaje="login"
    else:
        mensaje="register"
        user = registerTwitter(data)
        user_login(request,user.user)
    #api.update_status(status='tweepy + oauth!2') #The status must change on each execution

    return redirect('speakapp.views.list')
    #return HttpResponse("mensaje")

def userExist(twitterId):      
    user = False
    try:
        user = TwitterUser.objects.get(twitter_id=twitterId)
    except:
        exist = False
    return user

def registerTwitter(data):
    newUser = TwitterUser()
    baseUser = User.objects.create_user(
            username = data["username"],
            password = data["username"] + "salt",
            email = data["email"],            
            )
    newUser.user = baseUser
    newUser.twitter_id = data["id"]
    newUser.access_token = data["access_token"]
    newUser.access_token_secret = data["access_token_secret"]
    newUser.save()

    return newUser

def user_login(request, twitteruser):
    # Use Django's machinery to attempt to see if the username/password
    # combination is valid - a User object is returned if it is.
    user = authenticate(username=twitteruser.username, password=twitteruser.username+"salt")

    # If we have a User object, the details are correct.
    # If None (Python's way of representing the absence of a value), no user
    # with matching credentials was found.
    if user:
        # Is the account active? It could have been disabled.
        if user.is_active:        
            # If the account is valid and active, we can log the user in.
            # We'll send the user back to the homepage.
            login(request, user)
            return HttpResponseRedirect('/rango/')
        else:
            # An inactive account was used - no logging in!
            return HttpResponse("Your Rango account is disabled.")
    else:
        # Bad login details were provided. So we can't log the user in.
        #print "Invalid login details: {0}, {1}".format(username, password)
        return HttpResponse("Invalid login details supplied.")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    #return HttpResponse("logged out")
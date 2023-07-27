from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Min, Max
from .models import score1,score2,score3,score4,payment3,payment4
import json
import time
import random
import datetime
import re

def home(request):
    return render(request,"front.html")
@csrf_exempt
def ajaxview1(request):
    if request.method=='POST':
        return render(request,"reg.html")
    
@csrf_exempt
def ajaxview2(request):
    if request.method=='POST':
        return render(request,"login.html")
def reg(request):
    return render(request,"reg.html")
def reg_page(request):
    if request.method=="POST":
        e_mail=request.POST['email']
        user_name=request.POST['username']
        pass_word=request.POST['password']
        pattern="[a-zA-Z][a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z]+$"
        match=re.match(pattern,e_mail)
        obj1=User.objects.all()
        for i in obj1:
            if i.username==user_name:
                msg="User name is already exist"
                return render(request,"reg.html",{'msg':msg})
                break 
        else:

            if  not user_name.isalpha() or  user_name.isdigit() or " " in user_name:
                msg="invalid user name"
                return render(request,"reg.html",{'msg':msg})
            elif len(pass_word)!=4 or not pass_word.isprintable():
                msg="invalid password"
                return render(request,"reg.html",{'msg':msg})
            
            elif match is None:
                msg="invalid email"
                return render(request,"reg.html",{'msg':msg})
            else:
                user=User.objects.create_user(email=e_mail,username=user_name,password=pass_word,is_superuser=False)
                user.save()
                return redirect("home")
    else:
        return redirect("reg")
def logins(request):
    return render(request,"login.html")
@csrf_exempt
def main(request):
    return render(request,"main.html")
@csrf_exempt
def main_page(request):
    if request.method=="POST":
        
        global user_name
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request,user)
            return render(request,"main.html")
        else:
            msg="mismatched username"
            return render(request,"login.html",{"msg":msg})
    else:
        return redirect("login")

@csrf_exempt
def play(request):
    if request.user.is_authenticated:
        global flip
        flip=[]
        global list1
        list1=[] 
        global counts
        counts=0
        cards1=[["1music","bi-music-note","color:green"],["1heart","bi-heart-fill","color:red"],["1diamond","bi-diamond-fill","color:blue"],["1spade","bi-suit-spade-fill","color:black"],["1club","bi-suit-club-fill","color:purple"]]
        cards2=[["2music","bi-music-note","color:green"],["2heart","bi-heart-fill","color:red"],["2diamond","bi-diamond-fill","color:blue"],["2spade","bi-suit-spade-fill","color:black"],["2club","bi-suit-club-fill","color:purple"]]
        random.shuffle(cards1)
        random.shuffle(cards2)
        return render(request,"play.html",{"cards1":cards1,"cards2":cards2} )
    else:
        return redirect("home")


list1=[]  
flip=[]
@csrf_exempt
def check(request):
    if request.method=='POST':
        time.sleep(0.5)
        global flip
        global counts
        counts=counts+1
        
        data=json.loads(request.body)
        flip_id=data["card_id"]
        if len(flip)==0:
            
            flip.append(flip_id)
        else:
            if flip_id in flip:
                pass
            else:
                flip_id=flip_id[1:]
                flip.append(flip_id)
                if len(flip)==2:
                    flip[0]=flip[0][1:]
                    if flip[0]==flip[1]:
                        list1.append("matched")
                        flipid=["matched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        if len(list1)==5:
                            msg="you won"
                            now=datetime.date.today()
                            global user_name
                            user=User.objects.filter(username=user_name)
                            for i in user:
                                user_id=i.id
                                username=i.username
                                score=score1.objects.create(user_id=user_id,date_created=now,score=counts,user_name=username)
                                score.save()
                                return render(request,"check.html",{"flipid":flipid,"msg":msg,"counts":counts})
                            

                        return render(request,"check.html",{"flipid":flipid,"counts":counts})

                    else:
                        flipid=["unmatched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        msg="unmatched"
                        return render(request,"check.html",{"flipid":flipid,"counts":counts})
                else:
                    return redirect("play")
        return render(request,"check.html",{"counts":counts})
def level2(request):
    if request.user.is_authenticated:
        global flip
        flip=[]
        global list1
        list1=[] 
        global counts
        counts=0
        cards1=[["1gift","bi-gift-fill","color:purple"],["1bright","bi-brightness-low-fill","color:yellow"],["1tele","bi-telephone-fill","color:brown"],["1flower","bi-flower3","color:red"],["1key","bi-key-fill","color:black"]]
        cards2=[["2gift","bi-gift-fill","color:purple"],["2bright","bi-brightness-low-fill","color:yellow"],["2tele","bi-telephone-fill","color:brown"],["2flower","bi-flower3","color:red"],["2key","bi-key-fill","color:black"]]
        random.shuffle(cards1)
        random.shuffle(cards2)
        return render(request,"level2.html",{"cards1":cards1,"cards2":cards2} )
    else:
        return redirect("home")
def lock1(request):
    if request.user.is_authenticated:
        global user_name
        user=payment3.objects.filter(user_name=user_name)
        if user:
            global flip
            flip=[]
            global list1
            list1=[] 
            global counts
            counts=0
            cards1=[["1dice1","bi-dice-1-fill","color:black"],["1dice2","bi-dice-2-fill","color:black"],["1dice3","bi-dice-3-fill","color:black"],["1dice4","bi-dice-4-fill","color:black"],["1dice5","bi-dice-5-fill","color:black"],["1dice6","bi-dice-6-fill","color:black"]]
            cards2=[["2dice1","bi-dice-1-fill","color:black"],["2dice2","bi-dice-2-fill","color:black"],["2dice3","bi-dice-3-fill","color:black"],["2dice4","bi-dice-4-fill","color:black"],["2dice5","bi-dice-5-fill","color:black"],["2dice6","bi-dice-6-fill","color:black"]]
            random.shuffle(cards1)
            random.shuffle(cards2)
            return render(request,"level3.html",{"cards1":cards1,"cards2":cards2} )
        else:
            return render(request, 'level3lock.html')
    else:
        return redirect("home")
def lock2(request):
    if request.user.is_authenticated:
        global user_name
        user=payment4.objects.filter(user_name=user_name)
        if user:
            global flip
            flip=[]
            global list1
            list1=[] 
            global counts
            counts=0
            cards1=[["1wifi","bi-wifi","color:black"],["1cycle","bi-bicycle","color:purple"],["1sky","bi-skype","color:blue"],["1ear","bi-earbuds","color:black"],["1face","bi-facebook","color:blue"],["1twit","bi-twitter","color:blue"]]
            cards2=[["2wifi","bi-wifi","color:black"],["2cycle","bi-bicycle","color:purple"],["2sky","bi-skype","color:blue"],["2ear","bi-earbuds","color:black"],["2face","bi-facebook","color:blue"],["2twit","bi-twitter","color:blue"]]
            random.shuffle(cards1)
            random.shuffle(cards2)
            return render(request,"level4.html",{"cards1":cards1,"cards2":cards2} )
        else:
            return render(request, 'level4lock.html')
    else:
        return redirect("home")
       
@csrf_exempt
def check2(request):
    if request.method=='POST':
        time.sleep(0.5)
        global flip
        global counts
        counts=counts+1
        
        data=json.loads(request.body)
        flip_id=data["card_id"]
        if len(flip)==0:
            
            flip.append(flip_id)
        else:
            if flip_id in flip:
                pass
            else:
                flip_id=flip_id[1:]
                flip.append(flip_id)
                if len(flip)==2:
                    flip[0]=flip[0][1:]
                    if flip[0]==flip[1]:
                        list1.append("matched")
                        flipid=["matched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        if len(list1)==5:
                            msg="you won"
                            now=datetime.date.today()
                            global user_name
                            user=User.objects.filter(username=user_name)
                            for i in user:
                                user_id=i.id
                                username=i.username
                                score=score2.objects.create(user_id=user_id,date_created=now,score=counts,user_name=username)
                                score.save()
                                return render(request,"check1.html",{"flipid":flipid,"msg":msg,"counts":counts})
                            

                        return render(request,"check1.html",{"flipid":flipid,"counts":counts})

                    else:
                        flipid=["unmatched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        msg="unmatched"
                        return render(request,"check1.html",{"flipid":flipid,"counts":counts})
                else:
                    return redirect("play")
        return render(request,"check1.html",{"counts":counts})


@csrf_exempt
def check3(request):
    if request.method=='POST':
        time.sleep(0.5)
        global flip
        global counts
        counts=counts+1
        
        data=json.loads(request.body)
        flip_id=data["card_id"]
        if len(flip)==0:
            
            flip.append(flip_id)
        else:
            if flip_id in flip:
                pass
            else:
                flip_id=flip_id[1:]
                flip.append(flip_id)
                if len(flip)==2:
                    flip[0]=flip[0][1:]
                    if flip[0]==flip[1]:
                        list1.append("matched")
                        flipid=["matched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        if len(list1)==6:
                            msg="you won"
                            now=datetime.date.today()
                            global user_name
                            user=User.objects.filter(username=user_name)
                            for i in user:
                                user_id=i.id
                                username=i.username
                                score=score3.objects.create(user_id=user_id,date_created=now,score=counts,user_name=username)
                                score.save()
                                return render(request,"check3.html",{"flipid":flipid,"msg":msg,"counts":counts})
                            

                        return render(request,"check3.html",{"flipid":flipid,"counts":counts})

                    else:
                        flipid=["unmatched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        msg="unmatched"
                        return render(request,"check3.html",{"flipid":flipid,"counts":counts})
                else:
                    return redirect("play")
        return render(request,"check1.html",{"counts":counts})


@csrf_exempt
def check4(request):
    if request.method=='POST':
        time.sleep(0.5)
        global flip
        global counts
        counts=counts+1
        
        data=json.loads(request.body)
        flip_id=data["card_id"]
        if len(flip)==0:
            
            flip.append(flip_id)
        else:
            if flip_id in flip:
                pass
            else:
                flip_id=flip_id[1:]
                flip.append(flip_id)
                if len(flip)==2:
                    flip[0]=flip[0][1:]
                    if flip[0]==flip[1]:
                        list1.append("matched")
                        flipid=["matched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        if len(list1)==6:
                            msg="you won"
                            now=datetime.date.today()
                            global user_name
                            user=User.objects.filter(username=user_name)
                            for i in user:
                                user_id=i.id
                                username=i.username
                                score=score4.objects.create(user_id=user_id,date_created=now,score=counts,user_name=username)
                                score.save()
                                return render(request,"check4.html",{"flipid":flipid,"msg":msg,"counts":counts})
                            

                        return render(request,"check4.html",{"flipid":flipid,"counts":counts})

                    else:
                        flipid=["unmatched","1"+flip[0],"2"+flip[1]]
                        flip=[]
                        msg="unmatched"
                        return render(request,"check4.html",{"flipid":flipid,"counts":counts})
                else:
                    return redirect("play")
        return render(request,"check4.html",{"counts":counts})

@csrf_exempt
def leader1(request):
    if request.method=='POST':
        scores=score1.objects.values("user_name").annotate(min=Min("score"))[0:3]
        sorted_queryset = sorted(scores, key=lambda x: x['min'])
        l=1
        return render(request,"leadership.html",{"scores":sorted_queryset,"l":l})

@csrf_exempt
def leader2(request):
    if request.method=='POST':
        scores=score2.objects.values("user_name").annotate(min=Min("score"))[0:3]
        sorted_queryset = sorted(scores, key=lambda x: x['min'])
        l=2
        return render(request,"leadership.html",{"scores":sorted_queryset,"l":l})

@csrf_exempt
def leader3(request):
    if request.method=='POST':
        scores=score3.objects.values("user_name").annotate(min=Min("score"))[0:3]
        sorted_queryset = sorted(scores, key=lambda x: x['min'])
        l=3
        return render(request,"leadership.html",{"scores":sorted_queryset,"l":l})

@csrf_exempt
def leader4(request):
    if request.method=='POST':
        scores=score4.objects.values("user_name").annotate(min=Min("score"))[0:3]
        sorted_queryset = sorted(scores, key=lambda x: x['min'])
        l=4
        return render(request,"leadership.html",{"scores":sorted_queryset,"l":l})

def logout_views(request):
    logout(request)
    return redirect("home")
    
@csrf_exempt
def upi(request):
    if request.method=='POST':
        return render(request,"upi.html")
@csrf_exempt
def credit(request):
    if request.method=='POST':
        return render(request,"credit.html")

@csrf_exempt
def upi1(request):
    if request.method=='POST':
        return render(request,"upi1.html")
@csrf_exempt
def credit1(request):
    if request.method=='POST':
        return render(request,"credit1.html")

    
@csrf_exempt
def upi_check(request):
    if request.method=='POST':
        data=request.POST['upi']
        pattern="[a-zA-Z0-9]+@[a-zA-Z]+$"
        match=re.match(pattern,data)
        if match:
            now=datetime.date.today()
            global user_name
            user=User.objects.filter(username=user_name)
            for i in user:
                user_id=i.id
                username=i.username
                payment=payment3.objects.create(user_id=user_id,date_created=now,pay=data,user_name=username,amount=50)
                payment.save()
                global flip
                flip=[]
                global list1
                list1=[] 
                global counts
                counts=0
                cards1=[["1dice1","bi-dice-1-fill","color:black"],["1dice2","bi-dice-2-fill","color:black"],["1dice3","bi-dice-3-fill","color:black"],["1dice4","bi-dice-4-fill","color:black"],["1dice5","bi-dice-5-fill","color:black"],["1dice6","bi-dice-6-fill","color:black"]]
                cards2=[["2dice1","bi-dice-1-fill","color:black"],["2dice2","bi-dice-2-fill","color:black"],["2dice3","bi-dice-3-fill","color:black"],["2dice4","bi-dice-4-fill","color:black"],["2dice5","bi-dice-5-fill","color:black"],["2dice6","bi-dice-6-fill","color:black"]]
                random.shuffle(cards1)
                random.shuffle(cards2)
                return render(request,"level3.html",{"cards1":cards1,"cards2":cards2} )
        else:
            msg="INVALID UPI ID"
            return render(request,"level3lock.html",{"msg":msg})
            
    
@csrf_exempt
def credits_check(request):
    if request.method=='POST':
        data=request.POST['credit']
        pattern="[0-9]{4}"
        match=re.match(pattern,data)
        if match:
            now=datetime.date.today()
            global user_name
            user=User.objects.filter(username=user_name)
            for i in user:
                user_id=i.id
                username=i.username
                payment=payment3.objects.create(user_id=user_id,date_created=now,pay=data,user_name=username,amount=50)
                payment.save()
                global flip
                flip=[]
                global list1
                list1=[] 
                global counts
                counts=0
                cards1=[["1dice1","bi-dice-1-fill","color:black"],["1dice2","bi-dice-2-fill","color:black"],["1dice3","bi-dice-3-fill","color:black"],["1dice4","bi-dice-4-fill","color:black"],["1dice5","bi-dice-5-fill","color:black"],["1dice6","bi-dice-6-fill","color:black"]]
                cards2=[["2dice1","bi-dice-1-fill","color:black"],["2dice2","bi-dice-2-fill","color:black"],["2dice3","bi-dice-3-fill","color:black"],["2dice4","bi-dice-4-fill","color:black"],["2dice5","bi-dice-5-fill","color:black"],["2dice6","bi-dice-6-fill","color:black"]]
                random.shuffle(cards1)
                random.shuffle(cards2)
                return render(request,"level3.html",{"cards1":cards1,"cards2":cards2} )
        else:
            msg="INVALID CARD DETAILS"
            return render(request,"level3lock.html",{"msg":msg})
        
@csrf_exempt
def upi_check1(request):
    if request.method=='POST':
        data=request.POST['upi']
        pattern="[a-zA-Z0-9]+@[a-zA-Z]+$"
        match=re.match(pattern,data)
        if match:
            now=datetime.date.today()
            global user_name
            user=User.objects.filter(username=user_name)
            for i in user:
                user_id=i.id
                username=i.username
                payment=payment4.objects.create(user_id=user_id,date_created=now,pay=data,user_name=username,amount=100)
                payment.save()
                global flip
                flip=[]
                global list1
                list1=[] 
                global counts
                counts=0
                cards1=[["1wifi","bi-wifi","color:black"],["1cycle","bi-bicycle","color:purple"],["1sky","bi-skype","color:blue"],["1ear","bi-earbuds","color:black"],["1face","bi-facebook","color:blue"],["1twit","bi-twitter","color:blue"]]
                cards2=[["2wifi","bi-wifi","color:black"],["2cycle","bi-bicycle","color:purple"],["2sky","bi-skype","color:blue"],["2ear","bi-earbuds","color:black"],["2face","bi-facebook","color:blue"],["2twit","bi-twitter","color:blue"]]
                random.shuffle(cards1)
                random.shuffle(cards2)
                return render(request,"level4.html",{"cards1":cards1,"cards2":cards2} )
        else:
            msg="INVALID UPI ID"
            return render(request,"level4lock.html",{"msg":msg})
    
@csrf_exempt
def credits_check1(request):
    if request.method=='POST':
        data=request.POST['credit']
        pattern="[0-9]{4}"
        match=re.match(pattern,data)
        if match:
            now=datetime.date.today()
            global user_name
            user=User.objects.filter(username=user_name)
            for i in user:
                user_id=i.id
                username=i.username
                payment=payment4.objects.create(user_id=user_id,date_created=now,pay=data,user_name=username,amount=100)
                payment.save()
                global flip
                flip=[]
                global list1
                list1=[] 
                global counts
                counts=0
                cards1=[["1wifi","bi-wifi","color:black"],["1cycle","bi-bicycle","color:purple"],["1sky","bi-skype","color:blue"],["1ear","bi-earbuds","color:black"],["1face","bi-facebook","color:blue"],["1twit","bi-twitter","color:blue"]]
                cards2=[["2wifi","bi-wifi","color:black"],["2cycle","bi-bicycle","color:purple"],["2sky","bi-skype","color:blue"],["2ear","bi-earbuds","color:black"],["2face","bi-facebook","color:blue"],["2twit","bi-twitter","color:blue"]]
                random.shuffle(cards1)
                random.shuffle(cards2)
                return render(request,"level4.html",{"cards1":cards1,"cards2":cards2} )
        else:
            msg="INVALID CARD DETAILS"
            return render(request,"level4lock.html",{"msg":msg})




 


    




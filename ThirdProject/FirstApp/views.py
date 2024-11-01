from django.shortcuts import render

# Create your views here.
import datetime
def wish(request):
 date1 = datetime.datetime.now()
 msg1="hello dear user..GOOD"
 hr=int(date1.strftime("%H"))
 img="image1.jpg"
 if hr<10:
     msg1+=" MORING..!"
     img="image1.jpg"
 elif hr<16:
     msg1+=" ATERNOON..!"
     img="image2.jpg"
 elif hr<20:
     msg1+=" EVENING..!"
     img="image3.jpg"
 else:
     msg1+=" NIGHT..!"
     img="image4.jpg"
 DICT1={"date1":date1,"msg1":msg1,"img":img}
 return render(request,'FirstApp/wishes3.html',DICT1)

def imggallery(request):
    date1 = datetime.datetime.now()
    msg1="**DJango-Image-Gallery**";
    dict1={"date1":date1,"msg1":msg1}
    return render(request, "FirstApp/imgsgallery.html",dict1);

def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1="**DJango-Image-Gallery(product)**";
    dict1={"date1":date1,"msg1":msg1}
    return render(request, "FirstApp/imgsgallery2.html",dict1);

def hyperlinks(request):
    date1 = datetime.datetime.now()
    msg1="**DJango-HYPERLINKS**";
    dict1={"date1":date1,"msg1":msg1}
    return render(request, "FirstApp/hyperlinks.html",dict1);
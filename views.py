import email
from django.shortcuts import render, HttpResponseRedirect
from matplotlib.style import context
from numpy import delete
from .forms import CreatingTeam
from .models import Ipl
# Create your views here.
def home(request):
    return render(request,'index.html')
def team(request):
    return render(request,'team.html')
def auction(request):
    return render(request,'auction.html')
def match(request):
    return render(request,'match.html')
def show_squad(request):
    if request.method == 'POST':
        fm1 = CreatingTeam(request.POST)
        if fm1.is_valid():
            nm = fm1.cleaned_data['name']
            tm = fm1.cleaned_data['team']
            pr = fm1.cleaned_data['price']
            pl = fm1.cleaned_data['play']
            rl = fm1.cleaned_data['role']            
            make = Ipl(name=nm, team=tm, price=pr, play=pl, role=rl)
            make.save()
            fm1 = CreatingTeam()
    else:
        fm1 = CreatingTeam()
    result = Ipl.objects.all()
    return render(request,'addshow.html', {'form':fm1, 'result':result})
    
def delete_data(request, id):
    if request.method == 'POST':
        pi = Ipl.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/show_squad') 

def update_squad(request, id):
    if request.method == 'POST':
        pi = Ipl.objects.get(pk=id)
        fm1 = CreatingTeam(request.POST, instance=pi)
        if fm1.is_valid():
            fm1.save()
    else:
        pi = Ipl.objects.get(pk=id)
        fm1 = CreatingTeam(instance=pi)
    return render(request,'update.html', {'form':fm1})

def csk(request):
    return render(request,'csk.html')
def mi(request):
    return render(request,'mi.html')
def rcb(request):
    return render(request,'rcb.html')
def pks(request):
    return render(request,'pks.html')
def dc(request):
    return render(request,'dc.html')
def kkr(request):
    return render(request,'kkr.html')

#### chennai team------------------------------------------------
def faf(request):
    return render(request,'faf.html')
def rut(request):
    return render(request,'rut.html')
def amb(request):
    return render(request,'amb.html')
def sur(request):
    return render(request,'sur.html')
def msd(request):
    return render(request,'msd.html')
def moe(request):
    return render(request,'moe.html')
def rob(request):
    return render(request,'rob.html')
def dwa(request):
    return render(request,'dwa.html')
def rav(request):
    return render(request,'rav.html')
def dee(request):
    return render(request,'dee.html')
def sar(request):
    return render(request,'sar.html')
def sam(request):
    return render(request,'sam.html')
def imr(request):
    return render(request,'imr.html')
def jos(request):
    return render(request,'jos.html')
def mit(request):
    return render(request,'mit.html')

#### mumbai team------------------------------------------------
def qui(request):
    return render(request,'qui.html')
def roh(request):
    return render(request,'rohit.html')
def ish(request):
    return render(request,'isan.html')
def sury(request):
    return render(request,'surya.html')
def sau(request):
    return render(request,'saurab.html')
def sac(request):
    return render(request,'sachin.html')
def adi(request):
    return render(request,'aditya.html')
def kie(request):
    return render(request,'kieron.html')
def har(request):
    return render(request,'hardik.html')
def kur(request):
    return render(request,'kurnal.html')
def rah(request):
    return render(request,'rahul.html')
def jam(request):
    return render(request,'jame.html')
def jas(request):
    return render(request,'jasprit.html')
def jay(request):
    return render(request,'jayant.html')
def tre(request):
    return render(request,'trent.html')

#### rcb team------------------------------------------------
def dev(request):
    return render(request,'dev.html')
def vir(request):
    return render(request,'virat.html')
def abd(request):
    return render(request,'abd.html')
def glen(request):
    return render(request,'glen.html')
def aron(request):
    return render(request,'aron.html')
def raj(request):
    return render(request,'rajat.html')
def shah(request):
    return render(request,'shah.html')
def dav(request):
    return render(request,'david.html')
def akas(request):
    return render(request,'akas.html')
def mds(request):
    return render(request,'siraj.html')
def har(request):
    return render(request,'harsh.html')
def nav(request):
    return render(request,'nav.html')
def ada(request):
    return render(request,'adam.html')
def josh(request):
    return render(request,'josh.html')
def mitc(request):
    return render(request,'mitc.html')

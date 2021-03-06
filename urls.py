from django.urls import path,include
from iplapp import views
urlpatterns = [
 
 path('',views.home),
 path('team/',views.team),
 path('auction/',views.auction),
 path('match/',views.match),

 path('csk/',views.csk),
 path('mi/',views.mi),
 path('dc/',views.dc),
 path('kkr/',views.kkr),
 path('pks/',views.pks),
 path('rcb/',views.rcb),
 path('faf/',views.faf),
 path('rut/',views.rut), 
 path('amb/',views.amb), 
 path('sur/',views.sur), 
 path('msd/',views.msd), 
 path('moe/',views.moe), 
 path('rob/',views.rob), 
 path('dwa/',views.dwa), 
 path('rav/',views.rav), 
 path('dee/',views.dee), 
 path('sar/',views.sar), 
 path('sam/',views.sam), 
 path('imr/',views.imr), 
 path('jos/',views.jos), 
 path('mit/',views.mit), 
 path('show_squad/',views.show_squad, name='addshow'), 
 path('delete_data/<int:id>/',views.delete_data, name='deletedata'), 
 path('<int:id>/',views.update_squad, name='updatedata'), 
 path('qui/',views.qui), 
 path('roh/',views.roh), 
 path('ish/',views.ish), 
 path('sury/',views.sury), 
 path('sau/',views.sau), 
 path('sac/',views.sac), 
 path('adi/',views.adi), 
 path('kie/',views.kie), 
 path('har/',views.har), 
 path('kur/',views.kur), 
 path('rah/',views.rah), 
 path('jam/',views.jam), 
 path('jay/',views.jay), 
 path('jas/',views.jas), 
 path('tre/',views.tre), 

path('dev/',views.dev), 
 path('vir/',views.vir), 
 path('abd/',views.abd), 
 path('glen/',views.glen), 
 path('aron/',views.aron), 
 path('raj/',views.raj), 
 path('shah/',views.shah), 
 path('dav/',views.dav), 
 path('akas/',views.akas),
 path('mds/',views.mds), 
 path('har/',views.har), 
 path('nav/',views.nav), 
 path('ada/',views.ada), 
 path('josh/',views.josh), 
 path('mitc/',views.mitc), 

]

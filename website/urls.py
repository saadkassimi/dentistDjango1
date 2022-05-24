from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index.html"),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('appointment', views.appointment, name="appointment"),
    path('terms', views.terms, name="terms"),
    path('locations/', views.locations, name="locations"),
    path('privacy', views.privacy, name="privacy"),
    path('services/dental-bonding', views.dentalbonding, name="dental-bonding"),
    path('services/dental-bridges', views.dentalbridges, name="dental-bridges"),
    path('services/dental-checkup', views.dentalcheckup, name="dental-checkup"),
    path('services/dental-crowns', views.dentalcrowns, name="dental-crowns"),
    path('services/dental-implants', views.dentalimplants, name="dental-implants"),
    path('services/dental-invisalign', views.dentalinvisalign, name="dental-invisalign"),
    path('services/partial-dentures', views.partialdentures, name="partial-dentures"),
    path('services/dental-teeth-whitening', views.dentalteethwhitening, name="dental-teeth-whitening"),
    path('services/dental-white-composite-fillings', views.dentalwhitecompositefillings, name="dental-white-composite-fillings"),
    path('services/wisdom-teeth-removal', views.wisdomteethremoval, name="wisdom-teeth-removal"),
    path('services/dental-smile-imaging-technology', views.dentalsmileimagingtechnology, name="dental-smile-imaging-technology"),
    path('services/general-dentistry', views.generaldentistry, name="general-dentistry"),
    path('locations/east-colfax-avenue', views.eastcolfaxavenue, name="east-colfax-avenue"),
    path('locations/South-Broadway', views.SouthBroadway, name="South-Broadway"),
    path('locations/Larimer-Street', views.LarimerStreet, name="Larimer-Street"),
    path('locations/Antique-Row', views.AntiqueRow, name="Antique-Row"),
    path('locations/Humboldt-Street', views.HumboldtStreet, name="Humboldt-Street"),
    path('locations/16th-St-Mall', views.thStMall, name="16th-St-Mall"),
    path('locations/Speer-Boulevard', views.SpeerBoulevard, name="Speer-Boulevard"),
    path('locations/Welton-Street', views.WeltonStreet, name="Welton-Street"),
    path('locations/South-Gaylord-Street', views.SouthGaylordStreet, name="South-Gaylord-Street"),
    path('locations/east-colfax-avenue/dental-bonding-service', views.dentalbondingservice, name="dental-bonding-service"),
    path('locations/east-colfax-avenue/dental-bridges-service', views.dentalbridgesservice, name="dental-bridges-service"),
    path('locations/east-colfax-avenue/dental-checkup-service', views.dentalcheckupservice, name="dental-checkup-service"),
    path('locations/east-colfax-avenue/dental-crowns-service', views.dentalcrownsservice, name="dental-crowns-service"),
    path('locations/east-colfax-avenue/dental-implants-service', views.dentalimplantsservice, name="dental-implants-service"),
    path('locations/east-colfax-avenue/dental-invisalign-service', views.dentalinvisalignservice, name="dental-invisalign-service"),
    path('locations/east-colfax-avenue/partial-dentures-service', views.partialdenturesser, name="partial-dentures-service"),
    path('locations/east-colfax-avenue/dental-teeth-whitening-service', views.dentalteethwhiteningser, name="dental-teeth-whitening-service"),
    path('locations/east-colfax-avenue/dental-white-composite-fillings-service', views.dentalwhitefillingsser, name="dental-white-composite-fillings-service"),
    path('locations/east-colfax-avenue/wisdom-teeth-removal-service', views.wisdomteethremovalser, name="wisdom-teeth-removal-service"),
    path('locations/east-colfax-avenue/smile-imaging-technology-service', views.smileimagitechser, name="smile-imaging-technology-service"),
    path('locations/east-colfax-avenue/general-dentistry-service', views.generaldentistryser, name="general-dentistry-service"),
    path('locations/South-Broadway/services/dental-bonding', views.ssdb, name="ssdb"),
    path('locations/South-Broadway/services/dental-bridges', views.ssdgb, name="ssdgb"),
    path('locations/South-Broadway/services/dental-checkup', views.ssdcp, name="ssdcp"),
    path('locations/South-Broadway/services/dental-crowns', views.ssdc, name="ssdc"),
    path('locations/South-Broadway/services/dental-implants', views.sbsdi, name="sbsdi"),
    path('locations/South-Broadway/services/dental-invisalign', views.svsdi, name="svsdi"),
    path('locations/South-Broadway/services/partial-dentures', views.svpd, name="svpd"),
    path('locations/South-Broadway/services/dental-teeth-whitening', views.ssdtw, name="ssdtw"),
    path('locations/South-Broadway/services/dental-white-composite-fillings', views.ssdwcf, name="ssdwcf"),
    path('locations/South-Broadway/services/wisdom-teeth-removal', views.sswstr, name="sswstr"),
    path('locations/South-Broadway/services/dental-smile-imaging-technology', views.sssimt, name="sssimt"),
    path('locations/South-Broadway/services/general-dentistry', views.ssgd, name="ssgd"),
    path('locations/Larimer-Street/services/dental-bonding', views.mnjhg, name="mnjhg"),
    path('locations/Larimer-Street/services/dental-bridges', views.mnsdb, name="mnsdb"),
    path('locations/Larimer-Street/services/dental-checkup', views.chess, name="chess"),
    path('locations/Larimer-Street/services/dental-crowns', views.xsng, name="xsng"),
    path('locations/Larimer-Street/services/dental-implants', views.zsnb, name="zsnb"),
    path('locations/Larimer-Street/services/dental-invisalign', views.bgs, name="bgs"),
    path('locations/Larimer-Street/services/partial-dentures', views.bbs, name="bbs"),
    path('locations/Larimer-Street/services/dental-teeth-whitening', views.bss, name="bss"),
    path('locations/Larimer-Street/services/dental-white-composite-fillings', views.bsa, name="bsa"),
    path('locations/Larimer-Street/services/wisdom-teeth-removal', views.bsq, name="bsq"),
    path('locations/Larimer-Street/services/dental-smile-imaging-technology', views.bsrr, name="bsrr"),
    path('locations/Larimer-Street/services/general-dentistry-service', views.bsz, name="bsz"),
    path('locations/Antique-Row/services/dental-bonding', views.qqqq, name="qqqq"),
    path('locations/Antique-Row/services/dental-bridges', views.wqqq, name="wqqq"),
    path('locations/Antique-Row/services/dental-checkup', views.eqqq, name="eqqq"),
    path('locations/Antique-Row/services/dental-crowns', views.aqqq, name="aqqq"),
    path('locations/Antique-Row/services/dental-implants', views.zqqq, name="zqqq"),
    path('locations/Antique-Row/services/dental-invisalign', views.vqqq, name="vqqq"),
    path('locations/Antique-Row/services/partial-dentures', views.dqqq, name="dqqq"),
    path('locations/Antique-Row/services/dental-teeth-whitening', views.fqqq, name="fqqq"),
    path('locations/Antique-Row/services/dental-white-composite-fillings', views.jqqq, name="jqqq"),
    path('locations/Antique-Row/services/wisdom-teeth-removal', views.cqqq, name="cqqq"),
    path('locations/Antique-Row/services/dental-smile-imaging-technology', views.mqqq, name="mqqq"),
    path('locations/Antique-Row/services/general-dentistry', views.oqqq, name="oqqq"),
    path('locations/Humboldt-Street/services/dental-bonding', views.aaaa, name="aaaa"),
    path('locations/Humboldt-Street/services/dental-bridges', views.aaab, name="aaab"),
    path('locations/Humboldt-Street/services/dental-checkup', views.aaac, name="aaac"),
    path('locations/Humboldt-Street/services/dental-crowns', views.aaad, name="aaad"),
    path('locations/Humboldt-Street/services/dental-implants', views.aaaf, name="aaaf"),
    path('locations/Humboldt-Street/services/dental-invisalign', views.aaag, name="aaag"),
    path('locations/Humboldt-Street/services/partial-dentures', views.aaad, name="aaad"),
    path('locations/Humboldt-Street/services/dental-teeth-whitening', views.aaaw, name="aaaw"),
    path('locations/Humboldt-Street/services/dental-white-composite-fillings', views.aaaq, name="aaaq"),
    path('locations/Humboldt-Street/services/wisdom-teeth-removal', views.sssq, name="sssq"),
    path('locations/Humboldt-Street/services/dental-smile-imaging-technology', views.sssr, name="sssr"),
    path('locations/Humboldt-Street/services/general-dentistry', views.sssa, name="sssa"),
    path('locations/16th-St-Mall/services/dental-bonding', views.cccc, name="cccc"),
    path('locations/16th-St-Mall/services/dental-bridges', views.ccca, name="ccca"),
    path('locations/16th-St-Mall/services/dental-checkup', views.ccaa, name="ccaa"),
    path('locations/16th-St-Mall/services/dental-crowns', views.bbvv, name="bbvv"),
    path('locations/16th-St-Mall/services/dental-implants', views.vvaa, name="vvaa"),
    path('locations/16th-St-Mall/services/dental-invisalign', views.ccsa, name="ccsa"),
    path('locations/16th-St-Mall/services/partial-dentures', views.aasz, name="aasz"),
    path('locations/16th-St-Mall/services/dental-teeth-whitening', views.gggf, name="gggf"),
    path('locations/16th-St-Mall/services/dental-white-composite-fillings', views.ccxz, name="ccxz"),
    path('locations/16th-St-Mall/services/wisdom-teeth-removal', views.gtre, name="gtre"),
    path('locations/16th-St-Mall/services/dental-smile-imaging-technology', views.kkjj, name="kkjj"),
    path('locations/16th-St-Mall/services/general-dentistry', views.awera, name="awera"),
    path('locations/Speer-Boulevard/services/dental-bonding', views.vaas, name="vaas"),
    path('locations/Speer-Boulevard/services/dental-bridges', views.vasd, name="vasd"),
    path('locations/Speer-Boulevard/services/dental-checkup', views.xasd, name="xasd"),
    path('locations/Speer-Boulevard/services/dental-crowns', views.zxas, name="zxas"),
    path('locations/Speer-Boulevard/services/dental-implants', views.zasqw, name="zasqw"),
    path('locations/Speer-Boulevard/services/dental-invisalign', views.zasdq, name="zasdq"),
    path('locations/Speer-Boulevard/services/partial-dentures', views.qweri, name="qweri"),
    path('locations/Speer-Boulevard/services/dental-teeth-whitening', views.zasqjh, name="zasqjh"),
    path('locations/Speer-Boulevard/services/dental-white-composite-fillings', views.pbhju, name="pbhju"),
    path('locations/Speer-Boulevard/services/wisdom-teeth-removal', views.ahgtr, name="ahgtr"),
    path('locations/Speer-Boulevard/services/dental-smile-imaging-technology', views.ajhuipfd, name="ajhuipfd"),
    path('locations/Speer-Boulevard/services/general-dentistry', views.a, name="a"),
    path('locations/Welton-Street/services/dental-bonding', views.zarbi, name="zarbi"),
    path('locations/Welton-Street/services/dental-bridges', views.zarbis, name="zarbis"),
    path('locations/Welton-Street/services/dental-checkup', views.zap, name="zap"),
    path('locations/Welton-Street/services/dental-crowns', views.zapi, name="zapi"),
    path('locations/Welton-Street/services/dental-implants', views.welp, name="welp"),
    path('locations/Welton-Street/services/dental-invisalign', views.welpi, name="welpi"),
    path('locations/Welton-Street/services/partial-dentures', views.zad, name="zad"),
    path('locations/Welton-Street/services/dental-teeth-whitening', views.zadi, name="zadi"),
    path('locations/Welton-Street/services/dental-white-composite-fillings', views.zadis, name="zadis"),
    path('locations/Welton-Street/services/wisdom-teeth-removal', views.zahi, name="zahi"),
    path('locations/Welton-Street/services/dental-smile-imaging-technology', views.zajni, name="zajni"),
    path('locations/Welton-Street/services/general-dentistry', views.xadsi, name="xadsi"),
    path('locations/South-Gaylord-Street/services/dental-bonding', views.uarbi, name="uarbi"),
    path('locations/South-Gaylord-Street/services/dental-bridges', views.uarbis, name="uarbis"),
    path('locations/South-Gaylord-Street/services/dental-checkup', views.uap, name="uap"),
    path('locations/South-Gaylord-Street/services/dental-crowns', views.uapi, name="uapi"),
    path('locations/South-Gaylord-Street/services/dental-implants', views.uelp, name="uelp"),
    path('locations/South-Gaylord-Street/services/dental-invisalign', views.uelpi, name="uelpi"),
    path('locations/South-Gaylord-Street/services/partial-dentures', views.uad, name="uad"),
    path('locations/South-Gaylord-Street/services/dental-teeth-whitening', views.uadi, name="uadi"),
    path('locations/South-Gaylord-Street/services/dental-white-composite-fillings', views.uadis, name="uadis"),
    path('locations/South-Gaylord-Street/services/wisdom-teeth-removal', views.uahi, name="uahi"),
    path('locations/South-Gaylord-Street/services/dental-smile-imaging-technology', views.uajni, name="uajni"),
    path('locations/South-Gaylord-Street/services/general-dentistry', views.uadsi, name="uadsi"),
    path('Cookie-Policy', views.cookie, name="cookie"),
    ]

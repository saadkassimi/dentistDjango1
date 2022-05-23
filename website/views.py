from django.shortcuts import render
from django.core.mail import send_mail




def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			message_name,
			message,
			message_email,
			['shadekassimi@gmail.com'],
			)

		return render(request,'contact.html', {'message_name': message_name})
	
	else:	
	    return render(request,'contact.html', {})
	
	

def about(request):
	return render(request, 'about.html', {})

def terms(request):
	return render(request, 'terms.html', {})

def privacy(request):
	return render(request, 'privacy.html', {})

def locations(request):
	return render(request, 'locations.html', {})

def eastcolfaxavenue(request):
	return render(request, 'east-colfax-avenue.html', {})

def SouthBroadway(request):
	return render(request, 'South-Broadway.html', {})

def LarimerStreet(request):
	return render(request, 'Larimer-Street.html', {})

def AntiqueRow(request):
	return render(request, 'Antique-Row.html', {})

def HumboldtStreet(request):
	return render(request, 'Humboldt-Street.html', {})

def thStMall(request):
	return render(request, '16th-St-Mall.html', {})

def SpeerBoulevard(request):
	return render(request, 'Speer-Boulevard.html', {})

def WeltonStreet(request):
	return render(request, 'Welton-Street.html', {})

def SouthGaylordStreet(request):
	return render(request, 'South-Gaylord-Street.html', {})

def services(request):
	return render(request, 'services.html', {})

def dentalbonding(request):
	return render(request, 'dental-bonding.html', {})

def dentalbridges(request):	
	return render(request, 'dental-bridges.html', {})

def dentalcheckup(request):	
	return render(request, 'dental-checkup.html', {})

def dentalcrowns(request):	
	return render(request, 'dental-crowns.html', {})	

def dentalbondingservice(request):	
	return render(request, 'dental-bonding-service.html', {})

def dentalcheckupservice(request):	
	return render(request, 'dental-checkup-service.html', {})

def dentalbridgesservice(request):	
	return render(request, 'dental-bridges-service.html', {})

def dentalimplantsservice(request):	
	return render(request, 'dental-implants-service.html', {})

def dentalinvisalignservice(request):	
	return render(request, 'dental-invisalign-service.html', {})		

def dentalcrownsservice(request):	
	return render(request, 'dental-crowns-service.html', {})

def partialdenturesser(request):	
	return render(request, 'partial-dentures-service.html', {})

def dentalteethwhiteningser(request):	
	return render(request, 'dental-teeth-whitening-service.html', {})

def dentalwhitefillingsser(request):	
	return render(request, 'dental-white-composite-fillings-service.html', {})

def smileimagitechser(request):	
	return render(request, 'smile-imaging-technology-service.html', {})	

def wisdomteethremovalser(request):	
	return render(request, 'wisdom-teeth-removal-service.html', {})

def generaldentistryser(request):	
	return render(request, 'general-dentistry-service.html', {})						

def dentalimplants(request):	
	return render(request, 'dental-implants.html', {})

def dentalinvisalign(request):	
	return render(request, 'dental-invisalign.html', {})

def partialdentures(request):	
	return render(request, 'partial-dentures.html', {})

def dentalteethwhitening(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def wisdomteethremoval(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def dentalwhitecompositefillings(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def dentalsmileimagingtechnology(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def generaldentistry(request):	
	return render(request, 'general-dentistry.html', {})			

def ssdb(request):	
	return render(request, 'dental-bonding.html', {})

def ssdgb(request):	
	return render(request, 'dental-bridges.html', {})

def ssdcp(request):	
	return render(request, 'dental-checkup.html', {})

def ssdc(request):	
	return render(request, 'dental-crowns.html', {})

def sbsdi(request):	
	return render(request, 'dental-implants.html', {})

def svsdi(request):	
	return render(request, 'dental-invisalign.html', {})

def svpd(request):	
	return render(request, 'partial-dentures.html', {})

def ssdtw(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def ssdwcf(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def sswstr(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def sssimt(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def ssgd(request):	
	return render(request, 'general-dentistry.html', {})

def mnjhg(request):	
	return render(request, 'dental-bonding.html', {})

def mnsdb(request):	
	return render(request, 'dental-bridges.html', {})

def chess(request):	
	return render(request, 'dental-checkup.html', {})

def xsng(request):	
	return render(request, 'dental-crowns.html', {})

def zsnb(request):	
	return render(request, 'dental-implants.html', {})

def bgs(request):	
	return render(request, 'dental-invisalign.html', {})

def bbs(request):	
	return render(request, 'partial-dentures.html', {})

def bss(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def bsa(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def bsq(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def bsrr(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def bsz(request):	
	return render(request, 'general-dentistry.html', {})

def qqqq(request):	
	return render(request, 'dental-bonding.html', {})

def wqqq(request):	
	return render(request, 'dental-bridges.html', {})

def eqqq(request):	
	return render(request, 'dental-checkup.html', {})

def aqqq(request):	
	return render(request, 'dental-crowns.html', {})

def zqqq(request):	
	return render(request, 'dental-implants.html', {})

def vqqq(request):	
	return render(request, 'dental-invisalign.html', {})

def fqqq(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def jqqq(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def cqqq(request):	
	return render(request, 'wisdom-teeth-removal.html', {})																				

def oqqq(request):	
	return render(request, 'general-dentistry.html', {})

def dqqq(request):	
	return render(request, 'partial-dentures.html', {})

def mqqq(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def aaaa(request):	
	return render(request, 'dental-bonding.html', {})

def aaab(request):	
	return render(request, 'dental-bridges.html', {})

def aaac(request):	
	return render(request, 'dental-checkup.html', {})

def aaad(request):	
	return render(request, 'dental-crowns.html', {})

def aaaf(request):	
	return render(request, 'dental-implants.html', {})

def aaag(request):	
	return render(request, 'dental-invisalign.html', {})

def aaad(request):	
	return render(request, 'partial-dentures.html', {})

def aaaw(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def aaaq(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def sssq(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def sssr(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def sssa(request):	
	return render(request, 'general-dentistry.html', {})

def bbbb(request):	
	return render(request, 'dental-bonding.html', {})

def bbbc(request):	
	return render(request, 'dental-bridges.html', {})

def bbba(request):	
	return render(request, 'dental-checkup.html', {})

def bbbe(request):	
	return render(request, 'dental-crowns.html', {})

def bbbt(request):	
	return render(request, 'dental-implants.html', {})

def bbbj(request):	
	return render(request, 'dental-invisalign.html', {})

def bbby(request):	
	return render(request, 'partial-dentures.html', {})

def bbbr(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def bbbp(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def bbbz(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def bbbx(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def bbbm(request):	
	return render(request, 'general-dentistry.html', {})

def cccc(request):	
	return render(request, 'dental-bonding.html', {})

def ccca(request):	
	return render(request, 'dental-bridges.html', {})

def ccaa(request):	
	return render(request, 'dental-checkup.html', {})

def bbvv(request):	
	return render(request, 'dental-crowns.html', {})

def vvaa(request):	
	return render(request, 'dental-implants.html', {})

def ccsa(request):	
	return render(request, 'dental-invisalign.html', {})

def aasz(request):	
	return render(request, 'partial-dentures.html', {})

def gggf(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def ccxz(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def gtre(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def kkjj(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def awera(request):	
	return render(request, 'general-dentistry.html', {})

def vaas(request):	
	return render(request, 'dental-bonding.html', {})

def vasd(request):	
	return render(request, 'dental-bridges.html', {})

def xasd(request):	
	return render(request, 'dental-checkup.html', {})

def zxas(request):	
	return render(request, 'dental-crowns.html', {})

def zasqw(request):	
	return render(request, 'dental-implants.html', {})

def zasdq(request):	
	return render(request, 'dental-invisalign.html', {})

def qweri(request):	
	return render(request, 'partial-dentures.html', {})

def zasqjh(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def pbhju(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def ahgtr(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def ajhuipfd(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def a(request):	
	return render(request, 'general-dentistry.html', {})

def zarbi(request):	
	return render(request, 'dental-bonding.html', {})

def zarbis(request):	
	return render(request, 'dental-bridges.html', {})

def zap(request):	
	return render(request, 'dental-checkup.html', {})

def zapi(request):	
	return render(request, 'dental-crowns.html', {})

def welp(request):	
	return render(request, 'dental-implants.html', {})

def welpi(request):	
	return render(request, 'dental-invisalign.html', {})

def zad(request):	
	return render(request, 'partial-dentures.html', {})

def zadi(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def zadis(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def zahi(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def zajni(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def xadsi(request):	
	return render(request, 'general-dentistry.html', {})

def uarbi(request):	
	return render(request, 'dental-bonding.html', {})

def uarbis(request):	
	return render(request, 'dental-bridges.html', {})

def uap(request):	
	return render(request, 'dental-checkup.html', {})

def uapi(request):	
	return render(request, 'dental-crowns.html', {})

def uelp(request):	
	return render(request, 'dental-implants.html', {})

def uelpi(request):	
	return render(request, 'dental-invisalign.html', {})

def uad(request):	
	return render(request, 'partial-dentures.html', {})

def uadi(request):	
	return render(request, 'dental-teeth-whitening.html', {})

def uadis(request):	
	return render(request, 'dental-white-composite-fillings.html', {})

def uahi(request):	
	return render(request, 'wisdom-teeth-removal.html', {})

def uajni(request):	
	return render(request, 'dental-smile-imaging-technology.html', {})

def uadsi(request):	
	return render(request, 'general-dentistry.html', {})

def cookie(request):	
	return render(request, 'Cookie-Policy.html', {})
	
																								
def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_date = request.POST['your-date']
		your_departement = request.POST['your-departement']
		your_phone = request.POST['your-phone']
		your_message = request.POST['your-message']


		send_mail(
			your_name,
			your_message,
			your_email,
			['shadekassimi@gmail.com'],
			)

		return render(request,'appointment.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_date': your_date,
            'your_departement': your_departement,
            'your_phone': your_phone,
            'your_message': your_message,
             
             })
	
	else:	
	    return render(request,'home.html', {})

	
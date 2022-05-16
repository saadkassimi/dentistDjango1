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




def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_date = request.POST['your-date']
		your_departement = request.POST['your-departement']
		your_phone = request.POST['your-phone']
		your_message = request.POST['your-message']


		#send_mail(
			#message_name,
			#message,
			#message_email,
			#['shadekassimi@gmail.com'],
			#)

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

	
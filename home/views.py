from django.shortcuts import render, HttpResponse
from flask import redirect
from home.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    context = {
        'variable':'new variable'
    }
    return render(request, 'index.html',context)
    

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        # Retrieve values from the POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        # Check if email is provided
        if email:
            # Create an instance of the Contact model and save it
            Contact_instance = Contact(email=email, password=password)
            Contact_instance.save()
            
            return redirect('success')  # Redirect to a success page
        else:
            # Handle the case where email is not provided
            return render(request, 'contact.html', {'error_message': 'Email is required.'})
    
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')

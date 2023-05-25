from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'radio/index.html')


from django.shortcuts import render

def doctor_dashboard(request):
    # Add any necessary logic or data retrieval here
    return render(request, 'radio/doctor_dashboard.html')


from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Doctor

def create_account_page(request):
    if request.method == 'POST':
        # Get the values from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        birth_date = request.POST.get('birth_date')
       

        # Check if passwords match
        if password == repeat_password:
            # Save the user details in the database
            # Create a User object and save it
            user = User.objects.create_user(email=email, password=password)
            user.first_name = name
            user.save()

            # Save the additional details in the Doctor model
            doctor = Doctor(
                user=user,
                name=name,
                email=email,
                gender=gender,
                phone_number=phone_number,
                address=address,
                birth_date=birth_date,
                
            )
            doctor.save()

            return render(request, 'radio/create_account.html', {'success': True})
        else:
            return render(request, 'radio/create_account.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'radio/create_account.html')

def login_page(request):
    return render(request, 'radio/login.html')


from django.shortcuts import render
from django.shortcuts import redirect
from main.models import Plans, News
from django.contrib import messages


# Home page view
def home(request):
    # Fetch all insurance plans and news
    plans = Plans.objects.all()  # Using the correct model
    news = News.objects.all()

    # Pass the data to the template
    return render(request, 'index.html', {'plans': plans, 'news': news})

# About page view

def about(request):
    return render(request, 'about.html')


# Car insurance page view
def carinsurance(request):
    if request.method == 'POST':
        # Extract data from the form
        car_registration_number = request.POST.get('car_registration_number')
        car_make = request.POST.get('car_make')
        car_model = request.POST.get('car_model')
        car_year = request.POST.get('car_year')

        # Simple validation (can be more sophisticated based on requirements)
        if not car_registration_number or not car_make or not car_model or not car_year:
            messages.error(request, "All fields are required.")
            return render(request, 'plans/carinsurance.html')
        
        messages.success(request, "Car insurance information submitted successfully!")
        return redirect('home')  # Redirect to home or a success page

    return render(request, 'plans/carinsurance.html')

# views.py
def familyinsurance(request):
    if request.method == 'POST':
        policy_number = request.POST.get('policy_number')
        policy_holder_name = request.POST.get('policy_holder_name')
        email_address = request.POST.get('email_address')
        
        # Perform validation or renewal logic
        # If successful, redirect or show a success message
        messages.success(request, "Your family insurance policy has been successfully renewed!")
        return redirect('familyinsurance')  # Redirect to the same page or another success page

    return render(request, 'plans/familyinsurance.html')

def healthinsurance(request):
    if request.method == 'POST':
        # Capture form data
        family_member = request.POST.get('family_member')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        pincode = request.POST.get('pincode')
        
        # Add form processing logic here (e.g., save to database, send email, etc.)
        
        # Show success message
        messages.success(request, "Your health insurance application has been successfully submitted!")
        return redirect('healthinsurance')  # Or any other page you want to redirect to

    return render(request, 'plans/healthinsurance.html')

# House insurance page view
def houseinsurance(request):
    return render(request, 'plans/houseinsurance.html')

# Registration form view
def registration(request):
    return render(request, 'registration/registration.html')

# Registration success page view
def registration_success(request):
    return render(request, 'registration/registration_success.html')


def search_results(request):
    query = request.GET.get('query')
    
    # Check if the query matches 'carinsurance' and redirect if needed
    if query == 'carinsurance':
        return redirect('carinsurance')
    elif query == 'familyinsurance':
        return redirect('familyinsurance')
    elif query == 'houseinsurance':
        return redirect('houseinsurance')
    else:
        return redirect('healthinsurance')
    
    
        # Redirect to the car insurance page URL pattern name
        
    
    # Handle search results rendering
    results = Plans.objects.filter(heading__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'results': results})

# Updated plan_detail view
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from main.models import Plans, News

# Plan detail view
def plan_detail(request, id):
    # Get the plan by its primary key or return a 404 error if not found
    plan = get_object_or_404(Plans, pk=id)

    # Render the plan detail template with the plan context
    return render(request, 'plans/plan_detail.html', {'plans': plan})



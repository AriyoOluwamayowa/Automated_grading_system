from django.shortcuts import render, redirect
from .forms import UserCreationForm, CustomUser, StudentRegistrationForm, InstructorRegistrationForm
from django.contrib.auth.forms import authenticate
from django.contrib.auth import login  # Make sure to import the login function
from .forms import StudentLoginForm, InstructorLoginForm  # Import your custom login forms


# Home view
def home(request):
    return render(request, "home.html")

# Student registration view
def register_student(request):

    if request.method == 'POST':  # Checks if the request is a POST request
        form = StudentRegistrationForm(request.POST)  # Instantiates the form with POST data
        if form.is_valid():  # Checks form validity
            new_user = form.save(commit=False)  # Saves the form but doesn't commit to database yet
            new_user.user_type = 'STUDENT'  # Sets the user_type to STUDENT
            new_user.save()  # Commits the save to the database
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            
            # Authenticates and logs in the user
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('AccountsApp:login_student')  # Redirects to home page
        else:
            print("Form is not valid")  # Prints an error message if the form is invalid
            print(form.errors)  # Prints form errors
    else:
        form = StudentRegistrationForm()  # Instantiates an empty form if the request is not POST

    return render(request, 'AccountsApp/register_student.html', {'form': form})  # Renders the registration page


def register_instructor(request):
    if request.method == 'POST':  # Checks if the request is a POST request
        form = InstructorRegistrationForm(request.POST)  # Instantiates the form with POST data
        if form.is_valid():  # Checks form validity
            user = form.save(commit=False)  # Saves the form but doesn't commit to the database yet
            user.user_type = 'INSTRUCTOR'  # Sets the user_type to 'INSTRUCTOR'
            user.save()  # Commits the save to the database
            
            print("User saved")  # Prints a message indicating the user has been saved
            
            # It's often good to authenticate and login the user right after registration
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            
            return redirect('AccountsApp:login_instructor')  # Redirects to the instructor login page
        else:
            print("Form is not valid")  # Prints an error message if the form is invalid
            print(form.errors)  # Prints form errors
    else:
        form = InstructorRegistrationForm()  # Instantiates an empty form if the request is not POST

    return render(request, 'AccountsApp/register_instructor.html', {'form': form})  # Renders the registration page

from django.contrib.auth import authenticate, login

def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') or form.cleaned_data.get('matric_number')
            password = form.cleaned_data.get('password')
            
            # Use the custom authentication
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')
    else:
        form = StudentLoginForm()
    return render(request, 'AccountsApp/login_student.html', {'form': form})


# Function to handle instructor login
def login_instructor(request):
    if request.method == 'POST':  # Check if the request is a POST request
        form = InstructorLoginForm(data=request.POST)  # Instantiate the form with POST data
        if form.is_valid():  # Check if the form is valid
            user = form.get_user()  # Get the authenticated user object
            login(request, user)  # Log the user in
            return redirect('instructor_dashboard')  # Redirect to the instructor dashboard
    else:
        form = InstructorLoginForm()  # Instantiate an empty form for GET request
    return render(request, 'AccountsApp/login_instructor.html', {'form': form})  # Render the login page

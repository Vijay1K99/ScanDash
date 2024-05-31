import glob
import os
import csv
import xml.etree.ElementTree as ET
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# from django.contrib.auth.forms import  PasswordChangeForm

# Views Of Home Page
def home(request):
    return render(request, 'project/home.html')


# Views Of Signup Page
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations..!! You have Successfully signed in')
            form.save() 
            form = SignUpForm()  
    else:
        form = SignUpForm()
    return render(request, 'project/signup.html', {'form': form})


# Views Of Login Page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'project/login.html', {'form': form})
    else:
      return HttpResponseRedirect('/dashboard/')


# Views Of Dashboard
def dashboard(request):
    # Define the path to your CSV file
    csv_file_path = os.path.join(
        'D:\\Study\\shallVhack1\\shallvhack\\scanout.csv'
    )

    # Data containers for the entire CSV data
    csv_data = []
    csv_data1 = []
    csv_data2 = []

    # Variable to count occurrences of the word "filtered"
    filtered_word_count = 0

    # Read the CSV file to extract all data
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Read the header
        header = next(csv_reader)
        
        # Iterate over the CSV rows to extract data and count occurrences of "filtered"
        for row in csv_reader:
            csv_data.append(row)
            if len(row) >= 5:
                csv_data1.append(row[0])  # Assume IPs are in the first column
                csv_data2.append(row[1])  # Assume ports are in the second column

            # Count the occurrences of "filtered" in the entire row
            if "filtered" in " ".join(row):
                filtered_word_count += 1

    # Calculate statistics for IPs and ports
    total_ips = len(csv_data1)
    unique_ips = len(set(csv_data1))
    total_ports = len(csv_data2)
    unique_ports = len(set(csv_data2))

    # Find the number of XML files in a specific folder
    xml_folder_path = os.path.join('D:\\Study\\shallVhack1\\shallvhack')  # Adjust the path to your XML folder
    xml_files = glob.glob(os.path.join(xml_folder_path, '*.xml'))
    num_xml_files = len(xml_files)

    # Create the context dictionary to pass data to the template
    context = {
        'name': request.user.username,
        'header': header,  # Pass the header to the template
        'csv_data': csv_data,  # Pass all CSV data to the template
        'total_ips': total_ips,
        'unique_ips': unique_ips,
        'total_ports': total_ports,
        'unique_ports': unique_ports,
        'filtered_word_count': filtered_word_count,  # Number of times "filtered" is found
        'num_xml_files': num_xml_files,  # The count of XML files
    }

    # Render the template with the context data
    return render(request, 'project/dashboard.html', context)


# change password with old password 
# def user_change_pass(request):
#     if request.method == "POST":
#         fm = PasswordChangeForm(user=request.user, data=request.POST)
#         if fm.is_valid():
#             update_session_auth_hash(request, fm.user)
#             return HttpResponseRedirect('/login/')
#     else:
#         fm = PasswordChangeForm(user=request.user)
#     return render(request, 'project/changepass.html',{'form':fm})


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
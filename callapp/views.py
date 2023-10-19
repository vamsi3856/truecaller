# import subprocess
# from django.shortcuts import render

# # Create your views here.
# def lookup(request):
#     return render(request, "lookup.html")

# def truecaller_info(request):
#     if request.method=="POST":
#         phone_number = request.POST.get("contact")  # Replace with the phone number you want to lookup
#         lst=phone_number.split(',')
#         command_lst=[]
#         for i in lst:
#             command = f"truecallerpy -s {i} --name"
#             command_lst.append(command)
#             # print(command)
#         dct={}
#         for i in command_lst:
#             try:
#                 output = subprocess.check_output(i, shell=True, text=True)
#             except subprocess.CalledProcessError as e:
#                 output = f"Error: {e}"
#             # context = {
#             #     'phone_number': phone_number,
#             #     'command_output': output,
#             # }
#             dct[i]=output
#         return render(request, 'result.html', dct)
import subprocess
from django.shortcuts import render

def lookup(request):
    return render(request, "lookup.html")

def truecaller_info(request):
    if request.method == "POST":
        phone_numbers = request.POST.get("contact")  # Replace with the phone numbers you want to lookup
        phone_numbers_list = phone_numbers.split(',')
        results = {}

        for phone_number in phone_numbers_list:
            command = f"truecallerpy -s {phone_number.strip()} --name"
            try:
                output = subprocess.check_output(command, shell=True, text=True)
            except subprocess.CalledProcessError as e:
                output = f"Error: {e}"
            results[phone_number] = output

        context = {
            'results': results,
        }
        return render(request, 'result.html', context)

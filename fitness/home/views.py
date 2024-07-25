from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from.models import Payment, Trainers,otp
from .forms import AdmissionForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def trainers(request):
    dict_trainer={
        'trainers':Trainers.objects.all()
    }
    return render(request,'trainers.html',dict_trainer)


def admission(request):
  
  if request.method=="POST":
      print(request.method)
  form=AdmissionForm(request.POST)
  if form.is_valid():
      form.save()
      return render(request,'payment.html')
  form=AdmissionForm()
  dict_form={
      'form':form
  }
  return render(request,'admission.html', dict_form)


# def payment(request):
#    return render(request,'payment.html')

# views.py



def payment(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        card_number = request.POST.get('card_number')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')
        # Create a new payment instance
        payment = Payment.objects.create(
            person_name=person_name,
            card_number=card_number,
            expiry=expiry,
            cvv=cvv
        )
        # Redirect to a success page or perform further actions
        return redirect('otp')

    return render(request, 'payment.html')


# def otp(request):
#    return render(request,'otp.html')

# views.py



def otp(request):
    if request.method == 'POST':
        # # Retrieve OTP code entered by the user
        # otp_code = ''.join(request.POST.getlist('otp'))
        
        # # Check if the entered OTP code exists in the database
        # if otp.objects.filter(code=otp_code).exists():
        #     messages.success(request, 'OTP verified successfully!')
      return redirect('confirmation.html')
    else:
            # messages.error(request, 'Invalid OTP. Please try again.')

       return render(request, 'otp.html')



def confirmation(request):
    return render(request,'confirmation.html')






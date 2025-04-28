from django.shortcuts import render, redirect
from . models import Register_table, Band, Carttable
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def concerts(request):
    return render(request, 'concerts.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')
 
def usertable(request):
    obb = Register_table.objects.all()
    return render(request, 'users.html',{"data":obb})

def signup(request):
    if request.method == 'POST':
        username = request.POST['Username'] # username is the name of the input field in the login.html
        password = request.POST['Password'] # password is the name of the input field in the login.html
        obj = Register_table.objects.create(username=username, password=password)
        obj.save()
        if obj:
            return redirect("/login/")
        else:
            return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        obj = Register_table.objects.filter(username=username, password=password)
        if obj:
            request.session['session_variable1'] = username #session is a temporary storage location for the username and password from server side
            request.session['session_variable2'] = password
            for item in obj:
                idl = item.id
            request.session['idn'] = idl
            return render(request,'home.html')
        else:
            msg = "Invalid Username or Password..." #error message to be displayed is stored in msg variable
            return render(request,'login.html', {"error": msg} )#we give the error message as a dictionary in key value pairs:error is the key name

    return render(request,'login.html')

def edit(request,pk):
    obj = Register_table.objects.filter(id=pk)
    if request.method == 'POST':
        fnm = request.POST.get('first')
        pswd = request.POST.get('second')
        idl =request.POST.get('id')
        object = Register_table.objects.filter(id=idl)
        object.update(username=fnm, password=pswd)
        return redirect("/usertable/")
    return render(request,'edit.html',{"data":obj})

def delete(request,pk):
    obj = Register_table.objects.filter(id=pk)
    obj.delete()
    return redirect("/usertable/")

def addBand(request):
    if request.method == 'POST':
        band_name= request.POST['band_name']
        band_image= request.FILES['band_image']
        band_price= request.POST['band_price']
        band_description= request.POST['band_description']
        obj = Band.objects.create(band_name=band_name, band_image=band_image, band_price=band_price, band_description=band_description)
        obj.save()
        if obj:
            msg = "Band Added Successfully"
            return render(request,'addBand.html',{"message": msg})
    return render(request,'addBand.html')

def cards(request):
    obj = Band.objects.all()
    return render(request,'cards.html',{"data":obj})

def addTOcart(request,pk):
    cid = request.session['idn']
    prodobj = Band.objects.get(id=pk)
    custobj = Register_table.objects.get(id=cid)
    cartitem, created = Carttable.objects.get_or_create(customer=custobj, product=prodobj)
    if not created:
        cartitem.quantity += 1
        cartitem.save()
        messages.success(request, "added another..")
    messages.success(request, "Item added to cart")
    return redirect("/cards/")

def cart(request):
    idn = request.session['idn']
    cobj = Register_table.objects.get(id=idn)
    cartobject = Carttable.objects.filter(customer=cobj)
    if cartobject:
        total = 0
        for item in cartobject:
            total += item.product.band_price * item.quantity
        return render(request,'cart.html',{"data":cartobject,"total":total})
    else:
        msg = "No items in cart"
        return render(request,'cart.html',{"data":cartobject,"message":msg})
    
def remove_from_cart(request, pk):
    cartitem = Carttable.objects.get(id=pk)
    cartitem.delete()
    messages.success(request, "Item removed from cart")
    return redirect("/cart/")

def email(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        msg = "Thank you for your message, we will get back to you soon."
        return render(request,'contact.html',{"message": msg})
    return render(request,'email.html')
# Create your views here.

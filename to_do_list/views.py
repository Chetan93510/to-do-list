from django.shortcuts import render, redirect, HttpResponse
from django.utils.decorators import method_decorator

from .models import To_do, Gallery

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib import sessions


from .utils import filter_todo_with_id

# Create your views here.
# def name(request):

#     if request.method == "POST":
#         title = request.POST.get('title')
#         desc = request.POST.get('desc')
#         print(title)
#         print(desc)

#     return render(request,'index.html')

    
# @login_required(login_url="/login")
class Home(View):
        template_name = "index.html"

        @method_decorator(cache_page(60*15))
        @method_decorator(login_required(login_url="/login"))
        def get(self,request):
            #  todo = filter_todo_with_id(1)
             todo = To_do.objects.all()
             return render (request, self.template_name, {'todo': todo, 'gallery':Gallery.objects.all()})
        
class TodoCreateView(CreateView):
    model = To_do
    fields = ['title', 'description']
    success_url = '/'
    template_name = "add.html"


class TodoDeleteView(DeleteView):
    model = To_do
    success_url = '/'
    template_name = "delete.html"



class TodoUpdateView(UpdateView):
    model = To_do
    fields = ['title','description']
    success_url = '/'
    template_name = "edit.html"


class RegisterView(View):
        template_name = "register.html"

        def get(self,request):
             return render (request, self.template_name)
        
        def post(self, request):
            username = request.POST.get('username')
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            c_password = request.POST.get('c_password')


            if (User.objects.filter(username=username).exists()):
                 messages.error(request, "Username is already exists")
                 return redirect('/register')
            
            if (User.objects.filter(email=email).exists()):
                messages.error(request, "Email is already exists")
                return redirect('/register')
            
            if (password != c_password):
                messages.error(request, "Password and confirm password does not match")
                return redirect('/register')
            


            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()



            messages.success(request, "Successfully Registered..")
            return redirect('register')
        
class LoginView(View):
     
    template_name = 'login.html'


    def get(self, request):
         return render(request, self.template_name)


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
             login(request, user)
             messages.success(request, 'Logged In')
             return redirect('/')
        else:
             messages.error(request, "Invalid username or password")
             return redirect('login')
        

def mailSendView(request):
    name = "aman"
    # send_mail(
    #     "Test Mail From Django",
    #     f"<h1>Hello, {name}</h1>",
    #     "chetanmalav9692@gmail.com",
    #     ["amansoniji326@gmail.com"],
    #     fail_silently=False,
    # )

    context = {'name1':'rohit', 'name2':'AMan'}

    subject = "hello"
    from_email = "chetanmalav9692@gmail.com"
    to = "amansoniji326@gmail.com"
    text_content = "This is an important message."
    html_message = render_to_string('email_template.html', context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to, "rohitkrbxr11@gmail.com"])
    msg.attach_alternative(html_message, "text/html")
    msg.send()
    messages.success(request, "Successfully sent.")

    return redirect('/')




class GalleryCreateView(CreateView):
    model = Gallery
    fields = '__all__'
    template_name = "gallery.html"
    success_url = "/"



class SessionView(View):
     template =  'session.html'   

     products = [
             {
             'id': 1,
                'name': 'Laptop',
             'price': 52000
             },
             {
             'id': 2,
                'name': 'Mouse',
             'price': 150
             },
             {
             'id': 3,
                'name': 'Phone',
             'price': 15000
             }
        ]

     def get(self, request):
        cart_items = request.session.get('cart') or []
        items = []
        total = 0
        for item in cart_items:
            obj_index = item['product_id']
            obj = self.products[int(obj_index) - 1]
            obj['quantity'] = item['quantity']
            price = obj['price'] * obj['quantity']

            total = total + price
            items.append(obj)

        print(total)
        print(items)
        return render(request, self.template, {'products': self.products, 'cart_items': item})
     
     def post(self, request):
            cart = request.session.get('cart') or []
            prod_id = request.POST.get('product_id')
            quantity = request.POST.get('quantity')

            obj = {'product_id': prod_id,'quantity':quantity}

            cart.append(obj)

            request.session['cart'] = cart

            return redirect('s')

        
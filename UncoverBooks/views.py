from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, contact, Orders, OrderUpdate, ProductComment
from sklearn.metrics.pairwise import cosine_similarity
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
import pandas as pd
import json
import csv
import pickle


def index(request):
    products = Product.objects.all()
    params = {'product': products}
    return render(request, 'UncoverBooks/index1.html',params)


# def searchMatch(query, item):
#     if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.author_name.lower() or query in item.genre.lower():
#         return True
#     else:
#         return False


def search(request):
    query = request.GET.get('search')
    if len(query) == 0:
        pro = Product.objects.none()
    elif len(query) == 100:
        pro = Product.objects.none()
    else:
        # products = Product.objects.all()
        productName = Product.objects.filter(product_name__icontains=query)
        productDesc = Product.objects.filter(product_desc__icontains=query)
        productAuthName = Product.objects.filter(author_name__icontains=query)
        productGenre = Product.objects.filter(genre__icontains=query)
        pro = productName.union(productAuthName,productDesc,productGenre)
    # pro = [item for item in products if searchMatch(query,item)]
    params = {'product': pro, "query": query}
        # return render(request, 'UncoverBooks/index1.html',params)
    return render(request, 'UncoverBooks/search.html', params)


def tracker(request):
    if request.method =="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(ord_id = orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJSON":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{{"status":"error"}')

    return render(request, 'UncoverBooks/tracker.html')


def about(request):
    return render(request, 'UncoverBooks/about.html')


def cart(request):
    return render(request, 'UncoverBooks/cart.html')


def contact_us(request):
    if request.method == "POST":
        desc = request.POST.get('desc', '')
        con = contact(desc=desc)
        con.save()
    return render(request, 'UncoverBooks/contact.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    lis = recommendation(product[0])
    for i in lis:
        pass
    comment = ProductComment.objects.filter(post=product[0])
    return render(request, 'UncoverBooks/product_view.html', {'product': product[0], 'comments': comment, 'user': request.user, 'recommendation': lis})


def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postId = request.POST.get('postId')
        post = Product.objects.get(id=postId)
        comment = ProductComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request, "Your comment has been posted!")
    return redirect(f'product/{postId}')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        amount = request.POST.get('amount', '')
        order = Orders(items_json=items_json, name=name, email=email, address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, phone=phone,amount=amount)
        order.save()
        thank = True
        update = OrderUpdate(order_id=order.ord_id, update_desc="The order has been placed")
        update.save()
        id = order.ord_id
        return render(request, 'UncoverBooks/checkout.html', {'thank':thank,'id':id})
    return render(request, 'UncoverBooks/checkout.html')


def login(request):
    return render(request, 'UncoverBooks/login_page.html')


def handelLogin(request):
    if request.method =='POST':
        username = request.POST['uname']
        # email = request.POST['email']
        psw = request.POST['loginpsw']

        user = authenticate(username=username, password=psw)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("Home Page")
        else:
            messages.error(request,"Please enter the valid credentials")
            return redirect("login")
    return HttpResponse('404- Page Not found')


def handelLogout(request):
    # if request.method == "POST":
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("Home Page")


def signup(request):
    return render(request, 'UncoverBooks/signup_page.html')


def handelSignUp(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        if len(username) < 5:
            messages.success(request, "Username is too short!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')

        if psw != psw_repeat:
            messages.success(request, "Passwords do not match!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, psw)
        myuser.save()
        messages.success(request, "Account Created")
        return redirect('Home Page')
    else:
        return HttpResponse('404- Page Not found')


# def novel(request):
#     prod = Product.objects.filter(genre__icontains='Novel')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/novel.html',params)
#
#
# def textbook(request):
#     prod = Product.objects.filter(genre__icontains='Textbooks')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/textbook.html',params)
#
#
# def narrative(request):
#     prod = Product.objects.filter(genre__icontains='Narrative')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/narrative.html',params)
#
#
# def nonfiction(request):
#     prod = Product.objects.filter(genre__icontains='NonFiction')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/nonfiction.html',params)
#
#
# def mystery(request):
#     prod = Product.objects.filter(genre__icontains='Mystery')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/mystery.html',params)
#
#
# def poetry(request):
#     prod = Product.objects.filter(genre__icontains='Poetry')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/poetry.html',params)
#
#
# def horror(request):
#     prod = Product.objects.filter(genre__icontains='Horror')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/horror.html',params)
#
#
# def romance(request):
#     prod = Product.objects.filter(genre__icontains='Romance')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/romance.html',params)
#
#
# def humor(request):
#     prod = Product.objects.filter(genre__icontains='Humor')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/humor.html',params)
#
#
# def crime(request):
#     prod = Product.objects.filter(genre__icontains='Crime')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/crime.html',params)
#
#
# def fantasy(request):
#     prod = Product.objects.filter(genre__icontains='Fantasy')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/fantasy.html',params)
#
#
def genre_display(request, gen):
    prod = Product.objects.filter(genre__icontains=gen)
    params = {'product': prod,'genre':gen}
    return render(request, 'UncoverBooks/genre_display.html', params)
#
#
# def fiction(request):
#     prod = Product.objects.filter(genre__icontains='Fiction')
#     params = {'product': prod}
#     return render(request, 'UncoverBooks/fiction.html',params)


def exportcsv(request):
    product = Product.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=database.csv'
    writer = csv.writer(response)
    writer.writerow(['Index','id', 'product_name', 'product_desc', 'author_name', 'genre', 'price', 'created_at','image'])
    studs = product.values_list('Index','id', 'product_name', 'product_desc', 'author_name', 'genre', 'price', 'created_at','image')
    for std in studs:
        writer.writerow(std)
    return response


def get_title_from_index(Index):
    return Product.objects.get(Index=Index)


def get_index_from_title(BookTitle):
    return Product.objects.filter(product_name=BookTitle).values_list('Index')[0][0]



def recommendation(Book):
    tfv_matrix = pd.read_pickle('UncoverBooks/tfidf.pickle')
    cosine = cosine_similarity(tfv_matrix)
    recommended_books = []

    def get_recommendations(book):
        book_index = get_index_from_title(book)
        similar_books = list(enumerate(cosine[book_index]))
        sortedbooks = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:]
        i = 0
        for book in sortedbooks:
            recommended_books.append(get_title_from_index(book[0]))
            i = i + 1
            if i > 5:
                break

    get_recommendations(Book)
    return recommended_books
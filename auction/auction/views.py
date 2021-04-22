from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.utils import timezone

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listings')
        else:
            return render(request, 'login.html', {'error': 'Fill in correct credentials.'})
    
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('login')

    form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def view_listings(request):
    listings = Listing.objects.order_by('-id')
    return render(request, 'listings.html', {'listings': listings})


@login_required(login_url='login')
def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'lay.html', {'categories': categories})


@login_required(login_url='login')
def view_category(request, id):
    category = Category.objects.filter(id=id)
    return render(request, 'category.html', {'category': category})


@login_required(login_url='login')
def view_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    bid = Bid.objects.filter(listing=listing.id)
    comments = Comment.objects.filter(listing=listing_id)
    if bid:
        bid = bid[(len(bid[:]) - 1)]
    if comments:
        comments = listing.comment_set.order_by('-date_time')

    return render(request, 'listing.html', {'listing': listing, 'bid': bid,
                'comments': comments, 'note': 'Bid must be greater than current bid.'})
        

@login_required(login_url='login')
def create_listing(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        create_cat = request.POST.get('create-cat')
        image = request.FILES.get('image')

        if request.user.is_authenticated:
            user = request.user
            auctioneer, create = Auctioneer.objects.get_or_create(user=user)

        if category != 'none':
            category = Category.objects.get(name=category)
        elif category == 'none':
            category, create = Category.objects.get_or_create(auctioneer=auctioneer, name=create_cat)

        listing = Listing.objects.create(user=user, auctioneer=auctioneer, name=name, category=category,
                                        description=description, price=price, image=image)
        return redirect('listings')
            
    categories = Category.objects.all()
    return render(request, 'create.html', {'categories': categories})


@login_required(login_url='login')
def process_bid_and_comment(request, listing_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            bidder, create = Bidder.objects.get_or_create(user=user)

        listing = Listing.objects.get(id=request.POST.get('listing'))
        bid = request.POST.get('bid')
        comment = request.POST.get('comment')

        bids = Bid.objects.filter(listing=listing.id)

        if not listing.sold_out:
            if bid:
                if int(bid) <= listing.price:
                    return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
                elif not bids:
                    bid = Bid.objects.create(user=user, bidder=bidder, listing=listing, bid=bid,
                                            date_time=timezone.now())
                    if comment:
                        comment = Comment.objects.create(user=user, listing=listing,
                                            comment=comment, date_time=timezone.now())
                    return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
                else:
                    current_bid = bids[(len(bids[:]) - 1)].bid
                    if int(bid) <= current_bid:  
                        return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
                    else:
                        bid = Bid.objects.create(user=user, bidder=bidder, listing=listing, bid=bid,
                                                date_time=timezone.now())
                        if comment:
                            comment = Comment.objects.create(user=user, listing=listing,
                                                comment=comment, date_time=timezone.now())                   
                        return HttpResponseRedirect(reverse('listing', args=(listing.id,)))                
            else:
                comment = Comment.objects.create(user=user, listing=listing,
                                            comment=comment, date_time=timezone.now())
        else:
            if comment:
                comment = Comment.objects.create(user=user, listing=listing,
                                            comment=comment, date_time=timezone.now())
        auctioneers = Auctioneer.objects.all()
        for auctioneer in auctioneers:
            if user == auctioneer.user:
                if user.comment_set.all():
                    comments = user.comment_set.filter(comment='close')
                    for comment in comments:
                        if f'{comment}' == 'close':
                            item = user.listing_set.get(id=listing_id)
                            item.sold_out = True
                            item.save()
                            comments.delete()
            
        return HttpResponseRedirect(reverse('listing', args=(listing.id,)))   


@login_required(login_url='login')
def watchlist(request):
    if request.user.is_authenticated:
        user = request.user

    watchlist_items = WatchList.objects.filter(user=user).order_by('-id')

    return render(request, 'watch.html', {'watches': watchlist_items})


@login_required(login_url='login')
def add_to_watchlist(request, pk):
    if request.user.is_authenticated:
        user = request.user
    
    listing = get_object_or_404(Listing, pk=pk)
    watch, create = WatchList.objects.get_or_create(user=user, listing=listing)
    return redirect('watchlist')


@login_required(login_url='login')
def delete_from_watchlist(request, pk):
    watch = WatchList.objects.filter(id=pk).delete()
    return redirect('watchlist')        
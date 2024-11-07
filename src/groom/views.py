from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import GiftForm, GuestForm
from .models import Gift, Guest, Escorts
from django.http import HttpResponse


def groomHome(request):
    ctx = {}
    gifts = Gift.objects.all()

    if request.method == "POST":
        form = GiftForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()

            return redirect(reverse('home'))
    else:
        form = GiftForm()

    reservated = gifts.filter(reservated=True).count()
    not_reservated = gifts.filter(reservated=False).count()

    ctx['form'] = form
    ctx['gifts'] = gifts
    ctx['reservated'] = reservated
    ctx['not_reservated'] = not_reservated

    return render(
        request,
        'groom/home.html',
        ctx
    )


def guests(request):
    ctx = {}
    guests = Guest.objects.all()

    if request.method == "POST":
        form = GuestForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect(reverse('guests'))
    else:
        form = GuestForm()

    ctx['form'] = form
    ctx['guests'] = guests
    return render(request, 'groom/guests.html', ctx)


def seeGuests(request):
    ctx = {}

    token = request.GET.get('token')
    guest = get_object_or_404(Guest, token=token)
    gifts = Gift.objects.filter(reservated=False).order_by('-importance')
    escorts = Escorts.objects.filter(guest=guest)
    
    ctx['guest'] = guest
    ctx['gifts'] = gifts
    ctx['escorts'] = escorts

    return render(request, 'groom/see_guest.html', ctx)


def answerInvite(request):
    token = request.GET.get('token')
    answer = request.GET.get('answer')
    guest = get_object_or_404(Guest, token=token)

    guest.status = answer

    guest.save()

    return redirect(f'{reverse('see_guests')}?token={guest.token}')


def reserveGift(request, uid): 
    token = request.GET.get('token')
    guest = get_object_or_404(Guest, token=token)

    gift = get_object_or_404(Gift, uid=uid)
    gift.reservated_by = guest
    gift.reservated = True

    gift.save()

    return redirect(f'{reverse('see_guests')}?token={guest.token}')


def addEscort(request):
    token = request.GET.get('token')
    guest = get_object_or_404(Guest, token=token)
    if request.method == "POST":
        name = request.POST.get('name')

        if guest.max_escorts > 0:
            escort = Escorts.objects.create(
                escort=name,
                guest=guest
            )
            guest.max_escorts -= 1
            
    
    return redirect(f'{reverse('see_guests')}?token={guest.token}')
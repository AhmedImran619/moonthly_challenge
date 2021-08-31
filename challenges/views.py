from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

challenges = {
    'january': 'Challenge 1',
    'febuary': 'Challenge 2',
    'march': 'Challenge 3',
    'april': 'Challenge 4',
    'may': 'Challenge 5',
    'june': 'Challenge 6',
    'july': 'Challenge 7',
    'august': 'Challenge 8',
    'september': 'Challenge 9',
    'october': 'Challenge 10',
    'november': 'Challenge 11',
    'december': None,
    # 'december': 'Challenge 12',
}


# Create your views here.

def index(request):
    months = list(challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    month_list = list(challenges.keys())

    if month > len(month_list):
        redirect_path = reverse("month_challenge", args=[str(month)+'-'])
        return HttpResponseRedirect(redirect_path)

    month_to_redirect = month_list[month-1]
    redirect_path = reverse("month_challenge", args=[month_to_redirect])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = challenges[month]
        print(challenge)

        return render(request, 'challenges/challenge.html', context={
            'challenge': challenge,
            'month': month
        })
    except:
        raise Http404()

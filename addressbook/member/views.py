from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    members = Member.objects.all().order_by('-pk')
    return render(
        request,
        'member/index.html',
        {
            'members' : members
        }
    )
def detail(request, pk):
    member_detail = Member.objects.get(pk=pk)
    return render(
        request,
        'member/detail.html',
        {
            'm': member_detail
        }
    )
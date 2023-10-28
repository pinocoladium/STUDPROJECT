from django.http import HttpResponse

def home_view(request):
    al = HttpResponse(f'<div></b>Настя</b>, привет, <div> мы сегодня поедем <div>в магазин?<div>')
    return al

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
# ----------------email------------------------
from django.utils.html import strip_tags
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage

from .form import EmployeeForm, EmailForm
from .models import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            success = request.session['success'] = 'Employees created successfully'
            return render(request, 'form.html', {'form': form, 'success': success})
    else:
        form = EmployeeForm()  # use_required_attribute=False use to remove required attr in input tag
        # form.order_fields(field_order=['email', 'name']) use to order fields in template

    return render(request, 'form.html', {'form': form, 'title': 'Create'})


def empList(request):
    search = request.GET.get('search', None)
    if search:
        emp = Employee.objects.filter(
            Q(email__icontains=search) | Q(name__icontains=search)
        )
    else:
        emp = Employee.objects.all().order_by('id')
        paginator = Paginator(emp, 2)
        page_number = request.GET.get('page')
        emp = paginator.get_page(page_number)
    return render(request, 'listing.html', {'emp': emp})


def empUpdate(request, pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=emp)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'form.html', {'form': form, 'title': 'Update'})


def empDelete(request, pk):
    emp = Employee.objects.get(id=pk)
    if emp:
        emp.delete()
        return redirect('/')


def empView(request, pk):
    emp = Employee.objects.get(id=pk)
    if emp:
        emp.views += 1
        emp.save()
        return render(request, 'view.html', {'emp': emp})


def page_not_found(request, exception):
    return render(request, '404.html')


def empEmail(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'Test Django'
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('contact')
            to = form.cleaned_data.get('email')

            html_content = get_template("email_template.html").render({'name': name, 'message': message})
            try:
                email = EmailMessage(
                                subject,
                                html_content,
                                settings.APPLICATION_EMAIL,
                                [to],
                                headers={'Message-ID': 'foo'},
                                # reply_to=[settings.APPLICATION_EMAIL]
                            )
                email.content_subtype = 'html'
                success_sent = email.send(fail_silently=False)
                if success_sent:
                    success = request.session['success'] = 'Sent successfully'
            except:
                success = request.session['success'] = 'Sent failed'
            return render(request, 'form.html', {'form': form, 'success': success})
    else:
        form = EmailForm()
    return render(request, 'form.html', {'form': form, 'title': 'Sent Email'})


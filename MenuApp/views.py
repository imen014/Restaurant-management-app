from django.shortcuts import render, redirect, get_object_or_404
from MenuApp.models import MenuAppModel, Eater
from MenuApp.forms import CreateMenuApp, EaterForm, EaterFormUpdater




def create_menu(request):
    form = CreateMenuApp()
    message = ''
    if request.method=="POST":
        form = CreateMenuApp(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.menu_creator = request.user
            form.save()
            return redirect('get_menus')
    return render(request, 'MenuApp/menu_created.html', {'form':form, 'message':message})

def get_menus(request):
    menus = MenuAppModel.objects.all()
    return render(request, 'MenuApp/get_menu.html', {'menus':menus})


def update_menu(request, id):
    menu_instance = get_object_or_404(MenuAppModel, id=id)
    menu_form=CreateMenuApp(instance=menu_instance)
    if request.method=="POST":
            menu_form=CreateMenuApp(request.POST, request.FILES, instance=menu_instance)
            if menu_form.is_valid():
                 menu_form.save(commit=False)
                 menu_instance.menu_updater = request.user
                 menu_form.save()
    return render(request, 'MenuApp/menu_updated.html', {'menu_instance':menu_instance, 'menu_form':menu_form})

def delete_menu(request, id):
    menu_instance = get_object_or_404(MenuAppModel, id=id)
    menu_instance.delete()
    return redirect('get_menus')

def create_eater(request):
    eater_form = EaterForm()
    eater_instance = Eater()
    message = ''
    if request.method=="POST":
        eater_form = EaterForm(request.POST, request.FILES)
        if eater_form.is_valid():
            menu_type_name = eater_form.cleaned_data['menu_type']
            #menu_type_instance = MenuAppModel.objects.get(menu_type_food=menu_type_name)
            menu_type_instance = MenuAppModel.objects.filter(menu_type_food=menu_type_name).first()


            eater_instance.name = eater_form.cleaned_data['name']
            eater_instance.description = eater_form.cleaned_data['description']
            eater_instance.price = eater_form.cleaned_data['price']
            eater_instance.image= eater_form.cleaned_data['image']
            eater_instance.menu_type = menu_type_instance
            eater_instance. creator= request.user
            eater_instance.save()
            message = "eater created"
            return redirect('get_eaters')
        else:
            message = "verify data !"
    return render(request, 'MenuApp/eater_created.html',{'eater_form':eater_form,'eater_instance':eater_instance,'message':message})

def get_eaters(request):
    eaters = Eater.objects.all()
    return render(request, 'MenuApp/get_eaters.html', {'eaters':eaters})


def update_eater(request, id):
    eater = get_object_or_404(Eater, id=id)
    eater_form=EaterFormUpdater(instance=eater)
    message = ''
    if request.method == "POST":
        eater_form=EaterFormUpdater(request.POST, request.FILES, instance=eater)
        if eater_form.is_valid():
            eater_form.save(commit=False)
            eater.updater = request.POST
            eater_form.save()
            eater.save()
            message = 'eater updated'
            return redirect('get_eaters')
    return render(request, 'MenuApp/eater_updated.html', {'eater_form':eater_form, 'message':message})


def delete_eater(request, id):
    eater = get_object_or_404(Eater, id=id)
    eater.delete()
    return redirect('get_eaters')

def show_eater(request, id):
    eater_instance = get_object_or_404(Eater, id=id)
    return render(request, 'MenuApp/show_eater.html', {'eater_instance':eater_instance})

from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from command_food_app.forms import CommandFormCreator
from command_food_app.models import Command




def create_command(request):
    command = CommandFormCreator()
    message = ''
    if request.method == "POST":
        command = CommandFormCreator(request.POST)
        if command.is_valid():
            command.creator = request.user
            command.save()
            message = 'success'
    return render(request, 'command_food_app/command.html', {'command':command,'message':message})


def get_commands(request, place_of_delivery):
    commands = get_list_or_404(Command, place_of_delivery=place_of_delivery)
    return render(request, 'command_food_app/commands_by_place.html', {'commands':commands})

def get_commands_by_phone_number(request, command_client_phone_number):
    commands = get_list_or_404(Command, command_client_phone_number=command_client_phone_number)
    return render(request, 'command_food_app/commands_by_phone.html', {'commands':commands})


def get_my_commands(request):
    commands = get_list_or_404(Command, creator=request.user)
    return render(request, 'command_food_app/get_my_commands.html', {'commands':commands})


def modify_command(request, id):
    command = get_object_or_404(Command, id=id)
    command_form = CommandFormCreator(instance=command)
    message = ''
    if request.method == "POST":
        command_form = CommandFormCreator(request.POST, instance=command)
        if command_form.is_valid():
            command_form.save()
            message = 'success'
    return render(request,'command_food_app/command_modified.html',{'command_form':command_form,'message':message} )

def delete_command(request, id):
    command = get_object_or_404(Command, id=id)
    command.delete()
    return redirect('')


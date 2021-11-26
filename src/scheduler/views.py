from django.shortcuts import render,redirect

from scheduler.form import QueueForm
from scheduler.regression_algorithm import reg_model
from datetime import timedelta


def home_view(request):
    
    context = {}
    # Checks if the user is login
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        # Instantiate the form
        p_form = QueueForm(request.POST)
        # checks if the form imput is valid
        if p_form.is_valid():
            # print(p_form.cleaned_data)
            # Gets the form values
            p_arrival = p_form.cleaned_data.values()
            
            arrival_time_minute = []
            
            for t in p_arrival:
                # Split the hour and minute by :
                # mins = t.split(':')
                delta = timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1])) 
                
                minutes = delta.total_seconds()/60
                # print(minutes)
                arrival_time_minute.append(minutes) 
                 
                # Gets the minute
                # arrival_time_minute.append(mins) 
                
            print(arrival_time_minute)
            
            # Linear regression model 
            prediction = reg_model(arrival_time_minute) 
            total_p_schedule = prediction['total_min']/prediction['avg_time']
            context['total_p_schedule'] = total_p_schedule
            print(total_p_schedule)
            
            wait_time = []
            
            for i in arrival_time_minute:
                # Check track the first element in the array
                if arrival_time_minute.index(i) == 0:
                    p_waiting_time = prediction['avg_time']
                    print('Patients waiting time: ', p_waiting_time)
                    wait_time.append(int(p_waiting_time))
                    
                    # Delete the first element 
                    arrival_time_minute.pop(0)
                    
                # Calculate patient waiting time 
                p_waiting_time = prediction['avg_time'] + int(i)
                print('Patients waiting time: ', int(p_waiting_time))
                wait_time.append(int(p_waiting_time))
                
            # print(wait_time)
            context['wait_time'] = wait_time
            
    else:
        p_form = QueueForm()
        context['p_form']  = p_form

    return render(request, 'scheduler/home.html', context)

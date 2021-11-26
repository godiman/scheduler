from django import forms

from scheduler.models import Queue

class QueueForm(forms.ModelForm):
    
    class Meta:
        model = Queue 
        
        fields = ('arrival_time1', 'arrival_time2', 'arrival_time3', 'arrival_time4')
    
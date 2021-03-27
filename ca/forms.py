from django import forms as f

class AvailabilityForm(f.Form):
     name = f.CharField(required=True)
     emp_no = f.IntegerField(required=True)
     check_in = f.DateTimeField(required=True, input_formats=["%d-%m-%Y",])     
     check_out = f.DateTimeField(required=True, input_formats=["%d-%m-%Y",])
     
             
    

from django.shortcuts import render
from .models import Rate
from django.http import Http404

# Display all routes and rates
def index(request):
    data = Rate.objects.all()
    return render(request, 'index.html', {'data': data})

# Handle the form submission for printing the ticket
def print_ticket(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        quantity = request.POST.get('quantity', 1)  # Default quantity to 1 if not provided

        try:
            id_check = Rate.objects.get(id=id)
            quantity = int(quantity)  # Ensure quantity is an integer
            amount = id_check.rate * quantity

            return render(request, 'index.html', {
                'data': Rate.objects.all(),
                'id_check': [id_check],  # Pass as a list to iterate in the template
                'amount': amount,
                'quantity': quantity,
                'rate': id_check.rate
            })
        except Rate.DoesNotExist:
            # Handle case where ID does not exist
            return render(request, 'index.html', {
                'data': Rate.objects.all(),
                'error': f'No rate found with ID: {id}'  # Display an error message
            })
    return render(request, 'index.html', {'data': Rate.objects.all()})

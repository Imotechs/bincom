from django.shortcuts import render,redirect
from .models import PollingUnit,Lga,AnnouncedPuResults,AnnouncedLgaResults,Ward
from django.views.generic import ListView,DetailView,CreateView
from django.db.models import Q
from .forms import PollingUnitForm
# Create your views here.

#quuestion 1
class HomeListView(ListView):
    def get_queryset(self):
        return PollingUnit.objects.all()
    context_object_name = 'pollunits'
    template_name = 'home.html'
    paginate_by = 10
home = HomeListView.as_view()

class PollDetailView(DetailView):
    model = PollingUnit
    template_name = 'detail.html'


#question 2
#creating volts results
#lets create a view that use both get and Post Method
def local_gov_results(request,*args,**kwargs):
    lga = Lga.objects.all()
    context = {
        'lga':lga,
        'poll_units': [],  # Initialize an empty list for poll_units
        'party_totals': {}, # same for each party scores
    }
    if request.method =='POST':
        
        selected_lga = request.POST['lga']
        if selected_lga=='none':
            return redirect('results')#reload the same page if search is not selected
        #use the selected local govt to get the polling units under it
        polling_units = PollingUnit.objects.filter(lga_id = selected_lga)
        #acquire the polling units results using the polling units id
        party_totals = {}  # Dictionary to store party totals
        #lga_name = Lga.objects.filter(lga_id = selected_lga)
        #lga_check = AnnouncedLgaResults.objects.filter(lga_name = '33')
        for unit in polling_units:
            unit_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = unit.polling_unit_id)
            result_list = list(unit_result)  # Convert the queryset to a list
            for result in result_list:
                party_name = result.party_abbreviation  # Assuming party_name is the key for party names
                party_score = result.party_score  # Assuming party_score is the key for party scores
                if party_name in party_totals:
                    party_totals[party_name] += party_score
                else:
                    party_totals[party_name] = party_score

            context['party_totals'] = party_totals
            context['search']=Lga.objects.filter(lga_id = selected_lga).first()
            #context['lga_check'] = lga_check

            unit_data = {
                'unit_id': unit.polling_unit_number,
                'unit_name': unit.polling_unit_name,
                'result': result_list,
                }
            context['poll_units'].append(unit_data)

    return render(request,'results.html',context)
    

# PU search view for search on PU names
def search(request):
    search_items = request.GET['item']
    search_result = PollingUnit.objects.filter(Q(polling_unit_name__icontains = search_items))
    context = {
        'searched_pu':search_result
    }
    return render(request,'search.html',context)


#question 3
#creating a new polling unit
class CreateUnitView(CreateView):
    #model = PollingUnit
    template_name = 'add_post.html'
    #fields = '__all__'
    form_class = PollingUnitForm

new_polling_unit = CreateUnitView.as_view()


from django.shortcuts import render
from django.http import HttpResponse
from .forms import EstimateForm
import pickle
import pandas as pd

# Charger le modèle entraîné
with open('model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def estimate(request):
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            zipcode = form.cleaned_data['zipcode']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft_living = form.cleaned_data['sqft_living']
            sqft_lot = form.cleaned_data['sqft_lot']
            floors = form.cleaned_data['floors']
            sqft_above = form.cleaned_data['sqft_above']
            sqft_basement = form.cleaned_data['sqft_basement']
            yr_built = form.cleaned_data['yr_built']
            yr_renovated = form.cleaned_data['yr_renovated']

            data = pd.DataFrame({
                'zipcode': [zipcode],
                'bedrooms': [bedrooms],
                'bathrooms': [bathrooms],
                'sqft_living': [sqft_living],
                'sqft_lot': [sqft_lot],
                'floors': [floors],
                'sqft_above': [sqft_above],
                'sqft_basement': [sqft_basement],
                'yr_built': [yr_built],
                'yr_renovated': [yr_renovated],
            })

            prediction = pipeline.predict(data)

            return render(request, 'result.html', {'prediction': prediction[0]})
    else:
        form = EstimateForm()

    return render(request, 'estimate.html', {'form': form})
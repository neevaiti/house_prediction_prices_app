from django.shortcuts import render
from django.http import HttpResponse
from .forms import EstimateForm
import pickle
import pandas as pd

def estimation(request):
    form = EstimateForm()
    return render(request, 'estimation.html', {'form': form})

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
            grade = form.cleaned_data['grade']
            view = form.cleaned_data['view']
            waterfront = form.cleaned_data['waterfront']
            condition = form.cleaned_data['condition']


            # Charger le modèle entraîné
            pickle_in = open('house_price/src/knn_model.pkl', 'rb')
            pipeline = pickle.load(pickle_in)

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
                'sqft_living15': [2000],
                'sqft_lot15': [8000],
                'grade': [7],
                'view': [0],
                'waterfront': [0],
                'condition': [3],
            })

            # Utilisation du modèle pour faire la prédiction
            prediction = pipeline.predict(data)

        return render(request, 'test.html', {'prediction': prediction[0]})
    else:
        form = EstimateForm()

        return render(request, 'estimation.html', {'form': form})

from django.shortcuts import render
import pickle
import pandas as pd
from .forms import EstimateForm

def estimation(request):
    form = EstimateForm()
    return render(request, 'house_prediction_app/client/estimation.html', {'form': form})

def estimate(request):
    if request.method == 'POST':
        estimation_form = EstimateForm(request.POST)
        if estimation_form.is_valid():
            zipcode = estimation_form.cleaned_data['zipcode']
            bedrooms = estimation_form.cleaned_data['bedrooms']
            bathrooms = estimation_form.cleaned_data['bathrooms']
            sqft_living = estimation_form.cleaned_data['sqft_living']
            sqft_lot = estimation_form.cleaned_data['sqft_lot']
            floors = estimation_form.cleaned_data['floors']
            sqft_above = estimation_form.cleaned_data['sqft_above']
            sqft_basement = estimation_form.cleaned_data['sqft_basement']
            yr_built = estimation_form.cleaned_data['yr_built']
            yr_renovated = estimation_form.cleaned_data['yr_renovated']
            grade = estimation_form.cleaned_data['grade']
            waterfront = estimation_form.cleaned_data['waterfront']
            condition = estimation_form.cleaned_data['condition']


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
                'grade': [grade],
                'waterfront': [waterfront],
                'condition': [condition],
            })

            # Utilisation du modèle pour faire la prédiction
            prediction = pipeline.predict(data)

            # Ajouter la nouvelle estimation dans le contexte et rediriger vers la page de résultats
            context = {'prediction': prediction}
            return render(request, 'house_prediction_app/client/reveal_estimation.html', context)
    else:
        form = EstimateForm()
    # Afficher le formulaire pour la première fois ou afficher le formulaire avec des erreurs de validation
    return render(request, 'house_prediction_app/client/estimation.html', {'form': estimation_form})

# def estimate(request):
#     if request.method == 'POST':
#         form = EstimateForm(request.POST)
#         if form.is_valid():
#             zipcode = form.cleaned_data['zipcode']
#             bedrooms = form.cleaned_data['bedrooms']
#             bathrooms = form.cleaned_data['bathrooms']
#             sqft_living = form.cleaned_data['sqft_living']
#             sqft_lot = form.cleaned_data['sqft_lot']
#             floors = form.cleaned_data['floors']
#             sqft_above = form.cleaned_data['sqft_above']
#             sqft_basement = form.cleaned_data['sqft_basement']
#             yr_built = form.cleaned_data['yr_built']
#             yr_renovated = form.cleaned_data['yr_renovated']
#             grade = form.cleaned_data['grade']
#             waterfront = form.cleaned_data['waterfront']
#             condition = form.cleaned_data['condition']
#
#
#             # Charger le modèle entraîné
#             pickle_in = open('house_price/src/knn_model.pkl', 'rb')
#             pipeline = pickle.load(pickle_in)
#
#             data = pd.DataFrame({
#                 'zipcode': [zipcode],
#                 'bedrooms': [bedrooms],
#                 'bathrooms': [bathrooms],
#                 'sqft_living': [sqft_living],
#                 'sqft_lot': [sqft_lot],
#                 'floors': [floors],
#                 'sqft_above': [sqft_above],
#                 'sqft_basement': [sqft_basement],
#                 'yr_built': [yr_built],
#                 'yr_renovated': [yr_renovated],
#                 'grade': [grade],
#                 'waterfront': [waterfront],
#                 'condition': [condition],
#             })
#
#             # Utilisation du modèle pour faire la prédiction
#             prediction = pipeline.predict(data)
#
#         return render(request, 'reveal_estimation.html', {'prediction': prediction})
#     else:
#         form = EstimateForm()
#
#         return render(request, 'estimation.html', {'form': form})

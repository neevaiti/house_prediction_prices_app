from django import forms


class EstimateForm(forms.Form):
    # Champs pour les caractéristiques de la propriété
    bedrooms = forms.IntegerField(label='Nombre de chambres', min_value=0, max_value=20)
    bathrooms = forms.IntegerField(label='Nombre de salles de bain', min_value=0, max_value=20)
    sqft_living = forms.IntegerField(label='Surface habitable (en pieds carrés)', min_value=0, max_value=50000)
    sqft_lot = forms.IntegerField(label='Surface du terrain (en pieds carrés)', min_value=0, max_value=1000000)
    floors = forms.FloatField(label='Nombre d\'étages', min_value=0, max_value=10)
    waterfront = forms.ChoiceField(label='Vue sur l\'eau', choices=[('0', 'Non'), ('1', 'Oui')], widget=forms.RadioSelect)
    condition = forms.ChoiceField(label='Etat de la propriété', choices=[('1', 'Mauvais'), ('2', 'Médiocre'), ('3', 'Moyen'), ('4', 'Bon'), ('5', 'Excellent')], widget=forms.RadioSelect)
    grade = forms.ChoiceField(label='Classe de la propriété', choices=[('1', 'Basique'), ('2', 'Moyen'), ('3', 'Bonne'), ('4', 'Très bonne'), ('5', 'Excellente')], widget=forms.RadioSelect)
    sqft_above = forms.IntegerField(label='Surface habitable à l\'étage (en pieds carrés)', min_value=0, max_value=10000)
    sqft_basement = forms.IntegerField(label='Surface habitable en sous-sol (en pieds carrés)', min_value=0, max_value=10000)
    yr_built = forms.IntegerField(label='Année de construction', min_value=1800, max_value=2023)
    yr_renovated = forms.IntegerField(label='Année de rénovation', min_value=0, max_value=2023)
    zipcode = forms.IntegerField(label='Code postal', min_value=0, max_value=99999)


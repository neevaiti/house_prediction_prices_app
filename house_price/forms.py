from django import forms

zipcodes_select = [
    ('zip_98001', '98001'), ('zip_98002', '98002'), ('zip_98003', '98003'), ('zip_98004', '98004'),
    ('zip_98005', '98005'), ('zip_98006', '98006'), ('zip_98007', '98007'), ('zip_98008', '98008'),
    ('zip_98010', '98010'), ('zip_98011', '98011'), ('zip_98014', '98014'), ('zip_98019', '98019'),
    ('zip_98022', '98022'), ('zip_98023', '98023'), ('zip_98024', '98024'), ('zip_98027', '98027'),
    ('zip_98028', '98028'), ('zip_98029', '98029'), ('zip_98030', '98030'), ('zip_98031', '98031'),
    ('zip_98032', '98032'), ('zip_98033', '98033'), ('zip_98034', '98034'), ('zip_98038', '98038'),
    ('zip_98039', '98039'), ('zip_98040', '98040'), ('zip_98042', '98042'), ('zip_98045', '98045'),
    ('zip_98052', '98052'), ('zip_98053', '98053'), ('zip_98055', '98055'), ('zip_98056', '98056'),
    ('zip_98058', '98058'), ('zip_98059', '98059'), ('zip_98065', '98065'), ('zip_98070', '98070'),
    ('zip_98072', '98072'), ('zip_98074', '98074'), ('zip_98075', '98075'), ('zip_98077', '98077'),
    ('zip_98092', '98092'), ('zip_98102', '98102'), ('zip_98103', '98103'), ('zip_98105', '98105'),
    ('zip_98106', '98106'), ('zip_98107', '98107'), ('zip_98108', '98108'), ('zip_98109', '98109'),
    ('zip_98112', '98112'), ('zip_98115', '98115'), ('zip_98116', '98116'), ('zip_98117', '98117'),
    ('zip_98118', '98118'), ('zip_98119', '98119'), ('zip_98122', '98122'), ('zip_98125', '98125'),
    ('zip_98126', '98126'), ('zip_98133', '98133'), ('zip_98136', '98136'), ('zip_98144', '98144'),
    ('zip_98146', '98146'), ('zip_98148', '98148'), ('zip_98155', '98155'), ('zip_98166', '98166'),
    ('zip_98168', '98168'), ('zip_98177', '98177'), ('zip_98178', '98178'), ('zip_98188', '98188'),
    ('zip_98198', '98198'), ('zip_98199', '98199')]

class EstimateForm(forms.Form):
    # Champs pour les caractéristiques de la propriété
    bedrooms = forms.IntegerField(label='Nombre de chambres', min_value=0, max_value=20)
    bathrooms = forms.IntegerField(label='Nombre de salles de bain', min_value=0, max_value=20)
    sqft_living = forms.IntegerField(label='Surface habitable (en pieds carrés)', min_value=0, max_value=50000)
    sqft_lot = forms.IntegerField(label='Surface du terrain (en pieds carrés)', min_value=0, max_value=1000000)
    floors = forms.FloatField(label='Nombre d\'étages', min_value=0, max_value=10)
    waterfront = forms.ChoiceField(label='Vue sur l\'eau', choices=[('1', 'Oui'), ('0', 'Non')], widget=forms.RadioSelect)
    condition = forms.ChoiceField(label='Etat de la propriété', choices=[('1', 'Mauvais'), ('2', 'Médiocre'), ('3', 'Moyen'), ('4', 'Bon'), ('5', 'Excellent')], widget=forms.RadioSelect)
    grade = forms.ChoiceField(label='Classe de la propriété', choices=[('1', 'Basique'), ('2', 'Moyen'), ('3', 'Bonne'), ('4', 'Très bonne'), ('5', 'Excellente')], widget=forms.RadioSelect)
    sqft_above = forms.IntegerField(label='Surface habitable à l\'étage (en pieds carrés)', min_value=0, max_value=10000)
    sqft_basement = forms.IntegerField(label='Surface habitable en sous-sol (en pieds carrés)', min_value=0, max_value=10000)
    yr_built = forms.IntegerField(label='Année de construction', min_value=1800, max_value=2023)
    yr_renovated = forms.IntegerField(label='Année de rénovation', min_value=0, max_value=2023)
    zipcode = forms.CharField(widget=forms.Select(choices=zipcodes_select))
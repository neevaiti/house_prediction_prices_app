import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('../../components_machine_learning/house_cleaned_datas.csv')


# Features
numeric_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_living15', 'sqft_lot15', 'floors', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'grade', 'view', 'waterfront', 'condition']
categorical_features = ['zipcode']


# Transformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder()

# Pre-processing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features),
    ])

# Définition du Pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', KNeighborsRegressor(n_neighbors=5))])

X = df.drop(['price', 'lat', 'long', 'date'], axis=1)
y = df['price']

# Entraînement du modèle
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor.fit_transform(X)

# On laisse une parti du pipeline en entraînement
pipeline.fit(X_train, y_train)

# On passe l'étape de la prédiction aux tests
y_pred = pipeline.predict(X_test)

with open('knn_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)


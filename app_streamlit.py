import streamlit as st
import requests
import json

# Barre latérale
st.sidebar.title("Prédiction de la Progression du Diabète")
st.sidebar.write("Cette application utilise un modèle de régression pour prédire la progression du diabète en fonction de plusieurs indicateurs médicaux.")

# Titre de l'application
st.title("🩺 Prédiction de la Progression du Diabète")

# Introduction
st.write("Veuillez entrer les données nécessaires pour la prédiction ci-dessous :")

# Créer des colonnes pour organiser les entrées
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Âge', min_value=0.0, help="Âge du patient")
    sex = st.selectbox('Sexe', options=[0, 1], format_func=lambda x: 'Femme' if x == 0 else 'Homme', help="Sexe du patient (0: Femme, 1: Homme)")
    bmi = st.number_input('BMI (Indice de Masse Corporelle)', min_value=0.0, help="Indice de masse corporelle")
    bp = st.number_input('Pression Artérielle', min_value=0.0, help="Pression artérielle du patient")

with col2:
    s1 = st.number_input('S1: Taux de Cholestérol', min_value=0.0, help="Niveau de cholestérol du patient")
    s2 = st.number_input('S2: Lipoprotéines de Basse Densité', min_value=0.0, help="Niveau de lipoprotéines de basse densité")
    s3 = st.number_input('S3: Glycémie', min_value=0.0, help="Niveau de glycémie")
    s4 = st.number_input('S4: Lipoprotéines de Haute Densité', min_value=0.0, help="Niveau de lipoprotéines de haute densité")
    s5 = st.number_input('S5: Indice de Sensibilité à l’Insuline', min_value=0.0, help="Sensibilité à l'insuline")
    s6 = st.number_input('S6: Taux de Triglycérides', min_value=0.0, help="Niveau de triglycérides")

# Bouton pour soumettre les données
if st.button("🔍 Prédire la Progression du Diabète"):
    # Créer un dictionnaire avec les données
    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "bp": bp,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "s4": s4,
        "s5": s5,
        "s6": s6
    }

    # Convertir en JSON
    input_json = json.dumps(input_data)

    # Envoyer la requête à l'API
    api_url = "http://127.0.0.1:8000/predict"  # L'URL de ton API FastAPI
    response = requests.post(api_url, data=input_json, headers={"Content-Type": "application/json"})

    # Afficher la prédiction ou les erreurs
    if response.status_code == 200:
        st.success(f"✨ Prédiction de la progression du diabète : {response.text}")
    else:
        st.error("🚨 Une erreur est survenue lors de la prédiction. Veuillez vérifier les données saisies ou réessayer plus tard.")

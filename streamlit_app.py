import streamlit as st  # Zorg dat Streamlit geïmporteerd is

# Simpele validatie met vaste gebruikersnaam en wachtwoord
USERNAME = "admin"
PASSWORD = "GrowSustain123"

# Controleer of de gebruiker is ingelogd door de sessiestatus te gebruiken
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.title("ESG Index Assessment")

    if not st.session_state['logged_in']:
        # Gebruikersinvoer voor username en wachtwoord
        username = st.text_input("Gebruikersnaam")
        password = st.text_input("Wachtwoord", type="password")

        # Als op de knop wordt geklikt
        if st.button("Login"):
            # Controleer de inloggegevens
            if username == USERNAME and password == PASSWORD:
                st.success("Succesvol ingelogd!")
                st.session_state['logged_in'] = True
            else:
                st.error("Ongeldige gebruikersnaam of wachtwoord.")
    else:
        st.success("Succesvol ingelogd!")

    # Als de gebruiker is ingelogd, toon de link naar de ESG Assessment
    if st.session_state['logged_in']:
        st.write("Dit is de link naar de ESG Index Assessment. Klik op de link hieronder om de vragenlijst in te vullen.")
        typeform_url = "https://df64pnmoip3.typeform.com/to/J2UguXTi"
        st.markdown(f'<a href="{typeform_url}" target="_blank">Klik hier om naar de ESG Index Assessment te gaan</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    login()

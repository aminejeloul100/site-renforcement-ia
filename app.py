"""
Site — Renforcement des compétences des enseignants pour l'IA.
Accès réservé aux utilisateurs inscrits. La page d'accueil présente
le contenu du rapport, avec une vidéo pour ceux qui préfèrent regarder
plutôt que lire.
"""
from pathlib import Path

import streamlit as st

from auth import login, register
from contenu import CHAPITRES, VIDEO_URL

BASE_DIR = Path(__file__).parent
PDF_PATH = BASE_DIR / "data" / "Renforcement_competences_enseignants_IA_v2.pdf"

st.set_page_config(page_title="Renforcement des compétences IA — Enseignants", page_icon="🧠", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None


def ecran_auth():
    st.title("🧠 Renforcement des compétences en IA")
    st.caption("Accès réservé — connectez-vous ou créez un compte pour continuer")

    onglet = st.radio("", ["Se connecter", "Créer un compte"], horizontal=True, label_visibility="collapsed")

    if onglet == "Se connecter":
        with st.form("login"):
            username = st.text_input("Nom d'utilisateur")
            password = st.text_input("Mot de passe", type="password")
            ok = st.form_submit_button("Se connecter")
        if ok:
            if not username or not password:
                st.error("Merci de remplir tous les champs.")
            else:
                success, msg = login(username, password)
                if success:
                    st.session_state.user = username
                    st.rerun()
                else:
                    st.error(msg)
    else:
        with st.form("register"):
            username = st.text_input("Nom d'utilisateur")
            password = st.text_input("Mot de passe", type="password")
            ok = st.form_submit_button("Créer le compte")
        if ok:
            if not username or not password:
                st.error("Merci de remplir tous les champs.")
            else:
                success, msg = register(username, password)
                (st.success if success else st.error)(msg)


def page_accueil():
    st.title(f"🧠 Bonjour {st.session_state.user}")
    st.subheader("Renforcement des compétences des enseignants pour l'IA")
    st.caption("Résumé du rapport — pour le détail complet, télécharge le PDF en bas de page")

    st.divider()
    st.markdown("### 🎬 Vous préférez regarder plutôt que lire ?")
    st.video(VIDEO_URL)
    st.caption("Vidéo d'introduction simple sur l'intelligence artificielle, pour ceux qui veulent une explication en image.")

    st.divider()
    st.markdown("### 📖 Les points clés du rapport")

    for chap in CHAPITRES:
        with st.container(border=True):
            col_icone, col_texte = st.columns([1, 6])
            with col_icone:
                st.markdown(f"<div style='font-size:40px;text-align:center'>{chap['icone']}</div>", unsafe_allow_html=True)
            with col_texte:
                st.markdown(f"**{chap['titre']}**")
                st.write(chap["texte"])

    st.divider()
    st.markdown("### 📄 Le rapport complet")
    if PDF_PATH.exists():
        with open(PDF_PATH, "rb") as f:
            st.download_button(
                "⬇️ Télécharger le rapport complet (PDF)",
                data=f.read(),
                file_name="Renforcement_competences_enseignants_IA.pdf",
                mime="application/pdf",
            )
    else:
        st.info("Place le fichier PDF dans le dossier data/ pour activer le téléchargement.")

    st.divider()
    if st.button("Se déconnecter"):
        st.session_state.user = None
        st.rerun()


if st.session_state.user is None:
    ecran_auth()
else:
    page_accueil()

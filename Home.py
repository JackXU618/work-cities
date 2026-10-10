import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Work Cities")
st.write("Welcome to the Work Cities multipage Streamlit app. Use the button below to open the App page located in the pages folder.")

# Try to navigate to the multipage "App" page when the button is clicked.
# Streamlit's multipage navigation is handled by the toolbar, but we can set a query
# parameter as a best-effort navigation method and provide a direct link fallback.
if st.button("Open App"):
    try:
        # This sets a query parameter that Streamlit's UI may use to switch pages.
        st.experimental_set_query_params(page="App")
        st.experimental_rerun()
    except Exception:
        # If experimental API isn't available, show a message and fallback link.
        st.write("Unable to programmatically navigate. Use the link below to open the App page.")

st.markdown("---")
st.markdown("If the button doesn't navigate automatically, open the App page directly: [Open App](/?page=App)")

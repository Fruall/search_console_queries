import searchconsole
import streamlit as st
import pandas as pd

client_config ='client_secret_22068898197-ekqrfbiun76idmt0qiotqqimbkq1cedg.apps.googleusercontent.com.json'

connect_button = st.button('Connect')

account = None

def get_queries_number(siteUrl):
    webproperty = account[siteUrl]
    report = len(webproperty.query.range('today', days=-7).dimension('query').get())
    return report

if connect_button:

    account = searchconsole.authenticate(client_config=client_config,
                                         serialize='credentials.json')
    raw_properties = account.service.sites().list().execute().get('siteEntry', [])

    df = pd.DataFrame(raw_properties)
    df = df.drop(df[df.permissionLevel == 'siteUnverifiedUser'].index)

    df['Queries_Number'] = df['siteUrl'].apply(get_queries_number)

    st.write(df)


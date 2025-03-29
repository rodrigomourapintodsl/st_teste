import streamlit as st


@st.cache_data
def sqlteste():
    conn = st.connection("postgresql_servidor", type="sql")
    df = conn.query("SELECT EMPRESA.DSAPELIDO FROM EMPRESA;", 
                                     ttl=3600,
                                     show_spinner=None,
                                    #  params={idserie,dataini,datafim},
                                     )
    
if st.button("testesql"):
    st.write(sqlteste())


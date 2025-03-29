import streamlit as st

# Initialize connection.
conn = st.connection("postgresql_servidor", type="sql")

# Perform query.
df = conn.query('SELECT dsapelido,idserie FROM empresa;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.dsapelido} has a :{row.idserie}:")
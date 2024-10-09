import streamlit as st
from mem0 import MemoryClient

# Initialize MemoryClient
memory_client = MemoryClient(api_key='m0-4UuhqcTbRS8LrfkXwOGMvtx5VvWQZmvpWvwL6aqI')

# Define user IDs
user_ids = ['researcher', 'risk manager', 'junior trader']

# Streamlit app
st.title("Memory Training App")

# Create a form for each user ID
for user_id in user_ids:
    st.header(f"Configure Memory for {user_id}")
    includes = st.text_input(f"Includes for {user_id}", "sports related things")
    messages = st.text_area(f"Messages for {user_id}", "Enter messages separated by new lines")
    
    if st.button(f"Train {user_id}"):
        # Split messages by new lines
        message_list = messages.split('\n')
        print('mesages', message_list)
        # Add memory for the user with each message
        for message in message_list:
            memory_client.add(message, user_id=user_id, includes=includes)
        st.success(f"Memory trained for {user_id} with includes: {includes} and messages: {message_list}")

# Query section
st.header("Query Memory")
selected_user_id = st.selectbox("Select User ID", user_ids)
query = st.text_input("Enter your query")

if st.button("Query Memory"):
    # Here you would implement the logic to query the memory
    # For demonstration, we'll just display the query
    st.write(f"Querying memory for {selected_user_id} with query: {query}")
    response= memory_client.search(query, user_id=selected_user_id)
    st.write(response)
    # Example: response = memory_client.query(query, user_id=selected_user_id)
    # st.write(response)

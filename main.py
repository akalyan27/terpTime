import streamlit as st


st.write("Hello world")

def create_form(id): 
    with st.form(f"form_{id}"):
        st.write("Put your sections in here")
        courseTicker = st.selectbox(
            'Course: ', 
            ("CMSC131", "CMSC132", "CMSC216"),
            index=None,
            placeholder="e.g `CMSC131`")
        
        sectionTicker = st.selectbox(
            "Section: ", 
            ("0101", "0102", "0103"),
            index=None,
            placeholder="e.g `0101`")
        st.form_submit_button("Submit")

def main():

    if 'num_forms' not in st.session_state:
        st.session_state['num_forms'] = 1
    # session_state = st.session_state.setdefault("num_forms", 1)

    if st.button("Add another section"):
        st.session_state['num_forms'] += 1
        
    for i in range(st.session_state['num_forms']):
        create_form(i + 1)

        

st.button("Submit")



if __name__ == '__main__':
    main()
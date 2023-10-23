import streamlit as st
import pandas as pd
import numpy as np

def calculate_points(match_type, win_loss, score, challenger=None):
    sets = score.split(',')
    # ... (rest of the function code remains the same)
    return ('Invalid input', 'Invalid input')

def main():
    st.title('Match Points Calculator')

    try:
        data = pd.read_csv('data.csv')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame()

    # Bulk upload option
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        bulk_data = pd.read_csv(uploaded_file)
        st.write("Uploaded data:")
        st.table(bulk_data)
        if st.button('Append Uploaded Data'):
            try:
                data = pd.read_csv('data.csv')
            except (FileNotFoundError, pd.errors.EmptyDataError):
                data = pd.DataFrame()
            data = pd.concat([data, bulk_data]).reset_index(drop=True)
            data.to_csv('data.csv', index=False)

    # Existing dropdowns and input boxes


    names_list = [
        'Akihiro Hamada',
        'Alejandro',
        'Alex Paisecki',
        'Aman Luther',
        'Aubry Carmody',
        'Baaqir Yusuf',
        'Beomjun Ju',
        'Billy Clark',
        'Blake Hutchinson',
        'Brady Sowers',
        'Brandon Keisner',
        'Brett Eckles',
        'Byron Byars',
        'Chris LaFlam',
        'Chris Mack',
        'Christian Basa',
        'Craig Radley',
        'Curt Lawson',
        "Dan Nenon",
        'Dave Belcher',
        'Ed Sch',
        'Erik Swanson',
        'Ezra Sue-Ho',
        'Henry Kennelly',
        'Ian VonWald',
        'JB',
        'JD Mellott',
        'Jackson Cabell',
        'Jake Ortiz',
        'James Rees',
        'Joaquin Peralta',
        'Jon Canon',
        'Josh Collins',
        'JP Rufilffson',
        'Kwame Owen',
        'Louis Crow',
        'Luc Sanchez',
        'Matt Curry',
        'Matt Hanauer',
        'Matt James',
        'Max Gregson',
        'Naveen Natesh',
        'Nick Gilder',
        'Nick Lau',
        'Russell Li',
        'Ryan Berliner',
        'Ryan Lewis',
        'Spencer Johnson',
        'Spencer Llewellyn',
        'Thomas Gaither',
        'Tommy Hibbs',
        'Tyler Carroll',
        'Visakan',
        'Wes Watson',
        'Youngjun Lee'
    ]

    
    
    name_me = st.selectbox('Select your name:', names_list)
    name_opponent = st.selectbox('Select your opponent:', names_list)
    match_type = st.selectbox('Select the match type:', ['Proposal Match', 'Challenge Match'])
    
    challenger = None
    if match_type == 'Challenge Match':
        challenger = st.selectbox('Are you the Challenger or the Challenged?', ['Challenger', 'Challenged'])

    win_loss = st.selectbox('Select Win or Loss:', ['Win', 'Loss'])
    score = st.text_input('Enter the score:')

    if st.button('Calculate Points'):
        points_me, points_opponent = calculate_points(match_type, win_loss, score, challenger)
        
        data = data.append({
            'Name': name_me,
            # ... (rest of the player's data)
            'Points': points_me
        }, ignore_index=True)

        data = data.append({
            'Name': name_opponent,
            # ... (rest of the opponent's data)
            'Points': points_opponent
        }, ignore_index=True)

    if not data.empty:
        st.table(data)
        
        # Option to delete a row
        selected_row = st.selectbox('Select a row to delete:', range(len(data)), format_func=lambda x: f'Row {x}')
        if st.button('Delete selected row'):
            data = data.drop(selected_row).reset_index(drop=True)
        
    data.to_csv('data.csv', index=False)

if __name__ == "__main__":
    try:
        data = pd.read_csv('data.csv')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame()

    if not data.empty and 'Name' in data.columns:
        total_points = data.groupby('Name')['Points'].sum().sort_values(ascending=False)
        st.write("Total Points:")
        st.table(total_points)
    else:
        st.write("No data available or 'Name' column missing.")

    main()

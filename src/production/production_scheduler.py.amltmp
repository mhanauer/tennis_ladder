import streamlit as st
import pandas as pd
import numpy as np

def calculate_points(match_type, win_loss, score, challenger=None):
    sets = score.split(',')
    
    if match_type == 'Proposal Match':
        if win_loss == 'Win':
            if len(sets) > 2:
                return (2, 1)
            return (2, 0)
        elif win_loss == 'Loss':
            if len(sets) > 2:
                return (1, 2)
            else:
                return (0, 2)
    elif match_type == 'Challenge Match':
        if win_loss == 'Win':
            if len(sets) > 2 or '0-1' in sets or '1-0' in sets:
                return (3, 1)
            else:
                return (3, 0)
        elif win_loss == 'Loss':
            if len(sets) > 2 or '0-1' in sets or '1-0' in sets:
                return (1, 3)
            else:
                return (-1 if challenger == 'Challenger' else 0, 3)
    return ('Invalid input', 'Invalid input')

def main():
    st.title('Match Points Calculator')

    # Load existing data
    try:
        data = pd.read_csv('data.csv')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame()
    
    # Bulk Upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        bulk_data = pd.read_csv(uploaded_file)
        data = pd.concat([data, bulk_data]).reset_index(drop=True)

    

    names_list = [
        'Akihiro Hamada',
        'Alejandro',
        'Alex Paisecki',
        'Aman Luther',
        'Aubry Carmody',
        'Baaqir Yusuf',
        'Barry Gooch'
        'Beomjun Ju',
        'Billy Clark',
        'Blake Hutchinson',
        'Blake Watkins',
        'Brady Sowers',
        'Brandon Keisner',
        'Brett Eckles',
        'Byron Byars',
        'Chris LaFlam',
        'Chris Mack',
        'Christian Basa',
        'Craig Radley',
        'Curt Lawson',
        "David Nenon",
        'Daniel Gallo',
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
        'Kevin Moyung',
        'Kwame Owen',
        'Louis Crow',
        'Luc Sanchez',
        'Manuel Mariategui',
        'Matt Curry',
        'Matt Hanauer',
        'Matt James',
        'Max Gregson',
        'Michael Young',
        'Naveen Natesh',
        'Nick Gilder',
        'Nick Lau',
        'Russell Li',
        'Ryan Berliner',
        'Ryan Lewis',
        'Skeet',
        'Spencer Johnson',
        'Spencer Llewellyn',
        'Thomas Gaither',
        'Tommy Hibbs',
        'Tyler Carroll',
        'Visakan',
        'Wes Watson',
        'Youngjun Lee',
        'Zack C',
        'Mike P',
        'Russell Li',
        'Mo Dessouky'
    ]

    

    name_me = st.selectbox('Select your name:', names_list)
    name_opponent = st.selectbox('Select your opponent:', names_list)

    match_type = st.selectbox('Select the match type:', ['Proposal Match', 'Challenge Match'])
    
    challenger = None
    if match_type == 'Challenge Match':
        challenger = st.selectbox('Are you the Challenger or the Challenged?', ['Challenger', 'Challenged'])

    win_loss = st.selectbox('Select Win or Loss:', ['Win', 'Loss'])
    score = st.text_input('Enter the score:', '')

    if st.button('Calculate Points'):
        points_me, points_opponent = calculate_points(match_type, win_loss, score, challenger)

        data = data.append({
            'Name': name_me,
            'Opponent': name_opponent,
            'Match Type': match_type,
            'Challenger/Challenged': challenger,
            'Win/Loss': win_loss,
            'Score': score,
            'Points': points_me
        }, ignore_index=True)

        data = data.append({
            'Name': name_opponent,
            'Opponent': name_me,
            'Match Type': match_type,
            'Challenger/Challenged': 'Challenged' if challenger == 'Challenger' else 'Challenger',
            'Win/Loss': 'Win' if win_loss == 'Loss' else 'Loss',
            'Score': score,
            'Points': points_opponent
        }, ignore_index=True)

    if not data.empty:
        st.table(data)
        
        # Delete a row
        selected_row = st.selectbox('Select a row to delete:', range(len(data)), format_func=lambda x: f'Row {x}')
        if st.button('Delete selected row'):
            data = data.drop(selected_row).reset_index(drop=True)
    
    # Save data
    data.to_csv('data.csv', index=False)

    # Display total points
    data['Points'] = pd.to_numeric(data['Points'], errors='coerce')
    data.dropna(subset=['Points'], inplace=True)
    
    if not data.empty and 'Name' in data.columns:
        try:
            total_points = data.groupby('Name')['Points'].sum().sort_values(ascending=False)
            st.write("Total Points:")
            st.table(total_points)
        except Exception as e:
            st.write(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

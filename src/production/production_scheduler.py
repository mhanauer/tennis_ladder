import streamlit as st
import pandas as pd

def calculate_points(match_type, win_loss, score, challenger=None):
    sets = score.split(',')

    if match_type == 'Proposal Match':
        if win_loss == 'Win':
            return 2
        elif win_loss == 'Loss':
            if len(sets) > 2:  
                return 1
            else: 
                return 0

    elif match_type == 'Challenge Match':
        if win_loss == 'Win':
            return 3
        elif win_loss == 'Loss':
            if len(sets) > 2 or '0-1' in sets or '1-0' in sets: 
                return 1
            else:
                return -1 if challenger == 'Challenger' else 0

    return 'Invalid input'

def main():
    st.title('Match Points Calculator')

    # Load data from the previous session
    try:
        data = pd.read_csv('data.csv')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame()

    names_list = ['Matt Hanauer', 'Max Gregson', 'Alejandro', 'Aman Luther', 'Baaqir Yusuf', 'Billy Clark', 'Blake Hutchinson', 'Brady Sowers', 'Brett Eckles', 'Byron Byars', 'Craig Radley', 'Curt Lawson', 'Ed Sch', 'Erik Swanson', 'Ezra Sue-Ho', 'Henry Kennelly', 'Jackson Cabell', 'Jake Ortiz', 'James Rees', 'JB', 'JD Mellott', 'Jon Canon', 'Louis Crow', 'Luc Sanchez', 'Matt Curry', 'Matt James', 'Naveen Natesh', 'Ryan Berliner', 'Spencer Johnson', 'Spencer Llewellyn', 'Tommy Hibbs', 'Tyler Carroll', 'Visakan', 'Wes Watson', 'Youngjun Lee']

name = st.selectbox('Select your name:', names_list)
    match_type = st.selectbox('Select the match type:', ['Proposal Match', 'Challenge Match'])
    challenger = None
    if match_type == 'Challenge Match':
        challenger = st.selectbox('Are you the Challenger or the Challenged?', ['Challenger', 'Challenged'])
    win_loss = st.selectbox('Select Win or Loss:', ['Win', 'Loss'])
    score = st.text_input('Enter the score (e.g., "6-2, 6-3" for straight sets or "6-2, 3-6, 1-0" for split sets):')

    if st.button('Calculate Points'):
        points = calculate_points(match_type, win_loss, score, challenger)
        data = data.append({
            'Name': name,
            'Match Type': match_type,
            'Challenger/Challenged': challenger,
            'Win/Loss': win_loss,
            'Score': score,
            'Points': points
        }, ignore_index=True)

    if not data.empty:
        selected_row = st.selectbox('Select a row to delete:', range(len(data)), format_func=lambda x: f'Row {x+1}')
        if st.button('Delete selected row'):
            data = data.drop(selected_row)

    # Save data for the next session
    data.to_csv('data.csv', index=False)

    st.table(data)

    # Calculate the total points for each person
    total_points = data.groupby('Name')['Points'].sum()
    st.table(total_points)

if __name__ == "__main__":
    main()

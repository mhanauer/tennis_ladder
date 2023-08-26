import streamlit as st
import pandas as pd

def calculate_points(match_type, win_loss, score, challenger=None):
    sets = score.split(',')
    
    if match_type == 'Proposal Match':
        if win_loss == 'Win':
            return (2, 0)
        elif win_loss == 'Loss':
            if len(sets) > 2:  
                return (1, 2)
            else: 
                return (0, 2)

    elif match_type == 'Challenge Match':
        if win_loss == 'Win':
            return (3, -1 if challenger == 'Challenger' else 0)
        elif win_loss == 'Loss':
            if len(sets) > 2 or '0-1' in sets or '1-0' in sets: 
                return (1, 3)
            else:
                return (-1 if challenger == 'Challenger' else 0, 3)

    return ('Invalid input', 'Invalid input')

def main():
    st.title('Match Points Calculator')

    try:
        data = pd.read_csv('data.csv')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame()

    names_list = ['Matt Hanauer', 'Max Gregson', 'Alejandro', 'Aman Luther', 'Baaqir Yusuf', 'Billy Clark', 'Blake Hutchinson', 'Brady Sowers', 'Brett Eckles', 'Byron Byars', 'Craig Radley', 'Curt Lawson', 'Ed Sch', 'Erik Swanson', 'Ezra Sue-Ho', 'Henry Kennelly', 'Jackson Cabell', 'Jake Ortiz', 'James Rees', 'JB', 'JD Mellott', 'Jon Canon', 'Louis Crow', 'Luc Sanchez', 'Matt Curry', 'Matt James', 'Naveen Natesh', 'Ryan Berliner', 'Spencer Johnson', 'Spencer Llewellyn', 'Tommy Hibbs', 'Tyler Carroll', 'Visakan', 'Wes Watson', 'Youngjun Lee']
    
    name_me = st.selectbox('Select your name:', names_list)
    name_opponent = st.selectbox('Select your opponent:', names_list)

    match_type = st.selectbox('Select the match type:', ['Proposal Match', 'Challenge Match'])
    
    challenger = None
    if match_type == 'Challenge Match':
        challenger = st.selectbox('Are you the Challenger or the Challenged?', ['Challenger', 'Challenged'])

    win_loss = st.selectbox('Select Win or Loss:', ['Win', 'Loss'])
    score = st.text_input('Enter the score (e.g., "6-2, 6-3" for straight sets or "6-2, 3-6, 1-0" for split sets):')

    if st.button('Calculate Points'):
        points_me, points_opponent = calculate_points(match_type, win_loss, score, challenger)
        
        if match_type == "Proposal Match":
            challenger_me = None
            challenger_opponent = None
        else:
            challenger_me = challenger
            challenger_opponent = 'Challenged' if challenger == 'Challenger' else 'Challenger'
        
        # Player's data
        data = data.append({
            'Name': name_me,
            'Opponent': name_opponent,
            'Match Type': match_type,
            'Challenger/Challenged': challenger_me,
            'Win/Loss': win_loss,
            'Score': score,
            'Points': points_me
        }, ignore_index=True)

        # Opponent's data
        data = data.append({
            'Name': name_opponent,
            'Opponent': name_me,
            'Match Type': match_type,
            'Challenger/Challenged': challenger_opponent,
            'Win/Loss': 'Loss' if win_loss == 'Win' else 'Win',
            'Score': score,
            'Points': points_opponent
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

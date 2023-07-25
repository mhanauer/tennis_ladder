import streamlit as st

def calculate_points(match_type, win_loss, score):
    # Split the score into individual sets
    sets = score.split(',')

    if match_type == 'Proposal Match':
        if win_loss == 'Win':
            return 2
        elif win_loss == 'Loss':
            # A split set loss will have more than one set
            if any('-1' in s for s in sets):  # Loss but won at least one set (split sets loss)
                return 1
            else:
                return 0  # Straight sets loss

    elif match_type == 'Challenge Match':
        if win_loss == 'Win':
            return 3
        elif win_loss == 'Loss':
            if any('-1' in s for s in sets):  # Loss but won at least one set (split sets loss)
                return 1
            elif '0-1' in sets:  # Challenger lost in straight sets
                return -1
            else:
                return 0  # Challenged lost in straight sets
                
    return 'Invalid input'

def main():
    st.title('Match Points Calculator')
    match_type = st.selectbox('Select the match type:', ['Proposal Match', 'Challenge Match'])
    win_loss = st.selectbox('Select Win or Loss:', ['Win', 'Loss'])
    score = st.text_input('Enter the score (e.g., "6-2, 6-3" for straight sets or "6-2, 3-6, 1-0" for split sets):')

    if st.button('Calculate Points'):
        points = calculate_points(match_type, win_loss, score)
        st.write(f'Points for this match: {points}')


if __name__ == "__main__":
    main()

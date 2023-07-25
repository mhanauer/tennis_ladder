import streamlit as st

def calculate_points(match_type, win_loss, score):
    # Split the score into individual sets
    sets = score.split(',')

    if match_type == 'Proposal Match':
        if win_loss == 'Win':
            return 2
        elif win_loss == 'Loss':
            if '0-1' in sets or '1-0' in sets:  # Split sets loss
                return 1
            else:  # Straight sets loss
                return 0

    elif match_type == 'Challenge Match':
        if win_loss == 'Win':
            return 3
        elif win_loss == 'Loss':
            if '0-1' in sets or '1-0' in sets:  # Split sets loss
                return 1
            else:  # Challenger or Challenged loses in straight sets
                return -1 if '0-1' in sets or '1-0' in sets else 0

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

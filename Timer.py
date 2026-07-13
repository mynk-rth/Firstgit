
import streamlit as st
import time

st.title("⏳ Countdown Timer")

seconds = st.number_input(
    "Enter countdown time (seconds)",
    min_value=1,
    value=10,
    step=10
)

# Session state
if "finished" not in st.session_state:
    st.session_state.finished = False

@st.dialog("Countdown ")
def timer():
    placeholder = st.empty()
    for i in range(seconds, 0, -1):
        
        hrs = i // 3600
        mins = (i % 3600) // 60
        secs = i % 60
        timer_text = f"{hrs:02}:{mins:02}:{secs:02}"

        placeholder.markdown(
            f"""
            <h1 style='text-align: center; color: Black; font-size: 100px;'>
                 {timer_text}
            </h1>
            """,
            unsafe_allow_html=True
        )

        time.sleep(1)
    # Mark complete
    st.session_state.finished = True
    # Close popup
    st.rerun()

# Start button
if st.button("Start Timer"):
    timer()


# Show after popup closes
if st.session_state.finished:

    st.markdown(
        """
        <h1 style='text-align:center;
                   color:green;
                   font-size:80px;'>
            🎉 Time's Up!
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.toast("Timer Finished 🚀")

    # Reset
    st.session_state.finished = False
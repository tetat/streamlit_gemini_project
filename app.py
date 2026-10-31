import streamlit as st
from PIL import Image
from api_calling import note_generator, audio_transcription, quiz_generator

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photos of your note",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
    )

    if images:
        if len(images) > 3:
            st.error("Please upload at max 3 images.")
        else:
            cols = st.columns(len(images))

            st.subheader("Uploaded Images")

            for i,img in enumerate(images):
                with cols[i]:
                    st.image(img, caption=f"Image {i+1}")

    # Difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    if selected_option:
        st.markdown(f"**Selected Difficulty:** {selected_option}")
    else:
        st.error("You must select a difficulty")

    pressed = st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    if not selected_option:
        st.error("You must select a difficulty")

    if images and selected_option:
        # note
        with st.container(border=True):
            st.subheader("Your note")
            # the portion below will be replaced by API call
            with st.spinner("AI is writing note for you."):
                generated_notes = note_generator(images)
                st.markdown(generated_notes)

        # audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")
            # the portion below will be replaced by API call
            with st.spinner("AI is generating audio note."):
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                # generated_notes = generated_notes.replace("")
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

        # quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            # the portion below will be replaced by API call
            with st.spinner("AI is generating quizzes."):
                quizzes = quiz_generator(images, selected_option)
                st.markdown(quizzes)

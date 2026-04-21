import streamlit as st
from api_call import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quizes")
st.divider()

with st.sidebar:
    st.header("Controls")

    #image part 
    images = st.file_uploader("Upload the photos of your notes",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True)

    if images:
        if (len(images)>3):
            st.error("Upload at most 3 images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)


    #difficulty 

    selected_option = st.selectbox("Enter the difficulty of quiz:",
    ("Easy","Medium","Hard"),
    index=None)  

    #if selected_option:
    #    st.markdown(f"You selected **{selected_option}** as your difficulty")
    #else:
    #    st.error("You must select a difficulty")


    #button
    pressed = st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload one image")
    if not selected_option:
        st.error("You must select a difficulty")
    
    if images and selected_option:

        #note
        with st.container(border=True):
            st.subheader("Your note")

            #the portion below will be replaced by API call
            with st.spinner("AI is writing notes for you"):
                
                

                generated_notes = note_generator(images)
                #cleared markdowns
                generated_notes=generated_notes.replace("#","")
                generated_notes=generated_notes.replace("*","")
                generated_notes=generated_notes.replace("-","")
                generated_notes=generated_notes.replace("_","")
                st.markdown(generated_notes)

        #audio
        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("AI is reading notes for you"):
                #the portion below will be replaced by API call
                audio_transcript= audio_transcription(generated_notes)
                st.audio(audio_transcript)

        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz {selected_option} difficulty")
            
            with st.spinner("AI is creating quizzes for you"):
                quizzes= quiz_generator(images,selected_option)
                st.markdown(quizzes)

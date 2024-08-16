import speech_recognition as sr
import moviepy.editor as mp

# Load the video file and extract the audio
clip = mp.VideoFileClip(r'pray.mp4')
clip.audio.write_audiofile(r'pray.wav')  # Save the extracted audio as a .wav file

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file for processing
audio = sr.AudioFile('pray.wav')

# Process the audio and recognize the speech
with audio as source:
    audio_file = r.record(source)  # Record the audio from the file

try:
    # Use Google's speech recognition to convert the audio to text (in Arabic)
    t = r.recognize_google(audio_file, language='ar-AR')
    print(t)  # Print the recognized text

    # Save the recognized text to a file (appending to an existing file)
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.writelines(t)

# Handle cases where speech was not recognized
except sr.UnknownValueError as u:
    print("Could not understand audio:", u)

# Handle cases where there was an issue with the API request
except sr.RequestError as e:
    print("API request failed:", e)

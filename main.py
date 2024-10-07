import webbrowser
import pyttsx3
import face_recognition
import cv2
import speech_recognition as sr
import os
import subprocess
import pywhatkit

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_desktop_app(app_name):
    try:
        # Convert the input command to lowercase
        app_name = app_name.lower()
        

        # Add apps with correct paths
        if "notepad" in app_name:
            subprocess.Popen(["notepad.exe"])
            speak("Opening Notepad.")
        elif "calculator" in app_name:
            subprocess.Popen(["calc.exe"])
            speak("Opening Calculator.")
        elif "vs code" in app_name:
            subprocess.Popen(["C:\\Users\\ahmad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
            speak("Opening Visual Studio Code.")
        elif "linex" in app_name or "kali" in app_name:
            subprocess.Popen(["C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"])
            speak("Opening VirtualBox.")
        elif "vlc" in app_name:
            subprocess.Popen(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"])
            speak("Opening VLC Media Player.")
        elif "dev c++" in app_name:
            subprocess.Popen(["C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"])
            speak("Opening Dev C++.")
        elif "chrome" in app_name:
            # Open Chrome with the first logged-in user profile and restore previous tabs
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            profile_directory = "--profile-directory=Default"
            restore_tabs = "--restore-last-session"
            subprocess.Popen([chrome_path, profile_directory, restore_tabs])
            speak("Opening Google Chrome with the last session's tabs.")
        elif "excel" in app_name:
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"])
            speak("Opening Excel.")
        elif "powerpoint" in app_name:
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"])
            speak("Opening PowerPoint.")
        elif "word" in app_name:
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])
            speak("Opening Word.")
        elif "visual studio" in app_name:
            subprocess.Popen(["C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"])
            speak("Opening Visual Studio.")
        elif "d drive" in app_name:
            os.startfile("D:\\")
            speak("Opening D Drive.")
        elif "c drive" in app_name:
            os.startfile("C:\\")
            speak("Opening C Drive.")
        else:
            speak(f"Sorry, I cannot open {app_name} yet.")
    except Exception as e:
        speak(f"Failed to open {app_name}. Error: {str(e)}")

def processCommand(c):
    c = c.lower()
    who_are_you_responded = False

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp.")
    elif "open github" in c:
        webbrowser.open("https://github.com")
        speak("Opening GitHub.")

    # Searching on YouTube
    elif "search for" in c or "search" in c:
        if "youtube" in c:
            song_name = c.replace("search for", "").replace("search", "").replace("youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            speak(f"Searching for {song_name} on YouTube.")
        elif "instagram" in c:
            song_name = c.replace("search for", "").replace("search", "").replace("instagram", "").strip()
            webbrowser.open(f"https://www.instagram.com/search/people/?q={song_name}")
            speak(f"Searching for {song_name} on Instagram.")
        elif "facebook" in c:
            song_name = c.replace("search for", "").replace("search", "").replace("facebook", "").strip()
            webbrowser.open (f"https://www.facebook.com/search/top?q={song_name}")
            speak(f"Searching for {song_name} on Facebook.")
        elif "whatsapp" in c:
            song_name = c.replace("search for", "").replace("search", "").replace("whatsapp", "").strip()
            webbrowser.open(f"https://web.whatsapp.com/search/{song_name}")
            speak(f"Searching for {song_name} on WhatsApp.")
        elif "github" in c:
            song_name = c.replace("search for", "").replace("search", "").replace("github", "").strip()
            webbrowser.open(f"https://github.com/search?q={song_name}")
            speak(f"Searching for {song_name} on GitHub.")
            
    elif "play" in c:
        song_name = c.replace("play", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        speak(f"Searching for {song_name} on YouTube.")
    
    # Add a response to "Who are you?"
    elif "who are you" in c:
        speak("I am Jarvis, Mister Ahmad's personal AI assistant. I can help in various tasks. Also, i am at the very basic level of creation. But,  i am very helpful as a personal assistant.")
        who_are_you_responded = True
        return

    elif "hu r u" in c:
        speak("I am Jarvis, Mister Ahmad's personal AI assistant. I can help in various tasks. Also, i am at the very basic level of creation. But,  i am very helpful as a personal assistant.")
        who_are_you_responded = True
        return

    elif "who is your creator" in c or "who is your father" in c or "what about your creator" in c or "what about your father":
        speak("I was created by Mister Ahmad. He is a software developer, Mern stack developer, a very expert javascript developer and the most importantly python developer which is my mother language in which i am created")
        who_are_you_responded = True
        return

    # Extract topic and respond using chatbot logic
    if not who_are_you_responded:
        topic, response_type = extract_topic(c)
        if response_type == "chatbot":
            response = get_chatbot_response(topic)
            speak(response)

            # Open Google search on the topic
            if topic:
                webbrowser.open(f"https://www.google.com/search?q={topic}")
                speak(f"Opening Google search results for {topic}.")
    
    else:
        speak("Sorry, I don't understand the command.")

 

def extract_topic(command):
    # Keywords for chatbot
    chatbot_keywords = [
        "who is", "tell me about", "what can you tell me about",
        "who's", "give me info on", "describe",
        "information on", "explain who", "what about",
        "who are", "what is", "what's", "provide details on",
        "tell me who", "details about", "tell me the info on",
        "can you tell me about", "please tell me",
        "show me information on", "what can you say about", 
        "give me details on", "let me know about", 
        "enlighten me on", "share info about", 
        "can you tell me", "what do you know about",
        "what do you think about", "what is", "please tell me", "please let me know"
    ]
    
    # Keywords for search bot
    search_keywords = [
        "search for", "find", "look up", "search",
        "can you search for", "please search for", 
        "search this", "search that", "find out about"
    ]
    
    # Check for chatbot keywords
    for keyword in chatbot_keywords:
        if keyword in command.lower():  # Case-insensitive matching
            return command.lower().replace(keyword, "").strip(), "chatbot"

    # Check for search keywords
    for keyword in search_keywords:
        if keyword in command.lower():  # Case-insensitive matching
            return command.lower().replace(keyword, "").strip(), "search"

    return None, None

def get_chatbot_response(topic_name):
    # Replace this with actual API call or logic to get a response
    response = f"I found some information about '{topic_name}'."
    return response

def recognize_face():
    # Initialize OpenCV for face recognition
    video_capture = cv2.VideoCapture(0)  # Open the webcam
    start_time = cv2.getTickCount()  # Start the timer
    recognized = False

    while not recognized:
        # Read a frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image")
            break

        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all the faces in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)

        # Draw a rectangle around the recognized face(s)
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green rectangle

        # Display the resulting frame
        cv2.imshow("Face Recognition", frame)

        # Check if we have run for at least 4 seconds
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time > 4:  # Just check elapsed time
            if face_locations:  # Check for recognized faces
                recognized = True
                speak("Face detected, hello boss, Jarvis is ready to assist.")
            break

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows ()

    return recognized

def listen_for_activation(recognizer):
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Wake up Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

                command = recognizer.recognize_google(audio).lower()
                print(f"Detected: {command}")

                if "wake up jarvis" in command:
                    speak("Jarvis is now active, waiting for your command.")
                    return True
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            continue

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Perform face recognition only once when starting
    if recognize_face():
        print("Face recognized, Jarvis is ready to assist.")

    while True:
        if listen_for_activation(recognizer):
            active = True  # Jarvis will stay active until deactivated

            while active:
                try:
                     with sr.Microphone() as source:
                        print("Jarvis Active... Listening for commands")
                        recognizer.adjust_for_ambient_noise(source, duration=2)
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

                        command = recognizer.recognize_google(audio).lower()
                        print(f"Detected command: {command}")

                        if command.startswith("jarvis"):
                            user_command = command.replace("jarvis", "").strip()
                            if "open" in user_command:
                                app_name = user_command.replace("open", "").strip()
                                open_desktop_app(app_name)
                            elif "play" in user_command:
                                song_name = user_command.replace("play", "").strip()
                                pywhatkit.playonyt(song_name)
                                speak(f"Playing {song_name} on YouTube.")
                            else:
                                processCommand(user_command)
                        elif "ok jarvis" in command:
                            speak("Going idle. Say 'Wake up Jarvis' when you need me.")
                            active = False
                        elif "go to sleep jarvis" in command:
                            speak("Shutting down. Goodbye.")
                            exit()

                except sr.UnknownValueError:
                    continue
                except sr.RequestError as e:
                    print(f"Error with Google Speech Recognition: {e}")
                except sr.WaitTimeoutError:
                    continue
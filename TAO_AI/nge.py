import speech_recognition as sr

# Tạo một đối tượng Recognizer
robot_ear = sr.Recognizer()

# Sử dụng Microphone làm nguồn âm thanh
with sr.Microphone() as mic:
    print("Robot: I'm Listening")
    # Lắng nghe âm thanh từ mic và lưu vào biến audio
    audio = robot_ear.listen(mic)

try:
    # Sử dụng Google Speech Recognition để nhận diện giọng nói
    you = robot_ear.recognize_google(audio)
    print("You said: " + you)
except sr.UnknownValueError:
    # Xử lý nếu không thể nhận diện giọng nói
    print("Robot: Sorry, I could not understand the audio.")
except sr.RequestError as r:
    # Xử lý nếu có lỗi khi yêu cầu kết quả từ dịch vụ Google Speech Recognition
    print(f"Robot: Could not request results from Google Speech Recognition service; {r}")

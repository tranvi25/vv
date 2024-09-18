import locale
import os
import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
# Thiết lập locale để hỗ trợ Unicode
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# Tạo một đối tượng Recognizer
robot_ear = sr.Recognizer()
engine = pyttsx3.init()
robot_brain = ""
you = ""  # Khởi tạo biến you trước để tránh lỗi nếu không có đầu vào

# Thiết lập giọng nói cho engine (tiếng Việt)
voices = engine.getProperty('voices')
for voice in voices:
    if 'Vietnam' in voice.name:
        engine.setProperty('voice', voice.id)
        break

# Tăng cường chất lượng nhận diện
with sr.Microphone() as mic:
    # Điều chỉnh ngưỡng nhận diện âm thanh dựa trên tiếng ồn môi trường
    robot_ear.adjust_for_ambient_noise(mic, duration=1)  # Có thể điều chỉnh thời gian duration
    print("Robot: Tôi đang lắng nghe...")
    
    # Lắng nghe âm thanh từ mic và lưu vào biến audio
    audio = robot_ear.listen(mic, timeout=10, phrase_time_limit=20)  # Điều chỉnh thời gian lắng nghe
    
print("Robot: ...")
try:
    # Sử dụng Google Speech Recognition để nhận diện giọng nói bằng tiếng Việt
    you = robot_ear.recognize_google(audio, language='vi-VN')
    print("Bạn nói: " + you)
except sr.UnknownValueError:
    # Xử lý nếu không thể nhận diện giọng nói
    print("Robot: Xin lỗi, tôi không thể hiểu âm thanh này.")
except sr.RequestError as r:
    # Xử lý nếu có lỗi khi yêu cầu kết quả từ dịch vụ Google Speech Recognition
    print(f"Robot: Không thể yêu cầu kết quả từ dịch vụ Google Speech Recognition; {r}")

print("Bạn: " + you)

# Logic xử lý phản hồi
if you == "":
    robot_brain = "Sorry, I didn't hear you clearly, please try again."
elif "ngày" in you:
    today = date.today()
    robot_brain =  today.strftime("%d tháng %m năm %Y")   
elif  "mấy giờ" in you:
    now = datetime.now()   
    robot_brain =  now.strftime("%H giờ %M phút %S giây")  
elif  "xin chào" in you:
    robot_brain = "HI,nice to meet you:)))"
elif  "tổng thống" in you:
    robot_brain ="biden"   
    
else:
    robot_brain = "Today,I feel so good"    
    
print("Robot: " + robot_brain)   

# Nói
engine.say(robot_brain)
engine.runAndWait()

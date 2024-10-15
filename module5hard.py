
import hashlib
import time

class User:
    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 32)

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = (self.hash_password(password))
        self.age = age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 32)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошел в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему.")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео {video.title} добавлено.")
            else:
                print(f"Видео с названием {video.title} уже существует.")

    def get_videos(self, search_term):
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начало просмотра видео: {video.title}")
        for second in range(video.time_now, video.duration):
            print(f"Секунда {second + 1}")
            time.sleep(1)  # Пауза между выводами
        print("Конец видео")
        video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


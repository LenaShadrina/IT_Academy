if __name__ == "__main__":
    def auth(func):
        def check_login(*args, **kwargs):
            log1 = "N123"
            if log1 != login:
                print("Доступ запрещен.")
            else:
                value = func(*args, **kwargs)
                return value
        return check_login
    @auth
    def contribution(rub, login):
        print(f"Вы имеете доступ к сумме на счете {rub}.")

    login = input("Введите ваш логин: ")

    contribution(1000, login)











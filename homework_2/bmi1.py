if __name__ == "__main__":
    height = float(input("Введите свой рост в м: "))
    weight = float(input("Введите свой вес в кг: "))
    bmi = int(weight//(height**2))
    print("Ваш индекс массы тела:" + " " + str(bmi))

    start_index = "15"
    end_index = "40"
    scale = "========================="
    print(start_index + scale[0:bmi-16] + "|" + scale[bmi-15:] + end_index)

    
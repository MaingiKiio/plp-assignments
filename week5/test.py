import smartphone;



phone1 = smartphone.CameraPhone("Samsung", "Galaxy S23", 256, 108)
phone2 = smartphone.GamingPhone("Vivo", "ROG Phone 6", 64, "Adreno 730")

print(phone1.power_on())
print(phone1.take_photo())
print(phone1.check_storage())

print(phone2.power_on())
print(phone2.play_game("Call of Duty Mobile"))
print(phone2.check_storage())

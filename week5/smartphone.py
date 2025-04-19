class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now ON."
        return f"{self.brand} {self.model} is already ON."

    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} is now OFF."
        return f"{self.brand} {self.model} is already OFF."

    def check_storage(self):
        return f"{self.model} has {self.storage}GB of storage."


class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"{self.model} took a photo with its {self.camera_megapixels}MP camera!"


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu_model = gpu

    def play_game(self, game_name):
        return f"{self.model} is playing {game_name} with GPU: {self.gpu_model}."



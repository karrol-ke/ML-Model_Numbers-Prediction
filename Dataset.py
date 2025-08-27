import os
from PIL import Image

DATA_SET_FILE = "Data-Set\\data_set.csv"
data_set = open(DATA_SET_FILE, "w")


class CreateDataset:
    def __init__(self):
        self.source_folder = None

        for feature in range(784):
            data_set.write(f"v{feature},")

        data_set.write("numbers")
        data_set.write("\n")

    def generate(self, source_folder):
        self.source_folder = source_folder

        if os.path.exists(self.source_folder):
            for folders in os.listdir(source_folder):
                for files in os.listdir(os.path.join(source_folder, folders)):
                    image = Image.open(os.path.join(source_folder, folders, files)).convert("L")
                    compress_image = image.resize((28, 28))

                    for height in range(28):
                        for width in range(28):
                            value = round((compress_image.getpixel((height, width)) / 255), 2)
                            data_set.write(f"{value},")

                    data_set.write(folders)
                    data_set.write("\n")
            data_set.close()
        else:
            data_set.close()
            raise FileNotFoundError

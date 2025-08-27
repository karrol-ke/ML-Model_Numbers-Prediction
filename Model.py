import pandas
from sklearn import neural_network
import os
from PIL import Image

DATA_SET_FILE = "Data-Set\\data_set.csv"
PREDICT_DATA_FILE = "Predict-Data\\predict_data.csv"


class Model:
    def __init__(self):
        self.model = None
        self.image = None

    def train(self):
        if os.path.exists(DATA_SET_FILE):
            dataset = pandas.read_csv(DATA_SET_FILE)
            x_axis = dataset.drop("numbers", axis=1)
            y_axis = dataset["numbers"]
            try:
                model = neural_network.MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=5000)
                self.model = model
                model.fit(x_axis, y_axis)

            except Exception:
                raise Exception
        else:
            raise FileNotFoundError

    def prediction(self, image):
        self.image = image

        def setup():
            predict_data = open(PREDICT_DATA_FILE, "w")
            predict_features = ""
            predict_values = ""

            for feature in range(784):
                predict_features = predict_features + f"v{feature},"

            predict_data.write(predict_features[:-1])
            predict_data.write("\n")

            if self.image is None:
                raise AttributeError

            else:
                if os.path.exists(self.image):
                    predict_image = Image.open(self.image).convert("L")
                    compress_image = predict_image.resize((28, 28))

                    for height in range(28):
                        for width in range(28):
                            value = round((compress_image.getpixel((height, width)) / 255), 2)
                            predict_values = predict_values + f"{value},"

                    predict_data.write(predict_values[:-1])
                    predict_data.close()
                    return True

                else:
                    raise FileNotFoundError

        if setup() is True:
            predict_image_data = pandas.read_csv(PREDICT_DATA_FILE)
            predictions = self.model.predict(predict_image_data)
            return str(predictions[0])

        else:
            raise "Prediction Setup is Failure"

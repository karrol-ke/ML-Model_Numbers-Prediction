import Model
import Dataset

data_set = Dataset.CreateDataset()
model = Model.Model()

data_set.generate(source_folder="DataSource")

model.train()
output = model.prediction(image="input_image_file.png")

print(output)

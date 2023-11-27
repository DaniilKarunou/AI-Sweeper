import cv2
import numpy as np
import pandas as pd
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Flatten, Dense
import warnings

warnings.filterwarnings('ignore')

class NeuralNetwork():

    def __init__(self, model_path=None, csv_data_path=None, dataset_path=None, epochs=10, batch_size=32):
        self.model_path = model_path
        self.labels = None if not csv_data_path else pd.read_csv(csv_data_path)
        self.train_path = dataset_path
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self.build_model() if not model_path else self.load_model(model_path)

    def build_model(self):
        gen = ImageDataGenerator(
            rescale=1. / 255.,
            horizontal_flip=True,
            # validation_split=0.2
        )

        train_generator = \
            gen.flow_from_dataframe(self.labels,
                                    directory=self.train_path,
                                    x_col='name',
                                    y_col='class',
                                    subset="training",
                                    color_mode="rgb",
                                    target_size=(75, 75),
                                    class_mode="categorical",
                                    batch_size=self.batch_size,
                                    shuffle=True,
                                    seed=42,
                                    )

        # validation_generator = \
        #     gen.flow_from_dataframe(self.labels,
        #                             directory=self.train_path,
        #                             x_col='name',
        #                             y_col='class',
        #                             subset="validation",
        #                             color_mode="rgb",
        #                             target_size=(75, 75),
        #                             class_mode="categorical",
        #                             batch_size=self.batch_size,
        #                             shuffle=True,
        #                             seed=42,
        #                             )

        model = keras.Sequential([
            Flatten(input_shape=(75, 75, 3)),
            Dense(128, activation='relu'),
            Dense(10, activation='softmax')
        ])

        model.compile(optimizer='Adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy']
                      )

        model.summary()

        STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size
        #STEP_SIZE_VALID = validation_generator.n // validation_generator.batch_size

        model.fit(train_generator,
                  steps_per_epoch=STEP_SIZE_TRAIN,
                  #validation_data=validation_generator,
                  #validation_steps=STEP_SIZE_VALID,
                  epochs=self.epochs,
                  # callbacks=[early]
                  )

        model.save("Model.h5")
        return model

    def load_model(self, model_path):
        model = keras.models.load_model(model_path,
                                        compile=True
                                        )
        return model

    def predict(self, img_path):

        labels = {0: "air_bomb", 1: "c4", 2: "fake_bomb", 3: "grenade", 4: "hand_bomb", 5: "mine", 6: "molotov",
                  7: "nuke_bomb", 8: "tnt", 9: "water_mine"}

        img_width, img_height = 75, 75
        image = cv2.imread(img_path)
        image = cv2.resize(image, (img_width, img_height))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = image[np.newaxis, ...]
        image = image / 255.

        prediction = self.model.predict(image)
        prediction = np.squeeze(prediction)
        print("All predictions: ")
        print()
        for i in labels:
            print("          ", labels[i], ':', prediction[i])

        prediction = np.argmax(prediction).__index__()
        output = labels[prediction]
        print()
        print('Prediction of your photo:', output)
        return output

#example
#model = NeuralNetwork(csv_data_path="./data.csv", dataset_path="./dataset/")
#model.predict("./bomb.png")


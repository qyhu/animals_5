
# coding: utf-8

# In[2]:

# 载入与模型网络构建
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150,150,3)))
# filter大小3*3，数量32个，原始图像大小3,150,150
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(5))   #                               matt,几个分类就要有几个dense
model.add(Activation('softmax'))#                     matt,多分类

model.compile(loss='categorical_crossentropy',                                 # matt，多分类，不是binary_crossentropy
              optimizer='rmsprop',
              metrics=['accuracy'])


# In[3]:

#图像预处理
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        ".\\train",
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=32,
        class_mode='categorical')                               # matt，多分类

validation_generator = test_datagen.flow_from_directory(
        ".\\test",
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical')                             # matt，多分类
# class_mode='binary'


# In[4]:

#训练模型
model.fit_generator(
        train_generator,
        samples_per_epoch=2000,
        nb_epoch=50,
        validation_data=validation_generator,
        nb_val_samples=800)
model.save_weights('.\\first_try_animal5.h5')


# In[ ]:




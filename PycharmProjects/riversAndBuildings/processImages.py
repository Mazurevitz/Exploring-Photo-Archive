from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# img_path = '/home/wojciech/PycharmProjects/riversAndBuildings/data/train/architecture/*.jpeg'
img_path = '/home/wojciech/PycharmProjects/riversAndBuildings/data/train/rivers/*.jpeg'


def images_to_arrays():

    for imgs in glob.glob(img_path):
        img = load_img(imgs)  # this is a PIL image
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir='riversProcessed', save_prefix='river', save_format='jpeg'):
            i += 1
            if i > 20:
                break  # otherwise the generator would loop indefinitely

images_to_arrays()

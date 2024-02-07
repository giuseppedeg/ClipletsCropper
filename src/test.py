import os
import shutil
import config as C
import re
from PIL import Image
from json_reader import JsonReader
from utils import cropper
from tqdm import tqdm


JSON_FILE = "data/coco-homer32.json"
TEST_IMAGES_FOLDER = "data/images"

OUT_FOLDER = "output"

if os.path.exists(OUT_FOLDER):
    shutil.rmtree(OUT_FOLDER)
os.mkdir(OUT_FOLDER)

UNKNOW_TM = 0

j_reader = JsonReader(JSON_FILE, encoding=C.JSON_ENCODING)

for image_name in tqdm(os.listdir(TEST_IMAGES_FOLDER)):
    all_cliplets = j_reader.get_cliplets(image_name)

    cropper(os.path.join(TEST_IMAGES_FOLDER, image_name), 
            all_cliplets, OUT_FOLDER, 
            unknown_tm=UNKNOW_TM, 
            len_unknown_tm=C.UNKNOW_TM_LEN, 
            len_tm=C.TM_LEN, 
            extension="png",
            grayscale=False,
            resize=True,
            size=None,
            size_H=None, 
            size_W=500,
            )


print("done")
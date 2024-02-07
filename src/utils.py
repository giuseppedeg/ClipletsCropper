import os
import re
#import config as C
from PIL import Image

def _resize(img, size, size_H, size_W):
    
    if size is not None:
        new_size = size
    elif size_H is not None:
        old_h, old_w = img.size
        w = int(old_w * size_H / old_h)

        new_size = (w, size_H)
    else:
        old_h, old_w = img.size
        h = int(old_h * size_W / old_w)
        new_size = (size_W, h)

    img = img.resize(new_size)

    return img



def cropper(image_path, all_cliplets, outfolder, unknown_tm=0, len_unknown_tm=3, len_tm=6, extension="png", grayscale=False, resize=False, size=None, size_H=None, size_W=None):

    image_name = os.path.basename(image_path)

    tm = None
    if "TM" in  image_name:
        parts = image_name.split("_")
        for part in parts:
            if "TM" in part:
                tm = part
        tm_number = re.findall(r'\d+', tm)
        if len(tm_number)>0:
            tm_number=tm_number[0]
            tm_string = tm.replace(tm_number,"")
            tm = f"{tm_string}{tm_number.zfill(len_tm)}"
        else:
            tm = None
    
    
    if tm == None:
        tm = f"UNKNOWTM{str(unknown_tm).zfill(len_unknown_tm)}"
        unknown_tm += 1

    if not os.path.exists(os.path.join(outfolder, tm)):
        os.mkdir(os.path.join(outfolder, tm))

    imagename_folder = os.path.splitext(image_name)[0]
    
    if not os.path.exists(os.path.join(outfolder, tm, imagename_folder)):
        os.mkdir(os.path.join(outfolder, tm, imagename_folder))

    original_image = Image.open(image_path)
    if grayscale:
        original_image = original_image.convert("L")
    
    for letter, letter_all_info in all_cliplets.items():
        letter_index = 0

        if not os.path.exists(os.path.join(outfolder, tm, imagename_folder, letter)):
            os.mkdir(os.path.join(outfolder, tm, imagename_folder, letter))
        
        for cliplet_info in letter_all_info:
            bb = cliplet_info['bb']
            bt = cliplet_info['bt'][0]

            left = bb[0]
            top = bb[1]
            right = bb[0] + bb[2]
            bottom = bb[1] + bb[3]
            im_crop = original_image.crop((left, top, right, bottom))
            if resize:
                im_crop = _resize(im_crop, size, size_H, size_W)
            cliplet_name = (f"{letter}_{tm}_{imagename_folder}_{bt}_{letter_index}.{extension}")
            im_crop.save(os.path.join(outfolder, tm, imagename_folder, letter, cliplet_name))
            letter_index += 1
import json

class JsonReader():
    def __init__(self, json_filename, encoding="utf-8") -> None:

        with open(json_filename, encoding=encoding) as f:
            self.json_file = json.load(f)

        self.categoryID2Name = {}
        self.categoryName2ID = {}
        for cat in self.json_file["categories"]:
            self.categoryID2Name[cat['id']] = cat['name']
            self.categoryName2ID[cat['name']] = cat['id']

        self.imagesID2Name = {}
        self.imagesName2ID = {}
        for image in self.json_file["images"]:
            self.imagesID2Name[image['id']] = image['file_name']
            self.imagesName2ID[image['file_name']] = image['id']


    def get_cliplets(self, image_name):
        
        img_id = self.imagesName2ID[image_name]

        bbs = {}
        for annot in self.json_file["annotations"]:
            if annot['image_id'] == img_id:
                letter = self.categoryID2Name[annot['category_id']]
                bbs.setdefault(letter, []).append({'bb':annot['bbox'], 'bt':annot['tags']['BaseType']})
                ################################################## LINE INFORMATION
        
        return bbs



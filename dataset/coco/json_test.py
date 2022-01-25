import json
coco_anno = json.load(open('./aluminum/annotations/train.json'))

# 查看类别信息
print('\n物体类别:', coco_anno['categories'])

import os

train_images_path = r'./datasets/train/img/train_images'
train_gts_path = r'./datasets/train/gt/train_gts'

test_images_path = r'./datasets/test/img/test_images'
test_gts_path = r'./datasets/test/gt/test_gts'

train_file = r'./datasets/train.txt'
test_file = r'./datasets/test.txt'

train_images = sorted(os.listdir(train_images_path))
train_gts = sorted(os.listdir(train_gts_path))

test_images = sorted(os.listdir(test_images_path))
test_gts = sorted(os.listdir(test_gts_path))


with open(train_file, 'w') as f:
    for i in range(len(train_images)):
        image_path = os.path.join(train_images_path, train_images[i])
        gt_path = os.path.join(train_gts_path, train_gts[i])
        f.write(image_path)
        f.write('\t')
        f.write(gt_path)
        f.write('\n')

with open(test_file, 'w') as f:
    for i in range(len(test_images)):
        image_path = os.path.join(test_images_path, test_images[i])
        gt_path = os.path.join(test_gts_path, test_gts[i])
        f.write(image_path)
        f.write('\t')
        f.write(gt_path)
        f.write('\n')

import glob
import os
import argparse

from sklearn.preprocessing import label_binarize

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annotation", type=str, default="class",
	help="path to input image")
ap.add_argument("-p", "--percentage", type=int, default=10,
	help="path to input EAST text detector")
args = ap.parse_args()

root_dir = os.getcwd() # currently directory
label_dir = "Images" # Name folder of all images

annotation_dir = args.annotation # Name folder of images
percentage = args.percentage # Percentage of images to be used for the test set

print("\n----- PROCESSING -----\n")
print("Root dir: " + root_dir, "\nLabels dir: " + label_dir, "\nFolder: " + annotation_dir, "\nPercentage for test set: " + str(percentage))

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage)
print("Index test: " + str(index_test))
for pathAndFilename in glob.iglob(os.path.join(label_dir, annotation_dir, "*.jpg")):
    print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(root_dir + "/" + annotation_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(root_dir + "/" + annotation_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
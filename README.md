# FH-PS-AOP-grandchallenge


The FH-PS-AOP grand challenge offers an open-source dataset, accessible at https://zenodo.org/record/7851339#.ZEH6eHZBztU. The dataset consists of original images and their corresponding ground truth images. The original images have a size of 3* 256* 256, while the ground truth images have a size of 256*256. The ground truth images have pixels labeled as 0, 1, or 2, where 0 represents the background pixels, 1 represents the pubic symphysis pixels, and 2 represents the fetal head pixels.



The final accepted predicted image size is 256 * 256, where 0 represents background pixels, 1 represents pubic symphysis pixels, and 2 represents fetal head pixels.



The competition scoring criteria focus on measuring image segmentation accuracy using the dice, asd, and hd metrics, as well as measuring the angle of progression in ultrasound images. The specific standard is S=0.25mDSC+0.25[0.5(1-mHD/100)+0.5(1-mASD/100)]+0.5mean(1-△AoP/180). The average score for pubic symphysis, fetal head, and the population is calculated for each metric.






import cv2
import Comparer
import os

class Compare(object):
    def __init__(self):
        self.video = cv2.VideoCapture('E:\PyProjects\Resources\\test.mov')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        if success:
            cv2.imwrite('image1.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 50])
            cv2.imwrite('image.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])

            compressed_size = os.path.getsize('image1.jpg')
            uncompressed_size = os.path.getsize('image.jpg')

            imageA = cv2.imread('image1.jpg')
            imageB = cv2.imread('image.jpg')

            imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            mse = Comparer.compare_images(imageA, imageB, "imageA vs. imageB")

            return 'All ok', success, mse, compressed_size, uncompressed_size
        return 'DONE', success, 0, 0, 0


def gen(video):
    image_count = 0
    mmse = 0
    max_mse = 0
    min_mse = 0
    mean_uncomp_size = 0
    mean_comp_size = 0
    while True:
        frame, success, mse, curr_comp_size, curr_uncomp_size = video.get_frame()
        if success:
            mmse = mmse + mse
            image_count += 1
            result_mse = mmse / image_count

            mean_uncomp_size += curr_uncomp_size
            mean_comp_size += curr_comp_size

            if mse > max_mse:
                max_mse = mse

            if (mse < min_mse) & (min_mse > 0):
                min_mse = mse
            elif min_mse == 0:
                min_mse = mse

            yield (frame
                   + " current_mmse = {0}  ".format(result_mse)
                   + "current_frame = {0} ".format(image_count))
        else:
            result_mse = mmse / image_count
            result_uncomp_size = mean_uncomp_size / image_count
            result_comp_size = mean_comp_size / image_count
            yield ("result_mse = {0} ".format(result_mse)
                   + "frame_count = {0} ".format(image_count)
                   + "min_mse = {0} ".format(min_mse)
                   + "max_mse = {0} ".format(max_mse)
                   + "result_uncomp_size = {0}".format(result_uncomp_size)
                   + "result_comp_size = {0}".format(result_comp_size))
            break

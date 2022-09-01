import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images')
    parser.add_argument('--weights', '-w', default='./seg_model_weights.best1.hdf5', metavar='FILE',
                        help='Specify the file in which the model weights are stored')
    parser.add_argument('--input', '-i', metavar='INPUT', nargs='+',
                        help='Filenames of input images in current directory', required=True)
    parser.add_argument('--output', '-o', metavar='OUTPUT', nargs='+', help='Filenames of output images')
    parser.add_argument('--show', '-v', action='store_true',
                        help='Visualize the images as they are processed')
    parser.add_argument('--no-save', '-n', action='store_true', help='Do not save the output masks')
    parser.add_argument('--scale', '-s', type=float, default=0.5,
                        help='Scale factor for the input images')

    return parser.parse_args()


def get_args1():
    parser = argparse.ArgumentParser(description='Train the UNet on images and target masks')
    parser.add_argument('--epochs', '-e', metavar='E', type=int, default=100, help='Number of epochs')
    parser.add_argument('--steps', '-t', type=int, default=1, help='Maximum number of steps_per_epoch in training')
    parser.add_argument('--batch-size', '-b', dest='batch_size', metavar='B', type=int, default=1, help='Batch size')
    parser.add_argument('--load', '-f', type=str, default=False, help='Load model weights from a .hdf5 file')
    parser.add_argument('--validation', '-v', dest='val', type=float, default=20.0,
                        help='Percent of the data that is used as validation (0-100)')
    parser.add_argument('--net-scale', '-n', dest='net_scaling', type=float, default=1,
                        help='Downsampling inside the network')
    parser.add_argument('--img-scale', '-s', dest='img_scaling', type=float, default=0.5,
                        help='Downsampling in preprocessing')
    parser.add_argument('--val-imgs', '-i', dest='valid_img_count', type=int, default=1500,
                        help='Number of validation images to use')
    parser.add_argument('--train', type=str, default=r'C:\Users\katia\OneDrive\Робочий стіл/train_v2/',
                        help='Path to train folder')
    parser.add_argument('--test', type=str, default=r'C:\Users\katia\OneDrive\Робочий стіл/test_v2/',
                        help='Path to test folder')
    parser.add_argument('--segmentation', type=str, default=r'C:\train_ship_segmentations_v2.csv',
                        help='Path to train_ship_segmentations_v2.csv file')

    return parser.parse_args()

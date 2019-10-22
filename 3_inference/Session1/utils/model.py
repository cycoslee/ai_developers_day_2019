# Model download and UFF convertion utils
import os
import sys
import tarfile

import requests
import tensorflow as tf
import tensorrt as trt
import graphsurgeon as gs
import uff

from utils.paths import PATHS

# Model download functionality

def maybe_print(should_print, print_arg):
    """Prints message if supplied boolean flag is true.

    Args:
        should_print (bool): if True, will print print_arg to stdout
        print_arg (str): message to print to stdout
    """
    if should_print:
        print(print_arg)

def maybe_mkdir(dir_path):
    """Makes directory if it doesn't exist.

    Args:
        dir_path (str): directory path
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def download_file(file_url, file_dest_path, silent=False):
    """Downloads file from supplied URL and puts it into supplied directory.

    Args:
        file_url (str): URL with file to download
        file_dest_path (str): path to save downloaded file in
        silent (bool): if True, writes progress messages to stdout
    """
    with open(file_dest_path, "wb") as f:
        maybe_print(not silent, "Downloading {}".format(file_dest_path))
        response = requests.get(file_url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None or silent: # no content length header or silent, just write file
            f.write(response.content)
        else: # not silent, print progress
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write(
                    "\rDownload progress [{}{}] {}%".format(
                        '=' * done, ' ' * (50-done),
                        int(100 * dl / total_length)))
                sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.flush()

def download_model(model_name, silent=False):
    """Downloads model_name from Tensorflow model zoo.

    Args:
        model_name (str): chosen object detection model
        silent (bool): if True, writes progress messages to stdout
    """
    maybe_print(not silent, "Preparing pretrained model")
    model_dir = PATHS.get_models_dir_path()
    maybe_mkdir(model_dir)
    model_url = PATHS.get_model_url(model_name)
    model_archive_path = os.path.join(model_dir, "{}.tar.gz".format(model_name))
    download_file(model_url, model_archive_path, silent)
    maybe_print(not silent, "Download complete\nUnpacking {}".format(model_archive_path))
    with tarfile.open(model_archive_path, "r:gz") as tar:
        tar.extractall(path=model_dir)
    maybe_print(not silent, "Extracting complete\nRemoving {}".format(model_archive_path))
    os.remove(model_archive_path)
    maybe_print(not silent, "Model ready")

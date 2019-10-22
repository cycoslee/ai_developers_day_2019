FROM nvcr.io/nvidia/deepstream:4.0.1-19.09-devel

#RUN apt-get update

RUN apt-get install wget -y

RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1HxQyTmcfwLER407GPnQAUtNcn9odqqTc' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1HxQyTmcfwLER407GPnQAUtNcn9odqqTc" -O plugins.tar.gz && rm -rf /tmp/cookies.txt

RUN tar -zxvf plugins.tar.gz

RUN apt-get install jupyter -y


COPY configs/config_infer_primary_ssd_tlt.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/
COPY configs/config_infer_primary_ssd_trt.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/
COPY configs/deepstream_app_config_ssd_tlt.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/
COPY configs/deepstream_app_config_ssd_trt.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/
COPY configs/ssd_coco_labels_trt.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/
COPY configs/ssd_tlt_labels.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_SSD/

COPY configs/deepstream_app_config_yoloV3.txt /root/deepstream_sdk_v4.0.1_x86_64/sources/objectDetector_Yolo/
COPY configs/source30_1080p_dec_infer-resnet_tiled_display_int8.txt /root/deepstream_sdk_v4.0.1_x86_64/samples/configs/deepstream-app/
COPY configs/source4_1080p_dec_infer-resnet_tracker_sgie_tiled_display_int8.txt /root/deepstream_sdk_v4.0.1_x86_64/samples/configs/deepstream-app


COPY plugins/libnvinfer/v19.05/* /plugins/libnvinfer/v19.05/

COPY plugins/libnvinfer/v19.09/* /plugins/libnvinfer/v19.09/

RUN mkdir /plugins/lib_deepstream_backup/

RUN cp  /usr/lib/x86_64-linux-gnu/libnvinfer* /plugins/lib_deepstream_backup/

COPY deepstream_ssd.ipynb /root/deepstream_sdk_v4.0.1_x86_64/

run mkdir /root/deepstream_sdk_v4.0.1_x86_64/ds_figures/

COPY ds_figures/* /root/deepstream_sdk_v4.0.1_x86_64/ds_figures/


WORKDIR /root/deepstream_sdk_v4.0.1_x86_64/


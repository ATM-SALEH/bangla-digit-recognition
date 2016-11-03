FROM gcr.io/tensorflow/tensorflow
RUN apt-get -y update && apt-get install -y python-pandas python-numpy
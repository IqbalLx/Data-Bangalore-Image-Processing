docker run -it --rm -p 8501:8501 \
    -v ${PWD}/mnist_serving:/models/mnist \
    -e MODEL_NAME=mnist tensorflow/serving:2.8.0
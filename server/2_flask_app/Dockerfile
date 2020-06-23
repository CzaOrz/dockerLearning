FROM python:3.6.8
RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple

LABEL maintainer="CzaOrz"
ENV CUR_DIR="./"
ENV APP_DIR="/workplace/server/flask_app"

COPY $CUR_DIR $APP_DIR

WORKDIR $APP_DIR

CMD python app.py

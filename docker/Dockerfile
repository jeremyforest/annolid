FROM python:3.9.16
LABEL maintainer "Chen Yang <healthonrails@gmail.com>, Jeremy Forest <jerem.forest@gmail.com>"

ARG POETRY_VERSION=1.7.1

#TODO Figure out which ones of those a required and which ones are not
RUN \
  apt-get update -qq && \
  apt-get install -qq -y \
    git \
    wget \
    ca-certificates \
    python3 \
    python3-pip \
    python3-matplotlib \
    python3-pyqt5 \
    python3-opencv \
    python3-dev \
    python3-setuptools \
    sudo \
    ninja-build\
    ffmpeg \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \ 
    portaudio19-dev \
    libegl1 \ 
    libgl1 \ 
    libxkbcommon0 \
    && rm -rf /var/lib/apt/lists/*

# ENV QT_DEBUG_PLUGINS=1

RUN git clone --recurse-submodules https://github.com/healthonrails/annolid.git
WORKDIR annolid/

# Poetry install
# TODO Fix the dir copy for that. Right now copied manually in the docker folder which is bad
COPY poetry.lock pyproject.toml .
RUN pip install poetry==${POETRY_VERSION}

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install

# install detectron2
# Workaround for issue where detectron2 cannot be installed with poetry:
# - https://github.com/python-poetry/poetry/issues/2113
# - https://github.com/facebookresearch/detectron2/issues/2644
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

CMD ["poetry", "run", "python", "annolid/gui/app.py"]

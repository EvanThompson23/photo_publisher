FROM ros:humble-ros-base as build
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install-y python3-opencv
RUN apt-get -y install ros-humble-cv-bridge
RUN mkdir /workspace
COPY ./src /workspace
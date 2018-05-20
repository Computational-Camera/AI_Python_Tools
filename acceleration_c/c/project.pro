QT       += core
QT       -= gui

QT_CONFIG -= no-pkg-config
CONFIG += link_pkgconfig

PKGCONFIG += opencv

TARGET = pyopencv
TEMPLATE = lib

CONFIG   += optimize_full

HEADERS  = main.h        
SOURCES  = main.cpp

QMAKE_CXXFLAGS += -O3 -march=native -std=c++11 -m64 -pipe -ffast-math -Waggressive-loop-optimizations -Wall -fpermissive -fopenmp 

#INCLUDEPATH +=  /usr/include/hdf5/serial/
#INCLUDEPATH +=  /usr/local/include/eigen3/
#INCLUDEPATH +=  /usr/include/ceres/

LIBS += -fopenmp -lz -lhdf5_serial -lX11 -lglog -lgflags -lceres -lcxsparse -lcholmod -lblas -llapack #
LIBS += -L/user/local/lib/
#OBJECTS_DIR = ./obj
#DESTDIR     = ./bin


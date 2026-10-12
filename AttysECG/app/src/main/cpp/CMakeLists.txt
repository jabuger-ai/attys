cmake_minimum_required(VERSION 3.18.1)

project("attysecg_audio")

find_package(oboe REQUIRED CONFIG)

add_library(attysecg_audio SHARED
        AmbientAudio.cpp
        native-audio-jni.cpp
)

find_library(log-lib log)
find_library(android-lib android)

target_link_libraries(attysecg_audio
        oboe::oboe
        ${log-lib}
        ${android-lib}
)

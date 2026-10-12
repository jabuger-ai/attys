if(NOT TARGET oboe::oboe)
add_library(oboe::oboe SHARED IMPORTED)
set_target_properties(oboe::oboe PROPERTIES
    IMPORTED_LOCATION "/home/jacob-manning/.gradle/caches/8.14.5/transforms/ad06d3a0383875dfa85adf19176cd39f/transformed/jetified-oboe-1.9.0/prefab/modules/oboe/libs/android.x86/liboboe.so"
    INTERFACE_INCLUDE_DIRECTORIES "/home/jacob-manning/.gradle/caches/8.14.5/transforms/ad06d3a0383875dfa85adf19176cd39f/transformed/jetified-oboe-1.9.0/prefab/modules/oboe/include"
    INTERFACE_LINK_LIBRARIES ""
)
endif()


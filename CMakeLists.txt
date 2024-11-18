cmake_minimum_required(VERSION 3.29)
project(TareaAlgoco2_3)
include_directories(${CMAKE_SOURCE_DIR}/include)

set(CMAKE_CXX_STANDARD 20)

add_executable(TareaAlgoco2_3 main.cpp
        cost_functions.h
        BruteForce.cpp
        BruteForce.h
        DynamicProgramming.cpp
        DynamicProgramming.h
        cost_functions.cpp
)
target_link_libraries(TareaAlgoco2_3 pdh)

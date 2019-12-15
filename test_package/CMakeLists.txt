project(PackageTest CXX)
cmake_minimum_required (VERSION 3.9)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package("CvPlot" REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example CvPlot::CvPlot)

enable_testing()
add_test(NAME example
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND example)

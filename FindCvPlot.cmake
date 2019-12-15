cmake_minimum_required (VERSION 3.11)

message(STATUS "in FindCvPlot...")
if(TARGET CvPlot::CvPlot)
    message(STATUS "already there")
    set(CvPlot_FOUND TRUE)
else() #if(TARGET CONAN_PKG::CvPlot)
    message(STATUS "found CONAN_PKG::CvPlot")
    add_library(CvPlot::CvPlot INTERFACE IMPORTED)
    target_link_libraries(CvPlot::CvPlot INTERFACE CONAN_PKG::CvPlot)
    target_compile_features(CvPlot::CvPlot INTERFACE cxx_std_11)
    set(CvPlot_FOUND TRUE)
#else()
#    message(STATUS "not found")
#    set(CvPlot_FOUND FALSE)
endif()


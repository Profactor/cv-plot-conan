cmake_minimum_required (VERSION 3.11)

if(TARGET CvPlot::CvPlot)
    set(CvPlot_FOUND TRUE)
elseif(TARGET CONAN_PKG::CvPlot)
    add_library(CvPlot::CvPlot INTERFACE IMPORTED)
    target_link_libraries(CvPlot::CvPlot INTERFACE CONAN_PKG::CvPlot)
    target_compile_features(CvPlot::CvPlot INTERFACE cxx_std_11)
    set(CvPlot_FOUND TRUE)
else()
    set(CvPlot_FOUND FALSE)
endif()


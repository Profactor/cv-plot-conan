from conans import ConanFile, CMake, tools


class CvplotConan(ConanFile):
    license = "MIT"
    author = "PROFACTOR GmbH - https://www.profactor.at/"
    url = "https://github.com/wpalfi/cv-plot-conan.git"
    description = "fast modular opencv plotting library"
    topics = ("plot", "opencv")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    requires = "opencv/4.1.1@conan/stable"
    generators = "cmake"

    def config_options(self):
        self.options["opencv"].shared = self.options.shared
    
    def source(self):
        self.run("git clone https://github.com/wpalfi/cv-plot.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CVPLOT_HEADER_ONLY"] = False		
        cmake.configure(source_folder="cv-plot")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="cv-plot/CvPlot/inc")
        self.copy("*CvPlot.lib", dst="lib", keep_path=False)
        self.copy("*CvPlot.dll", dst="bin", keep_path=False)
        self.copy("*CvPlot.so", dst="lib", keep_path=False)
        self.copy("*CvPlot.dylib", dst="bin", keep_path=False)
        self.copy("*CvPlot.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["CvPlot"]


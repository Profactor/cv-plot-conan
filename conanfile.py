from conans import ConanFile, CMake, tools


class CvplotConan(ConanFile):
    license = "MIT"
    author = "PROFACTOR GmbH - https://www.profactor.at/"
    homepage = "https://github.com/Profactor/cv-plot.git"
    url = "https://github.com/Profactor/cv-plot-conan.git"
    description = "fast modular opencv plotting library"
    topics = ("plot", "opencv")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
            "header_only": [True, False]}
    default_options = {"shared": False, "header_only": False}
    requires = "opencv/4.1.1@conan/stable"
    generators = "cmake"
    exports_sources = "FindCvPlot.cmake"

    def config_options(self):
        if 'shared' in self.options:
            self.options["opencv"].shared = self.options.shared
    
    def configure(self):
        if self.options.header_only:
            self.settings.clear()
            self.options.remove("shared")
            
    def source(self):
        self.run("git clone %s -b release/%s" % (self.homepage,self.version))

    def build(self):
        if self.options.header_only:
            return
        cmake = CMake(self)
        cmake.definitions["CVPLOT_HEADER_ONLY"] = False		
        cmake.configure(source_folder="cv-plot")
        cmake.build()

    def package(self):
        self.copy("LICENSE", src="cv-plot")
        self.copy("*.h", dst="include", src="cv-plot/CvPlot/inc")
        if self.options.header_only:
            self.copy("*.ipp", dst="include", src="cv-plot/CvPlot/inc")
        else:
            self.copy("*CvPlot.lib", dst="lib", keep_path=False)
            self.copy("*CvPlot.dll", dst="bin", keep_path=False)
            self.copy("*CvPlot.so", dst="lib", keep_path=False)
            self.copy("*CvPlot.dylib", dst="lib", keep_path=False)
            self.copy("*CvPlot.a", dst="lib", keep_path=False)
        self.copy("FindCvPlot.cmake", dst=".", keep_path=False)

    def package_info(self):
        if self.options.header_only:
            self.cpp_info.defines.append("CVPLOT_HEADER_ONLY")
        else:
            self.cpp_info.libs = ["CvPlot"]
            if self.options.shared:
                self.cpp_info.defines.append("CVPLOT_SHARED")


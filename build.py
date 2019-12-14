from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="cv-plot:shared", pure_c=False)
    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++") #opencv requires c++11
    
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        
        if settings["compiler.libcxx"] == "libstdc++": #opencv requires c++11
            continue
            
        options["opencv:shared"] = False
        filtered_builds.append([settings, options, env_vars, build_requires, reference])
        
        if options["cv-plot:shared"] == True:
            options["opencv:shared"] = True
            filtered_builds.append([settings, options, env_vars, build_requires, reference])
            
    builder.builds = filtered_builds
    
    builder.run()

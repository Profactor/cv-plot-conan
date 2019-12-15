from cpt.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="cv-plot:shared", pure_c=False)
    
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        
        if "compiler.libcxx" in settings and settings["compiler.libcxx"] == "libstdc++": #opencv requires c++11
            continue
            
        filtered_builds.append([settings, options, env_vars, build_requires, reference])
    
    builder.builds = filtered_builds
        
    if CVPLOT_HEADER_ONLY in os.environ:
        builder.add(options={"header_only": True})
    
    builder.run()

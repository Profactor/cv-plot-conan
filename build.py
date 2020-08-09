from cpt.packager import ConanMultiPackager
import os
from conans import tools
import re

def getReference():
    git = tools.Git(folder=".")
    branch = git.get_branch()
    match = re.match(r"^release/(.+)$", branch)
    if not match:
        raise Exception('Not a release branch name: %s' % branch)
    version = match.group(1)
    return "CvPlot/%s" % version

if __name__ == "__main__":
    builder = ConanMultiPackager(reference=getReference())
    
    if 'CVPLOT_HEADER_ONLY' in os.environ:
        builder.add(options={"CvPlot:header_only": True})
    else:
        builder.add_common_builds(shared_option_name="CvPlot:shared", pure_c=False)
        
        filtered_builds = []
        for settings, options, env_vars, build_requires, reference in builder.items:
            
            if "compiler.libcxx" in settings and settings["compiler.libcxx"] == "libstdc++": #opencv requires c++11
                continue
                
            filtered_builds.append([settings, options, env_vars, build_requires, reference])
        
        builder.builds = filtered_builds
        
    
    builder.run()

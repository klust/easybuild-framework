import os

from easybuild.tools.module_naming_scheme.easybuild_mns import EasyBuildMNS


class EasyBuildNoLinksMNS(EasyBuildMNS):
    """Class implementing the UAntwerp Naming Scheme, we do not want the symbolic links for the module classes."""

    def det_module_symlink_paths(self, ec):
        """
        Determine list of paths in which symlinks to module files must be created.
        """
        # Return an empty list as we do not want symlinks.
        return []

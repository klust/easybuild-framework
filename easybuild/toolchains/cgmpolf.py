##
# Copyright 2013-2024 Ghent University
#
# This file is triple-licensed under GPLv2 (see below), MIT, and
# BSD three-clause licenses.
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for cgmpolf compiler toolchain (includes Clang, GFortran, MPICH, OpenBLAS, LAPACK,
ScaLAPACK and FFTW).

Authors:

* Dmitri Gribenko (National Technical University of Ukraine "KPI")
"""

from easybuild.toolchains.cgmpich import Cgmpich
from easybuild.toolchains.fft.fftw import Fftw
from easybuild.toolchains.linalg.openblas import OpenBLAS
from easybuild.toolchains.linalg.scalapack import ScaLAPACK


class Cgmpolf(Cgmpich, OpenBLAS, ScaLAPACK, Fftw):
    """Compiler toolchain with Clang, GFortran, MPICH, OpenBLAS, ScaLAPACK and FFTW."""
    NAME = 'cgmpolf'
    SUBTOOLCHAIN = Cgmpich.NAME

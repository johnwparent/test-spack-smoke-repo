# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from urllib.request import pathname2url

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Smoke1(CMakePackage):
    """Smoke test - compile and run a simple CMake project
    
    Basic Smoke test - compiles a one file CMake based project into an executable
    that accepts and adds two integer values, reporting the resultant value to stdout
    Behavior validated by a successful run of CMake, compilation, and Spack driven test
    """

    homepage = "https://spack.io"
    url = "file:" + pathname2url(os.path.join(os.path.dirname(__file__), "smoke1-0.1.tgz"))

    maintainers("spack")

    license("MIT")

    version("0.1", sha256="275a558bc1ada9adea8a3c2425d3e14d2f5fbe92e13bedf952c9de578cc13f1b")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def test_basic(self):
        exe_name = join_path(self.prefix.bin, "smoke1")
        exe = which(exe_name, required=True)
        assert "3" in exe("1", "2", output=str)
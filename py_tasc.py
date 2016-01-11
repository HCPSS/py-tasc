#!/usr/bin/env python
import os
from assembler import Assembler
from optionresolver import OptionResolver
from patchers import PatchManager, PatchPatcher

# Get the user supplied options
options = OptionResolver()

# Assemble the source code
assembler = Assembler(options.manifest()["projects"], options.destination(), options.extra_parameters())
assembler.assemble()

# Apply any patches
patchmanager = PatchManager(options.manifest()["patches"], options.destination())
patch_base = os.path.dirname(options.manifest_location())
patchmanager.add_patcher("patch_file", PatchPatcher(patch_base))
patchmanager.patch()

# np_probe_targets

[![Python
Versions](https://img.shields.io/pypi/pyversions/np_probe_targets.svg)](https://pypi.python.org/pypi/np-probe-targets/)

Tools for Neuropixels probe insertion: providing suggested targets, recording actual insertions, storing notes.

## creating new implant drawings
### export 2D view of 3D model
- get a .sldpart CAD model from MPE
- open in Solidworks
- rotate the view to face the top of the implant, matching the view from the rig scope
- Save As -> .dxf
- check "current" view only

### edit 2D drawing for widget
- open a copy of one of the existing .svg drawings in Inkscape/Illustrator, to use the same page size and colors
- add the new .dxf file 
- if the lines are too thick to see any detail, change them to 1pt for now
- resize the new drawing to fill the page, like the existing drawing
- with the two drawings side by side, update the new drawing to match:
  - the outline is fragmented and needs to be joined together so a white fill can be applied
  - holes that have straight edges will need joining to be fill-able
  - circular holes should already be fill-able
  - check the CAD model for probe-letter designations (A1, A2, B1, ...)
- when finished, export as .svg

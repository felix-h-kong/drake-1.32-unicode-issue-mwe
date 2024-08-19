# README
This is an MWE for https://stackoverflow.com/questions/78881961/writing-diagram-to-svg-uses-ascii-by-default-not-utf-8/78883286?noredirect=1#comment139081443_78883286

A github issue has been raised: https://github.com/RobotLocomotion/drake/issues/21819

### What to do
Run `pydot_test.py` to reproduce the error. It's a `UnicodeEncodeError` on the line that writes the SVG of the `Diagram` to file.

### How to make the problem appear/disappear:
- When using `MultibodySceneGraph()`, the error occurs. If you switch to using `MultibodyPlant()`, the error doesn't happen.
- When using `MultibodySceneGraph()`, you can make the error go away by commenting out the .vtk collision geometry in the SDF file
Data Analysis for apriltags detection from Pediatric Perimetry test.
04-NOV-2015

Authors - Tejaswi Kasarla, Dhruv Joshi
Srujana - Center for Innovation, LV Prasad Eye Insitute, Hyderabad

----------------------------------------------------------------------

After taking the data on test subjects from the Pediatric Perimeter, the recorded videos(at 120fps) were processed to detect the apriltags.

The data from apriltags was saved to a text file. It prints out distance, x, y, x, yaw, pitch, roll for each tag detection.

This text file is processed in this code and the relevant data has been created into numpy array and each value is plotted against time to observe the changes.

Right now, the missing tag detections are filled up with zero. Later we'll write a script to smoothen the graph by estimating the values.
<b>Update:</b> The missing tag detections are not plotted (the data when no tags are detected is set to No Number/NA) 

Also the yaw, ptich and roll values need to be converted to degrees from radians to see if any relevant data can be used for the analysis.

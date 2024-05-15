# Invisibility Cloak
<strong>This repository contains the code for an invisibility cloak made in Python for the computer vision discipline</strong>

<h1>How it works?</h1>
<p>
<h2>Initial Video Capture:<br></h2>
<p>
The code starts by capturing the first 60 frames of the video to define the initial background. These frames will be used as a reference for the static background.
</p>

<h2>Processing of Each Frame:</h2>
<ul>
    <li>After capturing the background, each subsequent frame of the video is processed.</li>
    <li>Each frame is converted to the HSV color space.
A mask is created to detect the color black (or other colors within the specified range).</li>
    <li>The mask is refined to remove noise and imperfections.</li>
    <li>The static background is combined with the current frame using the mask to create the "invisibility" effect.
    </li>
</ul>

<h2>Real-time Result Display:</h2>
<p>
The final result, with the effect applied, is displayed in a window.
</p>

<h2>Finishing:</h2>
<p>
The process continues until the user presses the 'ESC' key to exit, at which point the windows are closed and resources are freed.
</p>



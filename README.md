<h1>Invisibility Cloak</h1>
<p><strong>This repository contains the code for an invisibility cloak made in Python for the computer vision discipline</strong></p>

<h2>How it works?</h2>

<h3>Initial Video Capture:</h3>
<p>The code starts by capturing the first 60 frames of the video to define the initial background. These frames will be used as a reference for the static background.</p>

<h3>Processing of Each Frame:</h3>
<ul>
    <li>After capturing the background, each subsequent frame of the video is processed.</li>
    <li>A mask is created to detect the blue color in BGR.</li>
    <li>The mask is refined to remove noise and imperfections.</li>
    <li>The static background is combined with the current frame using the mask to create the "invisibility" effect.</li>
</ul>

<h3>Real-time Result Display:</h3>
<p>The final result, with the effect applied, is displayed in a window.</p>

<h3>Finishing:</h3>
<p>The process continues until the user presses the 'q' key to exit, at which point the windows are closed and resources are freed.</p>

<h2>Installation and Usage</h2>

<h3>Prerequisites</h3>
<p>Ensure you have Python installed. It's recommended to use a virtual environment.</p>

<h3>Install Dependencies</h3>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/danilobsilv/invisibility-cloak.git<br>cd invisibility-cloak</code></pre>
    </li>
    <li>Create a virtual environment:
        <pre><code>python -m venv venv</code></pre>
    </li>
    <li>Activate the virtual environment:
        <pre><code>
        venv\Scripts\activate
        </code></pre>
    </li>
    <li>Install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h3>Run the Code</h3>
<p>To run the invisibility cloak script, use:</p>
<pre><code>python invisibility_cloak.py</code></pre>
<p>Follow the on-screen instructions to define the background and see the invisibility effect in real time.</p>

<h2>Requirements</h2>
<p>The <code>requirements.txt</code> file should include:</p>
<pre><code>numpy<br>opencv-python</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! Please open an issue or submit a pull request.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
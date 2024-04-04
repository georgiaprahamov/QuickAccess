 <h1>QuickAccess Documentation</h1>
  
  <h2>Introduction</h2>
  <p>The QuickAccess Python script provides a convenient way for users to open the calculator application on their Windows system using a customizable hotkey (default: F12). Additionally, it allows users to gracefully exit the program by pressing 'q'.</p>
  
  <h2>Dependencies</h2>
  <ul>
    <li><strong>keyboard:</strong> Python library for registering and handling keyboard events.</li>
    <li><strong>subprocess:</strong> Python module for spawning new processes.</li>
    <li><strong>tkinter:</strong> Python's standard GUI (Graphical User Interface) toolkit.</li>
  </ul>
  
  <h2>Functions</h2>
  
  <h3><code>open_calculator()</code></h3>
  <p>This function attempts to open the calculator application when triggered by the specified hotkey.</p>
  
  <h3><code>main()</code></h3>
  <p>The main function initializes the Tkinter root window, sets up the hotkey to open the calculator, and displays informative messages using Tkinter's messagebox. The program runs indefinitely until the user chooses to exit by pressing 'q'.</p>
  
  <h2>Usage</h2>
  <ol>
    <li>Ensure that Python and the required libraries are installed on your system.</li>
    <li>Run the Python script.</li>
    <li>Press the designated hotkey (default: F12) to open the calculator application.</li>
    <li>To exit the program, press 'q'.</li>
  </ol>
  
  <h2>Example</h2>
  <pre><code>python QuickAccess.py</code></pre>

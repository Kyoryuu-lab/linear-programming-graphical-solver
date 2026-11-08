<h1>linear-programming-graphical-solver</h1>
<p>Graphical 2D Linear Programming (LP) and Feasible Region visualizer powered by NumPy and Matplotlib</p>

<h2>Project description</h2>
<p>This project implements an automated graphical analysis suite for 2D Linear Programming and Operations Research models:</p>
<ol>
  <li>
    <dl>
      <dt><b>Mathematical Constraint Modeling:</b></dt>
      <dd>Translates linear inequality systems ($A \cdot x \leq b$ and $A \cdot x \geq b$) into continuous functional boundary curves.</dd>
      <dd>Handles mixed directional constraints including lower-bound cutoffs (e.g. $x \geq 2$ and $x \geq 3$).</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Feasible Region Geometry:</b></dt>
      <dd>Computes point-wise upper and lower feasibility envelopes using <code>np.minimum</code> and <code>np.maximum</code>.</dd>
      <dd>Accurately renders convex polygonal solution sets as well as unbounded minimization spaces.</dd>
    </dl>
  </li>
  <li>Provides an integrated CLI runner (<code>main.py</code>) supporting targeted problem selection, batch rendering, and automated high-resolution PNG exports.</li>
</ol>

<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">linear-programming-graphical-solver</th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Master CLI orchestrator for executing, rendering, and exporting all 5 optimization models</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Mathematical documentation and operational guide</td>
  </tr>
  <tr>
    <td>.gitignore</td>
    <td>Exclusion rules for Python bytecode, virtual environments, and generated plots</td>
  </tr>
</table>

<h2>Covered Linear Models</h2>
<table>
  <tr>
    <th>Problem</th>
    <th>Linear Constraints</th>
    <th>Domain Characteristics</th>
  </tr>
  <tr>
    <td><b>Problem 1</b></td>
    <td>$x_1 + 0.75x_2 \leq 280$, $1.5x_1 + 2x_2 \leq 450$</td>
    <td>Production planning (Shirts &amp; Pajamas) with non-negativity</td>
  </tr>
  <tr>
    <td><b>Problem 2</b></td>
    <td>$2x_1 + x_2 \leq 40$, $x_1 + 3x_2 \leq 30$</td>
    <td>Standard convex bounded polygon</td>
  </tr>
  <tr>
    <td><b>Problem 3</b></td>
    <td>$4x + 3y \leq 36$, $2x + 4y \leq 40$, $x \geq 3$</td>
    <td>Bounded domain with vertical constraint boundary</td>
  </tr>
  <tr>
    <td><b>Problem 4</b></td>
    <td>$x + y \leq 12$, $x + 2y \leq 20$, $x \geq 2$</td>
    <td>Multi-constraint bounded feasible region</td>
  </tr>
  <tr>
    <td><b>Problem 5</b></td>
    <td>$x_1 + 2x_2 \geq 80$, $3x_1 + x_2 \geq 75$[span_52](start_span)[span_52](end_span)</td>
    <td>Unbounded minimization region above lower envelope</td>
  </tr>
</table>

<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone repository</dt>
        <dd>
          <code>git clone https://github.com/Kyoryuu-lab/linear-programming-graphical-solver.git</code>
        </dd>
        <dd>
          <code>cd linear-programming-graphical-solver</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install numpy matplotlib</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Run solver</dt>
        <dd>Visualize specific problem interactively: <code>python main.py --problem 1</code></dd>
        <dd>Batch export all models as PNG images: <code>python main.py --all --save</code></dd>
      </dl>
    </li>
  </b>
</ol>

<h2>Example of console output (python main.py --all --save)</h2>
<samp>
  <p>
    [*] Visualisiere Problem 1...<br />
    [+] Diagramm erfolgreich gespeichert unter: problem_1.png<br />
    [*] Visualisiere Problem 2...<br />
    [+] Diagramm erfolgreich gespeichert unter: problem_2.png<br />
    [*] Visualisiere Problem 3...<br />
    [+] Diagramm erfolgreich gespeichert unter: problem_3.png<br />
    [*] Visualisiere Problem 4...<br />
    [+] Diagramm erfolgreich gespeichert unter: problem_4.png<br />
    [*] Visualisiere Problem 5...<br />
    [+] Diagramm erfolgreich gespeichert unter: problem_5.png<br />
  </p>

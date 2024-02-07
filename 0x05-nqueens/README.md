# 0x05. N Queens

<div class="panel-body">
    <span id="user_id" data-id="364825"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"><br>
<small>Chess grandmaster <a href="/rltoken/fZ1ecpPEmVL9nvkBn8WQGg" title="Judit Polgár" target="_blank">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br></p>

<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>

<ul>
<li>Usage: <code>nqueens N</code>

<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>

<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don’t have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>

<p>Read: <a href="/rltoken/ghWqI1wvx6g-Ul7nrufMKA" title="Queen" target="_blank">Queen</a>, <a href="/rltoken/-hgZbgRFkwmxaKnLnCIuEQ" title="Backtracking" target="_blank">Backtracking</a></p>

<pre><code>julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>

  </div>
# AF-409 — The order-five Euler gate is explicitly positive for \(x\ge 50\)

## Status

`EXACT-DERIVED` · `FINITE-ORDER-POSITIVE-GATE` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `TODA` · `EFFECTIVE-TAIL-BOUND` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
L(x):=-\log(1-e^{-x}),\qquad f(t):=L(e^t),\qquad x=e^t,
\]

and let \(H_4\) and the order-five Toda gate \(A_4\) be as in AF-404 and AF-408:

\[
H_4(t)=\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{3},
\qquad
A_4(t)=-(\log H_4(t))''.
\]

Then

\[
\boxed{
A_4(t)>4e^t-3>0
\qquad\text{whenever }e^t\ge 50.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
A_4(t)>0\qquad(t\ge \log 50).
}
\tag{2}
\]

Since \(e>8/3\) and hence \(e^4>(8/3)^4=4096/81>50\), this proves in particular the right-endpoint inequality requested by `CLUE-effective-order-five-tail-cutoffs.md`:

\[
\boxed{
A_4(t)>0\qquad(t\ge4).
}
\tag{3}
\]

Thus AF-408's existential right-tail positivity can be replaced by an explicit cutoff. The left endpoint \(t\le-14\) remains open.

## First-harmonic matrix and exact perturbation

Write

\[
y=e^{-x}.
\]

The exact Euler-log series is

\[
f(t)=\sum_{n\ge1}\frac{y^n}{n}.
\tag{4}
\]

With \(D=d/dt=x\,d/dx\), define polynomials \(p_k\) by

\[
p_0(z)=1,\qquad
p_{k+1}(z)=z\bigl(p_k'(z)-p_k(z)\bigr).
\tag{5}
\]

Then

\[
D^k\!\left(\frac{y^n}{n}\right)
=\frac{p_k(nx)}{n}y^n.
\tag{6}
\]

For the first harmonic \(n=1\), let

\[
P(x):=\bigl(p_{i+j}(x)\bigr)_{i,j=0}^{3}.
\tag{7}
\]

Direct finite algebra gives

\[
\det P(x)=12x^6.
\tag{8}
\]

For reference, the exact inverse is

\[
P^{-1}=
\begin{pmatrix}
1-x+\frac{x^2}{2}-\frac{x^3}{6}
&
-\frac{x^2}{2}+\frac{3x}{2}-\frac{11}{6}
&
1-\frac{x}{2}
&
-\frac16
\\[2mm]
-\frac{x^2}{2}+\frac{3x}{2}-\frac{11}{6}
&
\frac{-9x^4+30x^3-39x^2+15x-4}{6x^3}
&
-\frac32+\frac4x-\frac3{x^2}+\frac1{x^3}
&
\frac{-3x^2+3x-2}{6x^3}
\\[2mm]
1-\frac{x}{2}
&
-\frac32+\frac4x-\frac3{x^2}+\frac1{x^3}
&
\frac{-3x^2+7x-3}{2x^3}
&
\frac{1-x}{2x^3}
\\[2mm]
-\frac16
&
\frac{-3x^2+3x-2}{6x^3}
&
\frac{1-x}{2x^3}
&
-\frac1{6x^3}
\end{pmatrix}.
\tag{9}
\]

Let

\[
M(x):=\bigl(D^{i+j}f(t)\bigr)_{i,j=0}^{3}.
\]

Factoring one \(y\) from every entry gives

\[
M=y(P+Q),
\tag{10}
\]

where

\[
Q=\sum_{n\ge2}\frac{y^{n-1}}{n}P_n,
\qquad
P_n:=\bigl(p_{i+j}(nx)\bigr)_{i,j=0}^{3}.
\tag{11}
\]

Hence, with

\[
B:=P^{-1}Q
=\sum_{n\ge2}y^{n-1}C_n,
\qquad
C_n:=\frac1nP^{-1}P_n,
\tag{12}
\]

we have the exact factorization

\[
H_4
=12x^6y^4\det(I+B).
\tag{13}
\]

The pure first harmonic is therefore not merely an asymptotic mnemonic: it is an explicit invertible reference matrix, and every higher Euler harmonic is isolated in \(B\).

## Uniform coefficient audit

Expand each of the 16 entries of \(C_n\) into monomials \(c\,n^a x^b\). The exponents satisfy

\[
-1\le a\le5,\qquad 0\le b\le6.
\tag{14}
\]

The sums of the absolute values of the rational coefficients in the 16 entries are

\[
\begin{pmatrix}
19/3 & 4/3 & 14/3 & 56/3\\
56/3 & 17 & 43 & 404/3\\
10 & 14 & 41 & 138\\
4/3 & 10/3 & 32/3 & 119/3
\end{pmatrix}.
\tag{15}
\]

In particular every entry has coefficient \(\ell^1\)-sum at most \(138\). Therefore, for \(n\ge2\) and \(x\ge50\),

\[
\|C_n\|_\infty
\le 552\,n^5x^6,
\tag{16}
\]

where \(\|\cdot\|_\infty\) is the induced maximum-row-sum norm.

For a monomial \(x^b y^{n-1}\),

\[
D(x^b y^{n-1})
=\bigl(b-(n-1)x\bigr)x^b y^{n-1}.
\tag{17}
\]

Because \(b\le6\), \(n\ge2\), and \(x\ge50\),

\[
|b-(n-1)x|<2nx.
\tag{18}
\]

A second differentiation gives the multiplier

\[
\bigl(b-(n-1)x\bigr)^2-(n-1)x,
\]

whose absolute value is at most \(5n^2x^2\). Applying these bounds termwise to the absolutely convergent series `(12)` gives

\[
\begin{aligned}
\|B\|_\infty
&\le552x^6\sum_{n\ge2}n^5y^{n-1},\\
\|DB\|_\infty
&\le1104x^7\sum_{n\ge2}n^6y^{n-1},\\
\|D^2B\|_\infty
&\le2760x^8\sum_{n\ge2}n^7y^{n-1}.
\end{aligned}
\tag{19}
\]

Since \(n\le2^{n-1}\) for \(n\ge2\),

\[
\sum_{n\ge2}n^r y^{n-1}
\le\frac{2^r y}{1-2^r y}.
\tag{20}
\]

Thus

\[
\begin{aligned}
\beta:=\|B\|_\infty
&\le\frac{17664\,x^6y}{1-32y},\\
\gamma_1:=\|DB\|_\infty
&\le\frac{70656\,x^7y}{1-64y},\\
\gamma_2:=\|D^2B\|_\infty
&\le\frac{353280\,x^8y}{1-128y}.
\end{aligned}
\tag{21}
\]

These bounds are deliberately coarse; their purpose is only to make the tail sign effective.

## Explicit numerical margin without floating-point assumptions

For \(x\ge50\), each \(x^k e^{-x}\) appearing in `(21)` decreases because \(x>k\). Also \(e>5/2\), so

\[
e^{-50}<\left(\frac25\right)^{50}.
\tag{22}
\]

Using `(22)` in `(21)` and the trivial bound
\((1-2^r y)^{-1}<2\) for \(r\le7\), direct rational evaluation gives

\[
\boxed{
\beta<10^{-5},\qquad
\gamma_1<\frac1{500},\qquad
\gamma_2<\frac7{20}.
}
\tag{23}
\]

In particular \(I+B\) is invertible. Put

\[
S:=(I+B)^{-1}.
\]

The Neumann bound gives

\[
\|S\|_\infty\le\frac1{1-\beta}<2.
\tag{24}
\]

Because the path \(I+sB\), \(0\le s\le1\), remains invertible, \(\det(I+B)>0\), so the real logarithm in `(13)` is legitimate.

Jacobi's determinant identity, applied with the derivation \(D\), yields

\[
D^2\log\det(I+B)
=
\operatorname{tr}\!\left(
S\,D^2B-S(DB)S(DB)
\right).
\tag{25}
\]

For a \(4\times4\) matrix \(X\),

\[
|\operatorname{tr}X|\le4\|X\|_\infty.
\]

Therefore `(23)`--`(25)` imply

\[
\begin{aligned}
\left|D^2\log\det(I+B)\right|
&\le
4\|S\|_\infty\gamma_2
+
4\|S\|_\infty^2\gamma_1^2\\
&<
8\cdot\frac7{20}
+
16\cdot\frac1{500^2}\\
&<3.
\end{aligned}
\tag{26}
\]

Finally, `(13)` gives

\[
\log H_4
=
\log12+6\log x-4x+\log\det(I+B).
\tag{27}
\]

Since \(D^2\log x=0\) and \(D^2(-4x)=-4x\),

\[
A_4
=-(\log H_4)''
=
4x-D^2\log\det(I+B).
\tag{28}
\]

Combining `(26)` and `(28)` proves

\[
A_4>4x-3\ge197>0
\qquad(x\ge50),
\]

which is `(1)`--`(3)`.

## Arithmetic-fidelity interpretation

AF-408 showed that the fifth-order fidelity gate becomes positive eventually on the right, but the statement was non-effective. AF-409 identifies a concrete mechanism for making the first-harmonic asymptotic rigorous: factor the exact derivative matrix by the first-harmonic matrix and price all discarded harmonics through the small perturbation \(B\).

The result is stronger than a sampled tail check. It says that once \(x=e^t\ge50\), the entire higher-harmonic contribution can alter the scalar Toda curvature by less than `3`, while the retained first harmonic contributes exactly \(4x\). Thus the right tail has a large certified fidelity margin.

This remains a property of the universal Euler-log kernel. It does not identify rational primes, does not see the zeta zero divisor, and does not by itself advance the continuation-side discriminator isolated elsewhere in the line.

## Prior-art and novelty audit

The determinant derivative/Jacobi identity, Neumann-series perturbation bound, Hankel/Toda machinery, and the general relation between logarithmic curvature and successive Hankel determinants are classical. AF-404 and AF-408 already locate the relevant Toda/total-positivity background.

A fresh search for the concrete Euler-log profile together with total positivity, Pólya-frequency/Hankel determinants, and Toda/log-concavity found general Hankel/Toda and total-positivity literature but no source supplying an explicit cutoff for this exact order-five Euler gate. No novelty claim is made. The new content here is the elementary line-specific effective estimate `(1)` obtained by isolating the first Euler harmonic and bounding the exact remainder.

## Boundaries and falsification checks

- The theorem proves only the **right** effective tail. It does not certify \(A_4>0\) for \(t\le-14\), and it does not close the compact interval.
- The constant `50` is intentionally non-optimal. It is chosen so that a very coarse norm audit already leaves a wide positive margin.
- The proof uses the exact full series `(4)`. Replacing the Euler-log profile by the first harmonic without the perturbation estimate would not justify the conclusion.
- The coefficient table `(15)` is a finite algebraic audit of \(C_n=n^{-1}P^{-1}P_n\). An error there would invalidate the quantitative constants but is independently checkable from `(5)`, `(7)`, and `(9)`.
- The norm estimate proves positivity of the scalar gate, not all-order total positivity. AF-217's eventual finite-order obstruction is untouched.
- Even global order-five positivity, if later obtained by closing the left and compact pieces, would still be a finite-order kernel statement rather than an arithmetic-prime or RH theorem.

## Consequence for the research line

The endpoint \(t=4\) is no longer part of the effective-tail gap: the stronger half-line \(t\ge\log50<4\) is certified analytically. The accepted effective-cutoff clue therefore reduces to one unresolved asymptotic bridge, namely a rigorous left-tail bound meeting \(t=-14\).

If the separate compact program proves \(A_4>0\) on `[-14,4]`, then only the left semi-infinite interval remains before AF-403/AF-404 can globalize the fifth-order certificate.

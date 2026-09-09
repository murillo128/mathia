# FD-002 — Franel quadratic discrepancy is an exact Cramér--von Mises--Mertens energy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CLASSICAL-IDENTITY + NORM-TRANSFER-CLOSURE + MERTENS-SPECTRAL-BRIDGE`. `FD-001` derives the exact denominator-shell Fourier decomposition of the continuous Farey counting discrepancy but leaves open a normalization issue: the classical Franel criterion is a **discrete rank-position quadratic sum**, whereas `FD-001` works with a continuous `L^2(0,1)` counting function. There is no lossy norm comparison here. A direct finite calculation, equivalently the classical one-sample Cramér--von Mises ordered-sample identity specialized to Farey reflection symmetry, gives an exact bridge.

For the Farey sequence of order `N`, write

\[
0=x_0<x_1<\cdots <x_M=1,
\qquad
M=M_N:=\sum_{q=1}^N\varphi(q).
\tag{1}
\]

Thus `M+1` is the total number of Farey points including both endpoints, while `x_1,\ldots,x_M` are the positive Farey points in `(0,1]`. Define the classical quadratic rank discrepancy

\[
\mathfrak F_N
:=\sum_{j=1}^{M}
\left(x_j-\frac jM\right)^2.
\tag{2}
\]

The `j=M` term vanishes, so including or omitting the endpoint `1` does not change the sum. Let `D_N` be the interior counting discrepancy of `FD-001`, with

\[
C_N=M-1,
\qquad
D_N(x)=\#\{x_j\in(0,1):x_j\le x\}-C_Nx.
\tag{3}
\]

Then, up to values at finitely many jump points,

\[
R_N(x):=D_N(x)-x
=\#\{1\le j\le M:x_j\le x\}-Mx.
\tag{4}
\]

The exact finite identity is

\[
\boxed{
\|R_N\|_{L^2(0,1)}^2
=\frac13+M\mathfrak F_N.
}
\tag{5}
\]

Equivalently, if

\[
F_N^{\rm emp}(x)
:=\frac1M\#\{1\le j\le M:x_j\le x\},
\]

then

\[
\boxed{
\int_0^1\left(F_N^{\rm emp}(x)-x\right)^2dx
=\frac1{3M^2}+\frac{\mathfrak F_N}{M}.
}
\tag{6}
\]

Combining (5) with the `FD-001` Fourier--Mertens formula gives a second exact identity. Write `\mathbf M(y)=\sum_{n\le y}\mu(n)` for the Mertens function and

\[
\mathcal B_N(k)
:=\sum_{\substack{d\mid k\\d\le N}}
 d\,\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right)
\qquad(k\ge1).
\tag{7}
\]

Then

\[
\boxed{
M\mathfrak F_N
=\frac1{2\pi^2}
\sum_{k\ge1}\frac{|\mathcal B_N(k)|^2}{k^2}
-\frac1{12}.
}
\tag{8}
\]

Thus the discrete Franel quadratic statistic is exactly a weighted square norm of a finite divisor transform of Mertens values, with a universal Cramér--von Mises floor. The norm-transfer gap in `FD-001` is therefore closed without losing a power of `N`, a maximum-gap factor, or any endpoint information.

## 1. Direct finite proof of the continuous/discrete identity

For `0\le j\le M`, put

\[
\varepsilon_j:=Mx_j-j.
\tag{9}
\]

Then `\varepsilon_0=\varepsilon_M=0`, and on the Farey gap `[x_j,x_{j+1})`,

\[
R_N(x)=j-Mx.
\]

Writing `x=x_j+t` and `g_j=x_{j+1}-x_j`,

\[
R_N(x)= -\varepsilon_j-Mt.
\]

The endpoint relation

\[
Mg_j=1+\varepsilon_{j+1}-\varepsilon_j
\tag{10}
\]

gives

\[
\begin{aligned}
\int_{x_j}^{x_{j+1}}R_N(x)^2dx
&=\int_0^{g_j}(\varepsilon_j+Mt)^2dt\\
&=\frac{(\varepsilon_j+Mg_j)^3-\varepsilon_j^3}{3M}\\
&=\frac{(1+\varepsilon_{j+1})^3-\varepsilon_j^3}{3M}.
\end{aligned}
\tag{11}
\]

Summing `j=0,\ldots,M-1` telescopes the cubic terms except for the unit shift:

\[
\|R_N\|_2^2
=\frac13
+\frac1M\sum_{j=1}^{M-1}\varepsilon_j
+\frac1M\sum_{j=1}^{M-1}\varepsilon_j^2.
\tag{12}
\]

Farey reflection gives

\[
x_{M-j}=1-x_j,
\qquad
\varepsilon_{M-j}=-\varepsilon_j,
\tag{13}
\]

so the linear term vanishes exactly. Finally,

\[
\frac1M\sum_{j=1}^{M-1}\varepsilon_j^2
=M\sum_{j=1}^{M-1}
\left(x_j-\frac jM\right)^2
=M\mathfrak F_N,
\tag{14}
\]

which proves (5). No estimate on individual Farey gaps is used.

This is also the standard one-sample Cramér--von Mises ordered-sample identity in a different centering. For ordered points `u_1\le\cdots\le u_M`, the classical formula uses the uniform midpoints `(2j-1)/(2M)` and the `1/(12M)` continuity term. Here

\[
x_j-\frac{2j-1}{2M}
=\left(x_j-\frac jM\right)+\frac1{2M}.
\]

Farey reflection makes the cross term vanish, while the midpoint shift contributes the extra `1/4` after rescaling from the empirical CDF to `R_N`; together with the classical `1/12` term this is precisely the `1/3` in (5).

## 2. The `FD-001` spectrum becomes the exact Franel spectrum

`FD-001` proves that `D_N` has mean zero and, for every nonzero integer `k`,

\[
\widehat D_N(k)
=\frac{\mathcal B_N(|k|)-1}{2\pi i k},
\tag{15}
\]

with the sign convention inherited from its Fourier transform. On the other hand,

\[
\widehat{x}(k)=-\frac1{2\pi i k}
\qquad(k\ne0),
\tag{16}
\]

so the endpoint correction in `R_N=D_N-x` cancels the `-1` in (15):

\[
\boxed{
\widehat R_N(k)
=\frac{\mathcal B_N(|k|)}{2\pi i k}
\qquad(k\ne0).
}
\tag{17}
\]

Also

\[
\widehat R_N(0)=\int_0^1(D_N(x)-x)dx=-\frac12.
\tag{18}
\]

Parseval therefore gives

\[
\boxed{
\|R_N\|_2^2
=\frac14
+\frac1{2\pi^2}
\sum_{k\ge1}\frac{|\mathcal B_N(k)|^2}{k^2}.
}
\tag{19}
\]

Combining (19) with (5) is exactly (8). The subtraction `1/12` is not a fitted normalization or an asymptotic artifact: it is the difference between the `1/3` Farey endpoint-grid floor and the `1/4` constant Fourier mode of `R_N`.

For each fixed `N`, the series in (19) is unproblematic. `R_N` is a bounded step-affine function, hence lies in `L^2`; alternatively (7) is bounded uniformly in `k` by a finite divisor sum depending only on `N`, so the `k^{-2}` weight gives absolute convergence.

## 3. The first spectral mode recovers the ordinary Mertens obstruction

At `k=1`, only `d=1` occurs in (7), hence

\[
\boxed{
\mathcal B_N(1)=\mathbf M(N).
}
\tag{20}
\]

Dropping the remaining nonnegative Fourier modes in (8) yields the exact consequence

\[
\boxed{
|\mathbf M(N)|^2
\le
2\pi^2\left(M\mathfrak F_N+\frac1{12}\right).
}
\tag{21}
\]

Thus the classical Franel quadratic estimate immediately forces the expected square-root-scale Mertens estimate. Using `M\asymp N^2`, the RH-equivalent bound

\[
\mathfrak F_N=O_\varepsilon(N^{-1+\varepsilon})
\]

implies

\[
\mathbf M(N)=O_\varepsilon(N^{1/2+\varepsilon}).
\]

The converse does **not** follow from this first-mode argument. Equation (8) shows exactly why: Franel controls the entire weighted family `\mathcal B_N(k)`, not only `\mathcal B_N(1)=\mathbf M(N)`. The higher modes mix Mertens values at the divisor-scaled arguments `\lfloor N/d\rfloor`. A proposed proof that replaces the full Franel energy by the single Mertens value `\mathbf M(N)` therefore drops genuine norm information unless it separately controls those divisor modes.

This is a sharper version of the collapse boundary in `FD-001`. The Farey quadratic criterion is not independent of Möbius arithmetic, but neither is it merely the square of one scalar Mertens value.

## 4. Consequence for the Farey research frontier

`FD-001` left open whether passing from its continuous shell-counting `L^2` object to the discrete Franel statistic might require a difficult gap-dependent comparison. Equations (5)--(8) remove that uncertainty completely. The relevant endpoint-aligned continuous discrepancy is **isometric to the Franel quadratic statistic up to one explicit universal constant and the exact factor `M`**.

This closes one possible source of fake geometric gain. Reweighting the continuous counting discrepancy and then claiming improvement only because discrete Farey gaps are nonuniform cannot create a new Franel bridge at this interface: the exact Cramér--von Mises identity already performs the transfer with no conditioning loss. Any stronger Farey mechanism must therefore improve the actual spectral/Mertens energy in (8), or retain pre-cumulative ordering/refinement information that is absent from `D_N` before this identity is applied.

Conversely, the result makes the `FD-001` spectrum directly RH-facing. An estimate for the complete weighted divisor-mode square sum in (8) at the Franel scale is exactly an estimate for the classical quadratic criterion, not merely for a neighboring continuous norm. This is an exact reformulation, not progress toward such an estimate by itself.

## 5. Prior art, audit, and evidence boundary

The ordered-sample identity underlying (5) is classical Cramér--von Mises mathematics. Harald Cramér, *On the Composition of Elementary Errors: Second Paper: Statistical Applications*, Scandinavian Actuarial Journal **1928** (1928), 141--180, DOI `10.1080/03461238.1928.10416872`, and Richard von Mises, *Wahrscheinlichkeit, Statistik und Wahrheit*, Springer, 1928, are the classical source boundary for integrated empirical-distribution quadratic discrepancy. The familiar finite formula

\[
W_M^2=\frac1{12M}
+\sum_{j=1}^M
\left(u_j-\frac{2j-1}{2M}\right)^2
\]

is standard and not a Mathia novelty claim. Equation (5) is its Farey-reflection specialization, also proved directly above so that no statistical normalization convention is imported silently.

The Franel quadratic criterion itself is classical and already represented by the line's Franel--Landau source anchor. The Fourier--Mertens input (15) is exactly `FD-001`. A targeted search for Farey applications of the Cramér--von Mises name did not locate this exact splice, but absence of that wording is not evidence of novelty; (5) is elementary once the two standard objects are put in compatible normalization.

The audit has four main boundaries. First, the `1/3` constant depends on using the positive Farey points `x_1,\ldots,x_M` with the endpoint-aligned grid `j/M`; changing endpoint conventions changes the displayed constant but not the underlying Cramér--von Mises identity. Second, the cancellation of the linear term in (12) uses exact Farey reflection. Third, (8) is an identity for the quadratic Franel statistic, not the Landau `L^1` statistic. Fourth, (21) is one-way when obtained by discarding higher modes; no claim is made that a scalar Mertens bound alone controls the full Farey discrepancy.

No new RH estimate, Mertens bound, discrepancy exponent, or independent arithmetic carrier is proved. The durable result is the exact closure of the continuous-to-discrete norm interface and the resulting identification of the full Franel quadratic statistic with the `FD-001` divisor-transformed Mertens spectrum.

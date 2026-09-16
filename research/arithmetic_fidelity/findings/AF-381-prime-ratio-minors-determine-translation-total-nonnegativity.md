# AF-381 — Prime-ratio minors determine continuous translation total nonnegativity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PRIME-LOGS` · `TWO-SIDED-SAMPLING` · `QUANTITATIVE-SAMPLING` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

AF-379 proves that sampling only the row variable of a continuous translation kernel on a set with vanishing tail mesh is already determining when the column variable remains arbitrary. The same closure mechanism survives the stronger compression in which **both** row and column variables are restricted to the same sampled set.

Let

\[
K_f(u,x)=f(u-x),
\qquad f:\mathbb R\to\mathbb R
\]

with `f` continuous. For `k\ge 1`, suppose a set `E\subset\mathbb R` satisfies the joint finite-pattern density condition

\[
\overline{\mathcal Q_k(E)}=\mathcal D_k,
\tag{1}
\]

where

\[
\mathcal Q_k(E)
=
\left\{
\left(
 u_2-u_1,\ldots,u_k-u_1,
 x_1-u_1,\ldots,x_k-u_1
\right):
\begin{array}{l}
 u_1<\cdots<u_k,\\
 x_1<\cdots<x_k,\\
 u_i,x_j\in E
\end{array}
\right\},
\tag{2}
\]

and

\[
\mathcal D_k
=
\left\{
(d_2,\ldots,d_k,c_1,\ldots,c_k):
0<d_2<\cdots<d_k,
\ c_1<\cdots<c_k
\right\}.
\tag{3}
\]

If

\[
\det\bigl(f(u_i-x_j)\bigr)_{i,j=1}^k\ge0
\tag{4}
\]

for every increasing row tuple and every increasing column tuple drawn from `E`, then every global order-`k` translation minor is nonnegative. If `(1)` holds for every `k\le r`, the restriction of `K_f` to `E\times E` determines total nonnegativity through order `r`.

A simple sufficient condition is again vanishing tail mesh. If `E` contains an increasing unbounded sequence

\[
e_1<e_2<\cdots,\qquad e_n\to\infty,
\]

with

\[
e_{n+1}-e_n\to0,
\tag{5}
\]

then `(1)` holds for every finite `k`. Thus, for continuous translation kernels, two-sided sampling on such an `E` is target-faithful for total nonnegativity.

For the arithmetic set

\[
E_{\mathbb P}=\{\log p:p\text{ prime}\},
\tag{6}
\]

the prime number theorem gives `(5)`. Therefore

\[
K_f\text{ is globally totally nonnegative}
\]

if and only if every finite prime-ratio minor

\[
\det\left(
 f\!\left(\log\frac{p_i}{q_j}\right)
\right)_{i,j=1}^k
\ge0
\tag{7}
\]

for all increasing prime tuples

\[
p_1<\cdots<p_k,
\qquad
q_1<\cdots<q_k.
\]

For integrable nonzero `f`, this says that full Pólya-frequency status can be tested, in principle, using only matrices indexed on both sides by rational primes. The prime labels do not make the final positivity property prime-specific: the prime-ratio grid is already dense enough, modulo common scaling, to determine the continuous translation target.

The finite-witness statement of AF-380 also survives two-sided sampling. If a fixed global minor has determinant `-\eta<0`, then Baker--Harman--Pintz short intervals place row **and** column prime logarithms close enough to a common large translate that a finite prime-ratio minor is negative. Under a local Hölder modulus of exponent `\alpha`, the required largest prime remains polynomial in `\eta^{-1}` with exponent `40/(19\alpha)`, up to target-dependent constants.

## Exact joint-pattern proof

Fix arbitrary increasing target rows and columns

\[
a_1<\cdots<a_k,
\qquad
b_1<\cdots<b_k.
\tag{8}
\]

Normalize by the first row:

\[
d_i=a_i-a_1\quad(i\ge2),
\qquad
c_j=b_j-a_1.
\tag{9}
\]

The vector `(d_2,\ldots,d_k,c_1,\ldots,c_k)` lies in `\mathcal D_k`. By `(1)`, choose sampled tuples

\[
u_1^{(m)}<\cdots<u_k^{(m)},
\qquad
x_1^{(m)}<\cdots<x_k^{(m)},
\]

with all entries in `E` such that

\[
u_i^{(m)}-u_1^{(m)}\to d_i,
\qquad
x_j^{(m)}-u_1^{(m)}\to c_j.
\tag{10}
\]

Then

\[
\begin{aligned}
 u_i^{(m)}-x_j^{(m)}
 &=
 \bigl(u_i^{(m)}-u_1^{(m)}\bigr)
 -\bigl(x_j^{(m)}-u_1^{(m)}\bigr)\\
 &\longrightarrow d_i-c_j\\
 &=a_i-b_j.
\end{aligned}
\tag{11}
\]

Continuity of `f` gives entrywise convergence of the sampled matrices to the arbitrary target matrix. Determinants are continuous, so nonnegativity of every sampled determinant implies

\[
\det\bigl(f(a_i-b_j)\bigr)_{i,j=1}^k\ge0.
\tag{12}
\]

The reverse implication is immediate. Thus joint pattern density is sufficient for exact two-sided fidelity.

## Vanishing mesh forces joint pattern density

Assume `(5)`. Fix a target vector in `\mathcal D_k` and choose a tolerance `\varepsilon>0` smaller than one third of the minimum gap inside the target row tuple and inside the target column tuple.

The normalized column offsets `c_j` need not be positive. Choose a common translation `T` so large that every point

\[
T,
\quad T+d_2,\ldots,T+d_k,
\quad T+c_1,\ldots,T+c_k
\tag{13}
\]

lies beyond a tail on which every consecutive gap of the sampled sequence is below `\varepsilon`.

Approximate each point in `(13)` from the same side by a sample in `E`, with error in an interval of length `<\varepsilon`. For sufficiently small `\varepsilon`, the selected row samples remain strictly increasing and so do the selected column samples. If the row errors are `\rho_i` and the column errors are `\kappa_j`, then

\[
|\rho_i-\rho_1|<\varepsilon,
\qquad
|\kappa_j-\rho_1|<\varepsilon.
\tag{14}
\]

Hence the normalized sampled vector approaches the prescribed point of `\mathcal D_k`. Letting `\varepsilon\downarrow0` proves `(1)`.

The extra column restriction therefore costs a stronger **joint** pattern requirement than AF-379's row-only condition, but vanishing mesh supplies that requirement automatically because one common translated window can approximate the union of both finite configurations.

## Quantitative prime-ratio witness

Suppose the target matrix

\[
A=(f(a_i-b_j))_{i,j=1}^k
\]

has

\[
\det A=-\eta<0.
\tag{15}
\]

Let

\[
m=\min(a_1,b_1),
\qquad
A_i=a_i-m,
\qquad
B_j=b_j-m,
\tag{16}
\]

so all offsets are nonnegative. Put

\[
D=\max(A_k,B_k),
\qquad
\Delta=
\min\left(
\min_{i<k}(a_{i+1}-a_i),
\min_{j<k}(b_{j+1}-b_j)
\right)>0.
\tag{17}
\]

As in AF-380, fix `r_0>0`, let

\[
J=\{a_i-b_j:1\le i,j\le k\},
\]

let `M` bound `|f|` on the `r_0`-neighborhood of `J`, and let `\omega(r)` be the local modulus of continuity there.

Baker--Harman--Pintz prove that, for every sufficiently large `x`, the interval

\[
[x,x+x^{21/40}]
\]

contains a prime. Therefore, for every sufficiently large logarithmic location `t`, there is a prime `p` with

\[
0\le \log p-t\le e^{-19t/40}.
\tag{18}
\]

Choose one common large `T`. Apply `(18)` independently to each `T+A_i` and each `T+B_j`. This produces increasing prime-log rows `u_i=\log p_i` and columns `x_j=\log q_j` provided

\[
r_T:=e^{-19T/40}<\Delta.
\tag{19}
\]

Write their one-sided errors as

\[
u_i=T+A_i+\rho_i,
\qquad
x_j=T+B_j+\kappa_j,
\qquad
0\le\rho_i,\kappa_j\le r_T.
\tag{20}
\]

The common translation cancels and

\[
(u_i-x_j)-(a_i-b_j)=\rho_i-\kappa_j,
\]

so

\[
|(u_i-x_j)-(a_i-b_j)|\le r_T.
\tag{21}
\]

Thus, exactly as in AF-380,

\[
\left|
\det\bigl(f(u_i-x_j)\bigr)-\det A
\right|
\le
k\,k!\,M^{k-1}\omega(r_T).
\tag{22}
\]

Consequently the fully sampled prime-ratio minor is negative whenever

\[
k\,k!\,M^{k-1}\omega(r_T)<\eta
\tag{23}
\]

and `r_T<\min(\Delta,r_0)`.

If `f` is locally Hölder,

\[
|f(s)-f(t)|\le L|s-t|^\alpha,
\qquad 0<\alpha\le1,
\tag{24}
\]

then a sufficient scale is

\[
T>
\frac{40}{19\alpha}
\log\frac{k\,k!\,M^{k-1}L}{\eta},
\tag{25}
\]

up to the fixed onset and ordering thresholds. The row and column primes satisfy

\[
p_i,q_j
\le
 e^{T+D}\bigl(1+e^{-19T/40}\bigr),
\tag{26}
\]

so for a fixed target configuration and fixed local regularity data,

\[
\max(p_i,q_j)
=O\!\left(\eta^{-40/(19\alpha)}\right)
\qquad(\eta\downarrow0).
\tag{27}
\]

The two-sided arithmetic restriction therefore does not worsen the inverse-margin exponent from AF-380. It only requires synchronizing both finite patterns inside the same fine prime-log tail.

## Arithmetic-fidelity interpretation

The observation in `(7)` looks substantially more arithmetic than the row-only criterion in AF-379: every matrix entry is evaluated at a logarithm of a ratio of rational primes, and no arbitrary real sampling coordinate remains.

Nevertheless, the retained Boolean certificate is still not rational-prime-specific. Vanishing prime-log mesh makes the set of joint row/column patterns dense modulo the one common translation that a translation kernel cannot observe. Continuity then removes the labels completely.

This separates two resources that can otherwise be conflated:

1. **arithmetic presentation** — every observed argument happens to be `log(p/q)`;
2. **arithmetic discrimination** — the truth value of the retained property differs for the rational-prime source and for admissible matched controls.

AF-381 proves the first does not imply the second in this category. Once every prime-ratio minor is nonnegative, the entire continuous translation total-positivity target follows without any further number theory.

For the Riemann Pólya-frequency formulation already audited in AF-371/AF-379, this gives a fully prime-indexed reformulation: the associated continuous kernel is Pólya-frequency exactly when all of its finite prime-ratio minors are nonnegative. Through the classical Schoenberg/Laguerre--Pólya bridge, the corresponding Riemann statement is equivalent to RH under the same kernel normalization used there.

This is **not** an arithmetic proof mechanism for those inequalities. The kernel already contains the global analytic object whose Pólya-frequency status is RH-equivalent. The substantive remaining question is upstream: whether prime arithmetic can force or control the sampled inequalities without importing the full target property.

## Prior-art and novelty audit

I. J. Schoenberg and A. M. Whitney, **“On Pólya Frequency Functions. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves,”** *Transactions of the American Mathematical Society* **74** (1953), provide the classical translation-determinant setting.

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1--8, DOI `10.1016/j.jmaa.2008.04.070`, defines the sampled condition on `E\times\mathbb R` and proves determining results for suitable `E`. Thus one-axis sampling determination is established prior art; AF-379 already placed Mathia's row-pattern argument inside that framework.

R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`, prove the short-interval estimate used for the quantitative two-sided prime-log net.

A focused search for two-sided `E\times E` Pólya-frequency determination, prime-ratio total-positivity tests, and prime-log row/column sampling did not identify this exact packaged corollary. The argument is nevertheless an elementary topological consequence of joint pattern density plus classical prime-gap input, so **no novelty is claimed**. The durable Arithmetic Fidelity content is the stronger compression boundary: even after removing all arbitrary real sample coordinates, prime-ratio sampling remains target-complete for continuous translation total positivity.

## Boundaries and failure modes

The theorem is specific to a translation kernel in the coordinate where the sampled set has vanishing mesh. AF-378's warning remains in force: a nonlinear reparameterization that merely makes displayed sample gaps small does not preserve a transported translation experiment unless the translation structure is genuinely intrinsic in the new coordinate.

Continuity is load-bearing. Without enough regularity to pass determinant inequalities through closure, dense joint sample patterns need not determine unsampled values.

Vanishing mesh is sufficient, not claimed necessary. More irregular sets may have dense joint finite patterns without consecutive mesh tending to zero.

The exact result assumes all sampled minors at all required orders. It does not provide a finite verification procedure. The quantitative result gives a finite witness only after a specific violating target minor, its margin, order, geometry, and local continuity modulus are known.

The Baker--Harman--Pintz exponent controls only the sampling horizon. It does not bound the first possible negative determinant order, the first target location, or the negativity margin for the Riemann kernel.

Most importantly, the theorem does not explain why prime-ratio minors should be nonnegative. It closes a representation/sampling question, not the RH sign mechanism.

## Consequence for the line

AF-380 left arithmetic column sampling as a separate joint-pattern problem. AF-381 closes that problem for prime-log sampling and, more generally, for every continuous translation kernel sampled on a vanishing-mesh tail.

The resulting boundary is sharper: **even a completely prime-indexed translation-positivity observation can be a universal target-complete sampling scheme rather than a surviving prime discriminator.** Future work in this branch should therefore look upstream of the final total-positivity certificate: at the mechanism producing the prime-ratio inequalities, at additional non-translation relational structure, or at source restrictions that make those inequalities derivable without already assuming the full Pólya-frequency target.
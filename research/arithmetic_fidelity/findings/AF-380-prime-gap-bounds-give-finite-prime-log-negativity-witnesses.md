# AF-380 — Prime-gap bounds turn prime-log determination into a finite negativity-witness modulus

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-CONDITIONING` · `TOTAL-POSITIVITY` · `PRIME-LOGS` · `QUANTITATIVE-SAMPLING` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

AF-379 proves qualitatively that the prime-log rows

\[
E_{\mathbb P}=\{\log p:p\text{ prime}\}
\]

determine total nonnegativity of every continuous translation kernel. The same mechanism admits a target-specific quantitative form: a strict negative global minor is inherited by a finite prime-log minor once the prime-log sampling mesh is smaller than the determinant's negativity margin measured through the local modulus of continuity of the kernel.

Let

\[
K_f(u,x)=f(u-x)
\]

with `f:\mathbb R\to\mathbb R` continuous. Fix increasing target rows and columns

\[
a_1<\cdots<a_k,
\qquad
b_1<\cdots<b_k,
\]

and suppose

\[
A=(f(a_i-b_j))_{i,j=1}^k,
\qquad
\det A=-\eta<0.
\tag{1}
\]

Write

\[
d_i=a_i-a_1,
\qquad
D=d_k,
\qquad
\Delta=\min_{1\le i<k}(a_{i+1}-a_i)>0.
\tag{2}
\]

Choose `r_0>0` and let

\[
J=\{a_i-b_j:1\le i,j\le k\},
\qquad
J_{r_0}=\{t:\operatorname{dist}(t,J)\le r_0\},
\tag{3}
\]

\[
M=\sup_{t\in J_{r_0}}|f(t)|,
\tag{4}
\]

and let the local modulus of continuity be

\[
\omega(r)
=
\sup\{|f(s)-f(t)|:s,t\in J_{r_0},\ |s-t|\le r\}.
\tag{5}
\]

Suppose a row-sampling set `E\subset\mathbb R` has the following one-sided approximation at some translation `T`: for every target offset `d_i` there is

\[
u_i\in E,
\qquad
T+d_i\le u_i\le T+d_i+r,
\tag{6}
\]

with

\[
0<r<\min(\Delta,r_0).
\tag{7}
\]

Then the sampled rows remain strictly increasing. With the translated columns

\[
y_j=b_j+u_1-a_1,
\tag{8}
\]

the sampled matrix

\[
B=(f(u_i-y_j))_{i,j=1}^k
\tag{9}
\]

satisfies

\[
|\det B-\det A|
\le
k\,k!\,M^{k-1}\omega(r).
\tag{10}
\]

Consequently, if

\[
k\,k!\,M^{k-1}\omega(r)<\eta,
\tag{11}
\]

then `\det B<0`. Thus a strict target violation survives any sufficiently fine one-sided row net, with an explicit target-relative error budget.

For prime-log rows there is an unconditional polynomial-rate net. Baker, Harman and Pintz proved that for all sufficiently large `x`, the interval

\[
[x,x+x^{0.525}]
=[x,x+x^{21/40}]
\tag{12}
\]

contains a prime. Applying this at `x=e^t` gives, for every sufficiently large `t`, a prime `q` such that

\[
0\le \log q-t
\le
\log(1+e^{-19t/40})
\le
e^{-19t/40}.
\tag{13}
\]

Therefore for every fixed finite pattern diameter `D`, the prime-log rows satisfy `(6)` uniformly over `0\le d\le D` with

\[
r_T=e^{-19T/40}
\tag{14}
\]

once `T` is large enough. Every fixed negative minor of a continuous translation kernel consequently has a finite negative prime-log-row witness.

If `f` is locally Hölder of exponent `0<\alpha\le1` on `J_{r_0}`,

\[
|f(s)-f(t)|\le L|s-t|^\alpha,
\tag{15}
\]

then a sufficient condition is

\[
k\,k!\,M^{k-1}L\,e^{-19\alpha T/40}<\eta,
\qquad
e^{-19T/40}<\min(\Delta,r_0).
\tag{16}
\]

For a fixed target configuration and fixed local regularity constants, the required prime scale is therefore polynomial in the inverse determinant margin:

\[
q_{\max}=O\!\left(\eta^{-40/(19\alpha)}\right)
\qquad(\eta\downarrow0),
\tag{17}
\]

up to constants depending on the target pattern, the local Hölder data, and the threshold in the Baker--Harman--Pintz theorem. In the locally Lipschitz case `\alpha=1`, the inverse-margin exponent is `40/19\approx2.1053`.

The result is not an effective finite test for RH. It gives a **conditional witness horizon once a specific violating minor, its margin, its geometry, and a local regularity bound are known**. It supplies no uniform lower bound for the first negative determinant margin, no bound on the required determinant order or target location, and no arithmetic mechanism proving the sampled inequalities.

## Quantitative transport proof

Write

\[
u_i=T+d_i+\varepsilon_i,
\qquad
0\le\varepsilon_i\le r.
\tag{18}
\]

Since `r<\Delta`,

\[
u_{i+1}-u_i
=(a_{i+1}-a_i)+(\varepsilon_{i+1}-\varepsilon_i)
\ge\Delta-r>0,
\tag{19}
\]

so the sampled rows are increasing.

Using `(8)` and `a_i=a_1+d_i`,

\[
\begin{aligned}
u_i-y_j
&=T+d_i+\varepsilon_i-b_j-u_1+a_1\\
&=a_i-b_j+(\varepsilon_i-\varepsilon_1).
\end{aligned}
\tag{20}
\]

Because both errors lie in `[0,r]`,

\[
|(u_i-y_j)-(a_i-b_j)|\le r.
\tag{21}
\]

Thus every sampled argument remains in `J_{r_0}` and

\[
|B_{ij}-A_{ij}|\le\omega(r),
\qquad
|A_{ij}|,|B_{ij}|\le M.
\tag{22}
\]

For one permutation `\sigma\in S_k`, telescope the product difference one factor at a time:

\[
\left|
\prod_{i=1}^k B_{i,\sigma(i)}
-
\prod_{i=1}^k A_{i,\sigma(i)}
\right|
\le
kM^{k-1}\omega(r).
\tag{23}
\]

Summing the `k!` signed permutation terms in the determinant gives `(10)`. Combining `(1)`, `(10)`, and `(11)` yields `\det B<0`.

This isolates the exact conditioning resource omitted by the qualitative closure argument: normalized row-pattern approximation must be fine relative not merely to geometric row separation but to the target determinant's distance from the zero-determinant boundary after propagation through the kernel's local modulus of continuity.

## Prime-log covering modulus

Baker--Harman--Pintz supply a one-sided covering estimate directly suited to `(6)`. For every sufficiently large `x`, choose a prime

\[
q\in[x,x+x^{21/40}].
\tag{24}
\]

Writing `x=e^t`,

\[
\frac{q}{e^t}
\le
1+e^{-19t/40},
\tag{25}
\]

and hence

\[
\log q-t
\le
\log(1+e^{-19t/40})
\le e^{-19t/40}.
\tag{26}
\]

For `t=T+d` with `0\le d\le D`, the right side is at most `e^{-19T/40}`. Thus every point of the translated interval `[T,T+D]` has a prime logarithm no farther than `r_T` to its right. Applying the construction simultaneously to the finitely many target offsets gives `(6)`.

The witness primes also lie in an explicit finite range. From `(24)`,

\[
q_i
\le
e^{T+d_i}\bigl(1+e^{-19(T+d_i)/40}\bigr)
\le
e^{T+D}\bigl(1+e^{-19T/40}\bigr).
\tag{27}
\]

For the Hölder case, define

\[
C=k\,k!\,M^{k-1}L.
\tag{28}
\]

Ignoring only fixed lower thresholds, `(16)` is forced by

\[
T>
\frac{40}{19\alpha}\log\frac{C}{\eta},
\tag{29}
\]

together with the independent ordering/neighborhood condition. Substitution into `(27)` gives the inverse-margin exponent in `(17)`.

## Relation to AF-379

AF-379 establishes a source-independent **Boolean determination theorem**: dense normalized finite row patterns, and in particular vanishing prime-log mesh, let continuity carry sampled nonnegativity to every real row configuration. It explicitly leaves finite prime ranges, noisy inequalities, and quantitative stability outside its scope.

AF-380 closes one precise part of that boundary. For a **fixed strict counterexample**, the determinant margin `\eta`, target row gap `\Delta`, local regularity modulus `\omega`, and prime-log covering radius together determine whether the counterexample must already be visible in a finite sampled range. The Baker--Harman--Pintz theorem turns the qualitative prime-log mesh `o(1)` into the unconditional power law `e^{-19T/40}`.

The two statements should not be conflated. AF-379 needs only continuity and proves exact implication from all sampled inequalities. AF-380 pays additional regularity/conditioning data to obtain a finite witness horizon. Exact fidelity and stable/effective fidelity are different currencies.

## Riemann specialization

AF-379 records the classical Schoenberg/Gröchenig bridge between RH and Pólya-frequency structure of the associated reciprocal-transform kernel. In any RH-facing use where the relevant translation profile satisfies the local regularity assumed here, a known strict failure of total nonnegativity can therefore be transferred to prime-log rows at a finite height with the bound above.

This does **not** make the prime labels the source of the RH discriminator. Once all prime-log minors are nonnegative, AF-379 propagates that Boolean property to all real row patterns, so the final total-positivity certificate has no residual prime specificity. AF-380 only quantifies how quickly a pre-existing global violation must become observable on the prime-log net.

Nor does `(17)` supply a search bound for an unknown RH counterexample. To use it algorithmically one would already need enough information to specify a violating determinant order, row/column configuration, negative margin, and local modulus. Those quantities may deteriorate with the first violation and no uniform lower bound is proved here. The arithmetic research problem remains upstream: produce or control the sampled inequalities intrinsically from prime data without importing the full Pólya-frequency target.

## Prior-art and novelty audit

R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`, prove the short-interval input used here: `[x,x+x^{0.525}]` contains a prime for all sufficiently large `x`.

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1--8, DOI `10.1016/j.jmaa.2008.04.070`, is the direct sampled-Pólya-frequency framework already audited in AF-373 and AF-379. Ganzburg shows that the determining behavior depends on the sampling set and source class; AF-380 does not claim a new general sampling theory.

The determinant perturbation estimate is elementary, and the log-prime covering bound `(13)` is an immediate change of variables in the Baker--Harman--Pintz theorem. A focused search for quantitative `E`-Pólya-frequency determination, prime-log total-positivity sampling, and determinant-margin witness bounds did not identify this exact packaged corollary. **No novelty is claimed.** The durable Arithmetic Fidelity content is the resource accounting: a classical short-interval prime theorem becomes an explicit conditioning modulus for transporting a fixed total-positivity violation through the prime-log compression.

The exponent `0.525` is used because Baker--Harman--Pintz give the classical all-sufficiently-large-`x` existence theorem at that scale. Later work on asymptotic prime counts in short intervals addresses a different regime and is not needed for this implication.

## Boundaries and failure modes

The bound is target-relative. A small determinant margin can force a very large witness horizon, and no source-independent positive lower bound on `\eta` is asserted.

The determinant order enters factorially through the elementary Lipschitz estimate. That constant is convenient rather than sharp. A better matrix-specific determinant condition number could improve the witness horizon without changing the fidelity mechanism.

The Hölder estimate is only one quantitative regularity model. For a merely continuous profile, `(10)` remains valid with its actual local modulus `\omega(r)` and still yields a finite witness for every fixed strict violation, but no power-law inverse-margin bound follows without a quantitative modulus.

The theorem uses arbitrary real columns exactly as AF-379 does. Discretized or arithmetic column sets introduce a second sampling problem and require their own joint pattern-density/conditioning analysis.

The Baker--Harman--Pintz estimate is an eventual one-sided net statement. Constants and the onset threshold are not made explicit here, so `(17)` is an asymptotic scaling law, not a numerically certified prime cutoff.

The logarithmic coordinate must be intrinsic to the declared translation kernel. AF-378 still forbids treating nonlinear coordinate densification as new information when the original kernel is merely transported rather than replaced by a genuinely logarithmic translation model.

Finally, this result detects **strict negativity**. It does not give a modulus for distinguishing an exactly zero determinant from a small positive one, nor does it transfer strict total positivity through limits.

## Decisive audit rule

When a sampled total-positivity proposal claims finite or stable fidelity, identify four quantities before invoking sampling density:

1. the target determinant margin from the zero-determinant boundary;
2. the intrinsic row-pattern covering radius at the relevant scale;
3. the kernel modulus of continuity on the actual target argument neighborhood;
4. the determinant sensitivity that transports entrywise error to the sign decision.

For prime-log rows, Baker--Harman--Pintz provide the unconditional covering resource `r_T\le e^{-19T/40}`. If the other three quantities are controlled, `(10)`--`(16)` give a finite witness. If they are not, qualitative determination does not by itself justify a practical or uniform finite-range conclusion.

## Consequences

AF-379's qualitative determining regime now has a target-specific quantitative companion. The prime-log sample set is not only asymptotically pattern-dense: unconditional short-interval prime theory gives a polynomial inverse-margin scale for detecting every fixed Hölder-regular strict total-positivity violation.

This sharpens the line-wide distinction between **discriminator survival, source identification, and destination conditioning**. A compression may be exactly target-faithful while the cost of exposing a small violation diverges. Conversely, improving the sampling modulus does not create prime specificity after the target has become universal under closure.

For the Riemann-facing branch, the geometry of prime-log row coverage is therefore no longer the live obstruction at either the qualitative or fixed-target quantitative level. The remaining substantive problem is to derive the sampled sign inequalities from arithmetic structure, or to identify a richer non-translation observable in which prime provenance survives the passage to the RH-equivalent destination.
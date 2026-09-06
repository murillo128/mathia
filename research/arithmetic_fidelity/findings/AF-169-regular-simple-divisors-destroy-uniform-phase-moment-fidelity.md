# AF-169 — Regular simple divisors destroy uniform phase-moment fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-167 shows that the degree together with the first `n` positive Fourier coefficients of a finite Blaschke phase derivative exactly recovers every degree-`n` zero divisor. AF-168 then shows that the inverse has a fixed-degree Hölder modulus and becomes singular at multiplicities. There is a distinct asymptotic obstruction even on simple, maximally symmetric divisors: **interior radial damping makes the same exact moment lift non-uniformly faithful as the degree grows.**

For `0<r<1`, let

\[
A_{n,r}=\{r\omega_n^j:0\le j<n\},
\qquad
\omega_n=e^{2\pi i/n},
\tag{1}
\]

be the regular degree-`n` divisor on the circle of radius `r`. All roots are simple. For the power-sum / phase-moment coordinates

\[
p_k(A)=\sum_{a\in A}a^k,
\qquad
M_n(A)=(p_1(A),\ldots,p_n(A)),
\tag{2}
\]

root-of-unity cancellation gives

\[
\boxed{
p_k(A_{n,r})=0\quad(1\le k<n),
\qquad
p_n(A_{n,r})=nr^n.}
\tag{3}
\]

Consequently, for any fixed `0<r<s<1`,

\[
\|M_n(A_{n,s})-M_n(A_{n,r})\|_\infty
=n(s^n-r^n)\longrightarrow0,
\tag{4}
\]

while the bottleneck distance between the two unordered divisors is exactly

\[
\boxed{d(A_{n,r},A_{n,s})=s-r.}
\tag{5}
\]

Thus there is **no degree-uniform recovery modulus** `omega(epsilon)->0` satisfying

\[
d(A,B)\le \omega(\|M_n(A)-M_n(B)\|_\infty)
\tag{6}
\]

on the growing family of all degree-`n` disk divisors. The retained phase-moment discrepancy can vanish exponentially while the declared divisor endpoint stays a fixed positive distance apart.

The local mechanism can also be computed exactly. At the regular divisor `(1)`, after labeling the roots `a_j=r\omega_n^j`, the Jacobian of `(2)` is

\[
J_{kj}=k a_j^{k-1}
=k r^{k-1}\omega_n^{j(k-1)},
\qquad 1\le k\le n.
\tag{7}
\]

Writing `F_n=(\omega_n^{j(k-1)})_{k,j}`, so that `F_nF_n^*=nI`, gives

\[
J=D_{n,r}F_n,
\qquad
D_{n,r}=\operatorname{diag}(1,2r,3r^2,\ldots,nr^{n-1}).
\tag{8}
\]

Hence the singular values are exactly

\[
\boxed{\sigma_k(J)=\sqrt n\,k r^{k-1}\quad(1\le k\le n),}
\tag{9}
\]

up to ordering. Since `k r^{k-1}` has no interior minimum, one obtains

\[
\sigma_{\min}(J)
=\sqrt n\min\{1,nr^{n-1}\}.
\tag{10}
\]

For every fixed `r<1`, eventually `nr^{n-1}<1`, and therefore

\[
\boxed{
\|J^{-1}\|_2
=\frac{1}{n^{3/2}r^{n-1}}.
}
\tag{11}
\]

The locally exact inverse is therefore exponentially ill-conditioned in degree even though every root is simple and the nodes are equally spaced on their radius circle.

This isolates a second stability gate beyond the multiplicity barrier of AF-168. Root collision can make the inverse singular at fixed degree; **radial attenuation of monomial moments can destroy uniform asymptotic fidelity without any multiplicity at all.** Exact finite recoverability does not prevent two endpoint-separated growing families from becoming indistinguishable in the retained unweighted moment norm.

## Derivation

### Regular polygons collapse all subcritical moments

For `(1)`,

\[
p_k(A_{n,r})
=r^k\sum_{j=0}^{n-1}\omega_n^{jk}.
\tag{12}
\]

The geometric sum is zero unless `n` divides `k`. Among the retained orders `1,...,n`, only `k=n` survives, proving `(3)`.

For fixed `r<s<1`, equation `(4)` follows immediately. The natural radial matching pairs `r\omega_n^j` with `s\omega_n^j`, giving bottleneck cost `s-r`. Conversely every point of one divisor has modulus differing from every point of the other by at least `s-r`, so no matching can do better; this proves `(5)`.

Suppose a degree-independent modulus `omega` as in `(6)` existed with `omega(t)->0` as `t->0`. Applying it to `A_{n,r},A_{n,s}` would give

\[
s-r
\le
\omega\!\left(n(s^n-r^n)\right)
\longrightarrow0,
\tag{13}
\]

which is impossible. This is stronger than saying that a condition number is large: it is an exact matched-control sequence showing failure of uniform continuity of the inverse across growing degree in these coordinates.

### The Jacobian is a radially weighted Fourier matrix

Differentiating the power sums at a locally labeled divisor gives

\[
\frac{\partial p_k}{\partial a_j}=k a_j^{k-1}.
\tag{14}
\]

At `a_j=r\omega_n^j`, equation `(8)` follows. The normalized matrix `F_n/\sqrt n` is unitary, so right multiplication by `F_n` does not mix the singular values of the diagonal row scaling except for the common factor `\sqrt n`. This proves `(9)`.

To locate the smallest diagonal weight, set

\[
f_k=k r^{k-1}.
\]

Then

\[
\frac{f_{k+1}}{f_k}=r\left(1+\frac1k\right),
\tag{15}
\]

which decreases with `k`. Thus the sequence can increase and then decrease but cannot have an interior minimum; its minimum is one of the endpoints. Equation `(10)` follows, and for fixed `r<1`, `nr^{n-1}->0`, yielding `(11)`.

There is also a direct radial differential witness. For a small `h`,

\[
M_n(A_{n,r+h})-M_n(A_{n,r})
=(0,\ldots,0,n((r+h)^n-r^n)),
\tag{16}
\]

so

\[
\|\Delta M_n\|_\infty
=n^2r^{n-1}|h|+O(h^2),
\qquad
d(A_{n,r+h},A_{n,r})=|h|.
\tag{17}
\]

Any local inverse Lipschitz constant measured in the raw sup norm of the retained moments is therefore at least `1/(n^2r^{n-1})` along this one-dimensional family. The spectral calculation `(11)` gives the corresponding exact Euclidean linearization profile for arbitrary local perturbation directions.

### The obstruction is radial, not merely angular collision

The minimum pairwise separation of the regular divisor is

\[
2r\sin(\pi/n)\sim \frac{2\pi r}{n}.
\tag{18}
\]

It does shrink with degree, as it must for `n` points on a fixed compact circle, but only polynomially. The retained radial signal `r^n` shrinks exponentially. The control therefore distinguishes two effects that are conflated by a generic "near-collision" warning: angular sampling becomes denser at order `1/n`, while the monomial basis suppresses interior high-order information at order `r^n`.

At the boundary value `r=1`, the unweighted Vandermonde part of `(8)` is exactly Fourier and perfectly conditioned up to normalization. For `r<1`, the factors `r^{k-1}` create the exponential dynamic range. This boundary/interior contrast identifies the radial monomial scaling as the source of the present failure.

## Prior art and novelty assessment

The conditioning mechanism is classical Vandermonde / moment-inversion mathematics, and no novelty is claimed for the Fourier diagonalization, singular-value calculation, or the general fact that Vandermonde systems inside the unit disk can be ill-conditioned.

- Fermín S. V. Bazán, **“Conditioning of Rectangular Vandermonde Matrices with Nodes in the Unit Disk,”** *SIAM Journal on Matrix Analysis and Applications* 21(2), 679--693 (2000), DOI `10.1137/S0895479898336021`, studies condition-number bounds for Vandermonde matrices with distinct nodes in the unit disk and their dependence on geometry and oversampling.
- Céline Aubel and Helmut Bölcskei, **“Vandermonde Matrices with Nodes in the Unit Disk and the Large Sieve,”** *Applied and Computational Harmonic Analysis* 47(1), 53--86 (2019), DOI `10.1016/j.acha.2017.07.006`, derives extremal-singular-value and condition-number bounds for nodes in the unit disk and explicitly contrasts that setting with the unit-circle large-sieve/Fourier regime.
- Victor Y. Pan, **“How Bad Are Vandermonde Matrices?”** *SIAM Journal on Matrix Analysis and Applications* 37(2), 676--694 (2016), DOI `10.1137/15M1030170`, emphasizes that large Vandermonde matrices are generally badly conditioned outside narrow configurations close to equally spaced unit-circle knots, while the DFT configuration is unitary up to scaling.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1), 199--220 (2020), DOI `10.1137/18M1212197`, gives sharp smallest-singular-value bounds for clustered unit-circle Vandermonde/Fourier nodes and separates clustering scale from recoverability.
- Stefan Kunis, Dominik Nagel, and Anna Strotmann, **“Multivariate Vandermonde matrices with separated nodes on the unit circle are stable,”** *Applied and Computational Harmonic Analysis* 58, 50--59 (2022), DOI `10.1016/j.acha.2022.01.001`, provides the complementary unit-circle result that sufficient separation can yield uniformly controlled conditioning.

These sources make the novelty boundary strict: this finding is not a new theorem about generic Vandermonde conditioning. The Arithmetic Fidelity contribution is the **endpoint-specific asymptotic audit of the exact minimal lift from AF-167**. On the regular radial family, one can see in closed form that the first-`n` phase-moment representation remains exactly injective at every finite `n` yet loses any degree-uniform inverse modulus. That is the precise failure mode the line needs when deciding whether a finite exact recovery theorem can survive a limiting arithmetic application.

## Boundary conditions and falsification checks

- The non-uniformity statement uses the raw, unweighted power-sum / phase-gradient Fourier coordinates and their ordinary `ell_infinity` or Euclidean norms. A different weighting changes the numerical conditioning and must be audited in its own data norm.
- In particular, exponentially amplifying high Fourier modes can renormalize the radial attenuation algebraically, but under a measurement model with roughly uniform absolute mode error it amplifies that error by the same exponential factor. A reweighting is therefore a genuine change of noise/precision geometry, not an automatic repair.
- The regular divisors are simple but not uniformly separated as `n->infinity`; their angular separation is `Theta(1/n)`. The claim is not that separation is irrelevant, but that the exact control exhibits exponential moment attenuation on top of only polynomial geometric crowding.
- Equations `(9)--(11)` concern the locally labeled moment map. The global matched-pair obstruction `(4)--(6)` is permutation-invariant and does not depend on a labeling choice.
- The two fixed radii `r<s<1` stay a positive distance from the unit circle. If the admissible family forces radii `r_n->1` sufficiently rapidly, the exponential attenuation may disappear; the relevant threshold must then be computed from `r_n^n` rather than inferred from this fixed-radius control.
- Conversely, if the intended endpoint is coarser than the full divisor and identifies `A_{n,r}` with `A_{n,s}`, the matched pair is endpoint-null and does not obstruct that endpoint. AF-165's quotient-relative rule still applies.
- The finding does not assert that raw power moments are the only possible intrinsic phase-sensitive lift. A different witness family may avoid the monomial radial damping; that is an escape route to be proved, not assumed.
- No statement about Riemann-zeta zeros follows directly. An RH-facing application must first justify an analogous growing-degree divisor model, identify the natural retained norm/noise scale, and show that its relevant analytic points live in a regime where the derived recovery modulus is quantitatively meaningful.

## Consequences for the research line

AF-168 made multiplicity and near-collision the first quantitative warning after exact phase-moment recovery. AF-169 adds a genuinely different gate: **a representation can be locally nonsingular at every finite stage and still fail asymptotic fidelity because its coordinates attenuate the surviving discriminator faster than the endpoint geometry contracts.**

For growing finite-divisor approximations, a useful recovery claim must therefore track at least three independent scales: the endpoint quotient actually required, the geometric multiplicity/separation profile, and the forward attenuation/noise normalization of the retained witnesses. A fixed-degree statement with an unspecified `C_n` is not enough.

The regular-polygon control provides a sharp test for proposed repairs. If a phase-like witness is claimed to be scalable, evaluate it on `A_{n,r}` and `A_{n,s}` (or the analogous symmetric family) and ask whether a fixed endpoint separation can still produce vanishing retained discrepancy. A successful alternative must either prevent that collapse through independently justified geometry, use a witness whose high-order information is not exponentially radially damped, or declare a coarser endpoint for which the radial distinction is genuinely irrelevant.
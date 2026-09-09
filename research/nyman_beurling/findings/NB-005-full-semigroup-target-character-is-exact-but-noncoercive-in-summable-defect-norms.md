# NB-005 — full semigroup target character is exact but noncoercive in summable defect norms

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + FULL-SEMIGROUP-UNIQUENESS + APPROXIMATE-SPECTRAL-ALIASING + LP-DEFECT-THRESHOLD + NEGATIVE/OBSTRUCTION`. `NB-004` proves that every fixed finite set of Bagchi dilation probes admits unit vectors exactly orthogonal to the Nyman target whose target-character defects tend simultaneously to zero. Passing from finitely many scales to the **entire integer semigroup** changes exact identification but, perhaps unexpectedly, does not restore quantitative coercivity in any defect norm whose natural scale weights are summable.

Let `A_m=T_m|_\mathcal M` be Bagchi's integer-dilation isometries on the canonical discrete space `\mathcal M`, and let `e=1` be the Nyman target. Then

\[
\boxed{
\bigcap_{m\ge2}\ker(A_m^*-m^{-1/2}I)=\mathbb C e.
}
\tag{1}
\]

So the full target character `m\mapsto m^{-1/2}` identifies the target direction **exactly**. Nevertheless, for every `2<p\le\infty`, if

\[
\mathfrak D_p(u)
:=
\left(
\sum_{m=2}^\infty
\|(A_m^*-m^{-1/2}I)u\|^p
\right)^{1/p}
\tag{2}
\]

with the usual supremum interpretation when `p=\infty`, then

\[
\boxed{
\inf_{\substack{u\in\mathcal M\cap e^\perp\\\|u\|=1}}
\mathfrak D_p(u)=0
\qquad(2<p\le\infty).
}
\tag{3}
\]

Thus exact full-semigroup uniqueness has **no stability modulus** in these natural scale-decaying norms. The obstruction is again Mellin recurrence, but now combined with the summability of `m^{-p/2}`: one can approximate more and more small scales simultaneously while the untouched large-scale tail costs arbitrarily little.

There is a sharp boundary for this specific alias mechanism. For every nonzero Mellin frequency `\tau`, the `NB-004` alias has

\[
\sum_{m=2}^M
\|(A_m^*-m^{-1/2}I)w_\tau\|^2
=
\frac{2\log M+O_\tau(1)}{1-|a_\tau|^2},
\tag{4}
\]

where `a_tau=<u_tau,e>`. Hence its full `\ell^2` defect diverges. This **does not prove** an `\ell^2` coercivity theorem for arbitrary vectors; it only shows that the projected-Mellin aliases which defeat every `p>2` norm no longer have finite total defect at the harmonic weight. A surviving semigroup certificate must therefore use a genuinely nonsummable aggregation, a scale family tied quantitatively to the finite section, or an independent source restriction on the residual's Mellin content.

## 1. The whole integer semigroup selects the target exactly

Retain the canonical real-space model and notation of `NB-004`. The space `\mathcal M\subset L^2((0,1])` consists of functions constant on

\[
I_n=\left(\frac1{n+1},\frac1n\right],
\]

and

\[
\Phi_n=\mathbf1_{(0,1/n]}
\]

is a total family. For `h\in\mathcal M` define

\[
F_n=\langle h,\Phi_n\rangle,
\qquad
c_n=nF_n.
\tag{5}
\]

`NB-004` reconstructs directly from

\[
T_m\Phi_n=\sqrt m\,\Phi_{mn}
\]

that

\[
A_m^*h=m^{-1/2}h
\quad\Longleftrightarrow\quad
c_{mn}=c_n\quad(n\ge1).
\tag{6}
\]

If the target-character equation holds for **every** integer `m>=2`, put `n=1` in (6). Then

\[
\boxed{c_m=c_1\qquad(m\ge1).}
\tag{7}
\]

If `h_n` denotes the value of `h` on `I_n`, the exact reconstruction from `NB-004` is

\[
h_n=(n+1)c_n-nc_{n+1}.
\tag{8}
\]

Equation (7) therefore gives `h_n=c_1` for every `n`; hence `h=c_1e` almost everywhere. Conversely `A_m^*e=m^{-1/2}e` is Bagchi's target covariance. This proves (1) without any reducing-subspace assumption and without resolving the still-open two-scale sequence problem `c_{2n}=c_{3n}=c_n`.

This distinction matters. Two fixed scales may or may not already have a one-dimensional **exact** compressed joint eigenspace; `NB-004` correctly leaves that question open. The entire integer semigroup does not: its exact joint eigenspace is one-dimensional for the elementary reason (7).

## 2. Diagonal Mellin recurrence approximates every fixed initial scale set

For real `\tau`, let

\[
h_\tau(x)=x^{i\tau},
\qquad
v_\tau=P_{\mathcal M}h_\tau,
\qquad
u_\tau=\frac{v_\tau}{\|v_\tau\|}.
\tag{9}
\]

`NB-004` proves

\[
A_m^*v_\tau=m^{-1/2-i\tau}v_\tau
\tag{10}
\]

for every integer `m>=1`, together with

\[
|\langle \nu_\tau,e\rangle|=O(|\tau|^{-1/2}).
\tag{11}
\]

Write

\[
a_\tau=\langle\nu_\tau,e\rangle,
\qquad
w_\tau=
\frac{\nu_\tau-a_\tau e}{\sqrt{1-|a_\tau|^2}}.
\tag{12}
\]

For large `|tau|`, `w_tau` is a unit vector in `\mathcal M\cap e^\perp`, and the target itself satisfies the same exact character. Consequently

\[
\boxed{
\|(A_m^*-m^{-1/2}I)w_\tau\|
=
\frac{m^{-1/2}|m^{-i\tau}-1|}
     {\sqrt{1-|a_\tau|^2}}.
}
\tag{13}
\]

Now choose a diagonal sequence `tau_j->infinity` for which

\[
\boxed{
 m^{-i\tau_j}\longrightarrow1
 \quad\text{for every fixed integer }m\ge2.
}
\tag{14}
\]

This requires no arithmetic independence among all logarithms. For each `j`, simultaneous Dirichlet approximation applied to the finite vector

\[
\left(\frac{\log2}{2\pi},\ldots,
      \frac{\log j}{2\pi}\right)
\]

produces arbitrarily accurate common returns to the identity on the finite torus generated by those phases. Taking successively finer returns and passing to an unbounded diagonal sequence gives (14). Equivalently, this is ordinary recurrence of the one-parameter orbit

\[
\tau\mapsto(e^{-i\tau\log2},e^{-i\tau\log3},\ldots)
\]

in each finite torus projection.

Equations (11), (13), and (14) imply that for every fixed `m`,

\[
\|(A_m^*-m^{-1/2}I)w_{\tau_j}\|\to0.
\tag{15}
\]

The new issue is whether these pointwise returns remain small after aggregating **all** scales.

## 3. Every `p>2` full-semigroup defect remains noncoercive

For all sufficiently large `j`, (11) gives

\[
(1-|a_{\tau_j}|^2)^{-1/2}\le2.
\]

Since `|m^{-i\tau}-1|<=2`, equation (13) supplies the uniform majorant

\[
\boxed{
\|(A_m^*-m^{-1/2}I)w_{\tau_j}\|
\le4m^{-1/2}.
}
\tag{16}
\]

Fix `2<p<infinity`. The sequence `m^{-p/2}` is summable. Combining the pointwise convergence (15) with the summable domination (16) and applying dominated convergence gives

\[
\boxed{
\mathfrak D_p(w_{\tau_j})^p
\longrightarrow0.
}
\tag{17}
\]

For `p=infinity`, split at an arbitrary fixed `M`. By (15),

\[
\max_{2\le m\le M}
\|(A_m^*-m^{-1/2}I)w_{\tau_j}\|\to0,
\]

while (16) gives

\[
\sup_{m>M}
\|(A_m^*-m^{-1/2}I)w_{\tau_j}\|
\le\frac4{\sqrt{M+1}}.
\tag{18}
\]

First send `j` to infinity and then `M` to infinity. This proves

\[
\boxed{
\mathfrak D_\infty(w_{\tau_j})\to0.
}
\tag{19}
\]

Every `w_{tau_j}` is a unit vector exactly orthogonal to `e`, so

\[
\operatorname{dist}(w_{\tau_j},\mathbb Ce)=1.
\tag{20}
\]

Equations (17)--(20) prove (3). In particular there is no function `omega_p(epsilon)->0` such that

\[
\operatorname{dist}(u,\mathbb Ce)
\le
\omega_p(\mathfrak D_p(u))
\tag{21}
\]

holds for all unit `u\in\mathcal M` when `p>2`, including `p=infinity`.

This is stronger than the finite-probe statement of `NB-004`. Every integer scale may be present in the observable; if their defects are aggregated with a summable `m^{-p/2}` tail, the observable still cannot distinguish the target direction from target-orthogonal Mellin aliases.

## 4. The harmonic `ell^2` aggregation blocks this particular alias construction

The borderline `p=2` behaves differently because the natural squared scale weight is `1/m`, which is not summable. For fixed `tau ne 0`, (13) gives

\[
\sum_{m=2}^M
\|(A_m^*-m^{-1/2}I)w_\tau\|^2
=
\frac1{1-|a_\tau|^2}
\sum_{m=2}^M
\frac{|m^{-i\tau}-1|^2}{m}.
\tag{22}
\]

Expand

\[
|m^{-i\tau}-1|^2
=2-2\cos(\tau\log m).
\tag{23}
\]

For fixed nonzero `tau`, elementary Euler summation gives

\[
\sum_{m\le M}m^{-1-i\tau}=O_\tau(1).
\tag{24}
\]

Indeed the difference between this sum and

\[
\int_1^M x^{-1-i\tau}\,dx
=\frac{M^{-i\tau}-1}{-i\tau}
\]

is bounded because the derivative of `x^{-1-i\tau}` is integrable on `[1,infinity)`. Taking real parts in (24), using

\[
\sum_{m\le M}\frac1m=\log M+O(1),
\]

and substituting into (22)--(23) yields

\[
\boxed{
\sum_{m=2}^M
\|(A_m^*-m^{-1/2}I)w_\tau\|^2
=
\frac{2\log M+O_\tau(1)}{1-|a_\tau|^2}.
}
\tag{25}
\]

Thus every nonzero pure Mellin alias has infinite full `ell^2` defect. The same is true before target orthogonalization.

Equation (25) is a **falsification boundary**, not a positive theorem. It does not show that an arbitrary target-orthogonal `u` has a uniformly positive or infinite `ell^2` defect, and it does not resolve whether a suitably normalized growing `ell^2` scale family controls actual finite-section residuals. It says only that the exact recurrence mechanism used in `NB-004` and in Section 3 cannot be transferred to `p=2` by dominated convergence: the harmonic scale tail retains order `log M` information.

## 5. Consequence for the target-aware finite-section route

The semigroup frontier now has three distinct levels.

First, finite fixed probe sets are non-identifying quantitatively by `NB-004`. Second, the whole infinite semigroup is **exactly** identifying by (1), but any `p>2` or supremum aggregation of its naturally attenuated defects remains quantitatively noncoercive by (3). Third, the nonsummable `ell^2` boundary survives the explicit Mellin-alias attack, but no theorem yet connects that boundary to the finite Nyman residual `d_N`.

A positive continuation therefore cannot simply add more scales and retain a summable norm. It needs at least one additional ingredient:

- a growing semigroup defect with nonsummable scale weight and a proved finite-section normalization;
- a source theorem restricting the Mellin-frequency content of near-optimal Nyman residuals, so that finite or summable probes acquire an anti-aliasing modulus;
- or direct use of the canonical target pairings `b_N`/a normed primal-dual certificate rather than inference from semigroup covariance.

The most concrete new question exposed by (25) is whether a **truncated harmonic defect** such as

\[
\frac1{\log M}
\sum_{m\le M}
\|(A_m^*-m^{-1/2}I)u\|^2
\tag{26}
\]

has a target-orthogonal lower bound on the particular source-selected class of finite-section residuals relevant to `V_N`, for an admissible relation between `M` and `N`. Equation (25) calibrates pure Mellin aliases at asymptotic value `2`; it does not establish such a lower bound for general `u`.

## 6. Prior art and evidence boundary

The load-bearing external input remains Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146; arXiv:math/0607733. Bagchi supplies the canonical discrete subspace, the integer dilation semigroup, and the covariance used by `NB-002`--`NB-004`. The full-semigroup uniqueness (7), the diagonal recurrence, dominated-convergence argument, and harmonic divergence calculation are elementary consequences reconstructed here.

A targeted search of Nyman--Beurling semigroup, joint-eigenvector, approximate-point-spectrum, and dilation-operator literature located neighboring operator-semigroup work, including Boqing Xue, *On a Hilbert Space Reformulation of Riemann Hypothesis*, arXiv:1911.04029, and recent Gram-ladder work of Hugh Carvill, arXiv:2510.18132. Those works study different operator/Gram questions and are not imported into (1)--(26). The search did not locate the specific compressed Bagchi-semigroup `p>2` noncoercivity / `p=2` alias boundary as a named theorem. This is a prior-art boundary, not a blanket novelty claim.

The result is unconditional but remains an information/stability theorem. It supplies no approximation-rate bound for `d_N`, no zero-free region, and no RH implication. The exact full-semigroup eigenspace statement should not be confused with quantitative stability, and the `ell^2` failure of the Mellin-alias counterexample should not be promoted to an `ell^2` coercivity theorem. Its durable effect is to locate a precise norm threshold that any semigroup-based target certificate must confront.
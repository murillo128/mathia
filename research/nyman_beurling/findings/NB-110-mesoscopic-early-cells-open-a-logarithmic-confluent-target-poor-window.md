# NB-110 — mesoscopic early cells open a logarithmic confluent target-poor window

**Status:** `DERIVED + GROWING-CONFLUENT-RANK + FULL-EARLY-CELL-BACKFILL + MESOSCOPIC-CELL-COERCIVITY + TARGET-AWARE-STATE-SUBSPACE + REPRESENTATION-INVARIANT + SOURCE-COMPATIBLE-WHEN-MULTIPLICITY-PRESENT + NEGATIVE/METHOD-BOUNDARY`.

`NB-109` removes the fixed-rank restriction from the one-zero confluent/Jordan channel, but its rate-free theorem stops below

\[
\frac12\frac{\log G}{\log\log G}.
\]

That threshold is not intrinsic to the fully backfilled Nyman state space. It comes from measuring the polynomial state only on a fixed terminal radial interval and then extrapolating all the way to the target endpoint, which costs roughly `(1+A)^d`, where `A=2a\log(m/r)`. The complete backfill contains much more information: a mesoscopic block of **actual early Nyman cells** already spans a radial interval whose length is a fixed fraction of `A`. Although individual cell averages can nearly vanish when the Mellin phase winds through multiples of `2pi`, a positive-density subset of cells stays uniformly away from those phase zeros. A rough Remez argument then promotes that subset to coercivity for the whole polynomial state with only a fixed-base exponential cost `C^d`.

That removes the `log log G` loss and reaches a genuine logarithmic rank window.

Let

\[
\rho_j=\frac12+a_j+iG_j,
\qquad 0<a_j<\frac12,
\qquad G_j\to\infty,
\]

put

\[
m_j=\lceil G_j\rceil,
\qquad R_j=m_jq_j,
\qquad L_j:=2a_j\log q_j\longrightarrow L\in(0,\infty),
\tag{1}
\]

and fix `r>=1`. For `0<=k<d_j`, use the confluent state vectors of `NB-108`--`NB-109`,

\[
\langle \phi_n,w_{k,j}\rangle
=
\sqrt{2a_j}\,m_j^{\lambda_j}
\int_n^{n+1}
\bigl(2a_j\log(t/m_j)\bigr)^k
 t^{-\lambda_j-3/2}\,dt,
\qquad
\lambda_j=a_j+iG_j,
\tag{2}
\]

and define

\[
S_j^{(d_j)}=\operatorname{span}\{w_{0,j},\ldots,w_{d_j-1,j}\},
\qquad
e_j=\sum_{n=r}^{R_j-1}\phi_n,
\]

\[
\delta_j^2
:=
\frac{\|P_{S_j^{(d_j)}}e_j\|_2^2}
     {\|e_j\|_2^2}.
\tag{3}
\]

Then there is a constant

\[
\boxed{c_{r,L}>0}
\]

such that

\[
\boxed{
 d_j\le c_{r,L}\log G_j
 \quad\Longrightarrow\quad
 \delta_j\longrightarrow0.
}
\tag{4}
\]

In particular every

\[
\boxed{d_j=o(\log G_j)}
\tag{5}
\]

confluent packet remains asymptotically target-poor after **all** earlier cells have been restored. For a genuine zeta zero of multiplicity at least `d_j`, this is again source-compatible in the precise sense of `NB-108`: the repeated Blaschke factor supplies exactly this derivative-state span.

The constant in `(4)` is not optimized and no significance is attached to its numerical value. The point is qualitative: the first unresolved multiplicity scale is now `Theta(log G)`, not `log G/log log G`.

## 1. A mesoscopic early annulus has positive phase-good density

Write, for one state and suppressing the index `j`,

\[
A:=2a\log\frac mr,
\qquad
u(t):=2a\log\frac tm.
\tag{6}
\]

If `A` is bounded by a sufficiently large fixed constant `K_r`, the sharper estimate already proved in `NB-109`,

\[
\delta^2
\ll_{r,L}
G^{-1}[C_L(1+A)]^{2d},
\tag{7}
\]

immediately gives `(4)` for a sufficiently small fixed multiple of `log G`. It therefore remains to treat `A>K_r`.

Choose the actual Nyman cells

\[
N=\lceil m^{3/4}\rceil,
\qquad
M=\lfloor m/10\rfloor,
\tag{8}
\]

and their radial interval

\[
J=[\nu(N),\nu(M+1)].
\tag{9}
\]

Its length is

\[
D:=|J|
=2a\log\frac{M+1}{N}
=\frac a2\log m+O(a)
=\frac A4+O_r(a).
\tag{10}
\]

Taking `K_r` large enough gives

\[
\frac A8\le D\le\frac A2.
\tag{11}
\]

Thus the target endpoint `-A` lies only a **fixed affine distance** outside `J`, uniformly in `a`, `G`, and `A`.

For one cell let

\[
h_n=\log(1+1/n),
\qquad
u_n=2a\log(n/m).
\]

After `t=ne^v`, the cell functional for a polynomial `p` of degree `<d` is

\[
I_n[p]
:=
\int_0^{h_n}
 p(\nu_n+2av)e^{-\rho v}\,dv.
\tag{12}
\]

Its frozen-polynomial factor is

\[
J_n:=\int_0^{h_n}e^{-\rho v}\,dv
=\frac{1-e^{-\rho h_n}}{\rho}.
\tag{13}
\]

Fix once and for all a small `eta in (0,pi/4)` and call a cell **phase-good** when

\[
\operatorname{dist}(G h_n,2\pi\mathbb Z)\ge\eta.
\tag{14}
\]

On a phase-good cell,

\[
|J_n|\ge \frac{c_\eta}{G}
\tag{15}
\]

for all large `G`, because the real damping over one cell is `o(1)` while the phase stays a fixed distance from a multiple of `2pi`.

These good cells occupy a fixed positive fraction of the radial interval `J`. Indeed, over `(8)` the phase variable

\[
x_n:=Gh_n
\]

runs monotonically from `asymp G^{1/4}` down to a fixed positive constant, its mesh satisfies

\[
|x_{n+1}-x_n|\ll \frac G{n^2}\ll G^{-1/2},
\tag{16}
\]

and radial length is asymptotically `2a dx/x`. In every full `2pi` phase period the excluded `eta`-neighborhoods have a fixed proportion strictly smaller than one in the `dx/x` measure; the finitely many low-phase boundary periods contribute only `O(a)`. Since `(11)` gives `D\gg_r a\log m` whenever this boundary contribution matters, a Riemann-sum comparison using `(16)` yields a fixed `kappa>0` such that the union `E_G subset J` of the phase-good radial cells satisfies

\[
\boxed{|E_G|\ge\kappa D}
\tag{17}
\]

for all sufficiently large `G`. The constant `kappa` is absolute after `eta` is fixed.

## 2. The good cells coerce the full polynomial state

For

\[
p(u)=\sum_{k=0}^{d-1}c_ku^k,
\qquad
w[p]=\sum_{k=0}^{d-1}c_kw_k,
\tag{18}
\]

the exact orthogonal-cell norm is

\[
\|w[p]\|_2^2
=
2a\,m^{2a}
\sum_{n=r}^{R-1}
 n(n+1)n^{-1-2a}|I_n[p]|^2.
\tag{19}
\]

The relevant polynomial inequality can be proved directly and does not need an external theorem.

**Rough `L^2` Remez lemma.** If `E subset J` is measurable with `|E|>=kappa|J|` and `deg p<d`, then

\[
\boxed{
\|p\|_{L^2(J)}
\le C_\kappa^d\|p\|_{L^2(E)}.
}
\tag{20}
\]

To see this, let `F subset E` be the set where

\[
|p(x)|\le (2/|E|)^{1/2}\|p\|_{L^2(E)}.
\]

Chebyshev gives `|F|>=|E|/2`. With

\[
h=\frac{\kappa|J|}{8d},
\]

a maximal `h`-separated subset of `F` has at least `d+1` points; otherwise its `h`-neighborhoods could not cover `F`. Choose ordered nodes `x_0<...<x_d`. Lagrange interpolation has numerator at most `|J|^d`, while the denominator for the `j`th basis polynomial is at least `h^d j!(d-j)!`. Summing the basis polynomials therefore costs at most `C_\kappa^d`, which bounds `sup_J|p|`; multiplying by `|J|^{1/2}` gives `(20)`. The same proof works for complex coefficients.

Now freeze `p` inside each phase-good cell. From `(15)`, `(19)`, and

\[
\Delta\nu_n=2ah_n\asymp\frac{2a}{n},
\]

the frozen contribution is bounded below by

\[
\sum_{n\ \mathrm{good}}
2a\,m^{2a}n^{1-2a}|p(\nu_n)J_n|^2
\gg
\sum_{n\ \mathrm{good}}
\left(\frac nm\right)^{2-2a}
|p(\nu_n)|^2\Delta\nu_n.
\tag{21}
\]

Because `n>=N=m^{3/4}+O(1)`,

\[
\left(\frac nm\right)^{2-2a}
\ge
m^{-(1-a)/2+o(1)}.
\tag{22}
\]

The radial mesh on the annulus is `O(a m^{-3/4})`. Comparing the good-cell samples with the integral on `E_G`, using the elementary `L^2` Markov estimate

\[
\|p'\|_{L^2(J)}
\ll \frac{d^2}{D}\|p\|_{L^2(J)},
\tag{23}
\]

and then `(20)`, shows that for `d<=c log G` with sufficiently small fixed `c`,

\[
\sum_{n\ \mathrm{good}}
|p(\nu_n)|^2\Delta\nu_n
\ge
C_0^{-d}\|p\|_{L^2(J)}^2.
\tag{24}
\]

There remains the error from freezing `p`. By the fundamental theorem of calculus and Cauchy--Schwarz,

\[
|I_n[p]-p(\nu_n)J_n|^2
\ll
 a h_n^3
\int_{\nu_n}^{\nu_{n+1}}|p'(u)|^2\,du.
\tag{25}
\]

Summing `(25)` through `(19)` over the annulus gives

\[
\|\mathrm{error}\|_2^2
\ll
 a^2m^{2a}N^{-2-2a}
\|p'\|_{L^2(J)}^2.
\tag{26}
\]

The useful cancellation is in the ratio with `(22)`: for `N=m^{3/4}`,

\[
\frac{a^2m^{2a}N^{-2-2a}}
     {m^{-(1-a)/2}}
\asymp
 a^2m^{-1}.
\tag{27}
\]

Using `(20)` and `(23)`, the squared error relative to the good frozen contribution is therefore

\[
\ll
m^{-1}C_1^d\frac{d^4}{(\log m)^2}.
\tag{28}
\]

This tends to zero for every sufficiently small fixed `c` when `d<=c log G`. Hence the actual full state, not merely the frozen model, satisfies the representation-free coercive bound

\[
\boxed{
\|w[p]\|_2^2
\ge
c_0 C_2^{-d}
 m^{-(1-a)/2}
\|p\|_{L^2(J)}^2.
}
\tag{29}
\]

The earlier and later cells omitted from the derivation only add nonnegative norm.

## 3. The exact target jet now has only fixed-base extrapolation cost

`NB-109` gives the exact full-backfill target functional

\[
\langle e,w[p]\rangle
=
\sqrt{2a}\,m^\lambda
\sum_{\ell=0}^{d-1}
\frac{(2a)^\ell}{\rho^{\ell+1}}
\left[
 p^{(\ell)}(-A)r^{-\rho}
 -p^{(\ell)}(L_j)R^{-\rho}
\right].
\tag{30}
\]

The difference from `NB-109` is that `(29)` controls `p` on the long interval `J`, whose length is comparable to `A`. By `(11)`, the point `-A` is a fixed affine distance outside `J`. Standard Lagrange interpolation on an affine copy of `J` therefore gives, directly and with no growing `(1+A)^d` factor,

\[
|p^{(\ell)}(-A)|
\le
C_3^d
\left(\frac{C_3d^2}{D}\right)^\ell
D^{-1/2}\|p\|_{L^2(J)}.
\tag{31}
\]

The point `L_j` is also at a uniformly bounded affine distance from `J` in the regime `A>K_r` because `L_j` stays in a fixed compact subset of `(0,infty)` and `D\asymp A`; enlarging `C_3` gives the same type of bound there.

After multiplication by `(2a/|rho|)^ell`, the derivative tail in `(30)` has ratio

\[
O\!\left(\frac{d^2}{G\log G}\right)=o(1)
\tag{32}
\]

for the logarithmic ranks under consideration. The lower endpoint `ell=0` therefore dominates at the scale needed here. Its squared contribution satisfies

\[
|\langle e,w[p]\rangle|^2
\ll_{r,L}
C_4^d\frac{a}{D}
G^{2a-2}
\|p\|_{L^2(J)}^2,
\tag{33}
\]

while the `R` endpoint is much smaller: its physical prefactor squared is `O(aG^{-3})` before polynomial extrapolation.

Divide `(33)` by `(29)`. Since `m\asymp G`, `a/D\asymp1/\log G`, and `a<1/2`,

\[
\frac{|\langle e,w[p]\rangle|^2}{\|w[p]\|_2^2}
\ll_{r,L}
\frac{C_5^d}{\log G}
G^{-\frac32(1-a)}
\le
\frac{C_5^d}{\log G}G^{-3/4}.
\tag{34}
\]

Also

\[
\|e\|_2^2
=
\sum_{n=r}^{R-1}\frac1{n(n+1)}
=
\frac1r-\frac1R
\asymp_r1.
\tag{35}
\]

Taking the supremum of `(34)` over nonzero `p` is exactly the squared norm of the projection of `e` onto the state space. Choosing `c_{r,L}>0` small enough that every fixed-base loss in `(24)`, `(28)`, and `(34)` is dominated by the available negative powers of `G` proves `(4)` in the `A>K_r` regime. Together with `(7)`, this proves the theorem for all possible radial approaches.

## 4. What was an artifact, and what remains genuinely open

The matched Chebyshev control in `NB-109` is sharp for a proof that keeps only a **fixed terminal radial interval**. It is not sharp for the actual fully backfilled Nyman state norm. The mesoscopic cells between `G^{3/4}` and `G/10` make the state pay for a polynomial over a radial interval of length `asymp A`; once that information is retained, extrapolation to the target endpoint costs only `C^d`. The `log log G` denominator in the previous rate-free theorem was therefore a representation/proof loss, not a genuine target-access threshold.

Several possible loopholes were stress-tested explicitly. Phase zeros of the individual cell averages do occur, but they remove only a fixed fraction of radial measure and Remez repairs the holes at fixed-base exponential cost. The regime `a->0` is uniform: either `A` is bounded and `(7)` applies, or `A>K_r` and the affine geometry `(11)` remains fixed. The exponent `3/4` in `(8)` is not structural; any fixed annulus start `G^theta` with `theta>1/2` leaves enough phase-mesh and freezing margin. It is fixed here only to avoid optimizing constants.

The proof does **not** settle arbitrary `d=O(log G)`. At `d=c log G`, the fixed-base factors `C^d` become genuine powers of `G`, so only a sufficiently small constant `c` is covered by the present coarse Remez/Markov bookkeeping. Pushing through the entire logarithmic multiplicity scale now requires either sharp constants for the full induced polynomial measure or extra source information. Many-distinct-zero packets are also untouched. Finally, this is a target-angle theorem for the one-zero Jordan state channel; it is not a direct finite-section Nyman-distance estimate and does not by itself imply RH.

The prior-art audit found the expected classical polynomial ingredients behind `(20)` and `(23)` and the already anchored Nyman/Beurling finite-section literature, but no result matching this use of a phase-good mesoscopic block of the exact Nyman cell measure to control a growing confluent state packet. No external theorem is load-bearing here: the rough measurable-set polynomial inequality needed in the proof is included above, so `SOURCES.md` requires no new dependency.

## Consequence for the research frontier

For the one-zero confluent escape, **sublogarithmic multiplicity is no longer a plausible rescue, and even a nonzero initial logarithmic window is excluded**. The remaining source-compatible question is now genuinely at the full `Theta(log G)` multiplicity scale: can the exact Nyman-induced polynomial measure improve the fixed-base constants enough to cover every allowed logarithmic Jordan rank, or can zeta-specific multiplicity information place actual repeated off-critical zeros inside the target-poor window `(4)`? If neither is available, the next qualitatively different escape is no longer another fixed or slowly growing confluence, but a collective packet involving many distinct zeros.
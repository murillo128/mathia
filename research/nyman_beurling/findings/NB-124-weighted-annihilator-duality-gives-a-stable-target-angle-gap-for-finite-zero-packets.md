# NB-124 — weighted annihilator duality gives a stable target-angle gap for finite zero packets

**Status:** `EXACT-DERIVED + WEIGHTED-ANNIHILATOR-DUALITY + STABLE-TARGET-ANGLE-GAP + APPROXIMATE-ZERO-POWER-RECURRENCE + NB-123-STRENGTHENING + SOURCE-REPRESENTATION + NEGATIVE/ROUTE-NARROWING`.

`NB-123` gives an exact separator between actual finite zero-power packets and the inverse-section matched controls of `NB-119`--`NB-122`: if a finite packet captures the visible target perfectly at cutoff `R`, then its total confluent rank must be at least `floor(log_2 R)`. Its explicit boundary is stability. Near-perfect capture only makes the geometric block increments approximately equal to the missing harmonic mode, and a naive recurrence argument appears to require uncontrolled Prony conditioning.

There is nevertheless an exact quantitative extension that uses the weighted Dirichlet geometry of `NB-117` rather than inverting a Prony system. The annihilator itself is a bounded linear functional on the first geometric block errors. Cauchy--Schwarz in the **same reciprocal block weights that occur in the Nyman cell energy** converts the missing-root value directly into a target-angle gap.

Let `F` be a finite multiset of actual nontrivial zeta zeros with `Re rho>1/2`, with distinct zeros `rho_1,...,rho_s`, multiplicities `m_1,...,m_s`, and total confluent rank

\[
d=d(F):=\sum_{j=1}^s m_j.
\tag{1}
\]

Fix an integer `q>=2`, put

\[
r:=q^{-1},
\tag{2}
\]

and use the annihilator from `NB-123`,

\[
A_{F,q}(z)
:=\prod_{j=1}^s
\bigl(z-q^{-\overline{\rho_j}}\bigr)^{m_j}
=\sum_{j=0}^{d} a_j z^j.
\tag{3}
\]

Define its normalized missing-root margin

\[
\boxed{
\mathfrak s_{F,q}
:=(1-r)
\frac{|A_{F,q}(r)|^2}
{\displaystyle\sum_{j=0}^{d}|a_j|^2r^j}.
}
\tag{4}
\]

Every actual nontrivial zero has `Re rho<1`, so `A_(F,q)(r) ne 0`; hence

\[
\mathfrak s_{F,q}>0.
\tag{5}
\]

Then for every cutoff satisfying

\[
R\ge q^{d+1},
\tag{6}
\]

and every nonzero compressed packet vector `Q_Rf`, `f in K_F`, the target angle of `NB-117` obeys

\[
\boxed{
q_R(f)
\le
\left(1+\frac{\mathfrak s_{F,q}}{L_R}\right)^{-1},
\qquad
L_R=1-\frac1R.
}
\tag{7}
\]

Consequently the entire packet target-capture fraction satisfies

\[
\boxed{
\chi_{F,R}
\le
\left(1+\frac{\mathfrak s_{F,q}}{L_R}\right)^{-1}
\le
\frac1{1+\mathfrak s_{F,q}}
<1.
}
\tag{8}
\]

Thus every **fixed finite actual zero packet has a cutoff-uniform positive target-angle gap** once the visible grid contains one full recurrence window. `NB-123` proved only that exact equality is impossible below logarithmic rank; `(8)` quantifies the separation without solving for the packet coefficients or imposing zero-node separation.

There is also a source-only lower bound on the margin. Put

\[
\beta_F:=\max_{\rho\in F}\Re\rho<1.
\tag{9}
\]

Then

\[
\boxed{
\mathfrak s_{F,q}
\ge
(1-q^{-1})
\left(
\frac{q^{-\beta_F}-q^{-1}}
{1+q^{-1/2}}
\right)^{2d}.
}
\tag{10}
\]

Therefore, if a packet family remains a fixed horizontal distance from the line `Re s=1`, polynomially near-perfect target capture still costs logarithmic confluent rank. More precisely, if

\[
\beta_F\le1-\sigma,
\qquad
\chi_{F,R}\ge1-\varepsilon,
\qquad
0<\sigma<\frac12,
\tag{11}
\]

and `R>=q^(d+1)`, define

\[
c_{q,\sigma}
:=
\frac{q^{-(1-\sigma)}-q^{-1}}
{1+q^{-1/2}}
\in(0,1).
\tag{12}
\]

Then

\[
\boxed{
d
\ge
\frac{
\log\!\left(
\frac{(1-q^{-1})(1-\varepsilon)}{L_R\varepsilon}
\right)
}
{2\log(c_{q,\sigma}^{-1})}
}
\tag{13}
\]

whenever the numerator is positive. Combining `(13)` with the complementary case `R<q^(d+1)` gives, for every fixed `alpha>0`,

\[
\boxed{
\beta_F\le1-\sigma,
\quad
\chi_{F,R}\ge1-R^{-\alpha}
\quad\Longrightarrow\quad
 d(F)\ge c_{q,\sigma,\alpha}\log R-O_{q,\sigma,\alpha}(1)
}
\tag{14}
\]

for an explicit `c_(q,sigma,alpha)>0`. This is a genuinely approximate version of the logarithmic-rank obstruction of `NB-123` in a fixed horizontal strip.

## 1. The annihilator acts directly on geometric block errors

Retain the target-tail primitive of `NB-117`,

\[
P_f(n)
=
\sum_{j=1}^{s}\sum_{\ell=0}^{m_j-1}
 c_{j,\ell}
 n^{-\overline{\rho_j}}(\log n)^\ell.
\tag{15}
\]

Sampling on `n=q^k` gives a confluent exponential-polynomial sequence. Exactly as in `NB-123`, its geometric block increments

\[
v_k:=P_f(q^k)-P_f(q^{k+1})
\tag{16}
\]

satisfy

\[
A_{F,q}(E)v=0.
\tag{17}
\]

Let

\[
A_f:=P_f(1)-P_f(R)
\tag{18}
\]

and let `H_f` be the unique harmonic-energy minimizer from `NB-117`,

\[
H_f(n)
=P_f(R)
+\frac{A_f}{L_R}
\left(\frac1n-\frac1R\right).
\tag{19}
\]

Its geometric block increments are the pure missing-root mode

\[
w_k
:=H_f(q^k)-H_f(q^{k+1})
=
\frac{A_f}{L_R}(1-r)r^k.
\tag{20}
\]

Write the block errors

\[
\varepsilon_k:=v_k-w_k
=(P_f-H_f)(q^k)-(P_f-H_f)(q^{k+1}).
\tag{21}
\]

If `(6)` holds, the first recurrence equation uses only visible blocks `0,...,d`. Since `(17)` annihilates `v` while `A(E)` acts on the pure mode `w_k=w_0r^k` by multiplication by `A(r)`, one gets the exact scalar identity

\[
\boxed{
\sum_{j=0}^{d}a_j\varepsilon_j
=-\frac{A_f}{L_R}(1-r)A_{F,q}(r).
}
\tag{22}
\]

This is the stable replacement for the contradiction in `NB-123`. Perfect target capture would set every `epsilon_j=0` and force `A(r)=0`; near-perfect capture instead has to pay enough weighted block error to realize the nonzero functional on the right-hand side.

## 2. Nyman cell energy supplies exactly the reciprocal block weights

Put

\[
h(n):=P_f(n)-H_f(n).
\tag{23}
\]

For the geometric block `q^k<=n<q^(k+1)`, Cauchy--Schwarz with weights `n(n+1)` gives

\[
\begin{aligned}
|\varepsilon_k|^2
&=\left|
\sum_{n=q^k}^{q^{k+1}-1}
\bigl(h(n)-h(n+1)\bigr)
\right|^2\\
&\le
\left(
\sum_{n=q^k}^{q^{k+1}-1}
 n(n+1)|h(n)-h(n+1)|^2
\right)
\left(
\sum_{n=q^k}^{q^{k+1}-1}
\frac1{n(n+1)}
\right).
\end{aligned}
\tag{24}
\]

The reciprocal weight telescopes exactly:

\[
\sum_{n=q^k}^{q^{k+1}-1}\frac1{n(n+1)}
=
q^{-k}-q^{-(k+1)}
=(1-r)r^k.
\tag{25}
\]

The first `d+1` geometric blocks are disjoint and lie inside the visible range by `(6)`. Hence the full `NB-117` residual energy satisfies

\[
\boxed{
\mathcal E_R(h)
\ge
\sum_{k=0}^{d}
\frac{|\varepsilon_k|^2}{(1-r)r^k}.
}
\tag{26}
\]

Apply weighted Cauchy--Schwarz once more to `(22)`:

\[
\left|\sum_{j=0}^{d}a_j\varepsilon_j\right|^2
\le
\left(
\sum_{j=0}^{d}
\frac{|\varepsilon_j|^2}{(1-r)r^j}
\right)
(1-r)
\sum_{j=0}^{d}|a_j|^2r^j.
\tag{27}
\]

Combining `(22)`, `(26)`, and `(27)` yields

\[
\boxed{
\mathcal E_R(P_f-H_f)
\ge
\frac{|A_f|^2}{L_R^2}
\mathfrak s_{F,q}.
}
\tag{28}
\]

No inversion of a Vandermonde, confluent Vandermonde, Hankel, or Prony map occurs. Node collisions can make standard parameter recovery ill-conditioned, but the target question needs only the norm of one explicit annihilator functional.

If `A_f=0`, the target pairing is zero and therefore `q_R(f)=0`, so `(7)` is trivial. If `A_f ne 0`, the exact identity from `NB-117`,

\[
q_R(f)
=
\frac1{1+L_R\mathcal E_R(P_f-H_f)/|A_f|^2},
\tag{29}
\]

combined with `(28)` proves `(7)` and `(8)`.

## 3. A crude radial bound already controls coefficient amplification

Let the roots of `(3)` be repeated according to their confluent multiplicities. For every such root

\[
\lambda=q^{-\overline\rho},
\qquad
q^{-1}<|\lambda|<q^{-1/2}.
\tag{30}
\]

Since `r=q^-1`, reverse triangle inequality gives

\[
|r-\lambda|
\ge |\lambda|-r
\ge q^{-\beta_F}-q^{-1}.
\tag{31}
\]

Therefore

\[
|A_{F,q}(r)|
\ge
\bigl(q^{-\beta_F}-q^{-1}\bigr)^d.
\tag{32}
\]

On the other hand, the coefficient `ell^1` norm of a monic product is bounded by the product of the factor `ell^1` norms:

\[
\sum_{j=0}^{d}|a_j|
\le
\prod_{\lambda}(1+|\lambda|)
\le
(1+q^{-1/2})^d.
\tag{33}
\]

Hence

\[
\sum_{j=0}^{d}|a_j|^2r^j
\le
\left(\sum_{j=0}^{d}|a_j|\right)^2
\le
(1+q^{-1/2})^{2d}.
\tag{34}
\]

Substitution into `(4)` proves `(10)`. In particular, no ordinate-separation hypothesis is needed for a positive stable gap at fixed packet rank. The coarse bound may be exponentially small in `d`, but that loss is explicit rather than hidden in an unspecified Prony condition number.

Under `beta_F<=1-sigma`, `(10)` gives

\[
\mathfrak s_{F,q}
\ge
(1-q^{-1})c_{q,\sigma}^{2d}.
\tag{35}
\]

If `chi_(F,R)>=1-epsilon`, equation `(8)` forces

\[
\frac{\mathfrak s_{F,q}}{L_R}
\le
\frac{\varepsilon}{1-\varepsilon}.
\tag{36}
\]

Equations `(35)`--`(36)` give `(13)`. If `(6)` fails, then `d>log_q R-1`; if it holds and `epsilon=R^-alpha`, equation `(13)` gives

\[
d
\ge
\frac{\alpha}{2\log(c_{q,\sigma}^{-1})}
\log R-O_{q,\sigma,\alpha}(1).
\tag{37}
\]

Taking the weaker of the two positive logarithmic constants proves `(14)`.

## 4. What this changes after NB-123

The stability issue left by `NB-123` is narrower than generic Prony conditioning suggests. For the target-angle question one does **not** need to reconstruct the zero nodes or the packet coefficients from noisy samples. The natural Nyman cell metric already assigns the geometric block errors the exact reciprocal capacities needed to test the annihilator as a dual functional.

Three regimes are now distinct.

First, a fixed finite packet is uniformly separated from perfect target capture for every sufficiently large cutoff by `(8)`. Second, a growing-rank packet whose zeros remain in `Re rho<=1-sigma` cannot achieve polynomially near-perfect capture unless its confluent rank is `Omega(log R)` by `(14)`. Third, the quantitative bound can still degenerate when rank grows and/or the rightmost packet zeros approach `Re s=1`, because the missing target root `q^-1` can then approach the sampled zero radii.

This does not eliminate all zero-node geometry. The exact margin `(4)` still depends on the full annihilator, and sharper estimates may exploit phase separation, minimal recurrence order, or structured cancellation. What `(10)` shows is that **near-collision of sampled ordinates is not required to explain loss of the present stable bound**: even after discarding all phase information, rank growth and horizontal approach to `Re s=1` already account for a complete explicit degeneration mechanism.

For the Nyman program, the next source-faithful question is therefore more specific than “make the recurrence stable.” One must either control the normalized missing-root margin `(4)` for the actual zero packets relevant to the endpoint, combine it with the horizontal-mass/height information of `NB-116`, or prove that any packet with enough target access must pay a rank/height/horizontal-depth cost incompatible with the continuum norm budget. Merely citing generic Prony instability no longer blocks a quantitative finite-packet target-angle theorem.

## 5. Prior-art and novelty boundary

Finite annihilating recurrences for exponential and confluent exponential sums are classical Prony theory; `NB-123` already records Gerlind Plonka, *Prony methods for recovery of structured functions*, GAMM-Mitteilungen 37 (2014), 239--258, DOI `10.1002/gamm.201410011`, as a representative source boundary. Stability of confluent Prony parameter recovery is also a developed subject; for example Dmitry Batenkov and Yosef Yomdin, *On the accuracy of solving confluent Prony systems*, SIAM J. Appl. Math. 73 (2013), 134--154, DOI `10.1137/110836584`, studies local recovery stability, while Turan--Nazarov/Remez-type theory supplies broader norming inequalities for exponential polynomials.

No novelty is claimed for annihilating filters, weighted Cauchy--Schwarz, Prony stability as a general topic, or norming inequalities for exponential polynomials. A search of the Nyman--Beurling/Baez-Duarte quantitative literature and neighboring Prony-stability formulations did not identify the specific estimate `(7)`--`(8)`: the line-local content is the exact splice between the `NB-117` harmonic Dirichlet-energy identity and the `NB-123` missing-root recurrence, with the geometric-block reciprocal weight `(25)` making the annihilator a direct dual certificate for target angle.

No external theorem is load-bearing in the proof. The recurrence is already proved in `NB-123`; `(24)`--`(28)` are finite Cauchy--Schwarz identities; `(31)`--`(34)` are elementary product bounds. Accordingly this finding adds no new durable dependency to `SOURCES.md`.

## 6. Boundary conditions and decisive audit tests

The cutoff condition `R>=q^(d+1)` is structural for this proof: one complete order-`d` recurrence equation for the block increments needs `d+1` visible geometric blocks. If the condition fails, the result supplies no angle bound, but the failure itself already implies `d>log_q R-1`.

The horizontal-strip corollary `(14)` requires a fixed `sigma>0`. It does not control packet families whose rightmost real parts tend to `1`; in that regime the elementary radial margin in `(31)` can vanish. Nor does `(8)` by itself exclude high-rank packets, prove a lower bound for the full Nyman approximation distance, or exclude any off-critical zero. It is a finite-packet target-angle obstruction, not an RH theorem.

The fastest audit is finite and algebraic. Expand `(3)`, choose any primitive of the form `(15)`, form the first `d+1` geometric block errors `(21)`, and check `(22)`. Independently partition the `NB-117` energy into those blocks and verify `(26)` using the telescoping identity `(25)`. The theorem then reduces to the dual norm inequality `(27)`. A counterexample to `(7)` would have to break one of those exact identities or the `NB-117` target-angle formula `(29)`.

A useful sharpness test is to minimize the first-block energy in `(26)` subject only to `(22)`. Equality in weighted Cauchy--Schwarz gives an error vector proportional to `conj(a_j)(1-r)r^j`; hence the factor `mathfrak s_(F,q)` is the exact cost of the annihilator constraint at the block-relaxed level. Any substantially stronger bound must therefore use additional consistency between block errors, further shifted recurrence equations, or arithmetic structure of the actual zero packet beyond this single recurrence window.

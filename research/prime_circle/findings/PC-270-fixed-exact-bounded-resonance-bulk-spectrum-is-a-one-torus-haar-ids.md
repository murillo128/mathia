# PC-270 — fixed exact bounded resonance bulk spectrum is a one-torus Haar IDS

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the exact bounded-resonance bulk branch left open by PC-261 and PC-269.

Let

\[
2<p_n<r_n<q_n,
\qquad q_n\to\infty,
\]

be distinct primes with

\[
\frac{p_n}{q_n}\to\alpha,
\qquad
\frac{r_n}{q_n}\to\beta,
\qquad
0<\alpha<\beta<1.
\tag{1}
\]

Assume that one fixed primitive bounded resonance is present at every sufficiently large level:

\[
\boxed{
 h p_n+k r_n=\ell q_n,
\qquad
(h,k,\ell)\in\mathbb Z^3,
\qquad
\gcd(h,k)=1,
}
\tag{2}
\]

with `(h,k) != (0,0)`. Then primality forces this to be the **only** fixed independent Fourier resonance eventually. Consequently the complete raw orbit of PC-258 does not converge to two-dimensional Haar measure; it converges exactly to Haar measure on the one-dimensional subtorus

\[
\boxed{
H_{h,k}:=\{(x,y)\in\mathbb T^2:hx+ky=0\pmod1\}.
}
\tag{3}
\]

For the collision rectangle

\[
W_{\alpha,\beta}=[1-\alpha,1)\times[1-\beta,1),
\tag{4}
\]

the collision density therefore has the deterministic limit

\[
\boxed{
\frac{\operatorname{rank}D_{p_n,r_n;q_n}}{q_n}
\longrightarrow
\delta_{h,k}(\alpha,\beta)
:=m_{H_{h,k}}(W_{\alpha,\beta}).
}
\tag{5}
\]

More strongly, for the native normalization

\[
\Delta_n=\frac{D_{p_n,r_n;q_n}}{q_n\sqrt{p_nr_n}}
\]

and the squared-singular empirical measure

\[
\nu_n=\frac1{p_n}\sum_{j=1}^{p_n}
\delta_{\sigma_j(\Delta_n)^2},
\tag{6}
\]

the whole bulk spectrum has a deterministic limit after conditioning on the fixed resonance. If `delta_{h,k}(alpha,beta)=0`, then

\[
\boxed{\nu_n\Longrightarrow\delta_0.}
\tag{7}
\]

If `delta_{h,k}(alpha,beta)>0`, then

\[
\boxed{
\nu_n\Longrightarrow
\nu^{\mathrm{res}}_{h,k;\alpha,\beta},
}
\tag{8}
\]

where the limit is the phase-averaged IDS of the same PC-257 finite-range collision operator, now induced from the circle rotation on `H_{h,k}` rather than from the full two-torus. It depends on the fixed resonance vector and limiting ratios, but not on the particular prime sequence realizing them. The same limit is obtained by admissible pairwise-coprime rational-partition controls satisfying the same fixed resonance.

Thus PC-261's sequence dependence at a rational point is real but has a sharper interpretation: different exact lifts select different classical one-dimensional subtori. Once that lift is fixed, the normalized bulk spectrum classicalizes again.

## 1. A fixed prime resonance leaves exactly one bounded annihilator

For

\[
\mu_n=
\frac1{q_n}\sum_{u=0}^{q_n-1}
\delta_{(u p_n/q_n,\,u r_n/q_n)\bmod1},
\tag{9}
\]

the Fourier coefficient at `(a,b) in Z^2` is the exact finite geometric sum

\[
\widehat\mu_n(a,b)
=
\begin{cases}
1,&q_n\mid a p_n+b r_n,\\
0,&\text{otherwise}.
\end{cases}
\tag{10}
\]

Every multiple `(a,b)=m(h,k)` resonates by (2). Conversely fix `(a,b)` not proportional to `(h,k)`. Suppose that (10) were `1` for infinitely many `n`. Then along a subsequence

\[
a p_n+b r_n=m q_n
\tag{11}
\]

for one fixed integer `m`, because the left side divided by `q_n` is bounded. Since

\[
\Delta:=hb-ak\neq0,
\]

solving (2) and (11) gives

\[
\frac{p_n}{q_n}
=\frac{\ell b-mk}{\Delta},
\qquad
\frac{r_n}{q_n}
=\frac{hm-a\ell}{\Delta}
\tag{12}
\]

exactly on that subsequence. In particular `p_n/q_n` would be one fixed nonzero rational number `A/B` in lowest terms. Then

\[
B p_n=A q_n.
\tag{13}
\]

For sufficiently large prime `q_n`, with `q_n!=p_n` and `q_n>|B|`, equation (13) is impossible: `q_n` would have to divide `B`. Hence no fixed independent character can resonate infinitely often.

The same argument shows that neither `h` nor `k` can vanish in a nontrivial infinite prime family: for example `h=0` would force `k r_n=\ell q_n`, impossible for distinct unbounded primes unless the relation is trivial.

Therefore for every fixed character

\[
\widehat\mu_n(a,b)
\longrightarrow
\mathbf 1_{\{(a,b)\in\mathbb Z(h,k)\}}.
\tag{14}
\]

The right side is precisely the Fourier transform of normalized Haar measure on (3). Fourier uniqueness on the compact torus gives

\[
\boxed{\mu_n\Longrightarrow m_{H_{h,k}}.}
\tag{15}
\]

No additional bounded-mode nonresonance hypothesis is needed once the exact primitive resonance and the all-prime source are imposed.

## 2. Collision density becomes a one-circle interval correlation

Because `gcd(h,k)=1`, Haar measure on (3) is parametrized by

\[
t\longmapsto(kt,-ht)\pmod1,
\qquad t\in\mathbb T.
\tag{16}
\]

The boundary of (4) meets this circle in only finitely many points because `h,k!=0`, hence it has zero `m_{H_{h,k}}` measure. PC-258 identifies collisions with visits to the corresponding moving rectangle, so (15) and the convergence of `(alpha_n,beta_n)` give (5), with the explicit classical correlation

\[
\boxed{
\delta_{h,k}(\alpha,\beta)
=
\int_0^1
\mathbf 1_{[1-\alpha,1)}(\{kt\})
\mathbf 1_{[1-\beta,1)}(\{-ht\})\,dt.
}
\tag{17}
\]

Equivalently, if `I_gamma=[1-gamma,1)` and hats denote circle Fourier coefficients,

\[
\boxed{
\delta_{h,k}(\alpha,\beta)
=
\sum_{j\in\mathbb Z}
\widehat{\mathbf 1_{I_\alpha}}(jh)
\widehat{\mathbf 1_{I_\beta}}(jk).
}
\tag{18}
\]

The series is absolutely convergent away from the harmless endpoint convention because the two nonzero interval coefficients contribute `O(j^{-2})` together. Thus the leading resonant rank is an ordinary correlation of interval codings on one circle. The finite-level modular-triangle discrepancy of PC-253 and the torus coding of PC-258 are two representations of the same bounded-resonance geometry at this scale.

## 3. Fixed spectral moments also reduce to the induced circle process

PC-262 writes the nonzero squared singular values of `Delta_n` as the eigenvalues of

\[
M_n=R_nG_{r,n}R_nG_{p,n},
\tag{19}
\]

where `R_n` contains the normalized Green collision weights and `G_{p,n},G_{r,n}` are nearest-neighbor path Gram matrices. Hence, for every fixed `m`,

\[
\int x^m\,d\nu_n(x)
=\frac1{p_n}\operatorname{tr}(M_n^m),
\tag{20}
\]

and each diagonal contribution to `M_n^m` depends only on a bounded collision-index neighborhood.

Let

\[
T_0(x,y)=(x+\alpha,y+\beta)\pmod1
\tag{21}
\]

restricted to `H_{h,k}`. If this circle rotation has infinite order, it is minimal; compactness then gives a uniform finite raw-time bound for returning to any fixed closed rectangle strictly inside `W_{alpha,beta}\cap H_{h,k}`. If it has finite order `Q`, every collision phase returns to itself after `Q` limiting steps. In either case, after removing an arbitrarily small neighborhood of the finitely many translated boundary points, every fixed number of successive collision events is determined by a raw orbit window whose length is bounded independently of `n`.

Since the exact vectors `(p_n/q_n,r_n/q_n)` lie on the same fixed subtorus and converge to `(alpha,beta)`, this bounded local coding is stable on the good set. Equation (15) then turns every fixed trace moment (20) into a Haar average on `H_{h,k}`. Thus for every `m>=1` there is a deterministic limit

\[
\lim_{n\to\infty}
\int x^m\,d\nu_n(x)
=\mathcal M_m^{\mathrm{res}}(h,k;\alpha,\beta).
\tag{22}
\]

The uniform norm estimate already proved in PC-262,

\[
\|\Delta_n\|\le\sqrt{\alpha_n\beta_n}<1,
\tag{23}
\]

places all `nu_n` in one compact interval. The Hausdorff moment problem is therefore determinate, so (22) proves (8).

If the circle intersection has zero Haar measure, (5) gives

\[
\frac{\operatorname{rank}D_{p_n,r_n;q_n}}{p_n}
\to0.
\tag{24}
\]

Together with (23), this means asymptotically all mass of (6) sits at the zero singular value, proving (7) without any return-time argument.

## 4. PC-261's two incompatible prime lifts are exactly two different subtori

At the common limiting point

\[
(\alpha,\beta)=(1/4,1/2),
\tag{25}
\]

PC-261 gives the exact zero family

\[
2p_n+r_n=q_n.
\tag{26}
\]

Here `(h,k,ell)=(2,1,1)`, so (17) is the Haar intersection of

\[
H_{2,1}:2x+y=0\pmod1
\]

with `[3/4,1) x [1/2,1)`. Parametrizing by `(x,y)=(t,-2t)` shows that the intersection has measure zero:

\[
\boxed{\delta_{2,1}(1/4,1/2)=0,}
\tag{27}
\]

consistent with PC-253/PC-261's exact identity `D=0`.

The opposite PC-261 family satisfies

\[
6p_n-r_n=q_n.
\tag{28}
\]

Now `(h,k,ell)=(6,-1,1)`. Parametrizing `H_{6,-1}` by `(-t,-6t)` gives

\[
\boxed{\delta_{6,-1}(1/4,1/2)=\frac16,}
\tag{29}
\]

exactly matching PC-261's asymptotic collision rank `rank(D)/q -> 1/6`.

PC-269 supplies a third all-prime branch approaching the same ratio pair while avoiding every fixed exact resonance. Its orbit instead converges to two-dimensional Haar measure and therefore has collision density

\[
\alpha\beta=\frac18.
\tag{30}
\]

The three densities

\[
0,\qquad\frac18,\qquad\frac16
\]

are therefore not mysterious competing prime asymptotics. They are respectively Haar intersections for two different one-dimensional resonant subtori and the full two-dimensional torus. The finite arithmetic lift selects the orbit closure; ordinary Haar geometry determines the bulk statistic once that closure is fixed.

## 5. Matched controls and RH-facing consequence

The proof after (2) uses only the exact affine relation, coprimality, rational-partition collision geometry, Fourier characters, finite-range path incidence, and the Green weight already isolated by PC-251--PC-258. Primality is used in Section 1 only to prove that a second independent **fixed** resonance cannot persist. An admissible pairwise-coprime control for which the same one-dimensional orbit-closure statement is imposed has exactly the same limiting local process and therefore the same bulk IDS.

Thus the route

\[
\text{fixed exact bounded resonance}
\longrightarrow
\text{bulk collision spectrum}
\longrightarrow
\text{new prime/RH invariant}
\]

fails after conditioning on the resonance vector. The resonance can change the operator by `O(1)` and can distinguish different finite lifts, as PC-261 proved, but its leading bulk effect is a classical one-frequency dynamical IDS. It supplies no intrinsic complex spectral parameter, functional equation, critical normalization, or zero detector.

This result does **not** close:

- resonance vectors `(h_n,k_n)` whose coefficients grow with `n`;
- mesoscopic windows that resolve drift on the inverse near-resonance scale;
- fine spacing, edge scaling, or outliers invisible to weak bulk convergence;
- singular functionals such as Lyapunov/log-determinant data not controlled by weak IDS alone;
- the arithmetic frequency with which different exact resonance sectors occur inside the primes; or
- a source-forced observable that still distinguishes prime shells from matched rational-partition controls after the same orbit closure and finite lift are fixed.

Those are the appropriate remaining places for an exact-resonance proposal to evade this boundary.

## 6. Prior-art and novelty audit

The abstract mechanisms used here are classical. Equation (15) is the standard Fourier/Pontryagin description of convergence to Haar measure on the closed subgroup determined by the surviving character annihilator; it is the subgroup version of the Kronecker--Weyl mechanism already used in PC-258. Coding a circle rotation by finitely many intervals is standard mechanical/Sturmian rotation coding, and phase-averaged spectral limits for finite-range periodic or quasiperiodic operators are standard IDS theory. PC-262 already anchors the finite-pattern/IDS literature, while PC-269 anchors the periodic/Jacobi representation relevant when the limiting circle translation has finite order.

A targeted novelty search against Kronecker--Weyl/subtorus equidistribution, interval codings of rotations, periodic and quasiperiodic Jacobi operators, and integrated density of states found exactly those established frameworks. No novelty is claimed for compact-group Fourier duality, circle rotations, mechanical words, moment determinacy, or IDS theory.

The durable project-local contribution is the combination specific to the Prime-Circle collision carrier: **one persistent primitive affine relation among an all-prime triple automatically exhausts all bounded Fourier resonances**, so the exact-resonance orbit closure is forced to be precisely one circle; the complete normalized bulk singular spectrum then classicalizes to the induced Haar IDS on that circle. This fills the gap between PC-261's two explicit source-realizable resonant lifts and PC-269's two-dimensional Haar theorem off exact bounded resonances.

## 7. Falsification and boundary audit

The result has direct failure tests.

1. Produce fixed `(a,b)` independent of `(h,k)` and infinitely many distinct prime triples satisfying both (2) and `q_n | a p_n+b r_n`; this would contradict the rational-ratio obstruction (12)--(13).
2. Produce a fixed-resonance sequence for which the finite orbit measures (9) have a Fourier limit different from the Haar transform in (14).
3. Produce a positive-measure collision intersection for which a fixed collision-index neighborhood cannot be recovered from any uniformly bounded raw orbit window away from a set of vanishing `H_{h,k}` measure.
4. Produce a fixed `m` for which the trace moment (20) depends on collision data outside the finite bandwidth forced by (19).
5. Produce an admissible matched rational-partition control with the same limiting one-circle process but a different bulk moment limit.

The theorem is deliberately a **bulk** classicalization at fixed resonance complexity. It makes no claim about growing-complexity resonances or non-bulk cocycle invariants.
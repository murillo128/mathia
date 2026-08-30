# PF-126 — the transported shift-clone metric defect lies in every `L^r`, `r>1`

**Status:** `EXACT-DERIVED + BOUNDARY`. PF-125 gives an explicit marked prime/shift-clone comparison whose per-pant bilipschitz constants tend to one, while PF-107 identifies the half-cuff displacement as reciprocal-prime scale. Combining those two facts with the fixed hyperbolic area of a pair of pants yields a global integrability statement for the actual transported metric coefficients: the defect is in every `L^r`, `r>1`, and in weak `L^1`. This is geometric evidence at the coefficient level only. It does not by itself imply any Schatten class for the relative resolvent, wave/scattering equivalence, a relative determinant, or an RH statement.

## Claim

Let `X` be the exact prime flute with hyperbolic metric `g`, and let `X_+` be the exact all-composite shift clone `p_n -> p_n+1`. Use the global marked homeomorphism `F:X->X_+` constructed in PF-125 and transport the clone metric to `X`:

\[
g_+:=F^*g_{X_+}.
\]

Away from the measure-zero seam/cuff locus, define the nonnegative coefficient defect

\[
D(x)
:=
\bigl\|g^{-1}g_+(x)-I\bigr\|_{\mathrm{op}}
+
\left|
\frac{d\operatorname{vol}_{g_+}}
     {d\operatorname{vol}_{g}}(x)-1
\right|.
\tag{1}
\]

Then

\[
\boxed{
D\in L^r(X,d\operatorname{vol}_g)
\qquad\text{for every }r>1.
}
\tag{2}
\]

Moreover,

\[
\boxed{D\in L^{1,\infty}(X,d\operatorname{vol}_g),}
\tag{3}
\]

where `L^{1,infinity}` is weak `L^1`.

No assertion `D in L^1` or `D notin L^1` is made.

## 1. PF-125 turns half-cuff displacement into a uniform pantwise coefficient bound

Write the canonical pants as

\[
P_n=P(2a_n,2a_{n+1},0),
\qquad
P_n^+=P(2a_n^+,2a_{n+1}^+,0),
\]

and put

\[
\delta_n:=a_n^+-a_n,
\qquad
\varepsilon_n:=\max(\delta_n,\delta_{n+1}).
\tag{4}
\]

PF-125 constructs `F` so that on the tail

\[
K_n:=\operatorname{Bilip}(F|_{P_n})
\le 1+C\varepsilon_n.
\tag{5}
\]

Let `B=g^{-1}g_+` be the positive metric endomorphism on `P_n`. A `K_n`-bilipschitz bound for lengths places both eigenvalues of `B` in

\[
[K_n^{-2},K_n^2].
\tag{6}
\]

Hence, once `K_n` is uniformly close to one,

\[
\|B-I\|_{\mathrm{op}}
\le C_1\varepsilon_n.
\tag{7}
\]

The volume-density ratio is `rho=(det B)^{1/2}`, so the same eigenvalue bound gives

\[
|\rho-1|
\le C_2\varepsilon_n.
\tag{8}
\]

Therefore there is an absolute tail constant `C_3` with

\[
\boxed{
\sup_{x\in P_n}D(x)
\le C_3\varepsilon_n.
}
\tag{9}
\]

The finitely many head pants have finite contribution to every finite `L^r` norm because PF-125's global map is bilipschitz.

## 2. The pantwise amplitudes are reciprocal-prime scale

PF-107 proves

\[
\ell_n^+-\ell_n
=\frac{2}{p_{n-1}}+o(p_{n-1}^{-1}).
\tag{10}
\]

Since `2a_n=ell_n`,

\[
\boxed{
\delta_n
=\frac{1}{p_{n-1}}+o(p_{n-1}^{-1}).
}
\tag{11}
\]

Thus

\[
\varepsilon_n=O(p_{n-1}^{-1}).
\tag{12}
\]

For every `r>1`,

\[
\sum_n \varepsilon_n^r<\infty,
\tag{13}
\]

because `sum_p p^{-r}` converges. No prime-number-theorem precision is needed.

At the endpoint `r=1`, (12) alone is only harmonic-prime scale and therefore cannot establish strong `L^1`. For weak `L^1`, the elementary bound `p_n>=n+1` is enough: after changing a finite constant,

\[
\varepsilon_n\le\frac Cn.
\tag{14}
\]

## 3. Fixed pant area converts sequence summability into surface integrability

Every complete hyperbolic pair of pants with two geodesic boundaries and one cusp has area

\[
\operatorname{area}_g(P_n)=2\pi
\tag{15}
\]

by Gauss--Bonnet. The pants have disjoint interiors and exhaust the tail. Combining (9), (13), and (15),

\[
\begin{aligned}
\int_X D(x)^r\,d\operatorname{vol}_g(x)
&\le C_{\rm head}
 +\sum_{n\gg1}
   \operatorname{area}_g(P_n)
   \bigl(C_3\varepsilon_n\bigr)^r\\
&\le C_{\rm head}
 +2\pi C_3^r\sum_{n\gg1}\varepsilon_n^r
<\infty.
\end{aligned}
\tag{16}
\]

This proves (2).

For (3), let `mu` be hyperbolic area. From (9) and (14), if `D(x)>t` on a tail pant then `n<C/t` for a fixed constant. Hence

\[
\mu\{x:D(x)>t\}
\le C_0+2\pi\frac{C_4}{t},
\tag{17}
\]

and therefore

\[
\sup_{t>0} t\,\mu\{D>t\}<\infty.
\tag{18}
\]

So `D in L^{1,infinity}`.

The seams and cuffs where PF-125's map is only piecewise smooth are one-dimensional and have zero hyperbolic area, so they do not affect (16)--(18).

## 4. Why this is the relevant coefficient-level boundary

PF-112 proves that a localized first relative resolvent for two non-isometric two-dimensional metrics has order `-2` and lies at the local weak-trace-class threshold: locally it is compatible with every `S_r`, `r>1`, but not with `S_1`. PF-125 then proves global compactness for the exact prime/shift pair.

PF-126 shows that the **actual global metric perturbation produced by the successful PF-125 marking has the matching integrability scale**:

```text
metric/density defect:
    weak-L1 and L^r for every r>1

localized first relative resolvent:
    weak-S1 scale and locally S_r-compatible for every r>1

global first relative resolvent:
    compact by PF-125, not S1 by PF-112
```

The alignment is mathematically suggestive but is not an operator-ideal theorem. On a compact manifold or in standard global pseudodifferential calculi, phase-space `L^r` symbol estimates are closely tied to Schatten membership. The prime flute has cusps, zero injectivity-radius infimum, and infinite type, so those standard implications cannot be imported without checking their global hypotheses.

## 5. Adversarial controls and limitations

Several overclaims are explicitly excluded.

First, (2) is an **upper** integrability result for one explicit successful marking. PF-107's non-`ell^1` additive cuff sequence does not imply `D notin L^1`; shrinking geometric support can compensate for a non-summable coordinate displacement, as PF-108 already demonstrates for collars and spine data.

Second, unweighted `L^r` control is not the same as the weighted heat-kernel/volume criteria that appear in scattering theory on manifolds with collapsing injectivity radius. Güneysu--Thalmaier's wave-operator criterion, for example, uses a metric-deviation integral weighted by an upper control on the heat kernel (and under Ricci lower bounds can be expressed using inverse unit-ball volumes). PF-126 does not verify that stronger weighted integral.

Third, no bounded-geometry pseudodifferential calculus is assumed. The lack of a uniform injectivity-radius lower bound is precisely why the passage from (2) to global Schatten membership remains a separate research problem rather than a corollary.

Finally, the control is adversarial for arithmetic interpretation: the second metric comes from an exact flute whose labels `p_n+1` are all composite. Any operator property forced solely by (2) and the generic two-dimensional calculus would therefore describe a prime/composite comparison class, not primality by itself.

## 6. Prior art and novelty audit

No novelty is claimed for Gauss--Bonnet, Lorentz-space estimates, reciprocal-prime summability, or the general relationship between symbol integrability and Schatten ideals.

The closest standard operator background remains the Birman--Solomyak/critical pseudodifferential theory already audited in PF-112. Joachim Toft's *Schatten-von Neumann properties in the Weyl calculus, and calculus of metrics on symplectic vector spaces*, Annals of Global Analysis and Geometry 30 (2006), 169--209, DOI `10.1007/s10455-006-9027-7`, is representative of global Weyl-Hörmander results where `L^p` symbol control yields Schatten information. Those results do not directly supply the required calculus on this degenerating infinite-type surface.

Batu Güneysu and Anton Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Annales de l'Institut Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, provide a different route to wave/scattering equivalence without an injectivity-radius lower bound, but through a stronger weighted integral condition rather than PF-126's unweighted `L^r` statement.

The durable Mathia contribution here is only the project-specific bridge

\[
\boxed{
\text{PF-125 explicit }K_n-1=O(1/p_n)
+
\operatorname{area}(P_n)=2\pi
\Longrightarrow
D\in L^{1,\infty}\cap\bigcap_{r>1}L^r.
}
\]

Directed searches found standard local/compact/bounded-geometry Schatten results and the no-injectivity-radius scattering criterion above, but no theorem that turns exactly this prime-flute coefficient estimate into a global `S_r` classification. Accordingly no novelty is claimed for such an operator conclusion because no such conclusion is established here.

## 7. Audit / falsification core

A later adversary can check PF-126 through a short chain:

1. verify PF-125's pantwise estimate `K_n<=1+C max(delta_n,delta_{n+1})` for the specific global marking used here;
2. convert a length-bilipschitz bound into the metric-endomorphism and density estimates (7)--(9);
3. use PF-107 to obtain `delta_n=1/p_{n-1}+o(1/p_{n-1})`;
4. use convergence of `sum_p p^{-r}` for `r>1` and `p_n>=n+1` for the weak-`L^1` endpoint;
5. use `area(P_n)=2pi` and disjoint pant interiors to prove (16)--(18);
6. do not infer any Schatten, determinant, or scattering statement without an additional global operator theorem adapted to the thin/infinite-type geometry.

A refutation would need to break the PF-125 pantwise metric bound, the half-cuff asymptotic imported from PF-107, or the measure conversion above. Failure of a proposed Schatten implication would not refute PF-126; it would instead identify the missing global thin-geometry mechanism.
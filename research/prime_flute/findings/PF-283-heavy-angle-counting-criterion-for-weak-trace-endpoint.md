# PF-283 — thresholded heavy-angle counting reduces the weak-trace endpoint to one Weyl bound

**Status:** `EXACT-DERIVED + CLASSICAL-SINGULAR-VALUE-CALCULUS + ENDPOINT-REDUCTION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle|PF-282]] factors the PF-281 normalized mixed form as

\[
T=F_P\Gamma F_H,
\qquad
F_P=f(|R_P|),\quad F_H=f(|R_H|),\quad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where `0\le F_P,F_H\le I` encode extension strength and `\Gamma=V_P^*V_H` is the physical low/high extension-angle operator. PF-282 proves exact ideal equivalence after fixing a positive heavy-strength threshold, but the weak-`S_1` endpoint still appeared to require an unspecified combination of heavy-channel population and angular decay as the threshold tends to zero.

There is a sharper exact reduction. Threshold the **bounded strength factors themselves**. For `0<\tau<1`, set

\[
Q_P^\tau=\mathbf1_{[\tau,1]}(F_P),
\qquad
Q_H^\tau=\mathbf1_{[\tau,1]}(F_H),
\]

and

\[
\Gamma_\tau=Q_P^\tau\Gamma Q_H^\tau,
\qquad
T_\tau=Q_P^\tau TQ_H^\tau.
\]

Then

\[
\boxed{\|T-T_\tau\|\le 2\tau}
\]

and, for every singular/approximation number,

\[
\boxed{s_j(T_\tau)\le s_j(\Gamma_\tau),\qquad
s_j(T)\le s_j(\Gamma_\tau)+2\tau.}
\]

Consequently, if

\[
N_A(a):=\#\{j:s_j(A)>a\}
\]

(with value `+\infty` allowed), then

\[
\boxed{N_T(a+2\tau)\le N_{\Gamma_\tau}(a).}
\]

In particular,

\[
\boxed{N_T(4\tau)\le N_{\Gamma_\tau}(2\tau).}
\]

Therefore the single scale-coupled estimate

\[
\boxed{
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_\tau}(2\tau)<\infty
}
\tag{PF-283 endpoint criterion}
\]

is sufficient for

\[
\boxed{T\in\mathcal S_{1,\infty}.}
\]

This converts the remaining endpoint problem into a concrete **heavy-angle Weyl count**. One no longer needs to guess separately how much weak-strength mass and how much angular decay are required: the relevant quantity is the number of singular directions of the `\tau`-heavy angle compression that still exceed the comparable angular scale `2\tau`.

## Claim

Under the hypotheses and notation of PF-282, define

\[
F_P=f(|R_P|),\qquad F_H=f(|R_H|),\qquad T=F_P\Gamma F_H,
\]

and for `0<\tau<1` define `Q_P^\tau,Q_H^\tau,\Gamma_\tau,T_\tau` as above. Then:

1. the weak-strength complement has operator norm at most `2\tau`:
   \[
   \|T-T_\tau\|\le2\tau;
   \]
2. the heavy mixed block is dominated singular-value by singular-value by its angle compression:
   \[
   s_j(T_\tau)\le s_j(\Gamma_\tau);
   \]
3. hence
   \[
   s_j(T)\le s_j(\Gamma_\tau)+2\tau
   \]
   and
   \[
   N_T(a+2\tau)\le N_{\Gamma_\tau}(a)
   \qquad(a>0);
   \]
4. if `\tau N_{\Gamma_\tau}(2\tau)` is uniformly bounded for all sufficiently small `\tau`, then `T\in\mathcal S_{1,\infty}`;
5. a still stronger but geometrically simple sufficient condition is
   \[
   \min\{\operatorname{rank}Q_P^\tau,
          \operatorname{rank}Q_H^\tau\}
   =O(\tau^{-1}),
   \]
   because `\operatorname{rank}\Gamma_\tau` is bounded by that minimum. If the heavy-channel population grows faster than `\tau^{-1}`, the endpoint can still hold, but the excess population must then be paid for by decay of the singular values of `\Gamma_\tau` at the matching scale.

## 1. Weak-strength channels are a norm-small remainder

Since `Q_P^\tau` is a spectral projection of `F_P`, it commutes with `F_P`, and similarly on the high side. Decompose

\[
T-T_\tau
=(I-Q_P^\tau)T
+Q_P^\tau T(I-Q_H^\tau).
\]

Using `T=F_P\Gamma F_H`, `\|\Gamma\|\le1`, and `\|F_P\|,\|F_H\|\le1`,

\[
\|(I-Q_P^\tau)T\|
\le\|(I-Q_P^\tau)F_P\|
\le\tau,
\]

while

\[
\|Q_P^\tau T(I-Q_H^\tau)\|
\le\|F_H(I-Q_H^\tau)\|
\le\tau.
\]

This proves

\[
\|T-T_\tau\|\le2\tau.
\tag{1}
\]

This is PF-282's norm-truncation principle expressed at the natural bounded-strength scale rather than at a threshold on the unbounded extension operators.

## 2. The heavy block is controlled by the heavy angle

Commutation with the spectral projections gives

\[
T_\tau
=F_PQ_P^\tau\,\Gamma_\tau\,Q_H^\tau F_H.
\]

Both outer factors are contractions. The ordinary two-sided singular-value inequality therefore yields

\[
s_j(T_\tau)\le s_j(\Gamma_\tau).
\tag{2}
\]

The standard perturbation inequality for approximation/singular numbers, together with (1), gives

\[
s_j(T)
\le s_j(T_\tau)+\|T-T_\tau\|
\le s_j(\Gamma_\tau)+2\tau.
\tag{3}
\]

Thus, if `s_j(T)>a+2\tau`, equation (3) forces `s_j(\Gamma_\tau)>a`. Counting such indices proves

\[
N_T(a+2\tau)\le N_{\Gamma_\tau}(a).
\tag{4}
\]

Taking `a=2\tau` gives

\[
N_T(4\tau)\le N_{\Gamma_\tau}(2\tau).
\tag{5}
\]

## 3. The exact weak-trace target is a scale-coupled heavy-angle count

Assume that for some `C,\tau_0>0`,

\[
N_{\Gamma_\tau}(2\tau)\le\frac{C}{\tau}
\qquad(0<\tau<\tau_0).
\tag{6}
\]

For `0<x<4\tau_0`, choose `\tau=x/4`. Equation (5) gives

\[
N_T(x)\le\frac{4C}{x}.
\tag{7}
\]

The standard counting-function characterization of weak trace class then gives

\[
T\in\mathcal S_{1,\infty}.
\tag{8}
\]

This is materially weaker than requiring the full angle operator `\Gamma` itself to lie in `\mathcal S_{1,\infty}`. Large angular multiplicity is allowed on channels whose extension strength is small enough, and large heavy-channel population is allowed if the corresponding angle singular values fall below the matching `O(\tau)` scale.

A purely population-based sufficient route falls out immediately:

\[
N_{\Gamma_\tau}(2\tau)
\le\operatorname{rank}\Gamma_\tau
\le\min\{\operatorname{rank}Q_P^\tau,
          \operatorname{rank}Q_H^\tau\}.
\]

Hence an `O(\tau^{-1})` Weyl bound for either heavy extension-strength population already proves the endpoint with no additional angular decay. If the canonical pant geometry has a denser heavy reservoir, the deficit is now quantified exactly: the angle compression must remove enough singular directions above scale `2\tau` to restore the same `O(\tau^{-1})` count.

## Relevance to the prime flute

PF-281 reduces the mixed Schur/commutator problem to `T\in\mathcal S_{1,\infty}`. PF-282 identifies `T` as a saturated extension-angle operator and shows that fixed-threshold angle compressions control compactness. The present reduction identifies the missing **quantitative** theorem surface:

\[
\tau\,N_{\Gamma_\tau}(2\tau)=O(1).
\]

That is a concrete target for the actual simultaneous pant-extension geometry. A geometric argument may prove it by counting reservoir-heavy extension directions, by showing principal-angle decay on those directions, or by a combination of both. Conversely, a canonical sequence `\tau_k\downarrow0` for which `\tau_kN_{\Gamma_{\tau_k}}(2\tau_k)\to\infty` would kill this sufficient endpoint route and identify precisely where the heavy reservoir defeats the weak-trace budget.

## Prior art and novelty assessment

The operator-ideal ingredients used here are classical: contraction stability of singular values, norm perturbation of approximation numbers, and the counting-function characterization of `\mathcal S_{1,\infty}` are standard trace-ideal/weak-Schatten calculus covered by the sources collected in [[research/prime_flute/SOURCES#s20--weak-trace-class-and-weak-schatten-endpoint-ideal-calculus|S20]]. No novelty is claimed for those inequalities.

The durable contribution is their exact specialization to PF-282's physical strength-angle factorization. It replaces the qualitative instruction “combine heavy-channel control with weak-strength population” by one scale-coupled counting condition on the canonical PF extension-angle operator. The literature audit found no reason to promote this elementary reduction as an external theorem or new operator-ideal principle.

## Boundary conditions and failure modes

This finding does **not** prove the endpoint criterion (6) for the prime flute. It gives only a sufficient reduction. In particular:

- it does not estimate the actual heavy-strength populations `Q_P^\tau,Q_H^\tau`;
- it does not estimate principal angles or singular values of `\Gamma_\tau`;
- failure of the sufficient bound `\tau N_{\Gamma_\tau}(2\tau)=O(1)` does not by itself prove `T\notin\mathcal S_{1,\infty}`;
- a fixed-threshold compactness statement from PF-282 is insufficient, because the endpoint depends on how the count behaves as `\tau\downarrow0`;
- no wave-operator, trace-formula, prime/clone separation, or RH consequence follows without the missing geometric estimate.

The reduction must also retain the physical `P/H` split. A scalar same-mode reservoir model or same-sector multiplicity cannot substitute for `\Gamma_\tau`.

## Decisive audit test

Re-derive (1)--(5) independently from the PF-282 factorization and test them on finite-rank models in which `F_P,F_H` have prescribed strength spectra and `\Gamma` ranges from identity overlap to rapidly decaying principal angles. The inequalities should remain exact at the stated constants.

For the actual prime flute, the decisive next theorem is to prove or refute

\[
\sup_{0<\tau<\tau_0}
\tau N_{\Gamma_\tau}(2\tau)<\infty
\]

from the simultaneous one-cusp-pant extension geometry, without replacing the operator-valued reservoir by a scalar surrogate.
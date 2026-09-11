# PF-286 — the physical extension-strength factors are noncompact, so population-only endpoint closure is unavailable

**Status:** `EXACT-DERIVED + NEGATIVE/ROUTE-NARROWING + STRENGTH-POPULATION-OBSTRUCTION`.

[[research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle|PF-282]] factors the physical energy-normalized mixed coupling as

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(K_P^{1/2}),\quad F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where `K_P=R_P^*R_P` and `K_H=R_H^*R_H` are the positive operators associated with the diagonal restrictions of the simultaneous normalized exterior form to the fixed physical low/high split of PF-212. [[research/prime_flute/findings/PF-285-complementary-weak-schatten-extension-strengths-close-the-weak-trace-endpoint-without-angle-decay|PF-285]] shows that complementary weak-Schatten decay of `F_P,F_H` would close the weak-trace endpoint without any angular decay.

For the canonical prime-flute split, that cheaper route is not available. The already-established low and high geometric mechanisms force **both strength factors to be noncompact**.

On the low side, [[research/prime_flute/findings/PF-216-positive-shift-pant-compression-has-a-growing-mass-floor|PF-216]] supplies orthonormal low-symmetric module vectors `u_n` lying in the PF-212 physical low sector and an exact form lower bound

\[
k_P\!\left[\sum_n x_nu_n\right]
\ge c\sum_n \frac{P_n}{\log P_n}|x_n|^2
\]

on every finitely supported combination after a finite head. Hence `K_P` is unbounded. Functional calculus then implies that for every `0<\tau<1`,

\[
\boxed{
\operatorname{rank}\mathbf 1_{[\tau,1]}(F_P)=\infty .
}
\]

Thus the low strength factor is not merely outside a favorable weak-Schatten exponent: it has infinitely many channels above **every** fixed positive strength threshold below one.

On the high side, [[research/prime_flute/findings/PF-227-fixed-physical-high-pass-does-not-remove-thin-pant-channel-multiplicity|PF-227]] gives a fixed `b>0` such that infinitely many adjacent module blocks of the physical high/high compression of `K` have singular values at least `b`, with growing multiplicity. If `F_H` were compact, then either `K_H` would be unbounded, forcing `\|F_H\|=1` without an eigenvalue at one and contradicting compactness, or `K_H` would be bounded. In the bounded case compactness of `F_H` would imply compactness of `K_H` by the inverse functional calculus. PF-227 then supplies an orthonormal sequence of source vectors on separated high modules whose `K_H` images retain a fixed matrix coefficient into the neighboring high module, contradicting compactness. Therefore `F_H` is noncompact, and consequently there is a fixed `\tau_H>0` such that

\[
\boxed{
\operatorname{rank}\mathbf 1_{[\tau,1]}(F_H)=\infty
\qquad(0<\tau\le\tau_H).
}
\]

The immediate consequence is precise: **no finite population exponents `p_P,p_H` exist for the canonical physical strength factors**, so PF-285's two-strength weak-Schatten closure cannot be the prime-flute endpoint theorem. This does *not* refute `T\in\mathcal S_{1,\infty}`. It says that compactness/weak-trace decay must come from the relative extension geometry carried by `\Gamma_{PF}` on genuinely infinite-dimensional heavy sectors (or from an equivalent threshold-dependent strength-angle mechanism), rather than from global decay of the two outer strength factors.

## Claim

Let

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0
\]

be the simultaneous normalized boundary precision and let `P=P_\kappa` be the fixed physical tangential-frequency projection of PF-212, with `H=I-P`. Assume the form-domain hypotheses already used in PF-281/PF-282, and let `K_P,K_H` be the positive self-adjoint operators associated with the diagonal restricted forms

\[
k_P[p]=k[p,p],\qquad k_H[h]=k[h,h].
\]

Put

\[
F_P=f(K_P^{1/2}),
\qquad
F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}}.
\tag{1}
\]

Then:

1. `K_P` is unbounded and, for every `0<\tau<1`,
   \[
   \boxed{
   \operatorname{rank}Q_P^\tau=\infty,
   \qquad
   Q_P^\tau:=\mathbf1_{[\tau,1]}(F_P).
   }
   \tag{2}
   \]
2. `F_H` is noncompact. Hence there is `\tau_H>0` such that
   \[
   \boxed{
   \operatorname{rank}Q_H^\tau=\infty
   \qquad(0<\tau\le\tau_H),
   \qquad
   Q_H^\tau:=\mathbf1_{[\tau,1]}(F_H).
   }
   \tag{3}
   \]
3. In particular neither `F_P` nor `F_H` lies in `\mathcal S_{p,\infty}` for any finite `p`, so the population-only sufficient criterion of PF-285 cannot apply to the canonical physical split.

No conclusion about compactness or weak-Schatten membership of `T=F_P\Gamma_{PF}F_H` follows from (2)--(3) alone.

## 1. PF-216 makes the physical low strength heavy at every threshold

PF-216 constructs normalized low-symmetric module vectors `u_n` and proves, after a finite head,

\[
\left\langle \sum_nx_nu_n,
K_{PF}\sum_nx_nu_n\right\rangle
\ge
c\sum_n m_n|x_n|^2,
\qquad
m_n:=\frac{P_n}{\log P_n}\longrightarrow\infty.
\tag{4}
\]

The vector `u_n` is the tangentially constant symmetric mode on module `n`; therefore it belongs to the PF-212 low sector for every fixed physical cutoff `\kappa\ge1`. Equation (4) is consequently an inequality for the restricted form `k_P` itself.

Taking `x` supported on one module already gives Rayleigh quotients tending to infinity, so `K_P` is unbounded. More strongly, for every `M>0` there is a tail subspace

\[
U_M=\overline{\operatorname{span}}\{u_n:n\ge N(M)\}
\]

of infinite dimension such that

\[
k_P[u]\ge M\|u\|^2,
\qquad u\in U_M\cap\operatorname{Dom}k_P.
\tag{5}
\]

By the spectral theorem, an unbounded positive self-adjoint operator cannot have a finite-dimensional spectral subspace above any finite threshold: if `\mathbf1_{[M,\infty)}(K_P)` had finite rank for some `M`, the restriction on that reducing finite-dimensional subspace would be bounded while the complementary spectrum lies below `M`, making `K_P` bounded. Thus

\[
\operatorname{rank}\mathbf1_{[M,\infty)}(K_P)=\infty
\qquad(M>0).
\tag{6}
\]

Since

\[
f(\sqrt\lambda)\ge\tau
\iff
\lambda\ge \lambda_\tau,
\qquad
\lambda_\tau:=\frac{\tau^2}{1-\tau^2},
\tag{7}
\]

functional calculus gives

\[
Q_P^\tau
=\mathbf1_{[\lambda_\tau,\infty)}(K_P),
\tag{8}
\]

and (2) follows.

This is stronger than merely saying that `F_P` is noncompact. The low-fed extension strength is saturated on an infinite-dimensional tail at every fixed positive strength level.

## 2. PF-227 forbids compactness of the physical high strength

PF-227 works with the same normalized precision `K_{PF}` and the same physical high projection. It proves that there are fixed constants `b>0` and, after a finite head, nonzero high subspaces on adjacent modules for which

\[
N_{H_{\kappa,n+1}B_nH_{\kappa,n}}(b)
\ge c s_n^{-1},
\qquad
B_n=\Pi_{n+1}K_{PF}\Pi_n.
\tag{9}
\]

In particular, for infinitely many mutually separated indices `n_j` one can choose unit vectors

\[
x_j\in H_{\kappa,n_j}\mathcal B_{n_j},
\qquad
y_j\in H_{\kappa,n_j+1}\mathcal B_{n_j+1}
\]

with the source vectors `x_j` orthonormal and

\[
|k_H[y_j,x_j]|
=|\langle y_j,B_{n_j}x_j\rangle|
\ge b.
\tag{10}
\]

Suppose for contradiction that `F_H=f(K_H^{1/2})` were compact.

If `K_H` were unbounded, spectral mapping would give `\|F_H\|=1`. A positive compact operator of norm one has an eigenvector with eigenvalue one, but `f(t)<1` for every finite `t`, so `1` has zero spectral projection for `f(K_H^{1/2})`. This is impossible. Hence compactness of `F_H` forces `K_H` to be bounded and `\|F_H\|<1`.

On `[0,\|F_H\|]` the inverse transform

\[
g(s)=\frac{s}{\sqrt{1-s^2}}
\]

is continuous and satisfies `g(0)=0`. Functional calculus therefore gives

\[
K_H^{1/2}=g(F_H),
\qquad
K_H=g(F_H)^2,
\tag{11}
\]

so `K_H` would be compact. But a compact operator maps the orthonormal sequence `x_j` to a norm-null sequence, whereas (10) gives

\[
\|K_Hx_j\|
\ge |\langle y_j,K_Hx_j\rangle|
\ge b.
\tag{12}
\]

This contradiction proves that `F_H` is noncompact.

For a positive contraction `F`, compactness is equivalent to finite rank of `\mathbf1_{[\tau,1]}(F)` for every `\tau>0`. Hence noncompactness of `F_H` yields a `\tau_H>0` for which `Q_H^{\tau_H}` has infinite rank, and monotonicity of the spectral projections gives (3).

The argument deliberately uses PF-227's **physical high/high** block rather than a generic high-frequency pseudodifferential heuristic. It therefore remains tied to the canonical simultaneous prime-flute precision and does not depend on replacing the one-cusp pants by a model cylinder.

## 3. The PF-285 strength-only route is decisively closed

PF-285's population criterion requires finite exponents `p_P,p_H` with

\[
\operatorname{rank}Q_P^\tau=O(\tau^{-p_P}),
\qquad
\operatorname{rank}Q_H^\tau=O(\tau^{-p_H})
\tag{13}
\]

as `\tau\downarrow0`. Equations (2)--(3) show that the left sides are already infinite at fixed positive thresholds. Therefore there is no finite weak-Schatten exponent to budget on either physical side.

This also removes the global three-currency shortcut

\[
\frac1{p_P}+\frac1r+\frac1{p_H}\ge1
\]

when it is interpreted through global weak-Schatten membership of all three factors: the two strength reciprocals contribute no finite compact-ideal currency in the canonical geometry.

What survives is PF-282/PF-283/PF-284's thresholded angle mechanism. The heavy spaces are genuinely infinite-dimensional, so the next theorem must show that the correlation operator

\[
\Gamma_{PF,\alpha,\beta}
=Q_P^\alpha\Gamma_{PF}Q_H^\beta
\]

itself loses enough singular mass despite both extension populations remaining heavy. In the strongest simple form one may still aim at `\Gamma_{PF}\in\mathcal S_{1,\infty}`; the threshold-dependent counts of PF-283/PF-284 remain the less restrictive endpoint currency.

## 4. Adversarial checks

Several tempting overstatements fail and are explicitly excluded.

First, noncompactness of `F_P` and `F_H` does **not** imply noncompactness of their sandwich. Two noncompact positive contractions can have a compact or even zero product through a sufficiently transverse middle operator. PF-282 was designed precisely to expose this distinction.

Second, PF-216's growing low floor is a statement about the diagonal restricted form, not about the mixed inverse. It is used here only to determine the spectrum of the **outer strength factor**. No inverse-locality conclusion is imported from PF-216.

Third, PF-227 concerns raw high/high normalized precision, not the final dressed weak-trace word. Its role here is only to refute compactness of the high diagonal strength. It does not provide a lower bound on `T`, on `PDH`, or on the relative resolvent.

Fourth, (3) asserts an infinite heavy high sector below some fixed threshold; it does not claim that every high-strength threshold below one has infinite rank. The low-side statement (2) is stronger because PF-216 proves unbounded low diagonal energy.

Finally, the finding assumes the PF-281/PF-282 form-domain split. If a future correction invalidated that split, the strength-angle factorization itself would have to be revisited before this consequence could be used.

## 5. Prior art and novelty assessment

The functional-analytic ingredients used here are classical: spectral functional calculus for positive self-adjoint operators, the fact that a compact positive operator has finite-rank spectral projections away from zero, and the characterization of compact operators by their action on orthonormal/weakly-null sequences. PF-282 already records standard bounded-transform references, including Schmüdgen's treatment of closed-operator bounded transforms; PF-285 records the standard weak-Schatten counting correspondence.

A targeted literature check found no reason to claim any new general operator theorem. The durable project-specific content is the combination of the **already proved canonical prime-flute estimates** PF-216 and PF-227 with PF-282's exact strength-angle factorization. That combination answers the first live question left by PF-285: the physical low/high strength census does not have finite polynomial exponents at all.

No additional external theorem is needed as a black box; the spectral-calculus steps above are included explicitly. `SOURCES.md` therefore needs no new dependency for this finding.

## Consequence for the research line

The accepted variable-corridor reservoir clue should no longer spend research effort estimating finite `p_P,p_H`: the canonical strength-only route has been falsified. The live geometric target is now the physical **heavy-sector extension angle**.

A decisive positive continuation is to prove enough compactness/counting decay for

\[
Q_P^\alpha\Gamma_{PF}Q_H^\beta
\]

on the actual simultaneous one-cusp-pant extension to satisfy PF-283's sufficient budget or a sharper asymmetric strength-angle budget. A decisive negative continuation would exhibit an infinite family of heavy low/high extension directions with nonvanishing correlation, producing a noncompact heavy compression as in PF-282's exact compactness criterion.

No wave-operator, determinant/resonance, prime/clone separation, zeta-zero, or RH conclusion follows from the present obstruction.
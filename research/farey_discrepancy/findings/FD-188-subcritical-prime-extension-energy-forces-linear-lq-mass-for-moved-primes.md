# FD-188 — Subcritical prime-extension energy forces linear Lq mass for moved primes

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** weighted source rigidity / moved-prime amplitude tariff / support-free stability
- **Depends on:** FD-185, FD-187

## Claim

`FD-185` shows that a moved prime has a positive-density **support** tariff when prime-extension multiplicativity energy is subcritical. That cardinality statement is deliberately insensitive to the size of the moved-prime error, so it becomes the wrong currency for dense perturbations whose amplitudes may be small. There is an exact weighted replacement: subcritical relation energy forces a linear amount of coefficient `L^q` mass whenever any prime value moves.

Let `a` be real-valued, supported on the squarefree integers, with

\[
a(1)=1,
\qquad
\delta(n):=a(n)-\mu(n),
\tag{1}
\]

and for fixed `1<=q<infinity` define the coefficient discrepancy mass

\[
\mathcal D_{a,q}(x)
:=
\sum_{\substack{n\le x\\\mu^2(n)=1}}
|\delta(n)|^q.
\tag{2}
\]

Retain the prime-extension energy

\[
\mathcal M_{a,q}(x)
:=
\sum_{\substack{n,pn\le x\\\mu^2(n)=\mu^2(pn)=1\\p\text{ prime}}}
|a(pn)-a(p)a(n)|^q.
\tag{3}
\]

Fix a prime `p` and write

\[
\eta_p:=a(p)+1=\delta(p),
\qquad
\Delta_p:=|\eta_p|.
\tag{4}
\]

If `q>1`, put `q'=q/(q-1)`. Then for every `lambda>0` and every `x>=p`,

\[
\boxed{
\mathcal D_{a,q}(x)+\lambda\mathcal M_{a,q}(x)
\ge
|E_{p,x}|\,
\frac{\Delta_p^q}
{\left(1+|a(p)|^{q'}+\lambda^{-1/(q-1)}\right)^{q-1}},
}
\tag{5}
\]

where

\[
E_{p,x}
:=
\{(n,pn):n\le x/p,\ \mu^2(n)=1,\ p\nmid n\}
\tag{6}
\]

is the fixed-`p` matching from `FD-185`. For `q=1`, the corresponding exact finite inequality is

\[
\boxed{
\mathcal D_{a,1}(x)+\lambda\mathcal M_{a,1}(x)
\ge
|E_{p,x}|\,
\frac{\Delta_p}
{\max\{1,|a(p)|,\lambda^{-1}\}}.
}
\tag{7}
\]

Since

\[
|E_{p,x}|
=
\frac{x}{\zeta(2)(p+1)}+O_p(\sqrt x),
\tag{8}
\]

choosing `lambda=log x` gives the weighted moved-prime tariff. If

\[
\mathcal M_{a,q}(x)=o(x/\log x),
\tag{9}
\]

then for `q>1`,

\[
\boxed{
\liminf_{x\to\infty}
\frac{\mathcal D_{a,q}(x)}x
\ge
\frac{\Delta_p^q}
{\zeta(2)(p+1)\left(1+|a(p)|^{q'}\right)^{q-1}},
}
\tag{10}
\]

and for `q=1`,

\[
\boxed{
\liminf_{x\to\infty}
\frac{\mathcal D_{a,1}(x)}x
\ge
\frac{\Delta_p}
{\zeta(2)(p+1)\max\{1,|a(p)|\}}.
}
\tag{11}
\]

Thus moved primes cannot be hidden by replacing sparse large edits with dense small-amplitude edits: every fixed nonzero prime error forces positive asymptotic `L^q` coefficient mass.

Combining this with the physical-prime rigidity of `FD-187` removes support cardinality entirely from the exact source-identification criterion:

\[
\boxed{
\mathcal D_{a,q}(x)=o(x)
\quad\text{and}\quad
\mathcal M_{a,q}(x)=o(x/\log x)
\quad\Longrightarrow\quad
a=\mu.
}
\tag{12}
\]

The linear scale in (10)--(11) is sharp. For the exact multiplicative one-prime deformation `a_(p,0)` from `FD-185`, obtained by setting the prime value `a(p)=0` and propagating it multiplicatively over the squarefree `p`-face,

\[
\mathcal M_{a_{p,0},q}(x)=0
\tag{13}
\]

and every changed coefficient has discrepancy magnitude one. Hence

\[
\boxed{
\mathcal D_{a_{p,0},q}(x)
=
\frac{x}{\zeta(2)(p+1)}+O_p(\sqrt x),
}
\tag{14}
\]

which attains the constant in (10) and (11) when `a(p)=0`.

## 1. One prime-labelled edge gives a three-variable stability inequality

Fix `(n,pn) in E_(p,x)` and abbreviate

\[
u:=\delta(n),
\qquad
v:=\delta(pn),
\qquad
e:=a(pn)-a(p)a(n).
\tag{15}
\]

Because `mu(pn)=-mu(n)` and `a(p)=-1+eta_p`, direct expansion gives the exact identity

\[
\boxed{
\eta_p\mu(n)=v-a(p)u-e.
}
\tag{16}
\]

This is the weighted analogue of the clean-edge identity in `FD-185`, but it does not require either endpoint to remain unchanged. Endpoint errors and multiplicativity error may share the burden arbitrarily.

For `q>1`, write `z=lambda^(1/q)e`. Hölder applied to

\[
\eta_p\mu(n)
=
v-a(p)u-\lambda^{-1/q}z
\tag{17}
\]

gives

\[
\Delta_p
\le
\left(|u|^q+|v|^q+\lambda|e|^q\right)^{1/q}
\left(
1+|a(p)|^{q'}+\lambda^{-1/(q-1)}
\right)^{1/q'}.
\tag{18}
\]

Raising to the `q`th power yields the exact local lower bound

\[
|u|^q+|v|^q+\lambda|e|^q
\ge
\frac{\Delta_p^q}
{\left(1+|a(p)|^{q'}+\lambda^{-1/(q-1)}\right)^{q-1}}.
\tag{19}
\]

The constant is the sharp value of the three-variable convex relaxation: equality in Hölder gives the minimizing proportions between parent error, child error and edge error.

For `q=1`, duality between `l^1` and `l^infinity` applied to (16) instead gives

\[
|u|+|v|+\lambda|e|
\ge
\frac{\Delta_p}
{\max\{1,|a(p)|,\lambda^{-1}\}},
\tag{20}
\]

which is again sharp for the isolated edge problem.

## 2. The fixed-prime matching prevents coefficient mass from being reused

The crucial geometry from `FD-185` survives the weighted relaxation. `E_(p,x)` is a matching: no squarefree coefficient is an endpoint of two distinct `p`-labelled edges. Therefore

\[
\sum_{(n,pn)\in E_{p,x}}
\left(|\delta(n)|^q+|\delta(pn)|^q\right)
\le
\mathcal D_{a,q}(x).
\tag{21}
\]

Likewise the selected `p`-edges are a subset of the full prime-extension graph, so

\[
\sum_{(n,pn)\in E_{p,x}}
|a(pn)-a(p)a(n)|^q
\le
\mathcal M_{a,q}(x).
\tag{22}
\]

Summing (19), or (20), over the matching proves (5)--(7). No sparsity assumption, sign restriction, bounded-amplitude hypothesis, or clean-edge selection appears anywhere in this step.

The edge count (8) is exactly the squarefree fixed-prime count already derived in `FD-185`. For completeness, it is the density of squarefree integers `n<=x/p` avoiding `p`, namely `x/(zeta(2)(p+1))+O_p(sqrt x)`.

## 3. Subcritical relation energy leaves a linear coefficient tariff

Set `lambda=log x`. Under (9),

\[
\lambda\mathcal M_{a,q}(x)=o(x).
\tag{23}
\]

For `q>1`, the denominator in (5) converges to

\[
\left(1+|a(p)|^{q'}\right)^{q-1},
\tag{24}
\]

while for `q=1` the denominator in (7) is eventually `max{1,|a(p)|}`. Combining this with (8) and subtracting the `o(x)` relation-energy term proves (10)--(11).

This is the amplitude-sensitive counterpart of the support tariff in `FD-185`. There a nonzero prime perturbation forced a positive density of **changed locations**, regardless of how small the perturbation was. Here the price scales continuously like `Delta_p^q` (up to the explicit local conditioning factor), so it remains meaningful when cardinal support is dense or otherwise uninformative.

## 4. Support-free exact rigidity

Assume the two hypotheses in (12). If some prime `p` is moved, then `Delta_p>0`; (10) or (11) gives

\[
\liminf_{x\to\infty}\mathcal D_{a,q}(x)/x>0,
\tag{25}
\]

contradicting `D_(a,q)(x)=o(x)`. Hence every prime is physical:

\[
a(p)=-1\qquad(p\text{ prime}).
\tag{26}
\]

If nevertheless `a!=mu`, then, because `a(1)=1` and both sources vanish on nonsquarefree integers, there is a changed squarefree composite `n_0`. `FD-187` applies on the physical-prime fibre and yields

\[
\liminf_{x\to\infty}
\frac{\log x}{x}\mathcal M_{a,q}(x)>0,
\tag{27}
\]

contradicting the second hypothesis in (12). Thus `a=mu`.

Compared with `FD-185 + FD-187`, the new criterion has replaced the support condition `S(x)=o(x)` by the strictly different weighted condition `D_(a,q)(x)=o(x)`. In particular it admits perturbations on a positive-density, or even full squarefree-density, set provided their `q`th-power amplitudes have vanishing mean.

## 5. Sharpness and failure modes

The one-prime source `a_(p,0)` shows that the scale `D_q(x)~x` is a genuine boundary, not an artefact of Hölder. Its relation energy is identically zero, while its coefficient mass has exactly the fixed-prime face density in (14). At `a(p)=0`, the asymptotic conditioning factor in (10) is one, so the leading constant is attained.

Several limits are deliberate. First, (10) is not claimed to be the optimal constant for every prescribed nonzero value `a(p)`; the local three-variable inequality is sharp, but simultaneous global consistency may force additional cost. Second, `D_q=o(x)` alone does not identify Möbius: relation energy is needed to exclude coherent multiplicative deformations. Third, relation energy alone does not identify prime values, exactly as the zero-energy controls of `FD-185` show. The theorem is a two-currency stability statement: coefficient fidelity controls the prime-label gauge, while relation energy controls composite inconsistency once that gauge is fixed.

The permanence of the source matters. For a fixed moved prime, `Delta_p` and `a(p)` are fixed constants as `x` grows. No uniform lower bound over all possible primes or all sources is asserted.

## Representation audit

Both quantities in the proof live directly on the arithmetic source. `D_(a,q)` is pointwise coefficient distance to Möbius; `M_(a,q)` is the existing prime-extension relation energy. The proof uses no cumulative inversion, adaptive basis, or spectral reweighting. The fixed-`p` matching is a literal subgraph of the squarefree prime-extension graph.

This also marks the result's limitation for the Farey program. `D_(a,q)` is an additional source-fidelity observable, not something derived here from Farey discrepancy. Therefore (12) is a source-side stability theorem, not a Franel--Landau estimate. `FD-182` still blocks any attempt to obtain the required relation-energy control from the exact dyadic midpoint ladder alone on the broad null-source class. A successful Farey bridge would have to expose enough spatial information to control the relevant source-side currencies without assuming them.

## Prior-art and novelty boundary

The generic background is classical stability of homomorphism and multiplicative functional equations. Hyers and Rassias, *Approximate homomorphisms*, Aequationes Mathematicae **44** (1992), 125--153, treats broad Ulam-stability questions for approximate homomorphisms on algebraic domains. Moore and Russell, *Approximate Representations, Approximate Homomorphisms, and Low-Dimensional Embeddings of Groups*, SIAM Journal on Discrete Mathematics **29** (2015), 182--197, DOI `10.1137/140958578`, studies averaged approximate homomorphism/representation defects on finite groups.

Those are prior-art boundaries rather than load-bearing inputs. The present proof is the elementary three-variable duality (16)--(20) plus the arithmetic fixed-prime matching already established in `FD-185`. A targeted literature search did not surface the specific deterministic statement that subcritical squarefree prime-extension energy forces the explicit linear `L^q` Möbius-distance tariff (10)--(11), or the resulting support-free criterion (12). No global novelty claim is made, and no new external theorem is required; `SOURCES.md` therefore needs no update.

## Research consequence

The source-fibre frontier is cleaner. The cardinal condition in `FD-185` is not essential for ruling out moved primes: vanishing mean `L^q` coefficient error suffices, even when the perturbation support itself is dense. Together with `FD-187`, this gives an exact support-free separator at the pair of scales

\[
\mathcal D_{a,q}(x)=o(x),
\qquad
\mathcal M_{a,q}(x)=o(x/\log x).
\tag{28}
\]

The remaining high-value question is still observation-side. One now has two precise source currencies and sharp controls showing what they buy; the Farey task is to identify a minimal spatial statistic that controls enough of them, or to construct a new null source showing that a proposed sparse spatial augmentation still cannot cross these thresholds.

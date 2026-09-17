---
id: WP-348
title: Ramified congruence factors are arithmetic inner controls, and fixed channel stripping kills the common zeta block
branch: weil_positivity
status: supported
kind: arithmetic-congruence-inner-factor-control
claim_strength: exact derivation from squarefree congruence scattering plus fixed-channel no-go and targeted prior-art audit
created: 2026-09-17
related: [WP-237, WP-242, WP-243, WP-345, WP-346, WP-347]
prior_art:
  - Carlo Angelantonj, Ioannis Florakis, and Boris Pioline, Rankin-Selberg methods for closed strings on orbifolds, JHEP 07 (2013) 181, arXiv:1304.4271
  - M. N. Huxley, Scattering matrices for congruence subgroups, in Modular Forms (Durham, 1983), Horwood, 1984, 141-156
  - Andrew R. Booker, Twist-minimal trace formulas and the Selberg eigenvalue conjecture, J. London Math. Soc. 102 (2020), 1009-1038
---

# WP-348 — Ramified congruence factors are arithmetic inner controls, and fixed channel stripping kills the common zeta block

## Claim

The specifically arithmetic escape left after `WP-347` is narrower than it first appears. One does not need a non-arithmetic point defect to obtain a source-defined reciprocal unitary-axis factor with an off-critical divisor. The **unperturbed squarefree congruence scattering matrix itself already contains such factors at every ramified prime**.

For squarefree `N`, `WP-242` derived in the constant Walsh--Hadamard cusp basis

\[
\lambda_\varepsilon(s)
=g(s)\prod_{p\mid N}\nu_{p,\varepsilon_p}(s),
\qquad
 g(s)=\frac{\zeta^\star(2s-1)}{\zeta^\star(2s)},
\tag{1}
\]

with

\[
\nu_{p,+}(s)=\frac{1+p^{1-s}}{1+p^s},
\qquad
\nu_{p,-}(s)=\frac{p^{1-s}-1}{p^s-1}.
\tag{2}
\]

Each local factor obeys

\[
\nu_{p,\pm}(1-s)=\nu_{p,\pm}(s)^{-1},
\qquad
\left|\nu_{p,\pm}\left(\frac12+it\right)\right|=1.
\tag{3}
\]

Nevertheless its divisor is not confined to the unitary axis. Explicitly,

\[
\begin{aligned}
\nu_{p,+}(s)=0
&\iff
s=1-\frac{(2k+1)\pi i}{\log p},\\
\nu_{p,+}(s)^{-1}=0
&\iff
s=\frac{(2k+1)\pi i}{\log p},
\end{aligned}
\qquad k\in\mathbb Z,
\tag{4}
\]

while

\[
\begin{aligned}
\nu_{p,-}(s)=0
&\iff
s=1-\frac{2k\pi i}{\log p},\\
\nu_{p,-}(s)^{-1}=0
&\iff
s=\frac{2k\pi i}{\log p},
\end{aligned}
\qquad k\in\mathbb Z,
\tag{5}
\]

up to the familiar possible cancellations at the real special points when the full global scalar is restored. For every nonreal point in (4), the completed-zeta factor `g(s)` is regular and nonzero, so these zeros survive in the **full arithmetic scattering eigenchannel** `lambda_epsilon` whenever `epsilon_p=+` and the remaining finitely many local factors are chosen away from accidental coincidences.

Thus

\[
\boxed{
\text{arithmetic congruence source}
+\text{self-adjoint Laplacian}
+\text{Hecke/Euler structure away from the bad primes}
+\text{unitary scattering on }\Re s=\tfrac12
\not\Rightarrow
\text{critical-line rigidity of the full scattering divisor}.
}
\tag{6}
\]

The surviving source-rigidity hypothesis cannot merely say `automorphic`, `arithmetic`, `Hecke`, or `Euler`. It must distinguish the **cofinite unramified global zeta normalizer** from the finitely ramified source-defined dressing.

There is also a second exact obstruction. In the same constant eigenbasis, no fixed linear channel readout can remove even one ramified logarithmic-derivative factor identically while retaining the common `g'/g` term. Therefore a fixed positive channel compression cannot obtain the desired unramified zeta block by simply projecting away the bad-prime factors.

**Classification:** `EXACT-DERIVED + ARITHMETIC-CONGRUENCE-INNER-FACTOR + OFF-CRITICAL-RAMIFIED-DIVISOR + FIXED-CHANNEL-STRIPPING-NO-GO + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

## 1. The squarefree local factors are source-defined inner/CDD-type controls

Put

\[
s=\frac12+z.
\tag{7}
\]

Then (2) becomes

\[
\nu_{p,+}\left(\frac12+z\right)
=
\frac{1+\sqrt p\,p^{-z}}
{1+\sqrt p\,p^z},
\qquad
\nu_{p,-}\left(\frac12+z\right)
=
\frac{\sqrt p\,p^{-z}-1}
{\sqrt p\,p^z-1}.
\tag{8}
\]

On `z=it`, numerator and denominator are complex conjugates, which proves the unit-modulus statement in (3). Replacing `z` by `-z` swaps numerator and denominator, proving reciprocity. In precisely the structural sense used by the matched controls of `WP-345`--`WP-347`, these are meromorphic inner/CDD-type factors: reciprocal across the central line, unitary on it, but free to carry reflected zero/pole pairs away from it.

The important difference from the earlier controls is **source identity**. The factors in (2) are not inserted deformations. They are forced by the actual cusp scattering of the arithmetic congruence surface `Gamma_0(N)\H`. Angelantonj--Florakis--Pioline give the squarefree tensor scattering formula from which `WP-242` derived (1)--(2); Huxley's classical congruence-subgroup formulas and later arbitrary-level treatments place the same phenomenon inside the standard Dirichlet-`L` description of arithmetic scattering.

No novelty is claimed for these formulas or their elementary zero sets. The new line-specific consequence is that the broad `arithmetic realizability should remove CDD freedom` escape left after the non-arithmetic and point-scatterer controls is false as stated: finite ramification supplies the same logical freedom internally.

## 2. The off-critical local zeros survive in a full arithmetic eigenchannel

For the `+` factor, the numerator vanishes when

\[
p^{1-s}=-1,
\tag{9}
\]

which gives the first line of (4). These points all lie on `Re s=1` and have nonzero imaginary part. At such a point `s_0`,

\[
2s_0-1
=1-\frac{2(2k+1)\pi i}{\log p},
\qquad
\Re(2s_0)=2.
\tag{10}
\]

The classical zero-free line gives

\[
\zeta(2s_0-1)\ne0,
\tag{11}
\]

and absolute convergence gives `zeta(2s_0) != 0`; the Gamma factors in the completion are also finite and nonzero there. Hence

\[
g(s_0)\ne0,\infty.
\tag{12}
\]

For `N=p`, this already proves

\[
\lambda_+(s_0)=g(s_0)\nu_{p,+}(s_0)=0
\tag{13}
\]

for an actual unperturbed congruence scattering eigenchannel. For larger squarefree `N`, choose a zero not coincident with the finite zero/pole lattices of the other bad-prime factors; then the same conclusion holds.

Reciprocity of the full scattering eigenvalue reflects these zeros into poles on `Re s=0`. The `-` channel gives the complementary even lattice in (5). The real points `s=0,1` require the usual bookkeeping with the global scalar and are irrelevant to the control because infinitely many nonreal reflected pairs remain.

This is not a counterexample to RH and not a claim that these ramified zeros are Riemann zeros. It proves exactly the opposite distinction needed by the research mandate: **arithmetic scattering has source-defined off-critical divisor components that are not the nontrivial zeta divisor**. Any positivity mechanism acting on the full scattering divisor without first distinguishing those analytic sources is therefore too coarse.

## 3. Fixed channel stripping cannot retain the common zeta logarithmic derivative

Differentiate (1) on a regular domain. Write

\[
f_{p,\pm}(s)
:=\frac{d}{ds}\log\nu_{p,\pm}(s).
\tag{14}
\]

Directly from (2),

\[
f_{p,+}(s)
=-\log p\left(
\frac{p^{1-s}}{1+p^{1-s}}
+
\frac{p^s}{1+p^s}
\right),
\tag{15}
\]

and

\[
f_{p,-}(s)
=-\log p\left(
\frac{p^{1-s}}{p^{1-s}-1}
+
\frac{p^s}{p^s-1}
\right).
\tag{16}
\]

For a fixed linear readout of the diagonal channels with coefficients `c_epsilon`,

\[
R(s)
:=
\sum_\varepsilon c_\varepsilon
\frac{d}{ds}\log\lambda_\varepsilon(s),
\tag{17}
\]

one gets

\[
R(s)
=C\frac{g'(s)}{g(s)}
+
\sum_{p\mid N}
\left(
A_{p,+}f_{p,+}(s)
+A_{p,-}f_{p,-}(s)
\right),
\tag{18}
\]

where

\[
C=\sum_\varepsilon c_\varepsilon,
\qquad
A_{p,\pm}
=\sum_{\varepsilon:\,\varepsilon_p=\pm}c_\varepsilon.
\tag{19}
\]

For every fixed `p`, the pole lattices of `f_{p,+}` and `f_{p,-}` are disjoint. The former has poles at the odd lattices

\[
s=\frac{(2k+1)\pi i}{\log p},
\qquad
s=1-\frac{(2k+1)\pi i}{\log p},
\tag{20}
\]

whereas the latter has poles at the even lattices

\[
s=\frac{2k\pi i}{\log p},
\qquad
s=1-\frac{2k\pi i}{\log p}.
\tag{21}
\]

Therefore

\[
A_{p,+}f_{p,+}(s)+A_{p,-}f_{p,-}(s)\equiv0
\tag{22}
\]

forces

\[
A_{p,+}=A_{p,-}=0.
\tag{23}
\]

But from (19), for that same prime,

\[
C=A_{p,+}+A_{p,-}.
\tag{24}
\]

Hence

\[
\boxed{
\text{fixed channel readout removes the }p\text{-local derivative identically}
\Longrightarrow
C=0
\Longrightarrow
\text{the common }g'/g\text{ block is removed too}.
}
\tag{25}
\]

This no-go does not even require positivity of the coefficients. It holds for arbitrary fixed signed linear channel combinations. A fixed positive compression is a special case: in the constant eigenbasis its diagonal channel weights are nonnegative, so it cannot evade (25).

The result is deliberately about **fixed channel readouts**. An `s`-dependent renormalization can algebraically divide an eigenvalue by its known local factor and recover `g`; that is simply analytic normalization, not a consequence of inherited Hilbert positivity. Likewise one may subtract `f_{p,pm}` by hand after identifying it. Neither operation supplies the independent sign theorem required by the Weil-positivity mandate.

## 4. Aggressive falsification and surviving escapes

**Does the bad-prime divisor disappear if one considers the determinant rather than individual channels?** No in general; classical congruence scattering determinants themselves contain finite local/conductor factors. But the present claim does not need a determinant statement: one exact arithmetic eigenchannel at `N=p` is already a matched control against broad divisor-rigidity claims.

**Could the zero of `nu_{p,+}` be cancelled by the zeta normalizer?** Not at the nonreal lattice (4). Equations (10)--(12) use the zero-free line `Re zeta=1` and absolute convergence at `Re zeta=2` to exclude that cancellation. The special real points of the `-` lattice are excluded from the argument.

**Does this destroy all possible arithmetic rigidity theorems?** No. It destroys only a theorem whose hypotheses treat the complete congruence scattering divisor uniformly. A stronger theorem could distinguish the unramified global normalizer from ramified local factors by genuinely adelic/source-defined structure. That distinction is now mandatory rather than optional.

**Can standard normalization simply factor off the bad primes?** Algebraically yes. That is already visible in (1). But `WP-242` proves that after this factorization the desired completed-zeta arithmetic is one common scalar across all channels. Equation (25) adds that fixed channel geometry cannot perform the factor removal while retaining that scalar. A successful route must make the unramified/ramified distinction *inside a positive geometric form*, not merely in a meromorphic factorization written after scalarization.

**Could an `s`-dependent moving compression evade (25)?** Possibly; (25) is not claimed for arbitrary moving weights. Such a construction would need a source-forced rule, a domain/regularity analysis, and an independent positivity theorem. Existing `WP-238`--`WP-242` controls already warn that a moving compression which merely reads the known scalar factor back out is not a new positivity mechanism.

## 5. Prior-art and novelty boundary

The explicit congruence scattering formulas are classical. Huxley computed scattering matrices and determinants for congruence subgroups in terms of Dirichlet `L`-functions; Booker explicitly summarizes this arbitrary-level result. Angelantonj--Florakis--Pioline give the squarefree `Gamma_0(N)` tensor formula used in `WP-242`, from which (2) follows by constant Hadamard diagonalization. The existence and locations of the elementary local zeros/poles are immediate consequences of those formulas and are not claimed as new mathematics.

A targeted search around congruence scattering, local factors, scattering zeros/poles, inner factors and CDD terminology found standard arithmetic scattering formulas and literature relating automorphic scattering zeros to zeta zeros, but did not identify the exact Mathia-specific falsification statement (6) together with the fixed-channel implication (25) as a named prior result. This is not a historical novelty proof. The durable contribution here is the **research-boundary correction**: the arithmetic escape left after `WP-347` cannot be phrased as generic Hecke/Euler realizability, because actual congruence ramification already realizes source-defined off-critical reciprocal factors; and the constant cusp-channel geometry cannot strip those factors while keeping the common zeta derivative.

## Consequence for `weil_positivity`

The control chain now reaches inside the arithmetic category:

\[
\boxed{
\begin{array}{c}
\text{squarefree congruence Maaß--Selberg/scattering geometry}\\
\Downarrow\\
\lambda_\varepsilon(s)=g(s)\prod_{p\mid N}\nu_{p,\varepsilon_p}(s)\\
\Downarrow\\
\text{ramified }\nu_{p,\pm}\text{ are source-defined unitary inner factors with off-critical divisors}
\end{array}
}
\tag{26}
\]

while

\[
\boxed{
\text{fixed channel stripping of one }\nu_p
\Longrightarrow
\text{loss of the common }g'/g.
}
\tag{27}
\]

Accordingly, the surviving Maaß--Selberg route is not `find an arithmetic self-adjoint scattering realization`. That already exists and is still divisor-indefinite in the relevant broad sense. A viable mechanism must instead produce a **source-defined positive form that distinguishes the cofinite unramified completed-zeta normalizer from finite ramified dressing before scalar channel readout**, or use a different noncentral/global coupling in which that distinction and the sign theorem arise together. Merely dividing out bad-prime factors, choosing channel combinations, or inspecting their zero sets after the fact is analytic normalization, not geometric Weil positivity.

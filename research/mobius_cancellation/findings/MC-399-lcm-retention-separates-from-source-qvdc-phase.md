# MC-399 — Lcm retention separates exactly from the source q-vdC phase

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact source-signature/Selberg setup of `MC-397` and the lcm-fiber compression of `MC-398`. Let

\[
f(n)=\left(\sum_{d\mid n}g(d)\right)^2
=\sum_{\ell\mid n} C_g(\ell),
\qquad g(d)=0\quad(d>B),
\]

and let `W` be the source-mode group, `H=|W|`, with common-modulus Dirichlet characters `\chi_I` and signature map `\Phi` as in `MC-397`. For the normalized uniform source vector, the exact post-Selberg incidence quantity of `MC-398` is

\[
\mathcal S(N)
:=
H\sum_{\substack{\ell\le B^2\\(\ell,P)=1}}
C_g(\ell)
\#\left\{
m\le N/\ell:
(m,P)=1,
\Phi(m)=\Phi(\ell)^{-1}
\right\}.
\tag{1}
\]

Finite character orthogonality and complete multiplicativity give the exact factorization

\[
\boxed{
\mathcal S(N)
=
\sum_{I\in W}
\sum_{\ell\le B^2}
C_g(\ell)\chi_I(\ell)
M_I(N/\ell),
}
\tag{2}
\]

where

\[
M_I(X):=\sum_{m\le X}\chi_I(m).
\tag{3}
\]

Equivalently,

\[
\boxed{
\mathcal S(N)
=
\sum_{I\in W}\sum_{n\le N} f(n)\chi_I(n).
}
\tag{4}
\]

Thus, after the exact source Fourier expansion, the surviving lcm variable `\ell` does **not** remain nonseparably inside the source-character phase. For each fixed source mode `I`,

\[
\chi_I(\ell m)=\chi_I(\ell)\chi_I(m).
\tag{5}
\]

Consequently every standard additive van-der-Corput correlation applied to the inner `m`-sum loses the lcm factor immediately. If

\[
F_{I,\ell}(m):=\chi_I(\ell m),
\]

then for every shift `h`,

\[
\boxed{
F_{I,\ell}(m+h)\overline{F_{I,\ell}(m)}
=
\chi_I(m+h)\overline{\chi_I(m)}
}
\tag{6}
\]

whenever `(\ell,P)=1`; the equality also extends harmlessly across non-units because Dirichlet characters vanish there. The scalar factor `\chi_I(\ell)` has modulus one and cancels before any post-Cauchy diagonal is counted. The same is true after further additive differencing.

Therefore the **single lcm variable left by `MC-398` cannot, in the standard source-character representation, reproduce the specific Stadlmann retained-variable mechanism merely by being kept inside the `m`-side q-van-der-Corput step**. Stadlmann's gain comes from an arithmetic variable that remains nonseparably inside the post-Cauchy congruence and changes the diagonal count. Here the source phase factors before that geometry is formed.

What survives is still potentially nontrivial: `\ell` remains inside the signed coefficient `C_g(\ell)\chi_I(\ell)` and the moving endpoint `N/\ell`. A collective estimate for the hyperbola transform in `(2)`, a direct signature-incidence theorem, or a genuinely non-lcm-factorable pre-quadratic representation may still improve the source-cost frontier. The present finding rules out only the **Stadlmann-style mixed-phase interpretation of the standard lcm variable**.

No estimate for `M(x)` follows.

## 1. Exact source-character factorization of the lcm incidence sum

For units modulo `P`, `MC-397` gives the finite Fourier identity

\[
H\,\mathbf 1_{\Phi(n)=1}
=
\sum_{I\in W}\chi_I(n).
\tag{7}
\]

Using the common-modulus convention, both sides vanish when `(n,P)>1`, so globally

\[
H\,\mathbf 1_{(n,P)=1}\mathbf 1_{\Phi(n)=1}
=
\sum_{I\in W}\chi_I(n).
\tag{8}
\]

For `(\ell,P)=1`, the condition in `(1)` is equivalent to

\[
\Phi(\ell m)=1.
\]

Insert `(8)` with `n=\ell m` into `(1)`. Since Dirichlet characters are completely multiplicative,

\[
\chi_I(\ell m)=\chi_I(\ell)\chi_I(m),
\]

and hence

\[
\begin{aligned}
\mathcal S(N)
&=
\sum_{\ell\le B^2} C_g(\ell)
\sum_{m\le N/\ell}
\sum_{I\in W}\chi_I(\ell m)\\
&=
\sum_{I\in W}
\sum_{\ell\le B^2}
C_g(\ell)\chi_I(\ell)
\sum_{m\le N/\ell}\chi_I(m),
\end{aligned}
\]

which is `(2)`.

There is also a useful one-variable form. Since `f(n)=\sum_{\ell\mid n}C_g(\ell)`, writing `n=\ell m` yields

\[
\begin{aligned}
\sum_{I\in W}\sum_{n\le N}f(n)\chi_I(n)
&=
\sum_{I\in W}\sum_{n\le N}\chi_I(n)
\sum_{\ell\mid n}C_g(\ell)\\
&=
\sum_{I\in W}\sum_{\ell\le B^2}C_g(\ell)
\chi_I(\ell)M_I(N/\ell),
\end{aligned}
\]

proving `(4)`.

Equations `(2)` and `(4)` are exact identities, not estimates. They identify where the remaining lcm information actually lives: in a divisor-hyperbola decomposition of one source-character-weighted Selberg sum.

## 2. The first additive correlation removes the lcm source phase exactly

Fix a source mode `I` and a unit `\ell` modulo `P`. Inside the inner sum of `(2)`, the source-character kernel is

\[
F_{I,\ell}(m)=\chi_I(\ell)\chi_I(m).
\tag{9}
\]

Apply the elementary correlation appearing in additive van der Corput:

\[
\Delta_h F_{I,\ell}(m)
:=F_{I,\ell}(m+h)\overline{F_{I,\ell}(m)}.
\]

Because `|\chi_I(\ell)|=1`,

\[
\begin{aligned}
\Delta_h F_{I,\ell}(m)
&=
\chi_I(\ell)\chi_I(m+h)
\overline{\chi_I(\ell)\chi_I(m)}\\
&=
\chi_I(m+h)\overline{\chi_I(m)},
\end{aligned}
\]

which is `(6)`. No approximation, averaging, or conductor estimate is involved.

Further additive differencing acts on the right-hand side and therefore cannot recover an `\ell`-dependent source phase that has already disappeared. Thus any q-vdC analysis that treats `\ell` as an additional sample **only because the kernel was written as `\chi_I(\ell m)` rather than `\chi_I(\ell)\chi_I(m)` is representation-dependent**.

This statement is deliberately narrower than saying that `\ell` is analytically useless. The moving endpoint `N/\ell`, the signed Selberg coefficient, and correlations between different lcm coefficients remain outside `(6)`. They can support hyperbola, bilinear, large-sieve, or incidence arguments, but such a gain would be a theorem about the lcm-coefficient family rather than an automatic extra q-vdC dimension in the source phase.

## 3. Rectangular signature incidence has an exact finite-rank factorization

The same separation can be seen without selecting one source mode. Let `E` and `J` be finite sets of positive integers, and let `c_\ell`, `d_m` be arbitrary complex weights. Define

\[
\mathcal B(E,J)
:=
H\sum_{\ell\in E}\sum_{m\in J}
 c_\ell d_m
\mathbf 1_{(\ell m,P)=1}
\mathbf 1_{\Phi(\ell m)=1}.
\tag{10}
\]

Using `(8)` and complete multiplicativity,

\[
\boxed{
\mathcal B(E,J)
=
\sum_{I\in W}
A_I(E)D_I(J),
}
\tag{11}
\]

with

\[
A_I(E)=\sum_{\ell\in E}c_\ell\chi_I(\ell),
\qquad
D_I(J)=\sum_{m\in J}d_m\chi_I(m).
\tag{12}
\]

Equivalently, aggregate the weights by source signature:

\[
C_\sigma
:=\sum_{\substack{\ell\in E\\(\ell,P)=1\\\Phi(\ell)=\sigma}}c_\ell,
\qquad
D_\tau
:=\sum_{\substack{m\in J\\(m,P)=1\\\Phi(m)=\tau}}d_m.
\]

Then

\[
\boxed{
\mathcal B(E,J)
=H\sum_{\sigma\in\widehat W}
C_\sigma D_{\sigma^{-1}}.
}
\tag{13}
\]

This is the exact finite-group content of the source incidence relation. In a rectangular region there is no hidden joint source phase: the coupling factors either through the `H` character modes in `(11)` or through the `H` signature classes in `(13)`.

For example, finite Fourier orthogonality gives

\[
\sum_{I\in W}|A_I(E)|^2
=
H\sum_{\sigma\in\widehat W}|C_\sigma|^2.
\tag{14}
\]

Thus a useful lcm-side family gain would have to come from genuine cancellation or concentration of the lcm coefficients inside source-signature classes. Merely counting every lcm as a new oscillatory dimension does not supply such a gain.

The actual region in `(2)` is hyperbolic rather than rectangular because `m\le N/\ell`. That moving boundary is exactly one of the pieces **not** removed by the factorization and is why this finding does not close all collective lcm estimates.

## 4. Why this does not reproduce Stadlmann's retained-variable gain

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (arXiv:2309.00425; Adv. Math. 474 (2025), 110190) explicitly identifies her main new ingredient as a modified q-van-der-Corput process that exploits additional averaging in the Type I exponential sums.

In the proof sketch, the earlier treatment contains an arithmetic `y`-sum that is not used inside q-vdC; its diagonal forces the range `\Delta<N/Y^2`. After reorganizing the congruence so that both `n` and `y` survive inside the differencing/Cauchy geometry, the diagonal has only `O(N/Y)` admissible `n` for fixed outer data, giving a diagonal contribution `O(\Delta N/Y)` and allowing `\Delta<N/Y`.

The load-bearing feature is therefore not the existence of two written summation symbols. The retained arithmetic variable remains coupled to the post-Cauchy congruence and changes the number of diagonal configurations.

The standard lcm/source-character kernel here behaves differently. Equation `(5)` separates the lcm coordinate before q-vdC, and `(6)` removes its source-character scalar at the first additive correlation. The lcm may still affect the endpoint geometry or its own coefficient sum, but it does not remain in the source phase in the manner required for the Stadlmann diagonal mechanism.

This is the decisive comparison for the accepted retained-variable clue: the analogy survives only if a new representation exhibits a variable whose arithmetic dependence **does not separate before the relevant correlation**.

## Prior art and novelty boundary

Every algebraic ingredient used above is classical.

- Dirichlet characters are completely multiplicative; see NIST DLMF §27.3, especially equation 27.3.9 and the accompanying statement that Dirichlet characters are examples: https://dlmf.nist.gov/27.3.
- The finite character orthogonality/projector identity is classical and was already specialized to the endpoint source family in `MC-397`.
- The Selberg lcm expansion and lcm-fiber coefficients are classical and were isolated for the present frame in `MC-398`.
- Stadlmann's retained-variable q-vdC mechanism is prior art from arXiv:2309.00425: https://arxiv.org/abs/2309.00425.

No novelty is claimed for complete multiplicativity, finite Fourier factorization, the divisor-hyperbola identity, or van-der-Corput scalar cancellation. The Mathia-specific contribution is a **frontier classification**: when those standard facts are applied to the exact post-`MC-398` source/Selberg object, the remaining standard lcm coordinate fails the specific nonseparable-phase test required by the proposed Stadlmann transfer.

## Boundaries and falsification tests

- **The lcm variable is not proved useless.** Equation `(2)` leaves a nontrivial twisted lcm/end-point transform `\sum_\ell C_g(\ell)\chi_I(\ell)M_I(N/\ell)`.
- **The hyperbola boundary remains live.** The dependence of `N/\ell` on `\ell` is genuine coupling and may support a method that is not the mixed-phase q-vdC mechanism ruled out here.
- **Differencing or averaging in the lcm variable itself is not ruled out.** Such a method must obtain its gain from the arithmetic sequence `C_g(\ell)\chi_I(\ell)` or from signature incidence, not from pretending `\chi_I(\ell m)` is nonseparable.
- **A pre-quadratic representation remains open.** If divisor/source variables enter an arithmetic phase or congruence separately before the lcm collapse and remain nonseparable after the relevant Cauchy step, `(5)`--`(6)` do not apply to that new kernel.
- **Direct signature-incidence estimates remain open.** Equation `(13)` is an exact normal form, not an estimate of the signature-class sums.
- **No independent-character estimate is improved here.** The `2^{O(A)}` conductor-depth tariff from the current modewise recursion remains the analytic barrier unless another estimate avoids it.
- **No global-radical power loss is introduced or removed.** The fixed-`P^\theta` family barrier remains a separate constraint.
- **No analytic continuation or zero-free region is used.** The argument is finite character algebra, divisor rearrangement, and the first correlation identity.
- **No Möbius or RH conclusion follows.** This finding only removes one surviving interpretation of the retained-variable route.

A proposed counterexample to this finding must exhibit, within the exact standard lcm representation `(2)`, an `\ell`-dependent source phase that survives the factorization `(5)` and correlation `(6)`. A method that instead exploits the moving endpoint, twisted lcm coefficient, direct signature incidence, or a different pre-quadratic kernel is not a counterexample; it is precisely outside the obstruction's scope.

## Consequence for the research line

`MC-397` removed the source-mode index as a free averaging variable by exact Fourier projection. `MC-398` removed the two Selberg divisor labels as independent variables after the quadratic majorant by exact lcm compression. The present result performs the next representation test: **the surviving standard lcm coordinate also separates from the source-character phase and disappears from the first additive correlation.**

The accepted retained-variable clue should therefore stop treating the standard lcm variable as a candidate for a Stadlmann-style mixed q-vdC diagonal gain. The live frontier is narrower:

1. prove a genuinely collective estimate for the twisted lcm/end-point transform or the equivalent signature-incidence problem that beats the existing source-depth/global-modulus costs; or
2. expose a pre-quadratic arithmetic variable whose phase/congruence is demonstrably non-lcm-factorable and remains nonseparable through the relevant Cauchy/differencing step.

Either route requires new arithmetic input. Keeping another already-separable index visible is not enough.
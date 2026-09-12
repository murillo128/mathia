# MC-237 — Smooth-CRT Möbius variance closes only the support boundary

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the hard ordinary-progression surface exposed by `MC-233`. For a fixed interior scaling pair

\[
0<\alpha<\frac14,
\qquad
\beta\ge0,
\qquad
2\alpha+\beta<\frac12,
\]

the source-selected component has

\[
q=Q_S=X^{2\alpha+o(1)},
\qquad
Z=X^{1-\beta+o(1)},
\qquad
(a,q)=1,
\]

and the sufficient componentwise target is

\[
|M_\mu(Z;q,a)|\le X^{1/2+o(1)}.
\tag{1}
\]

The modulus `q` is an exceptionally smooth square-supported modulus: every prime divisor lies in the logarithmic shell `(c log X,2c log X]`. This makes the individual-smooth-modulus variance theorem of Klurman--Mangerel--Teräväinen (`MC-S45`, Theorem 1.3) applicable directly to the exact deep CRT modulus `Q_S`, not merely to the logarithmic primorial studied in `MC-188`.

However, after specialization to Möbius, the theorem controls only the residual around one best-pretending character at relative scale `X^{-o(1)}`. Its residue-class RMS is

\[
\boxed{
\left(
\frac1{\varphi(q)}
\sum_{b\,({\rm mod}\ q)}^{*}
|E_b|^2
\right)^{1/2}
\ll
\sqrt\varepsilon\,\frac Zq
=
X^{1-\beta-2\alpha+o(1)},
}
\tag{2}
\]

where

\[
E_b
:=
M_\mu(Z;q,b)
-
\frac{\chi_1(b)}{\varphi(q)}
\sum_{n\le Z}\mu(n)\overline{\chi_1(n)}.
\tag{3}
\]

The target `(1)` is smaller than the natural progression occupancy `Z/q` by the fixed factor

\[
X^{-\delta+o(1)},
\qquad
\delta:=\frac12-2\alpha-\beta>0.
\tag{4}
\]

By contrast, the smallest theorem parameter allowed while retaining the required smoothness is only logarithmically/subpower small. Thus `(2)` cannot supply the fixed factor `X^{-\delta}`. At exponent resolution the variance theorem reaches the `X^{1/2}` scale only when

\[
2\alpha+\beta\ge\frac12,
\tag{5}
\]

which is exactly the region `MC-233` already closes by support alone.

This remains true even in the deliberately favorable hypothetical case that the distinguished-character main term in `(3)` is already negligible. Therefore the obstruction is prior to the principal-character issue of `MC-188`: **smooth-modulus transverse dispersion itself is power-insufficient on the strict hard CRT region.**

No estimate `(1)`, no bound for `B_S`, no improvement of the first-shell energy, and no consequence for `M(X)` or the zeta zero set is proved here.

## 1. The exact deep CRT modulus satisfies the smooth-modulus hypotheses

`MC-233` has

\[
q=Q_S=\prod_{r\in S}r^2,
\qquad
r\in(c\log X,2c\log X],
\]

with

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X}.
\]

Hence

\[
\log q
=2\sum_{r\in S}\log r
=(2\alpha+o(1))\log X,
\]

which gives `q=X^{2 alpha+o(1)}` as above. Also

\[
P^+(q)\ll\log X.
\tag{6}
\]

Apply `MC-S45`, Theorem 1.3 with its variables `x=Z` and `Q=q`. The theorem requires `q<=Q<=x/10`, a small parameter `epsilon`, `q^(epsilon')`-smoothness with

\[
\varepsilon'=e^{-\varepsilon^{-3}},
\]

and a typicality condition beginning at `(x/Q)^(epsilon^2)`.

The range condition is automatic in the strict hard region because

\[
\frac qZ
=X^{2\alpha+\beta-1+o(1)}
\le X^{-1/2-\delta+o(1)}.
\tag{7}
\]

Choose, for concreteness,

\[
\varepsilon_X
=\left(\frac2{\log\log X}\right)^{1/3}.
\tag{8}
\]

Then

\[
\varepsilon'_X
=(\log X)^{-1/2},
\]

and therefore

\[
q^{\varepsilon'_X}
=
\exp\!\left((2\alpha+o(1))\sqrt{\log X}\right)
\gg\log X
\gg P^+(q).
\tag{9}
\]

So the exact source modulus is `q^(epsilon'_X)`-smooth.

For typicality, since

\[
\frac Zq
=X^{1-\beta-2\alpha+o(1)},
\]

the theorem's lower prime scale is

\[
Y_X
:=
(Z/q)^{\varepsilon_X^2}
=
\exp\!\left(
\frac{(1-\beta-2\alpha+o(1))2^{2/3}\log X}
     {(\log\log X)^{2/3}}
\right).
\tag{10}
\]

Thus `Y_X >> log X`. Every prime divisor of `q` already lies below `Y_X`, so the required large-scale typicality inequality is eventually automatic. Finally, `(8)` decreases much more slowly than the theorem's lower bound `(log(Z/q))^(-1/200)`. Hence all hypotheses hold for sufficiently large `X` at each fixed interior pair `(alpha,beta)`.

This direct applicability matters: there is no exceptional-modulus escape here. The selected modulus is not being discarded as an atypical arithmetic object.

## 2. The theorem gives subpower relative RMS, not fixed-power bias control

With `f=mu`, Theorem 1.3 of `MC-S45` yields a character `chi_1 mod q` for which

\[
\sum_{b\,({\rm mod}\ q)}^{*}|E_b|^2
\ll
\varepsilon_X\,\varphi(q)\left(\frac Zq\right)^2.
\tag{11}
\]

Dividing by `phi(q)` and taking square roots gives `(2)`.

Because every prime divisor of `q` is `asymp log X`,

\[
\frac{\varphi(q)}q
=
\prod_{r\mid q}\left(1-\frac1r\right)
=
1+o(1),
\tag{12}
\]

since

\[
\sum_{r\mid q}\frac1r
\ll
\frac{|S|}{\log X}
\ll
\frac1{\log\log X}.
\]

Thus the natural unsigned occupancy of a reduced class is indeed `Z/q=X^(1-beta-2alpha+o(1))`, and the theorem improves it only by

\[
\sqrt{\varepsilon_X}
=(\log\log X)^{-1/6+o(1)}
=X^{-o(1)}.
\tag{13}
\]

The required relative gain is instead `(4)`. For every fixed strict hard pair, `delta>0`, so

\[
X^{-o(1)}\gg X^{-\delta}.
\]

Consequently the smooth-modulus variance estimate does not change the power exponent of the progression amplitude.

The same calculation explains why the theorem appears to become adequate exactly at `(5)`: once `2alpha+beta>=1/2`, the trivial occupancy `Z/q` itself is already at most `X^(1/2+o(1))`. The variance theorem has not crossed the cancellation barrier there; the support count already has.

## 3. Averaging over residue classes cannot certify the source-selected residue at the target scale

One might hope that `(11)` is nevertheless useful because the source selects only one residue

\[
a=-P u^{-1}\pmod q
\]

for each smooth dilation `u`. But at the target threshold `X^(1/2+o(1))`, Chebyshev/Markov applied to `(11)` is already vacuous at exponent scale in the strict hard region.

Indeed, suppressing subpower factors, the fraction of reduced residues whose residual exceeds `X^(1/2)` is bounded by

\[
\frac{(Z/q)^2}{X}
=
X^{2\delta+o(1)},
\tag{14}
\]

which is larger than `1` when `delta>0`. Thus `(11)` cannot even show that a positive proportion of residue classes meet the `MC-233` target, let alone that the specific source-coupled residues do.

The direct single-residue consequence obtained by discarding all other nonnegative terms in `(11)` is weaker still:

\[
|E_a|
\ll
\sqrt{\varepsilon_X\varphi(q)}\,\frac Zq
=
X^{1-\beta-\alpha+o(1)},
\tag{15}
\]

which remains above `X^(1/2+o(1))` throughout the strict hard region.

Therefore the obstacle is not merely the usual `average versus selected residue` quantifier mismatch. The average theorem's own RMS scale is already too large before that mismatch is considered.

## 4. Relation to the existing progression and transference barriers

This result is distinct from `MC-188`. There the modulus was the full logarithmic primorial, and the key failure was that smooth-modulus dispersion is transverse to the rough Möbius principal mode. Here the modulus is the current deep CRT object `Q_S`, and the failure occurs even after granting favorable control of the distinguished-character main term: the residual variance has the wrong fixed-power scale.

It also sharpens the role of `MC-227`. Classical Möbius BDH gives arbitrarily strong logarithmic savings after summing over the shallow first-shell square moduli, but no fixed-power gain. The present calculation shows that moving to the much more specialized theorem for **individual smooth moduli** does not change that conclusion on the deep CRT components: smoothness removes an exceptional-modulus concern but does not buy the relative power `X^-delta`.

Finally, it is consistent with `MC-234`--`MC-236`. The 2026 Linnik dense-model machinery breaks the parity-existence barrier and even supplies both signs at full occupancy exponent, but its transference resolution remains subpower. The 2023 smooth-modulus variance theorem reaches the same information boundary from a different direction: it supplies genuine signed second-moment information at every exact smooth source modulus, yet only at subpower relative resolution.

These are independent warnings against interpreting `very smooth modulus` as the missing mechanism. The active target needs a theorem whose **relative signed accuracy tracks the fixed deficit**

\[
\delta=\frac12-2\alpha-\beta,
\]

or an aggregate identity that cancels the `X^{o(1)}` smooth-dilation components before they are estimated separately.

## 5. Prior-art and novelty boundary

The variance theorem is prior art: Oleksiy Klurman, Alexander P. Mangerel and Joni Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proceedings of the London Mathematical Society 127 (2023), 366--446, DOI `10.1112/plms.12546`, arXiv `1909.12280`; it is already recorded as `MC-S45` in `SOURCES.md`.

No novelty is claimed for Theorem 1.3, smoothness/typicality, character orthogonality, or the elementary exponent computations. The durable line-specific result is the specialization and rate audit on the exact `MC-233` modulus/length phase plane.

A targeted literature check also found work on smooth-supported multiplicative functions and on primes/smooth numbers in progressions to smooth moduli, but those results concern different coefficient families or average-modulus distribution. Nothing located in that bounded check supplies a fixed-power individual-residue Möbius discrepancy estimate on the source-selected `Q_S` family. This is not a global literature-absence claim.

## 6. Boundaries and falsification tests

- The derivation is stated for fixed `alpha>0` and fixed strict interior deficit `delta>0`. Regimes with `alpha->0` or `delta->0` require a separate uniformity audit and are not covered by the fixed-parameter statement.
- Equation `(11)` controls the residual after subtraction of one distinguished character. It does not bound the character main term. The obstruction is deliberately stronger: even pretending that main term is harmless, the residual theorem remains power-insufficient.
- The theorem may contain useful structure beyond the scalar variance `(11)`. A source-coupled bilinear identity, correlations between residues/moduli, or a refinement with fixed-power dependence on the smoothness parameter would contain information absent here and is not ruled out.
- The Markov calculation `(14)` is only a no-go for extracting the target from this second moment alone. It does not say the selected residue is actually large.
- Smoothness of `Q_S` is a proved applicability advantage, not evidence of cancellation. Any future claim using smoothness must exhibit a fixed-power improvement after all theorem parameters are substituted.

## Consequence for the live frontier

The exact deep CRT family is already inside a strong unconditional smooth-modulus dispersion theorem, so `find a variance theorem that applies to Q_S` is no longer an open escape route. After the theorem parameters are priced, its RMS residual has the same leading power as trivial progression occupancy and reaches the `X^(1/2)` target only where support alone already reaches it.

The unresolved frontier therefore remains genuinely **source-coupled signed amplitude**: either obtain fixed-power relative bias control in the strict hard region, or exploit cancellation across the smooth-dilation family before triangle inequality. Smooth-modulus variance by itself cannot cross the `2alpha+beta=1/2` boundary.
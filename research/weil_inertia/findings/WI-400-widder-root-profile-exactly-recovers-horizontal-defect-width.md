# WI-400 — the Widder prime-root profile exactly recovers horizontal defect width

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent finding:** WI-399.

## Claim

The fixed-height Widder hierarchy isolated in WI-399 does more than give a one-way effective-shift implication. After clipping exponential root rates at the neutral threshold `1`, its prime-side root profile and its zero-side spectral-radius profile are **exactly identical**. Consequently the full family of prime root rates recovers the maximal horizontal displacement of a nontrivial zeta zero by an explicit formula.

For fixed `T>=2`, write

\[
L_{\mathcal P}(T)
:=
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m},
\]

and retain Rafik's zero-side spectral radius

\[
\mathcal R(T)
:=
4T^2\max_{\rho}
\left|
\frac{w_\rho}{(T^2+w_\rho)^2}
\right|,
\qquad
w_\rho=(\gamma-i\delta)^2,
\]

for

\[
\rho=\frac12+\delta+i\gamma.
\]

Then

\[
\boxed{
\max\{1,L_{\mathcal P}(T)\}
=
\max\{1,\mathcal R(T)\}
}
\qquad(T\ge2).
\tag{1}
\]

Let

\[
M(\sigma)
:=
\frac{2}{1+\sqrt{1-4\sigma^2}},
\qquad 0\le \sigma<\frac12.
\tag{2}
\]

For every `0<=a<=1/2`, the following are equivalent:

\[
\boxed{
|\Re\rho-1/2|\le a
\quad\text{for every nontrivial zero }\rho
}
\tag{3}
\]

and

\[
\boxed{
L_{\mathcal P}(T)
\le M(a/T)
\quad\text{for every fixed }T\ge2.
}
\tag{4}
\]

Thus WI-399's effective-width implication has an exact converse.

More strongly, put

\[
\Delta
:=
\sup_{\rho}
|\Re\rho-1/2|
\in[0,1/2]
\tag{5}
\]

and

\[
C(T):=\max\{1,L_{\mathcal P}(T)\}.
\tag{6}
\]

Since

\[
M^{-1}(c)=\frac{\sqrt{c-1}}{c}
\qquad(1\le c<2),
\tag{7}
\]

the maximal horizontal defect is recovered exactly by

\[
\boxed{
\Delta
=
\sup_{T\ge2}
T\frac{\sqrt{C(T)-1}}{C(T)}.
}
\tag{8}
\]

The immediate research consequence is a no-go theorem for the most tempting bootstrap suggested by WI-399. If the only zero-side information retained is a strip width `Delta<=a`, the sharp universal Widder envelope is `M(a/T)`. Feeding that envelope back through the exact inverse gives

\[
T M^{-1}(M(a/T))=a
\tag{9}
\]

for every `T`: the width update is the identity, not a contraction. A strict defect-to-zero bootstrap therefore cannot arise by repeatedly converting a scalar strip width into this same scalar Widder root envelope and back. Any contraction must add information not contained in the width alone — for example signed prime cancellation beyond the strip-implied envelope, height/depth coupling, phase information, zero-density/correlation structure, or another independent invariant.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Primary-source identities

The primary source is Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026. It is a recent non-peer-reviewed preprint and is not treated as established peer-reviewed evidence.

The source proves in Proposition A1 that

\[
\limsup_{m\to\infty}
|T^2A'_m(T^2)|^{1/m}
=
\mathcal R(T).
\tag{10}
\]

Lemma A1 gives the exact fixed-height explicit-formula relation

\[
2T^2A'_m(T^2)
=
\mathcal H_m(T)-\mathcal P_m(T),
\qquad
\mathcal H_m(T)=O_T(1).
\tag{11}
\]

Theorem A2 uses these identities to obtain the endpoint criterion

\[
\mathrm{RH}
\iff
L_{\mathcal P}(T)\le1
\quad\text{for every fixed }T\ge2.
\tag{12}
\]

Proposition A2 independently proves the absolute-convergence estimate

\[
L_{\mathcal P}(T)
\le
M(1/(2T)).
\tag{13}
\]

WI-399 then identifies the exact one-zero factor

\[
R_{\delta,\gamma}(T)
=
4T^2
\frac{|w_\rho|}{|T^2+w_\rho|^2}
\tag{14}
\]

with the same shifted beta-kernel rational function used in Proposition A2 and derives

\[
R_{\delta,\gamma}(T)
\le M(|\delta|/T).
\tag{15}
\]

For every fixed depth `d=|delta|`, equality in (15) is attained by choosing `T` at the exact saddle

\[
\boxed{
T^2
=
2d^2+
\sqrt{(\gamma^2+d^2)^2+4d^4}.
}
\tag{16}
\]

The source and WI-399 supply all ingredients used below. Equations (1), (3)--(9) are the new exact synthesis.

## 2. Bounded explicit-formula terms preserve every root threshold above one

The key observation is a general elementary lemma. If two complex sequences `x_m,y_m` satisfy

\[
x_m-y_m=O(1),
\]

and

\[
L_x:=\limsup|x_m|^{1/m},
\qquad
L_y:=\limsup|y_m|^{1/m},
\]

then

\[
\boxed{
\max\{1,L_x\}
=
\max\{1,L_y\}.
}
\tag{17}
\]

Indeed the triangle inequality gives

\[
L_x\le\max\{L_y,1\},
\]

and the reverse inequality follows by interchanging `x` and `y`.

Apply this to

\[
x_m=\mathcal P_m(T),
\qquad
y_m=-2T^2A'_m(T^2),
\]

using (11). Multiplication by the fixed scalar `2` does not change an `m`th-root limsup, so (10) and (17) give exactly (1).

An equivalent threshold formulation will be useful: for every `K>=1`,

\[
\boxed{
L_{\mathcal P}(T)\le K
\iff
\mathcal R(T)\le K.
}
\tag{18}
\]

This is stronger than merely saying that both sides detect RH at the special threshold `K=1`. Every exponential root threshold at or above one transfers exactly between the prime and zero sides.

## 3. Exact strip-width equivalence

Assume first that every zero satisfies

\[
|\delta|\le a.
\]

Equation (15), monotonicity of `M`, and the definition of `mathcal R(T)` give, for every `T>=2`,

\[
\mathcal R(T)
\le
M(a/T).
\tag{19}
\]

Because `M(a/T)>=1`, (18) gives (4).

Conversely suppose (4) holds but some zero has depth

\[
d:=|\delta|>a.
\]

Choose `T` by (16). Every nontrivial zeta zero has ordinate exceeding `14`, so this saddle has `T>\gamma>14>2` and lies in the allowed fixed-height family. WI-399's exact saddle calculation gives

\[
R_{\delta,\gamma}(T)
=
M(d/T).
\tag{20}
\]

Since `M` is strictly increasing on positive arguments,

\[
M(d/T)>M(a/T)>1.
\tag{21}
\]

Therefore

\[
\mathcal R(T)
\ge
R_{\delta,\gamma}(T)
>
M(a/T).
\tag{22}
\]

Equation (18) now forces

\[
L_{\mathcal P}(T)>M(a/T),
\]

contradicting (4). This proves the equivalence (3)--(4), including the endpoint `a=1/2` corresponding to the ordinary critical strip.

The point is logical rather than computational: a prime-side root estimate with effective width `a` is neither weaker nor stronger than the global horizontal zero-strip assertion with the same width. Across the whole fixed-`T` family they contain exactly the same scalar-width information.

## 4. Exact recovery formula for the maximal defect

Solving `c=M(sigma)` gives

\[
\sqrt{1-4\sigma^2}
=
\frac{2-c}{c},
\]

hence (7).

Let `Delta` be (5). Since every zero has depth at most `Delta`, (19) with `a=Delta` and (1) imply

\[
C(T)
\le
M(\Delta/T).
\]

Applying the increasing inverse (7),

\[
T\frac{\sqrt{C(T)-1}}{C(T)}
\le
\Delta.
\tag{23}
\]

Taking the supremum in `T` proves the `<=Delta` half of (8).

For the reverse inequality, fix any zero of depth `d`. At its saddle (16), (20) gives

\[
\mathcal R(T)
\ge M(d/T).
\]

Using (1) and then the monotonicity of `M^{-1}`,

\[
T\frac{\sqrt{C(T)-1}}{C(T)}
\ge d.
\tag{24}
\]

This holds for every zero after choosing its own saddle. Taking the supremum over all zero depths proves

\[
\sup_{T\ge2}
T\frac{\sqrt{C(T)-1}}{C(T)}
\ge
\sup_\rho|\delta_\rho|
=
\Delta,
\]

completing (8).

Thus the scalar prime-root profile is an exact norm for the worst horizontal defect. A finite or zero-density off-line population cannot hide from it; conversely the profile contains no automatic scalar-width reserve beyond that worst defect.

## 5. The width bootstrap is idempotent

Suppose a stage of an argument knows only

\[
\Delta\le a.
\tag{25}
\]

The sharp geometric one-zero envelope compatible with (25) is precisely

\[
C(T)\le M(a/T).
\tag{26}
\]

Sharpness here is a statement about the geometric class constrained only by the width: for fixed `T` and depth `a`, the rational factor (14) reaches `M(a/T)` at its explicit saddle ordinate. It is **not** a claim that the actual zeta zero set attains that envelope.

Now infer a new width using the exact recovery map (8). The envelope (26) yields at best

\[
\Delta_{\mathrm{new}}
\le
\sup_{T\ge2}T M^{-1}(M(a/T))
=a.
\tag{27}
\]

There is no strict gain. Repeating the same passage leaves `a` fixed at every iteration.

This closes the naive defect-to-zero loop

\[
\text{strip width}
\longrightarrow
\text{Widder root envelope}
\longrightarrow
\text{strip width}
\]

as an exact identity map. A genuine bootstrap must insert a theorem that makes the prime root profile **strictly smaller** than the width-only envelope, or retain more structure than the single scalar `a`.

This also sharpens the interpretation of WI-399. Its conditional estimate

\[
L_{\mathcal P}(T)\le M(a/T)
\]

is not merely sufficient to prove the width `a`; over all fixed heights it is quantitatively equivalent to that width. Therefore deriving the same estimate only from a previously known width `a` is circular in the strongest possible sense.

## 6. Prior art and novelty boundary

Rafik's preprint already contains the decisive literature ingredients: Proposition A1 gives the exact zero-side root radius, Lemma A1 transports it to the prime functional up to bounded terms, Theorem A2 records the `K=1` RH criterion, Proposition A2 identifies the absolute-convergence endpoint, Corollary A2 makes individual off-line zeros into real generating-function poles, and Remark A4 states that reaching the terminal semicircle requires genuinely new information about `-zeta'/zeta` in the critical strip. The source explicitly warns that its pole reformulation is not an independent proof of RH.

WI-399 adds the exact equality between the shifted beta-kernel saddle and the one-zero horizontal-amplification saddle, and formulates the one-way effective-width theorem. The present finding adds the converse threshold transfer, the exact global width-recovery formula (8), and the idempotence obstruction (27).

A targeted prior-art search around Widder root growth, horizontal zero-free strips, and the specific `M(a/T)` envelope located the Rafik preprint itself and classical neighboring Stieltjes/Widder material, but no separate source stating (8) or the identity-map bootstrap obstruction. This is recorded only as a novelty audit; no priority claim is made.

## 7. Boundaries and failure modes

This result does **not** show that estimating `mathcal P_m(T)` is useless. On the contrary, any arithmetic estimate that beats `M(a/T)` at some scale contains information stronger than the width assumption `Delta<=a` and, through (8), can exclude deeper zeros. The barrier says only that the same scalar width cannot manufacture such an improvement by being fed back through the same hierarchy.

The equivalence uses the full family of fixed heights `T>=2`. A bound at one isolated `T` constrains only the corresponding spectral radius and does not determine the global strip width. Likewise (8) measures the worst horizontal displacement; it does not encode the density, multiplicity, or ordinate distribution of the exceptional zeros.

The saddle choice (16) lies above `2` for every nontrivial zeta zero because their ordinates exceed `14`. For a different entire function with low-lying zeros, the permitted `T` range would have to be checked separately.

Finally, the primary Widder source is a fresh unrefereed preprint. The algebra from its stated Proposition A1 and Lemma A1 to (1), and from WI-399's rational saddle to (3)--(9), is exact and elementary; nevertheless any future correction to those load-bearing source identities would require this finding to be revisited.

## 8. Consequences for the research line

The Widder hierarchy remains important because it detects even a single off-line zero, unlike density-normalized moving-carrier observables. But its scalar effective-width variable is now fully classified: it is an exact coordinate for the worst horizontal defect, not an autonomous contraction mechanism.

The next useful arithmetic target is therefore not to rederive `M(a/T)` from a known strip of width `a`. It is to prove a strict prime-side improvement below that envelope using information unavailable to the width-only model. Alternatively one must enrich the state beyond `a`, for example with height-dependent depth bounds, phase-sensitive constraints, or population information that survives the passage to the prime side.

In particular, the naive iterative route suggested after WI-399 is decisively closed: without genuinely new arithmetic or extra zero-side structure, the effective-width bootstrap has contraction factor exactly one.

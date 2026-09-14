# WI-288 — two-island complete screening is exactly a nearest-prime-power gap condition

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened, symmetric two-island** branch of `WI-284`--`WI-287`. This finding asks whether the next step can gain anything, on this fixed support topology, merely by retaining the entire aperture-growing family of prime-power screening equalities instead of the one-prime width consequence used in `WI-286`--`WI-287`.
- **Result:** at the support-geometric level, it cannot. For two symmetric open intervals narrow enough to avoid same-island prime-power overlaps, complete screening by **all** active prime powers is equivalent to a single scalar condition: the half-width must not exceed one half of the logarithmic distance from the island separation to the nearest prime power. Combining this exact equivalence with the zero-bottom condition of `WI-284` and the gamma/pole bounds of `WI-287` yields a new necessary arithmetic condition: any large two-island completely screened zero-critical support must sit inside a two-sided prime-power gap of Lambert-`W` scale,

  \[
  \sqrt{x}\,\delta_{\rm pp}(x)
  \ge W(c_0\sqrt{x})
  =\frac12\log x-\log\log x+O(1)
  \]

  for some absolute `c_0>0`. Equivalently, both neighboring prime powers must be at additive distance at least

  \[
  \sqrt{x}\left(\frac12\log x-\log\log x+O(1)\right)
  \]

  from the center `x`.
- **What it does not claim:** this does not prove such large prime-power gaps exist or do not exist, does not construct a Suzuki first null mode, does not control many-component or fractal supports, does not treat sign-changing or incompletely screened modes, and does not say that the theorem-derived width cap in `WI-287` was equivalent to full screening. The distinction is important: the **actual** nearest-prime-power gap is equivalent to full support screening on two islands; a coarse uniform theorem bounding that gap is only a relaxation.
- **Novelty boundary:** Suzuki supplies the exact localized Weil form; Baker--Harman--Pintz and, at a lower evidence tier, Runbo Li supply current uniform prime-in-short-interval inputs. Forbidden-distance support geometry is classical. The new line-local deductions are the exact collapse of all prime-power zero-overlap constraints to the nearest prime-power logarithmic gap on this topology, and the resulting Lambert-`W` lower bound on an actual prime-power gap forced by the `WI-284` zero-bottom requirement. Targeted searches found the standard prime-gap inputs and numerical literature on gaps between prime powers, but no statement of this Suzuki-support implication. Search absence is audit context only, not a priority claim.

## Claim

Let

\[
E_{R,b}
:=(-R-b,-R+b)\cup(R-b,R+b),
\qquad
R>b>0,
\tag{1}
\]

and put

\[
\Delta:=2R,
\qquad
x:=e^\Delta,
\qquad
a:=R+b.
\tag{2}
\]

Retain the narrow-island regime used in `WI-286`,

\[
0<b<\frac{\log2}{4}.
\tag{3}
\]

Let

\[
\mathcal Q:=\{q\ge2:\Lambda(q)>0\}
=\{p^k:p\text{ prime},\ k\ge1\}
\tag{4}
\]

and define the nearest-prime-power logarithmic distance

\[
\boxed{
\delta_{\rm pp}(x)
:=\min_{q\in\mathcal Q}|\log q-\log x|.
}
\tag{5}
\]

Then the following are equivalent:

\[
|E_{R,b}\cap(E_{R,b}-\log q)|=0
\quad
\text{for every active }q\in\mathcal Q,
\ \log q<2a,
\tag{6}
\]

and

\[
\boxed{2b\le\delta_{\rm pp}(x).}
\tag{7}
\]

Thus, for this support topology, the complete aperture-growing prime-power family carries **no additional zero-overlap geometry beyond the actual nearest prime-power gap**.

Now assume in addition that `E_{R,b}` is the positivity support of a hypothetical completely screened one-signed Suzuki first-crossing null mode. By `WI-284`, the exact prime-deleted form then has restricted bottom zero:

\[
\boxed{
\inf_{0\ne u\in\mathfrak D(q_{\rm arch}^a)\cap L^2(E_{R,b})}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}=0.
}
\tag{8}
\]

There is an absolute constant `c_0>0` such that every sufficiently large such support satisfies

\[
\boxed{
\sqrt{x}\,\delta_{\rm pp}(x)
\ge W(c_0\sqrt{x}).
}
\tag{9}
\]

Consequently

\[
\boxed{
\delta_{\rm pp}(x)
\ge
\frac{\frac12\log x-\log\log x+O(1)}{\sqrt{x}}.
}
\tag{10}
\]

If `q_-(x)<x<q_+(x)` are the consecutive prime powers bracketing `x`, then (9) gives

\[
\boxed{
 x-q_-(x),\ q_+(x)-x
\ge
\sqrt{x}\,W(c_0\sqrt{x})\,(1-o(1)).
}
\tag{11}
\]

In particular, the consecutive-prime-power gap containing `x` must have length at least

\[
\boxed{
q_+(x)-q_-(x)
\ge
2\sqrt{x}\,W(c_0\sqrt{x})\,(1-o(1))
=
\sqrt{x}\log x-2\sqrt{x}\log\log x+O(\sqrt{x}).
}
\tag{12}
\]

This is a **necessary condition on the hypothetical RH-failure branch**, not an unconditional assertion that prime-power gaps of this size occur.

## 1. Complete two-island screening is exactly one nearest-gap constraint

For a positive translation lag `d`, two points in the same component of `E_{R,b}` can overlap after translation only when

\[
0<d<2b.
\tag{13}
\]

Every prime-power lag satisfies

\[
d=\log q\ge\log2>2b
\tag{14}
\]

under (3), so same-island overlaps are impossible for all von-Mangoldt lags.

The only possible overlap is therefore between the left and right islands. Their positive difference set is exactly

\[
(\Delta-2b,\Delta+2b).
\tag{15}
\]

Hence, up to null endpoint contacts,

\[
|E_{R,b}\cap(E_{R,b}-d)|>0
\quad\Longleftrightarrow\quad
|d-\Delta|<2b.
\tag{16}
\]

If (16) holds for a prime-power lag, then automatically

\[
d<\Delta+2b=2a,
\tag{17}
\]

so that lag is active. Conversely, an active prime-power lag outside (15) produces no overlap. Therefore

\[
\begin{aligned}
&|E_{R,b}\cap(E_{R,b}-\log q)|=0
\quad\text{for every active prime power }q\\
&\qquad\Longleftrightarrow\qquad
(\Delta-2b,\Delta+2b)
\cap\{\log q:q\in\mathcal Q\}=\varnothing\\
&\qquad\Longleftrightarrow\qquad
2b\le\min_{q\in\mathcal Q}|\log q-\Delta|.
\end{aligned}
\tag{18}
\]

This proves (7). Equality is allowed because the islands are open and endpoint contact has measure zero.

Equivalently, in multiplicative coordinates complete screening is exactly the prime-power-free annulus condition

\[
\boxed{
\mathcal Q\cap(xe^{-2b},xe^{2b})=\varnothing.
}
\tag{19}
\]

If `q_-<x<q_+` are the adjacent prime powers, then

\[
\delta_{\rm pp}(x)
=\min\!\left\{
\log\frac{x}{q_-},
\log\frac{q_+}{x}
\right\}.
\tag{20}
\]

Thus the entire family of screening equalities has collapsed, **exactly and without an arithmetic estimate**, to the two nearest prime-power neighbors of `x`.

This sharpens the interpretation of `WI-286`--`WI-287`. Those findings replaced the unknown actual quantity `\delta_pp(x)` by an unconditional upper bound coming from one guaranteed nearby prime. That replacement loses arithmetic information. But, on the two-island topology itself, retaining all screening equalities does not create any further multi-prime geometric invariant beyond `\delta_pp(x)`.

## 2. Zero spectral bottom forces the island width onto the Lambert-W scale

`WI-287` proved two support-uniform estimates for Suzuki's prime-deleted form. For every nonzero supported form-domain vector,

\[
\frac{G(u)}{\|u\|_2^2}
\ge\log\frac1b-C_1
\tag{21}
\]

for an absolute constant `C_1`, while the exact negative spectral edge of the rank-two pole term gives

\[
\frac{P_a(u)}{\|u\|_2^2}
\ge
-4\bigl(\sinh(b)\cosh(R)-b\bigr).
\tag{22}
\]

Since `q_arch^a=G+P_a`, the zero-bottom requirement (8) implies that the common lower bound cannot be positive:

\[
\boxed{
\log\frac1b-C_1
\le
4\bigl(\sinh(b)\cosh(R)-b\bigr).
}
\tag{23}
\]

Complete screening includes screening by primes. Therefore the peer-reviewed Baker--Harman--Pintz theorem, exactly as used in `WI-286`, gives for all sufficiently large `x`

\[
2b\le\log(1+x^{-19/40}),
\tag{24}
\]

so in particular

\[
b=O(x^{-19/40})\to0.
\tag{25}
\]

Introduce the natural pole-scale variable

\[
y:=2b\sqrt{x}.
\tag{26}
\]

Because

\[
2\cosh R=\sqrt{x}+\frac1{\sqrt{x}}
\tag{27}
\]

and `\sinh b\le b e^b`,

\[
4\sinh(b)\cosh(R)
\le
y e^b(1+x^{-1}).
\tag{28}
\]

The width bound (24) gives `y=O(x^{1/40})`, hence

\[
y(e^b-1)=O(yb)=O(x^{-18/40})=o(1),
\tag{29}
\]

and therefore

\[
4\bigl(\sinh(b)\cosh(R)-b\bigr)
\le y+o(1).
\tag{30}
\]

On the other hand,

\[
\log\frac1b
=\frac12\log x-\log y+\log2.
\tag{31}
\]

Substituting (30)--(31) into the necessary inequality (23) gives

\[
y+\log y
\ge
\frac12\log x+\log2-C_1-o(1).
\tag{32}
\]

Choose once and for all, for example,

\[
c_0:=2e^{-C_1-1}>0.
\tag{33}
\]

For all sufficiently large `x`, (32) implies

\[
y+\log y\ge\log(c_0\sqrt{x}).
\tag{34}
\]

Since `t\mapsto t+\log t` is strictly increasing on `(0,\infty)`, and

\[
W(z)+\log W(z)=\log z,
\tag{35}
\]

we obtain

\[
\boxed{2b\sqrt{x}=y\ge W(c_0\sqrt{x}).}
\tag{36}
\]

This is the lower-width half that was implicit but not extracted in `WI-287`: a prime-deleted zero ground state cannot live on islands much thinner than the Lambert-`W` width.

## 3. Exact screening converts the spectral lower-width condition into a large prime-power gap

Equation (7) gives

\[
2b\le\delta_{\rm pp}(x).
\tag{37}
\]

Multiplying by `\sqrt{x}` and inserting (36) proves (9):

\[
\sqrt{x}\,\delta_{\rm pp}(x)
\ge2b\sqrt{x}
\ge W(c_0\sqrt{x}).
\tag{38}
\]

The standard large-argument expansion of Lambert `W` gives

\[
W(c_0\sqrt{x})
=\frac12\log x-\log\log x+O(1),
\tag{39}
\]

which proves (10).

Because (24) also implies `\delta_pp(x)\to0` after replacing `b` by the exact nearest-gap quantity through (18) only when needed for the support under consideration, the additive and logarithmic scales agree to relative `1+o(1)` at the critical lower bound. More directly, (20) and (9) imply

\[
q_+\ge x\exp\!\left(\frac{W(c_0\sqrt{x})}{\sqrt{x}}\right),
\tag{40}
\]

and

\[
q_-\le x\exp\!\left(-\frac{W(c_0\sqrt{x})}{\sqrt{x}}\right).
\tag{41}
\]

Since `W(c_0\sqrt{x})/\sqrt{x}\to0`, expanding the exponentials yields (11), and adding the two one-sided distances gives (12).

The important logical direction is worth keeping explicit:

\[
\boxed{
\text{two-island complete screening}
+\text{first-crossing zero bottom}
\Longrightarrow
\text{a prime-power gap of size }\asymp\sqrt{x}\log x.
}
\tag{42}
\]

No converse is asserted.

## 4. Why the current prime-gap theorems still do not close the branch

Primes are themselves prime powers, so

\[
\delta_{\rm pp}(x)\le\delta_{\rm prime}(x).
\tag{43}
\]

Thus every uniform short-interval theorem for primes is automatically an upper bound for the quantity in (9). Baker--Harman--Pintz gives, on the relevant forward scale,

\[
\delta_{\rm pp}(x)
\ll x^{-19/40},
\qquad
\sqrt{x}\,\delta_{\rm pp}(x)
\ll x^{1/40}.
\tag{44}
\]

The current Runbo Li preprint, kept at the explicitly lower evidence tier already recorded in `SOURCES.md`, improves this to

\[
\sqrt{x}\,\delta_{\rm pp}(x)
\ll x^{0.02}.
\tag{45}
\]

Both upper bounds are still asymptotically much larger than the necessary Lambert scale

\[
W(c_0\sqrt{x})\asymp\log x.
\tag{46}
\]

So there is no contradiction. This is the same arithmetic miss seen spectrally in `WI-286`--`WI-287`, but (9) identifies its exact support-geometric meaning: a hypothetical two-island zero-critical support would force `x` to lie in an exceptionally large gap between consecutive prime powers.

Conversely, any unconditional theorem implying

\[
\boxed{
\sqrt{x}\,\delta_{\rm pp}(x)
\le W(\sqrt{x})-\omega(x),
\qquad
\omega(x)\to\infty,
}
\tag{47}
\]

for all sufficiently large `x` would contradict (9), because `W(c_0\sqrt{x})=W(\sqrt{x})+O(1)`. A theorem about primes alone at that scale would suffice, but (47) also makes clear that a genuinely stronger theorem about the union of all prime powers would be enough.

The targeted prior-art search did not locate such a uniform prime-power-gap theorem. Numerical catalogues of gaps between prime powers exist, but they do not supply the asymptotic every-`x` upper bound required here. The established peer-reviewed baseline remains Baker--Harman--Pintz; Li's `0.52` statement remains a current preprint frontier.

## 5. Decisive barrier for the proposed “use all primes simultaneously” refinement

The frontier after `WI-287` listed several pieces of information discarded by the nearest-prime width relaxation, including “simultaneous screening by the entire aperture-growing prime family.” Equation (18) shows that this option must now be split into two very different meanings.

At the **support-zero-overlap level**, there is nothing further to recover on two symmetric intervals:

\[
\boxed{
\{C_v(\log q)=0\text{ for every prime power }q\}
\quad\Longleftrightarrow\quad
2b\le\delta_{\rm pp}(x)
}
\tag{48}
\]

for every nonnegative profile whose positivity set is `E_{R,b}`. Once `\delta_pp(x)` is known exactly, all other prime-power screening equalities are redundant for this topology. There is no hidden multi-prime packing gain waiting to be extracted from the same zero set.

What **does** remain outside this barrier is source-specific information that is not support geometry. In particular, the global weak null equation may be tested against functions not supported in `E`; those equations can couple translated amplitudes across the complement even though the prime operator vanishes on the supported subspace in `WI-284`. Likewise, with three or more support components there are several independent pairwise separations, and the prime-power family no longer reduces to one nearest-gap scalar.

Therefore the next two-island step must do at least one of the following:

1. prove a substantially stronger uniform upper bound for the actual nearest prime-power gap, at the Lambert scale (47);
2. use the **global** Suzuki null equation or another amplitude-sensitive constraint that survives outside `L^2(E)`; or
3. leave the two-island topology and exploit simultaneous arithmetic constraints on several independent component separations.

Merely replacing the one guaranteed prime in `WI-286` by a longer list of zero-overlap statements, while staying on the same two intervals and using only their support geometry, is now closed.

## 6. Prior-art and novelty audit

The operator input is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), which supplies the localized closed Weil form and the exact gamma/von-Mangoldt/pole decomposition used in `WI-240`, `WI-284`, and `WI-287`.

The peer-reviewed arithmetic baseline is R. C. Baker, G. Harman and J. Pintz, **The difference between consecutive primes, II**, *Proceedings of the London Mathematical Society* 83:3 (2001), 532--562, DOI `10.1112/plms/83.3.532`, proving primes in intervals of length `x^0.525` for all sufficiently large `x`. The current stronger but unrefereed input is Runbo Li, **The number of primes in short intervals and numerical calculations for Harman's sieve**, arXiv:2308.04458v8, whose abstract states the exponent `0.52`. Their evidence tiers and roles are already recorded in `research/weil_inertia/SOURCES.md`.

Measurable forbidden-distance support problems are classical and were already audited in `WI-282`, including de Oliveira Filho--Vallentin and DeCorte--de Oliveira Filho--Vallentin. The equivalence (18) is an elementary specialization of interval difference geometry, not a claim of a new general distance-avoiding theorem.

The novelty audit against the line-local chain gives the following boundary. `WI-286` observed the exact overlap condition `|d-Delta|<2b` and then inserted **one guaranteed nearby prime** to obtain a necessary width cap. `WI-287` deliberately defined a width relaxation from such a theorem-derived cap and correctly warned that its negative half did not satisfy full screening. Neither finding records that, for the symmetric two-interval support itself, the complete family of prime-power screening equalities is exactly equivalent to the **actual** nearest-prime-power distance, nor do they convert `WI-284`'s zero-bottom condition into the actual gap lower bound (9)--(12). Those are the durable additions here.

Targeted searches across consecutive prime powers, prime powers in short intervals, Suzuki/Weil support restrictions, and forbidden-distance formulations located the standard ingredients but no source stating this combined implication. No historical priority claim is made.

## 7. Stress tests and boundaries

- **Prime powers, not only primes.** The exact scalar in (5) ranges over every `p^k` with `Lambda(p^k)>0`. Using nearest primes alone would give a weaker condition and would not justify the exact equivalence (18).
- **Activity cutoff is automatic.** Any prime-power lag close enough to `Delta` to create cross-island overlap satisfies `d<Delta+2b=2a`, so no offending lag is accidentally discarded as inactive.
- **Endpoint equality is harmless.** At `|d-Delta|=2b` the open intervals only touch at an endpoint, giving zero-measure intersection; this is why (7) is non-strict.
- **The narrow-island hypothesis removes self-overlap.** Equation (3) is stronger than needed but matches the established `WI-286` branch. Without a condition ensuring `2b<log2`, small prime-power lags could overlap an island with itself and the one-scalar cross-gap equivalence would fail.
- **No misuse of the BHP bound.** Baker--Harman--Pintz is used only to guarantee `b->0` fast enough that the exact pole edge has asymptotic size `y+o(1)`. The load-bearing lower gap (9) comes from the Suzuki zero-bottom condition plus exact screening, not from assuming an unproved prime-gap law.
- **No converse from a large gap.** Even if an interval between prime powers is wide enough to admit `b` at the Lambert scale, this does not produce global firstness `q_a>=0`, an actual null vector, or the global weak null equation. It only removes this particular support-geometric obstruction.
- **No extension to many islands for free.** With several components the difference set contains many macroscopic separations. Full screening then constrains a family of prime-power-free windows simultaneously, and genuine collective arithmetic geometry may reappear.

## Research consequence

`WI-287` showed that a **theorem-derived nearest-prime width relaxation** has a Lambert-`W` spectral endpoint. The present finding identifies the exact arithmetic object behind that endpoint for the symmetric two-island branch:

\[
\boxed{
\text{actual complete screening}
\Longleftrightarrow
\text{actual nearest prime-power log gap},
}
\tag{49}
\]

and

\[
\boxed{
\text{actual complete screening}
+\text{restricted zero ground state}
\Longrightarrow
\sqrt{x}\,\delta_{\rm pp}(x)
\ge W(c_0\sqrt{x}).
}
\tag{50}
\]

So “use the entire prime family simultaneously” is **not** a remaining support-geometric lever on two intervals. The surviving routes are now more sharply separated: improve the actual prime-power gap input to the Lambert scale, use amplitude information from the global null equation that `WI-284`'s support restriction discards, or move to a topology with several independent separations where simultaneous screening has genuinely higher-dimensional content.
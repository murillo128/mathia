# MC-449 — Centered complement duality closes the near-complete fixed-lcm Fourier escape

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-INGREDIENTS` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the fixed-lcm prime-conductor branch of `MC-448`. Let `p` be prime, let `chi` be a nonprincipal multiplicative character modulo `p`, let `a in F_p^*`, and write

\[
f_a(x):=\chi(x+a)\overline{\chi(x)},
\qquad
S_H(u,a):=\sum_{k=1}^H f_a(u+k),
\qquad 0\le H\le p.
\tag{1}
\]

The complete correlation is

\[
\sum_{x\bmod p} f_a(x)=-1.
\tag{2}
\]

Therefore the correct source-sensitive kernel is the mean-zero centering

\[
g_a(x):=f_a(x)+\frac1p,
\qquad
G_H(u,a):=\sum_{k=1}^H g_a(u+k)
=S_H(u,a)+\frac Hp.
\tag{3}
\]

For every `H`, put

\[
R:=p-H.
\tag{4}
\]

Then there is an exact complementary-interval identity

\[
\boxed{
G_H(u,a)=-G_R(u-R,a).
}
\tag{5}
\]

Consequently, for any weight `W:F_p -> C`, with

\[
\mathcal T_H(W,a)
:=\sum_{u\bmod p}W(u)G_H(u,a)
=T_H(W,a)+\frac Hp\sum_u W(u),
\tag{6}
\]

and translated weight `W_R(v):=W(v+R)`, one has

\[
\boxed{
\mathcal T_H(W,a)=-\mathcal T_R(W_R,a).
}
\tag{7}
\]

Translation preserves `||W||_1`, `||W||_2`, support size and effective occupancy. Combining `(7)` with the same mixed-Weil Fourier estimate used in `MC-448` therefore gives the symmetric bound

\[
\boxed{
|\mathcal T_H(W,a)|
\le C_0\sqrt{p\,m(H)}\,\|W\|_2,
\qquad
m(H):=\min(H,p-H).
}
\tag{8}
\]

The corresponding centered pointwise estimate is

\[
|\mathcal T_H(W,a)|
\le \left(1+\frac1p\right)m(H)\,\|W\|_1.
\tag{9}
\]

Thus a uniform Fourier-envelope plus Parseval/Cauchy argument can certify a gain over the natural complementary trivial bound only when, up to an absolute constant,

\[
R_{\rm eff}(W):=\frac{\|W\|_1^2}{\|W\|_2^2}
\gtrsim \frac{p}{m(H)}.
\tag{10}
\]

For one fixed-lcm CRT slice in the clean `MC-447` regime,

\[
R_{\rm eff}(W)\le |\operatorname{supp}W|
\le 2^{\omega(L)}=p^{o(1)}
\qquad (L<p).
\tag{11}
\]

This closes the near-complete loophole left explicitly open by `MC-448`. If `p-H<=p^{1-delta}` for any fixed `delta>0`, then `(10)` requires a fixed power `p^delta`, while the source slice has only subpolynomial occupancy. The long interval is exactly a complete source-independent scalar plus the negative of a short complementary translated correlation; it does not create a cheap high-occupancy regime.

More strongly, **for every interval length `H`, this one-fixed-lcm uniform-envelope method can produce at most a subpolynomial conductor saving on the source-sensitive component.** Indeed `m(H)<=p/2`, and any improvement factor furnished only through `R_eff(W)` is at most

\[
\sqrt{R_{\rm eff}(W)}\le p^{o(1)}.
\tag{12}
\]

So even in the central range `H\asymp p`, where the occupancy threshold in `(10)` is only constant and the method may be numerically nontrivial, it cannot remove a fixed positive conductor-power tariff. Near either endpoint it is asymptotically blocked by the stronger threshold `p/m(H)`.

The uncentered term removed in `(6)` is not hidden source cancellation. It is exactly the zero Fourier mode forced by the complete-period identity `(2)`:

\[
T_H(W,a)
=\mathcal T_H(W,a)-\frac Hp\sum_uW(u).
\tag{13}
\]

If the outer well-factorable coefficients cancel this scalar, only `\mathcal T_H` remains and the complement obstruction applies. If they do not, the surviving contribution is a source-independent incidence/coefficient term of the type already separated from genuine character phase in `MC-413`; it cannot be credited as a new retained source variable.

This result is method-specific. It does not rule out a theorem using the detailed weighted Fourier spectrum of the CRT-idempotent set, cancellation across several lcm values before Cauchy, modulus factorization before completion, variable-length coupling, or a nonuniform estimate correlated with the actual source weights. No estimate for `M(x)`, a twisted Mertens sum, or an individual incomplete character sum follows.

## 1. Exact complement identity after removing the universal zero mode

Equation `(2)` is the prime-conductor specialization already used in `MC-448`: for `a!=0`, the substitution `y=1+a/x` gives

\[
\sum_x\chi(x+a)\overline{\chi(x)}=-1.
\tag{14}
\]

Hence `g_a` in `(3)` has exact mean zero over one period:

\[
\sum_{x\bmod p}g_a(x)=0.
\tag{15}
\]

Now let `H=p-R`. The `p` consecutive values `u+1,...,u+p` form a complete residue system, so

\[
0
=\sum_{k=1}^{p}g_a(u+k)
=G_H(u,a)+\sum_{k=H+1}^{p}g_a(u+k).
\tag{16}
\]

Writing `k=H+j=p-R+j` in the last sum and reducing modulo `p` gives

\[
\sum_{k=H+1}^{p}g_a(u+k)
=\sum_{j=1}^{R}g_a(u-R+j)
=G_R(u-R,a),
\tag{17}
\]

which proves `(5)`. Multiplying by `W(u)`, summing over `u`, and changing variable `v=u-R` proves `(7)`.

Without centering the same calculation reads

\[
S_{p-R}(u,a)=-1-S_R(u-R,a).
\tag{18}
\]

Thus the apparent near-complete advantage consists of exactly two pieces: the universal complete-period scalar `-1`, and a short complementary incomplete correlation. There is no third source-sensitive term.

## 2. Fourier-Weil control must use the shorter side of the period

The additive Fourier transform of `g_a` vanishes at frequency zero and agrees with that of `f_a` at every nonzero frequency. Hence the mixed rational Weil estimate from `MC-448` still gives

\[
|\widehat g_a(t)|\le C_0\sqrt p
\qquad (t\ne0).
\tag{19}
\]

Applying the `MC-448` Parseval/Cauchy calculation directly at length `H` yields

\[
|\mathcal T_H(W,a)|\le C_0\sqrt{pH}\,\|W\|_2.
\tag{20}
\]

Applying it instead to the exact complement `(7)` gives

\[
|\mathcal T_H(W,a)|
=|\mathcal T_R(W_R,a)|
\le C_0\sqrt{pR}\,\|W_R\|_2
=C_0\sqrt{pR}\,\|W\|_2.
\tag{21}
\]

Taking the better estimate proves `(8)`.

The same symmetry applies to the trivial estimate. Since `|g_a(x)|<=1+1/p`, direct summation and complementary summation give `(9)`. Comparing `(8)` and `(9)` yields `(10)` up to the harmless absolute factor `(1+1/p)^2`.

The conclusion is important for interpretation: when `H` approaches `p`, the relevant incomplete scale is not `H` but `p-H` once the universal complete-period mode has been removed. The small threshold `p/H` appearing in the uncentered one-sided comparison of `MC-448` was therefore not a genuine near-complete source-phase escape.

## 3. Fixed-lcm sparsity rules out a conductor-power gain at every interval length

Under the clean separated/coprime hypotheses of `MC-447`, fixing the lcm fixes `a`, and the distinct starts are indexed by the Boolean CRT choices of prime factors of `L`. Thus `(11)` holds. The elementary bound already proved in `MC-448` says that for every `eta>0`,

\[
2^{\omega(L)}\ll_\eta L^\eta\ll_\eta p^\eta.
\tag{22}
\]

If the shorter side satisfies

\[
m(H)\le p^{1-\delta}
\tag{23}
\]

for fixed `delta>0`, the threshold `(10)` is at least `p^delta`, while `(22)` is `p^eta` for arbitrarily smaller fixed `eta`. Hence the method cannot even certify a gain over the centered complementary trivial bound for all sufficiently large `p`.

If instead `m(H)=p^{1-o(1)}`, the threshold can be subpolynomial and a gain is not excluded. But the gain available from generic `L^2` occupancy is bounded by the square root of `(11)`, hence by `p^{o(1)}`. In particular, no fixed `kappa>0` can be supplied uniformly as a saving `p^{-kappa}` from this mechanism.

This is the precise closure relevant to the source-depth problem. `MC-448` already ruled out a fixed-lcm uniform-envelope gain throughout every fixed-power incomplete range measured from `H=0`. The complement identity extends that obstruction to fixed-power neighborhoods of `H=p`, while `(12)` shows that the remaining central/transition range can offer only subpolynomial savings because the source slice itself has subpolynomial effective occupancy.

## 4. Prior art and novelty boundary

No new character-sum theorem is claimed. Equation `(14)` is the same classical complete translated-character correlation used in `MC-413` and `MC-448`; finite Fourier inversion, Parseval and the mixed Weil bound are already anchored by `MC-S55` (Cochrane--Pinner). The complement identity `(5)` is an elementary consequence of periodicity and zero centering.

A targeted literature search on 21 September 2026 found the standard treatment of incomplete character sums as sums over intervals shorter than one complete period and the usual complete-sum cancellation background, but no reason to assign independent novelty to subtracting a complementary interval. The mathematical content here is the branch-specific consequence after combining that elementary symmetry with the exact fixed-lcm source-cardinality bound of `MC-447`.

The durable conclusion is therefore not a new finite-field estimate. It is a closure statement for a particular proposed escape in the Mathia source-frame argument: **near-complete fixed-lcm intervals do not bypass the polynomial occupancy tariff once the universal complete-period mode is separated, and the entire one-lcm uniform-Fourier-envelope route is incapable of a fixed conductor-power gain.**

## Boundaries and falsification tests

- **Centering is structural, not optional bookkeeping.** The removed term `(H/p) sum W` is the zero Fourier mode forced by the exact complete correlation. Any later use of that term must treat it as source-independent coefficient/incidence structure rather than restored character phase.
- **The result is still one-lcm and prime-conductor.** Coupling different `L` values before Cauchy or factoring a composite/smooth conductor can change the available variables and lies outside the proof.
- **Uniform spectral control is the target of the no-go.** A theorem using the actual correlation between `widehat W(t)` and the nonuniform multiplier `widehat f_a(t)D_H(t)` is not bounded by the effective-occupancy comparison alone.
- **Variable lengths are not globally scalarized here.** Identity `(5)` holds for every individual length, but a family with `H=H_{d,e}` can correlate its boundary lengths with the divisor weights. Such a collective theorem must keep that dependence before Cauchy.
- **A subpolynomial gain is not excluded in the central range.** The claim is that generic one-lcm occupancy cannot supply the fixed positive conductor power needed to change the existing source-depth tariff.
- **No lower bound for the true weighted correlation is asserted.** Failure of the generic estimate to produce a power saving is not evidence that the exact weighted sum is large.
- **No RH input is present.** The argument is finite periodicity, the classical complete correlation, finite Fourier analysis and the already established CRT source geometry.

## Consequence for the research line

The near-complete interval caveat in `MC-448` is now resolved for the same uniform Fourier-Weil/Cauchy mechanism. After centering away the universal complete-period scalar, length `H` and complementary length `p-H` are exactly equivalent up to translation of the source weights. Therefore the apparent fall of the occupancy threshold when `H` approaches `p` does not produce a new source-phase regime.

For one fixed lcm, uniform mixed-Weil control followed by generic Parseval/Cauchy is now **power-closed for all interval lengths**: it is blocked by a polynomial occupancy deficit near either endpoint and can yield at most a subpolynomial saving in the remaining range. The accepted clue should retain only mechanisms that use information discarded by this closure: detailed weighted CRT Fourier geometry, cross-lcm coupling, modulus factorization before scalarization, or genuinely collective variable-length structure.
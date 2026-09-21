# MC-448 — Fixed-lcm Fourier-Weil averaging still pays polynomial occupancy

**Status:** `EXACT-DERIVED` · `CLASSICAL-INGREDIENTS` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the incomplete translated-character branch of `MC-413`, after the full-box occupancy obstruction `MC-446` and the CRT fibre classification `MC-447`.

Let `p` be prime, let `chi` be a nonprincipal multiplicative character modulo `p`, let `a in F_p^*`, and for `1<=H<=p` write

\[
f_a(x):=\chi(x+a)\overline{\chi(x)},
\qquad
S_H(u,a):=\sum_{k=1}^H f_a(u+k).
\tag{1}
\]

For an arbitrary complex weight `W:F_p -> C`, define the fixed-shift aggregate

\[
T_H(W,a):=\sum_{u\bmod p}W(u)S_H(u,a).
\tag{2}
\]

There is an absolute constant `C_0` such that

\[
\boxed{
|T_H(W,a)|\le C_0\sqrt{pH}\,\|W\|_2.
}
\tag{3}
\]

The proof is only finite Fourier analysis plus the classical Weil bound for a mixed additive-multiplicative character sum of the fixed rational function `(x+a)/x`. In particular, if

\[
R_{\rm eff}(W):=\frac{\|W\|_1^2}{\|W\|_2^2},
\tag{4}
\]

then the uniform estimate `(3)` beats the pointwise bound

\[
|T_H(W,a)|\le H\|W\|_1
\tag{5}
\]

only in the range

\[
\boxed{
R_{\rm eff}(W)>C_0^2\frac pH.
}
\tag{6}
\]

This is a genuine factor-`p` improvement over the full two-parameter ambient-box tariff `R_eff \gtrsim p^2/H` from `MC-446`: fixing the constrained shift coordinate before Cauchy is analytically meaningful even though `MC-447` shows that, in the separated source regime, it is only fixing the lcm.

However, the improvement is still insufficient for one fixed-lcm CRT slice in every fixed-power incomplete range. Under the clean `MC-447` hypotheses

\[
(h,P(z))=1,
\qquad d,e\le D,
\qquad D^2<p,
\tag{7}
\]

fix `L=[d,e]`. Then `a=hL^{-1} (mod p)` is fixed and the supported source starts satisfy

\[
|\operatorname{supp}W|\le 2^{\omega(L)}.
\tag{8}
\]

Consequently

\[
R_{\rm eff}(W)\le 2^{\omega(L)}.
\tag{9}
\]

For every `eta>0` there is a constant `C_eta` with the elementary bound

\[
2^{\omega(L)}\le C_\eta L^\eta.
\tag{10}
\]

Since `L<p`, for every fixed `delta>0` and every common incomplete length

\[
H\le p^{1-\delta},
\tag{11}
\]

choose `eta<delta`. Then, for sufficiently large `p`, `(9)`--`(10)` are asymptotically smaller than the threshold in `(6)`, because

\[
R_{\rm eff}(W)\ll_\eta p^\eta
\qquad\text{but}\qquad
\frac pH\ge p^\delta.
\tag{12}
\]

Thus the most direct one-dimensional repair of `MC-446` also closes: **Fourier-diagonalize the fixed-`a` translated correlation, apply a uniform Weil bound to every nonzero Fourier mode, and then use Parseval/Cauchy on the source weights.** It lowers the ambient occupancy cost from quadratic to linear in the conductor, but a fixed-lcm CRT-idempotent slice has only subpolynomial cardinality and cannot pay even that reduced tariff at any fixed distance below a complete conductor block.

This is not a no-go for the accepted clue. It leaves precisely the mechanisms that use more than a uniform Fourier-envelope bound: cancellation in the actual well-factorable coefficients, detailed Fourier structure of the CRT-idempotent set, coupling several lcm values before Cauchy, modulus factorization, variable-length structure, or the wraparound/nonunit regimes excluded by `MC-447`. No estimate for `M(x)`, a twisted Mertens sum, or an individual incomplete character sum follows.

## 1. The fixed-shift kernel has square-root Fourier envelope

Use the additive Fourier transform

\[
\widehat f_a(t)
:=\sum_{x\bmod p}f_a(x)e_p(-tx),
\qquad
e_p(y):=e^{2\pi i y/p}.
\tag{13}
\]

At zero frequency one has the exact identity

\[
\widehat f_a(0)=-1.
\tag{14}
\]

Indeed, on `x!=0` substitute `y=1+a/x`. This bijects `F_p^*` with `F_p\setminus\{1\}`; the omitted zero of `chi(x+a)` contributes zero, so

\[
\sum_x\chi(x+a)\overline{\chi(x)}
=\sum_{y\ne1}\chi(y)=-1.
\tag{15}
\]

For `t!=0`, the Fourier coefficient is

\[
\widehat f_a(t)
=\sum_{x\bmod p}
\chi\!\left(\frac{x+a}{x}\right)e_p(-tx),
\tag{16}
\]

with the character extended by zero at the pole/zero in the usual way. The rational multiplicative phase `(x+a)/x` has one simple zero and one simple pole and is not a nontrivial power compatible with `chi`; the additive phase is nonconstant. The classical Weil bound for mixed character sums of rational functions therefore gives

\[
|\widehat f_a(t)|\le C_0\sqrt p
\qquad (t\ne0),
\tag{17}
\]

for an absolute constant `C_0` depending only on this fixed rational-function complexity. Increasing `C_0` if necessary makes `(17)` valid uniformly for all frequencies including `(14)`.

The important point is structural rather than the best constant: after fixing `a`, the translated-character kernel is a bounded-complexity trace function with Fourier operator norm `O(sqrt(p))`.

## 2. Fourier inversion gives the linear occupancy tariff

Let

\[
D_H(t):=\sum_{k=1}^H e_p(tk).
\tag{18}
\]

Fourier inversion in `(1)` gives

\[
S_H(u,a)
=\frac1p\sum_{t\bmod p}
\widehat f_a(t)D_H(t)e_p(tu).
\tag{19}
\]

Hence, with `\widehat W(t)=\sum_u W(u)e_p(-tu)`,

\[
T_H(W,a)
=\frac1p\sum_{t\bmod p}
\widehat f_a(t)D_H(t)\widehat W(-t).
\tag{20}
\]

Use `(17)` and Cauchy in frequency. Parseval gives

\[
\sum_t|D_H(t)|^2=pH,
\qquad
\sum_t|\widehat W(t)|^2=p\|W\|_2^2.
\tag{21}
\]

Therefore

\[
\begin{aligned}
|T_H(W,a)|
&\le \frac{C_0\sqrt p}{p}
\left(\sum_t|D_H(t)|^2\right)^{1/2}
\left(\sum_t|\widehat W(t)|^2\right)^{1/2}\\
&=C_0\sqrt{pH}\,\|W\|_2,
\end{aligned}
\tag{22}
\]

which proves `(3)`.

Comparing `(22)` with `(5)` gives `(6)`. This comparison is deliberately method-specific: failure of `(6)` says that this **uniform Fourier-envelope plus Parseval/Cauchy estimate** does not certify a gain over the pointwise bound. It does not lower-bound the true size of `T_H(W,a)` and therefore does not exclude additional cancellation tied to the exact source weights.

## 3. A fixed-lcm CRT slice is too sparse at fixed power distance from completion

In the coprime-shift separated regime of `MC-447`, fixing the frame coordinate

\[
a=hL^{-1}\pmod p
\tag{23}
\]

fixes the integer lcm `L` itself. The same finding shows that, for fixed `L`, each prime divisor not shared with the shift makes at most one binary side choice in the CRT residue, while shift-common primes are absent under `(h,P(z))=1`. Hence the distinct starts in a fixed-`L` source slice satisfy `(8)`; when the complete divisor support is available the count is exactly `2^{omega(L)}`.

The subpolynomial estimate `(10)` needs no prime-number theorem. Fix `eta>0` and split the prime divisors of `L` at `Y=2^{1/eta}`. The finitely many primes `r<=Y` contribute at most the constant `2^{pi(Y)}`, while for every prime `r>Y` one has `2<r^eta`. Thus

\[
2^{\omega(L)}
\le 2^{\pi(Y)}\prod_{\substack{r\mid L\\r>Y}}r^\eta
\le C_\eta L^\eta.
\tag{24}
\]

Since the separated range gives `L<=de<=D^2<p`, equations `(6)` and `(24)` are incompatible for all sufficiently large `p` whenever `H<=p^{1-delta}` and `eta<delta`. The obstruction is therefore not merely that a fixed-lcm slice is smaller than the full `p^2` box. It remains too small even after exploiting the correct one-dimensional fixed-shift Fourier geometry.

This also locates the boundary of the argument. If `H=p^{1-o(1)}`, the threshold `p/H` can become subpolynomial and the cardinality comparison alone no longer closes the route. That is exactly the near-complete regime in which `MC-413` warns that full conductor blocks collapse to the divisor-independent Ramanujan scalar, so any surviving near-complete argument must keep track of the boundary remainder rather than count it as a generic fixed-power incomplete gain.

## 4. Prior art and novelty boundary

All analytic ingredients used above are classical. Finite Fourier inversion and Parseval are standard. The needed estimate `(17)` is a fixed-degree instance of the Weil bound for mixed additive-multiplicative character sums with rational-function arguments. Cochrane and Pinner, *Using Stepanov's method for exponential sums involving rational functions*, Journal of Number Theory 116 (2006), 270--292, DOI `10.1016/j.jnt.2005.04.001`, gives such Weil bounds for additive and multiplicative characters over finite fields and rational functions.

There is also an established literature on character sums over sparse subsets of finite fields; for example Mérai, Shparlinski and Winterhof, *Character sums over sparse elements of finite fields*, Bulletin of the London Mathematical Society 56 (2024), 1488--1510, DOI `10.1112/blms.13008`, treats a different notion of sparsity coming from sparse coordinate representations in extension fields. It does not supply a theorem for the present CRT-idempotent source slice.

A targeted audit on 21 September 2026 found the mixed rational Weil estimate and broader sparse-subset character-sum literature, but no reason to claim a new finite-field theorem in `(3)`. No novelty is claimed for the Fourier bound, the Weil estimate, Parseval, or the subpolynomial bound for `2^{omega(L)}`.

The durable Mathia result is the branch-specific implication obtained after inserting the exact `MC-447` source geometry: fixing `a` improves the generic `MC-446` occupancy tariff by one conductor power, yet the actual fixed-lcm CRT slice remains subpolynomial and therefore still cannot make this uniform Fourier-Weil/Cauchy route nontrivial at any fixed-power distance from completion.

## Boundaries and falsification tests

- **Prime conductor is essential to the stated finite-field argument.** Composite and especially smooth conductors may factor the mixed transform or admit q-van der Corput reductions not represented by `(17)`. Modulus factorization remains a live escape.
- **The obstruction is to a specific generic estimate, not to the actual weighted sum.** A theorem exploiting the detailed values of `\widehat W(t)`, cancellation in the well-factorable coefficients, or correlations between `\widehat W` and `\widehat f_a D_H` lies outside `(3)`.
- **One lcm is fixed before Cauchy.** Coupling many `L` values while the factorable weights are still present may create another averaging variable and is not ruled out.
- **A common incomplete length `H` is assumed.** The source family in `MC-413` can have boundary lengths depending on the CRT residue. Any application to the complete weighted family must control that variation rather than silently replace it by one interval.
- **The fixed-power conclusion is asymptotic.** It says that for each fixed `delta>0`, the route fails for sufficiently large prime conductors when `H<=p^(1-delta)`. It does not give an optimized finite-`p` threshold.
- **Near-complete intervals are not closed by the cardinality argument.** When `p/H` is subpolynomial, `(12)` no longer separates the two sides. Such intervals must be analyzed together with the exact complete-block collapse of `MC-413`.
- **The source-count bound uses the clean separated/coprime regime of `MC-447`.** Wraparound `D^2>=p`, shifts noninvertible modulo the conductor, shift-common sieve primes, and prime-power divisor support require separate analysis.
- **No RH-scale information is imported.** Everything here is finite character harmonic analysis plus the already established CRT source geometry.

## Consequence for the research line

`MC-446` showed that full `(u,a)` averaging has genuine `sqrt(H)` RMS cancellation but requires effective occupancy about `p^2/H`. `MC-447` then showed that in the clean source regime the coordinate `a` is only the lcm label and that same-frame multiplicity does not provide free occupancy. The present result tests the natural repair: condition on that lcm first and use the one-dimensional Fourier geometry of the remaining start variable.

That repair is quantitatively real but still too expensive. The generic tariff falls to `p/H`, whereas one fixed-lcm source slice contains at most `2^{omega(L)}=p^{o(1)}` distinct starts. Consequently the accepted restricted-frame clue should no longer spend effort on **uniform mixed-Weil control plus Parseval/Cauchy for one fixed lcm** in a fixed-power incomplete range.

The next useful calculation must exploit information discarded by that step: the actual Fourier spectrum of the CRT-idempotent weighted set, cancellation across lcm scales before Cauchy, modulus factorization before scalarization, or a boundary regime where the present source-cardinality comparison no longer applies.
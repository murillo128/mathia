# RE-007 — clean peaks force a square-root prime gap or Chebyshev excursion

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SECOND-LAYER-ASYMPTOTIC + CLEAN-PEAK-SQUARE-ROOT-SELECTOR + PRIME-GAP/CHEBYSHEV-DICHOTOMY + PRIOR-ART-BOUNDED`. `RE-006` shows that a sufficiently large clean regular self-tangent CA local peak, with `X=log C` and consecutive first-layer boundary primes `p<q`, satisfies the exact identity

\[
X-p
=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr),
\qquad p<X<q.
\tag{1}
\]

At logarithmic resolution this yields the exact residual window of `RE-006`. At the next natural scale, the higher-layer term itself has a rigid leading asymptotic: the second prime-power layer contributes `sqrt(2X)` and all deeper layers are `o(sqrt X)`. Comparing this with the ordinary prime-power correction in Chebyshev's function

\[
\psi(x):=\sum_{r^k\le x}\log r
\]

gives, along every such clean peak,

\[
\boxed{
\psi(p)-p
=(X-p)-(\sqrt2-1)\sqrt p+o(\sqrt p).
}
\tag{2}
\]

Thus the clean chamber has a source-selected square-root dichotomy. For every fixed `delta>0`, if

\[
\psi(p)-p
\ge-(\sqrt2-1-\delta)\sqrt p,
\tag{3}
\]

then necessarily

\[
\boxed{q-p\ge\delta\sqrt p+o(\sqrt p).}
\tag{4}
\]

Conversely, any clean peak sequence with

\[
q-p=o(\sqrt p)
\tag{5}
\]

must satisfy the tuned negative excursion

\[
\boxed{
\psi(p)-p
=-(\sqrt2-1+o(1))\sqrt p.
}
\tag{6}
\]

This does not close the Robin route: neither square-root pointwise prime gaps nor exclusion of the selected Chebyshev excursion is available unconditionally at the required quantifiers. The gain is a sharper source-selection boundary. A hypothetical clean counterexample sequence cannot merely occupy prime gaps larger than the mean-gap scale from `RE-006`; unless the prime-counting error repeatedly tunes itself to the specific negative coefficient `sqrt(2)-1`, the boundary gap must expand to square-root scale.

## 1. The second CA prime-power layer has coordinate `p^2/2`

Retain the event coordinates of `RE-001`--`RE-004`. For prime `r` and layer `j>=1`,

\[
\lambda_{r,j}
=\log\frac{1-r^{-(j+1)}}{1-r^{-j}},
\qquad
\frac1{\eta_{r,j}\log\eta_{r,j}}
=\frac{\lambda_{r,j}}{\log r}.
\tag{7}
\]

For `j=2` the abundance increment simplifies exactly to

\[
\lambda_{r,2}
=\log\!\left(1+\frac1{r(r+1)}\right).
\tag{8}
\]

Put `u_r=1/(r(r+1))`. The elementary inequalities

\[
\frac{u_r}{1+u_r}
\le\log(1+u_r)\le u_r
\tag{9}
\]

show that

\[
\frac1{\lambda_{r,2}}
=r^2\left(1+O(r^{-1})\right).
\tag{10}
\]

Hence

\[
\eta_{r,2}\log\eta_{r,2}
=r^2\log r\left(1+O(r^{-1})\right).
\tag{11}
\]

This already locates `eta_(r,2)` at quadratic scale. Indeed, comparison of `x log x` at fixed multiples of `r^2` first gives `eta_(r,2) asymp r^2`, so

\[
\log\eta_{r,2}=2\log r+O(1).
\]

Substituting this back into (11) yields

\[
\boxed{
\eta_{r,2}
=\frac{r^2}{2}\,(1+o(1)).
}
\tag{12}
\]

No assumption about spacing between different event coordinates is used. In particular, ties with deeper layers do not affect the mass calculation below.

## 2. Higher-layer event mass is `sqrt(2X)+o(sqrt X)`

Write, as in `RE-006`,

\[
\Phi_{\ge2}(X)
:=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\
                   \eta_{r,j}\le X}}
  \log r.
\tag{13}
\]

Let `Phi_2(X)` be the `j=2` part. Equation (12) implies the following sandwich: for every fixed `epsilon>0` and all sufficiently large `X`, primes up to

\[
\sqrt{\frac{2X}{1+\varepsilon}}
\]

have their second-layer event before `X`, while any prime whose second-layer event is before `X` is at most

\[
\sqrt{\frac{2X}{1-\varepsilon}},
\]

apart from finitely many fixed primes. Therefore

\[
\vartheta\!\left(\sqrt{\frac{2X}{1+\varepsilon}}\right)+O(1)
\le\Phi_2(X)
\le
\vartheta\!\left(\sqrt{\frac{2X}{1-\varepsilon}}\right)+O(1).
\tag{14}
\]

The prime number theorem `vartheta(y)~y`, followed by `epsilon downarrow0`, gives

\[
\boxed{
\Phi_2(X)=\sqrt{2X}+o(\sqrt X).
}
\tag{15}
\]

The deeper layers are smaller. `RE-004` proves

\[
M_{\ge3}(X)
=O\!\left((X\log X)^{1/3}\log X\right)
\tag{16}
\]

for their total event occurrences. `RE-003` bounds the prime weight of every event up to `X` by `O(log X)`. Consequently

\[
\sum_{\substack{r,\,j\ge3\\\eta_{r,j}\le X}}\log r
=O\!\left(X^{1/3}(\log X)^{7/3}\right)
=o(\sqrt X).
\tag{17}
\]

Combining (15)--(17),

\[
\boxed{
\Phi_{\ge2}(X)=\sqrt{2X}+o(\sqrt X).
}
\tag{18}
\]

This leading square-root prime-frontier correction is not asserted as a new asymptotic object. The recent Mantovanelli self-tangent/workload preprint already contains a square-root-scale prime-frontier normal form, as recorded in `SOURCES.md` and in the prior-art boundary of `RE-006`. Equations (8)--(18) independently reconstruct the exact normalization needed for the splice below.

## 3. Ordinary prime powers contribute `sqrt p` to `psi(p)-vartheta(p)`

The standard Chebyshev identity is

\[
\psi(p)-\vartheta(p)
=\sum_{k\ge2}\vartheta(p^{1/k}).
\tag{19}
\]

The `k=2` term is

\[
\vartheta(\sqrt p)=\sqrt p+o(\sqrt p)
\tag{20}
\]

by the prime number theorem. For `k>=3`, the elementary Chebyshev bound `vartheta(y)=O(y)` gives

\[
\sum_{k\ge3}\vartheta(p^{1/k})
=O(p^{1/3}\log p)
=o(\sqrt p).
\tag{21}
\]

Hence

\[
\boxed{
\psi(p)-\vartheta(p)
=\sqrt p+o(\sqrt p).
}
\tag{22}
\]

The important point is the mismatch of the two square-root coefficients. The CA second layer is activated at `eta_(r,2)~r^2/2`, so its mass at event coordinate `X` reaches primes of size about `sqrt(2X)`. The ordinary Chebyshev prime-power correction at the boundary prime `p` reaches only `sqrt p`.

## 4. Self-tangency converts the coefficient mismatch into a selected Chebyshev error

Return now to a clean regular self-tangent CA local peak from `RE-006`. Its boundary primes `p<q` are consecutive and satisfy

\[
p<X<q.
\tag{23}
\]

The prime number theorem implies `q/p->1` along any unbounded sequence of consecutive primes, hence

\[
\frac Xp\to1,
\qquad
\sqrt{2X}=\sqrt2\sqrt p+o(\sqrt p).
\tag{24}
\]

Rewrite the exact identity (1) using

\[
p-\vartheta(p)
=p-\psi(p)+\bigl(\psi(p)-\vartheta(p)\bigr).
\tag{25}
\]

Substituting (18), (22), and (24) gives

\[
\begin{aligned}
X-p
&=\sqrt{2X}-\left[p-\psi(p)+\sqrt p\right]+o(\sqrt p)\\
&=\psi(p)-p+(\sqrt2-1)\sqrt p+o(\sqrt p).
\end{aligned}
\tag{26}
\]

This is equivalent to (2).

Equation (26) is stronger than a free-standing asymptotic for the higher layers because `X` is not arbitrary: it is the intrinsic self-tangent coordinate of a genuine CA local Robin peak, and `p,q` are its actual clean neighboring first-layer transitions. The exact displacement `X-p` therefore couples the prime-power background to a source-selected ordinary prime gap.

## 5. The clean chamber splits at square-root scale

The geometric containment (23) immediately gives

\[
0<X-p<q-p.
\tag{27}
\]

Together with (2), this implies the necessary bounds

\[
\boxed{
\psi(p)-p
>-(\sqrt2-1)\sqrt p+o(\sqrt p),
}
\tag{28}
\]

and

\[
\boxed{
\psi(p)-p
<(q-p)-(\sqrt2-1)\sqrt p+o(\sqrt p).
}
\tag{29}
\]

Now fix `delta>0`. If (3) holds along such a peak sequence, then (26) gives

\[
X-p\ge\delta\sqrt p+o(\sqrt p),
\]

and (27) proves (4). Conversely, if (5) holds, then `X-p=o(sqrt p)` by (27), and (2) becomes (6).

Thus a hypothetical infinite clean counterexample sequence forced by `RE-001` has only two square-root-scale possibilities:

\[
\boxed{
\begin{array}{l}
\text{either the selected consecutive-prime gap carries a positive }\sqrt p\text{-scale width},\\
\text{or }\psi(p)-p\text{ repeatedly tracks }-(\sqrt2-1)\sqrt p\text{ to }o(\sqrt p)\text{ accuracy}.
\end{array}}
\tag{30}
\]

The alternatives are deliberately source-conditioned; this is not a theorem that every large prime gap or every Chebyshev excursion has this form.

## 6. Prior-art and feasibility boundary

The coefficient `sqrt(2)-1` itself is not a novelty claim. Jean-Louis Nicolas's 2022 treatment of Ramanujan's divisor-sum expansion records the classical RH-conditional term `2(sqrt(2)-1)/sqrt(log n)`. The present derivation has a different role: it identifies the same characteristic coefficient as the difference between the exact CA second-layer frontier `sqrt(2X)` and the ordinary prime-power correction `sqrt p`, and then inserts that difference into the clean self-tangent peak selector. A targeted literature search did not locate the exact selected relation (2) or the prime-gap/Chebyshev dichotomy (30), but the coefficient and the surrounding square-root divisor-sum scale are classical.

Nor does current unconditional prime-gap technology close (30). Runbo Li's current Harman-sieve preprint proves primes in `[x-x^0.52,x]` for all sufficiently large `x`; the exponent `0.52` remains above the square-root scale. Such a theorem bounds a consecutive gap by `O(p^0.52)` and therefore cannot exclude the `delta sqrt(p)` branch. This is a prior-art boundary only; no sieve estimate is imported into the derivation.

On the Chebyshev side, applying RH-conditional error estimates would be circular for this program. The line needs an unconditional source-selection theorem saying that the specific boundary primes selected by self-tangent counterexample peaks cannot realize the excursion in (6), or a theorem excluding the competing square-root-gap branch on the same selected subsequence. Generic prime-number-theorem error bounds are much too coarse for that task.

## 7. Boundaries and research consequence

The clean-boundary hypothesis remains load-bearing. If either neighboring CA transition contains a higher prime-power layer or a tie, `p<X<q` with two clean first-layer boundary primes is unavailable and the exact identity of `RE-006` does not reduce to (2). Those peaks remain in the zero-transition-count-density exceptional chamber of `RE-004`.

Equation (30) is also only a necessary condition. It neither proves square-root prime gaps occur along self-tangent peaks nor proves the Chebyshev excursion can occur. The two possibilities may coexist on different subsequences. In particular, no unproved prime-gap conjecture such as Legendre, Andrica, or Cramer is being assumed to eliminate the first branch.

The result nevertheless changes the clean frontier. `RE-006` required a mean-gap-scale container plus logarithmic alignment of the exact higher-layer mass. `RE-007` shows what that alignment becomes after exposing the dominant higher layer: unless the ordinary Chebyshev error is tuned to the classical coefficient `-(sqrt(2)-1)`, the clean self-tangent selector pushes the actual consecutive-prime gap from logarithmic to square-root scale.

Together with `RE-004`, a future closure can now attack three sharply separated source-selection failures rather than generic CA geometry: concentration on the zero-density exceptional transition chamber, recurrent square-root gaps at the clean self-tangent boundary primes, or recurrent `-(sqrt(2)-1)sqrt(p)` Chebyshev excursions at those same selected primes. Excluding any one branch does not by itself prove Robin's inequality; a complete argument must eliminate the alternatives forced on a hypothetical counterexample sequence.
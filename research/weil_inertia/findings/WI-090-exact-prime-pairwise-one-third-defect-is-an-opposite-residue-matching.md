# WI-090 — Exact prime pairwise one-third defect is an opposite-residue matching

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes the exact-ceiling consistency question left by WI-089 for residual **prime pairwise** Ramanujan rank defect: same-residue prime pairs cannot carry a free 3-cycle at all, so their defect is universally on the one-quarter cycle-counting scale. Consequently every positive case attaining the sharp WI-088 one-third ceiling is one of the two opposite-residue Loewner--Bezout boundary families already constructed in WI-087/WI-089. At any fixed observation length, the full exact-ceiling graph is therefore a matching, not merely a bounded-degree graph.

Let `p<q<2p` be distinct odd primes in the residual regime of WI-088,

\[
\delta=\delta_N(p,q)>q-1.
\tag{1}
\]

Inside the only exceptional strip, write

\[
d=q-p,\qquad
t=2p-q=p-d,
\tag{2}
\]

and

\[
\delta=kq+s,
\qquad
d<s<p.
\tag{3}
\]

The exact row-kernel graph from WI-088 uses

\[
A=\{0,\ldots,s-d-1\},
\qquad
C=\{s-d,\ldots,s-1\},
\qquad
B=\{s,\ldots,p-1\},
\tag{4}
\]

with `|C|=d`, and the partial map

\[
g(x)=
\begin{cases}
x+(k+1)d,&x\in A,\\
x+kd,&x\in B,
\end{cases}
\pmod p.
\tag{5}
\]

Every true row-kernel vector is constant on the free cycles of this partial map; WI-088 proves that there are no free cycles of length one or two and that, if `c` is the number of free cycles,

\[
\tau_{p,q}(\delta)
:=(p-1)-\operatorname{rank}G_{p,q}^{(N)}
\le \max\{0,c-1\}.
\tag{6}
\]

WI-089 further proves that a free 3-cycle can occur only when

\[
k=k_0:=\left\lfloor\frac p3\right\rfloor,
\tag{7}
\]

and then contains exactly

\[
a_0:=p-3k_0\in\{1,2\}
\tag{8}
\]

vertices from `A` and `3-a_0` vertices from `B`.

The missing observation is that, when `p` and `q` lie in the **same** nonzero residue class modulo `3`, the middle deleted interval `C` is itself three times the reduced step size. That interval is too wide for any `A`-vertex to jump directly into `B` at the only quotient where a 3-cycle is arithmetically possible.

The resulting exact strengthening is

\[
\boxed{
 p\equiv q\pmod3,\quad p,q>3
 \quad\Longrightarrow\quad
 \tau_{p,q}(\delta)
 \le
 \max\left\{0,
 \left\lfloor\frac{2p-q}{4}\right\rfloor-1
 \right\}.
}
\tag{9}
\]

Moreover, if the positive WI-088 ceiling is attained,

\[
\tau_{p,q}(\delta)
=
\left\lfloor\frac{2p-q}{3}\right\rfloor-1
\ge1,
\tag{10}
\]

then necessarily the two primes occupy opposite nonzero residue classes modulo `3`, and the boundary is exactly one of

\[
\boxed{
\begin{aligned}
p\equiv2,\ q\equiv1\pmod3:
&\qquad
\delta=\delta_-:=\frac{pq+p-q}{3},\\[1mm]
p\equiv1,\ q\equiv2\pmod3:
&\qquad
\delta=\delta_+:=\frac{pq+q-p}{3}.
\end{aligned}}
\tag{11}
\]

Conversely, WI-087 and the mirror construction in WI-089 prove that both families in (11) attain the ceiling exactly. Thus (11) is an **if and only if classification** of every positive exact-ceiling residual prime pair.

Finally, WI-089 already proves that the edges in these two opposite-residue families form a matching at each fixed observation length `N`. Since (11) shows that there are no other exact-ceiling edges,

\[
\boxed{
\text{for each fixed }N,
\text{ the entire positive exact WI-088-ceiling graph is a matching.}
}
\tag{12}
\]

In particular every prime is incident to at most one pair attaining the one-third ceiling at that `N`. This upgrades WI-089's coarse degree-`40` bound for the full exact-ceiling graph to the sharp structural bound `deg_N<=1`.

## 1. Same residue modulo three makes the deleted interval a three-step barrier

Assume first that

\[
p\equiv q\pmod3,
\qquad p,q>3.
\tag{13}
\]

Then

\[
d=q-p=3h
\tag{14}
\]

for an integer `h>=1`.

If `k!=k_0`, WI-089 already excludes every free 3-cycle. Hence it remains only to study the exceptional quotient `k=k_0`.

There are two residue orientations.

### Case `p≡q≡1 (mod 3)`

Write

\[
p=3k_0+1.
\tag{15}
\]

Modulo `p`, the two translations in (5) reduce to

\[
(k_0+1)d
=3(k_0+1)h
=(p+2)h
\equiv 2h\pmod p,
\tag{16}
\]

and

\[
k_0d
=(p-1)h
\equiv-h\pmod p.
\tag{17}
\]

Take any `x in A`. Since `x<=s-d-1=s-3h-1` and `s<p`,

\[
x+2h
\le s-h-1
<s
\tag{18}
\]

and also `x+2h<p`; there is no modular wrap. Therefore

\[
\boxed{x\in A\Longrightarrow g(x)=x+2h\notin B.}
\tag{19}
\]

But here `a_0=1`. By WI-089, any hypothetical free 3-cycle would contain exactly one `A`-vertex and two `B`-vertices. The successor of that unique `A`-vertex in the directed cycle would necessarily lie in `B`, contradicting (19). Hence no free 3-cycle exists.

### Case `p≡q≡2 (mod 3)`

Now

\[
p=3k_0+2.
\tag{20}
\]

The `A`-translation reduces to

\[
(k_0+1)d
=3(k_0+1)h
=(p+1)h
\equiv h\pmod p.
\tag{21}
\]

Again, for every `x in A`,

\[
x+h
\le s-2h-1
<s,
\tag{22}
\]

with no modular wrap. Thus

\[
\boxed{x\in A\Longrightarrow g(x)=x+h\notin B.}
\tag{23}
\]

Here `a_0=2`, so a hypothetical free 3-cycle would contain two `A`-vertices and one `B`-vertex. In a directed 3-cycle with this composition, the predecessor of the unique `B`-vertex is necessarily an `A`-vertex. That would give an `A -> B` edge, again contradicting (23).

Therefore same-residue prime pairs admit **no free 3-cycle for any residual boundary**.

## 2. No 3-cycle forces the one-quarter defect scale

WI-088 already excludes free cycles of lengths one and two. Section 1 excludes length three in the same-residue case. Hence every free cycle has length at least four.

Only the `t=2p-q` vertices outside the forced-zero/path part of the WI-088 graph can contribute to free cycles. Therefore

\[
c\le\left\lfloor\frac t4\right\rfloor.
\tag{24}
\]

Combining with (6) gives exactly (9):

\[
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac t4\right\rfloor-1
\right\}.
\tag{25}
\]

This is not merely an equality-case statement. It separates the same-residue residual regime from the one-third obstruction uniformly. In particular, along any sequence of same-residue residual prime pairs with `t -> infinity`,

\[
\frac{\tau_{p,q}(\delta)}{t}
\le\frac14+o(1).
\tag{26}
\]

Thus any sequence with `tau/t -> 1/3` must eventually use opposite nonzero residue classes modulo `3`, strengthening WI-089's near-extremizer localization from a quotient/population condition to an arithmetic residue condition.

## 3. Exact positive ceiling forces opposite residues

For completeness, one can rule out same-residue equality directly from WI-089's equality bookkeeping as well.

Write

\[
t=3r+j,
\qquad j\in\{0,1,2\}.
\tag{27}
\]

If the positive WI-088 ceiling `tau=r-1>=1` is attained, WI-089 proves that the number `c_3` of free 3-cycles obeys

\[
c_3\ge r-j.
\tag{28}
\]

If `p≡q≡1 mod 3`, then `t≡1 mod 3`, so `j=1`; positivity gives `r>=2`, hence `c_3>=1`. If `p≡q≡2 mod 3`, then `j=2`. Because `p,q` are odd, `t=2p-q` is odd, so `r` is odd. Positivity excludes `r=1`, hence `r>=3` and again `c_3>=1`.

Section 1 proves `c_3=0` in both cases. Therefore no same-residue prime pair can attain a positive WI-088 ceiling.

For opposite nonzero residue classes, `t≡0 mod 3`, so `j=0`. WI-089's equality localization then forces the unique remainder `e=0`, which is precisely the appropriate member of (11). WI-087 proves the `delta_-` family has

\[
\operatorname{rank}G_{p,q}^{(\delta_-)}
=\frac{p+q}{3},
\qquad
\tau_{p,q}(\delta_-)
=\frac{2p-q-3}{3},
\tag{29}
\]

and WI-089 proves the same formula for the mirrored `delta_+` family. This establishes both necessity and sufficiency in (11).

The exceptional prime `3` creates no omitted positive-ceiling case: with `p=3<q<2p`, necessarily `q=5`, and the WI-088 ceiling is zero.

## 4. The fixed-N exact-ceiling graph is therefore a matching

WI-089 proved a stronger compatibility statement for the two canonical opposite-residue sharp families. At a common endpoint `ell`, a sharp edge with partner `m` satisfies

\[
3N\equiv\eta\,\varepsilon(\ell)m\pmod\ell,
\qquad
\eta\in\{+1,-1\},
\tag{30}
\]

where `epsilon(ell)=+1` for `ell≡1 mod 3` and `-1` for `ell≡2 mod 3`. Two distinct canonical sharp neighbors of one prime would force either an even larger partner or a partner divisible by `3`; hence those canonical edges form a matching.

WI-089 could not promote that statement to all exact-ceiling pairs because its necessary remainder window (there called (16)) still allowed same-residue candidates. Section 1 removes precisely that residual family. Therefore every positive exact-ceiling edge is canonical, and the existing matching theorem applies to the full graph. This proves (12).

This matters for any global assembly of pairwise Ramanujan rank losses. The sharp local obstruction from WI-087/WI-088 is genuine, but at a fixed observation length it cannot be placed repeatedly around the same modulus. A proof that upper-bounds a global signed-inertia defect by freely summing independent one-third pair losses is therefore structurally too pessimistic at the exact ceiling.

## 5. Falsification checks

The proof is exact and finite, but the two vulnerable transitions were also checked directly against the WI-088 partial map before persistence:

1. the reduction of the `A`-translation modulo `p` to `+2h` in the `1 mod 3` case and to `+h` in the `2 mod 3` case;
2. the claim that these reduced positive translations cannot cross the literal middle interval `C` of length `3h`.

An exact integer enumeration of all same-residue prime pairs `5<=p<q<2p<200`, all residual quotients `1<=k<=(p-1)/2`, and all exceptional-strip remainders `d<s<p` found no free 3-cycle. This is only a falsification check; equations (16)--(23), not the enumeration, carry the theorem.

A future generalization should not extrapolate (9) blindly to composite moduli. The proof uses the prime-row-kernel graph and WI-089's prime arithmetic classification of 3-cycles. Composite Ramanujan dimensions and noninvertible steps can change the cycle structure.

## 6. Prior art and novelty boundary

The ambient ingredients are classical or already persisted Mathia results.

- WI-081 supplies the nearest-LCM boundary factorization and exact prime residue-sum row-kernel equations.
- WI-086 identifies the residual prime rank defect after both primitive-frequency dimensions saturate.
- WI-087 supplies the first exact Loewner--Bezout one-third family.
- WI-088 proves the universal one-third ceiling by the forced-zero/partial-cycle graph.
- WI-089 proves that 3-cycles force the unique quotient `k=floor(p/3)`, derives the bounded equality remainder window, constructs the mirrored Loewner family, and proves the canonical fixed-`N` matching theorem.

The broader literature contains several nearby but different structures:

- Terence Tao, **An uncertainty principle for cyclic groups of prime order**, *Mathematical Research Letters* 12 (2005), 121--127, DOI `10.4310/MRL.2005.v12.n1.a11`, proves the sharp prime cyclic Fourier uncertainty principle and is equivalent to Chebotarev nonvanishing of all prime Fourier minors. That is an ambient full-Fourier statement, not a classification of the nearest-LCM finite-window partial-permutation cycles used here.
- P. P. Vaidyanathan and the Ramanujan-subspace literature recorded in `research/weil_inertia/SOURCES.md` give the classical primitive-period/Ramanujan spectral decomposition behind WI-080--WI-086. They do not supply the close-prime finite-window same-residue cycle exclusion.
- Ricardo Pachón, Pedro Gonnet and Joris van Deun, **Fast and Stable Rational Interpolation in Roots of Unity and Chebyshev Points**, *SIAM Journal on Numerical Analysis* 50 (2012), 1713--1734, DOI `10.1137/100797291`, is relevant roots-of-unity rational-interpolation prior art for the Loewner side of WI-087/WI-089, but the present deduction does not use a rational-interpolation rank theorem; it is a direct consequence of the exact WI-088 graph.
- Maria Loukaki, **Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle**, *Bulletin of the London Mathematical Society* (2025), DOI `10.1112/blms.70192`, gives recent composite-order Fourier-minor/uncertainty extensions under arithmetic hypotheses. Its object is again Fourier-minor nonsingularity rather than the finite-window boundary-cycle equality geometry here.

A targeted audit of these Fourier-minor, Ramanujan-subspace, roots-of-unity rational-interpolation, and recent `pq` uncertainty results did not locate a theorem that directly gives (9), the iff classification (11), or the full matching conclusion (12). **No priority claim is made.** The durable claim is only the exact deduction from the already-persisted WI-088/WI-089 graph and the explicit boundary families.

## 7. Research consequence

The residual prime-pair rank interface is now sharper than the one-third scalar ceiling alone suggests:

\[
\boxed{
\begin{array}{ll}
\text{same residue mod }3
&\Longrightarrow\text{ quarter-scale defect at worst},\\[1mm]
\text{opposite residues, generic boundary}
&\Longrightarrow\text{ below the exact one-third ceiling},\\[1mm]
\text{opposite residues, canonical boundary}
&\Longleftrightarrow\text{ exact positive one-third ceiling}.
\end{array}}
\tag{31}
\]

At fixed `N`, the last line is a matching. Hence the exact one-third local obstruction cannot be globally repeated with high vertex multiplicity.

This closes the cheapest remaining pairwise-rank refinement suggested by WI-089. A further global gain cannot come from merely improving the **existence** classification of exact one-third prime-pair rank defects: that classification is now explicit. The live information is quantitative near-ceiling stability, singular-value magnitude rather than rank alone, compatibility across three or more moduli, and the source weights/signs or factorization labels discarded by scalarization. Those are genuinely stronger interfaces than another worst-case pairwise rank count.
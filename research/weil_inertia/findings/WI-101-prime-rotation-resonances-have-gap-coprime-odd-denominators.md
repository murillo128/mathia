# WI-101 — Prime rotation resonances have gap-coprime odd denominators

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It strengthens the residual prime-pair classification of WI-095--WI-100: every true free-cycle resonance has denominator coprime to the prime gap `d=q-p`. Since distinct odd primes have even gap, every admissible cycle denominator is therefore **odd**. In particular the apparent one-quarter sector left by WI-089/WI-090 is empty: once the three-cycle resonance is unavailable, the next possible residual defect scale is one fifth, not one quarter.

Let `p<q<2p` be distinct odd primes, put

\[
d=q-p,
\qquad
t=2p-q=p-d,
\]

and work in the genuinely residual exceptional strip of WI-088,

\[
\delta=kq+s,
\qquad
\delta>q-1,
\qquad
d<s<p.
\tag{1}
\]

The partial map is

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B,
\end{cases}
\pmod p,
\tag{2}
\]

where

\[
A=\{0,\ldots,s-d-1\},
\quad
C=\{s-d,\ldots,s-1\},
\quad
B=\{s,\ldots,p-1\}.
\tag{3}
\]

WI-096 proves that if this graph has `c` free cycles then the exact residual row-rank defect is

\[
\tau=c-1
\tag{4}
\]

whenever `c>0`. WI-099 proves that all free cycles have one common length `ell`, one common number `a` of visits to `A`, and one common reduced resonance

\[
\ell k+a=mp,
\qquad
1\le a<\ell,
\qquad
1\le m<\frac\ell2,
\qquad
\gcd(m,\ell)=1.
\tag{5}
\]

The new conclusions are

\[
\boxed{
\gcd(d,\ell)=1
}
\tag{6}
\]

and an exact identification of the cyclic rotation speed on every free orbit. If

\[
h=\left\lfloor\frac{kd}{p}\right\rfloor,
\tag{7}
\]

then, after listing the `ell` vertices of one free cycle in ambient cyclic order, `g` advances by exactly

\[
\boxed{
 u=dm-\ell h
 =dm\pmod\ell,
\qquad
1\le u<\ell.
}
\tag{8}
\]

Here `dm mod ell` means its least positive residue. In particular

\[
\gcd(u,\ell)=1
\quad\Longrightarrow\quad
\boxed{
\gcd(dm,\ell)=1,
}
\tag{9}
\]

which gives (6) and independently recovers the coprimality of `m` and `ell`.

Because `d=q-p` is even,

\[
\boxed{
\ell\text{ is odd for every free cycle.}
}
\tag{10}
\]

Thus all even-denominator layers admitted by the coarse resonance set of WI-095 are spurious for the actual prime residual map.

## 1. A free cycle forbids a carry between the two translation branches

Set

\[
h_0=\left\lfloor\frac{kd}{p}\right\rfloor,
\qquad
h_1=\left\lfloor\frac{(k+1)d}{p}\right\rfloor.
\tag{11}
\]

Since `0<d<p`, one has `h_1-h_0 in {0,1}`. The first step is the exact no-carry statement

\[
\boxed{c>0\Longrightarrow h_1=h_0.}
\tag{12}
\]

Assume instead that `h_1=h_0+1`. Write

\[
kd=h_0p+r,
\qquad
0<r<p.
\tag{13}
\]

The carry assumption says `r+d>=p`. Put

\[
w=p-r.
\tag{14}
\]

Then `1<=w<=d`. Equality `w=d` would give

\[
(k+1)d=(h_0+1)p,
\]

which is impossible because `p` is prime, `0<d<p`, and the nearest-boundary range gives `1<k+1<p`. Hence

\[
1\le w<d.
\tag{15}
\]

Modulo `p`, the two branch translations now become

\[
kd\equiv-w,
\qquad
(k+1)d\equiv d-w.
\tag{16}
\]

For `j in B=[s,p-1]`, therefore,

\[
g(j)=j-w
\]

as an ordinary integer. Since `w<d<s`, this lies in `B union C`, never in `A`; while it remains in the domain it strictly decreases. For `j in A=[0,s-d-1]`, similarly,

\[
g(j)=j+d-w,
\]

which lies in `A union C`, never in `B`; while it remains in the domain it strictly increases.

A free cycle cannot meet `C`, because `C` is outside the domain. It also cannot stay forever in `A` under a strict ordinary increase, nor forever in `B` under a strict ordinary decrease. Thus no free cycle exists under the carry assumption, proving (12).

This is stronger than merely knowing the cycle-closure congruence of WI-095. Recurrence itself forces the two modular translations to use the same quotient by `p`.

## 2. Oriented arc length identifies the rotation speed

Assume now that a free cycle exists and put

\[
h=h_0=h_1,
\qquad
r=kd-hp.
\tag{17}
\]

Then the no-carry identity gives

\[
0<r<r+d<p.
\tag{18}
\]

Consequently the positive clockwise circular displacement of every `B` edge is exactly `r`, while that of every `A` edge is exactly `r+d`.

Take one free cycle `O` of length `ell`, and list its vertices in ambient cyclic order as

\[
y_0<y_1<\cdots<y_{\ell-1}<p.
\tag{19}
\]

WI-099 proves that the free recurrent restriction is cyclic-order preserving. Hence on this cycle there is a unique

\[
1\le u<\ell,
\qquad
\gcd(u,\ell)=1,
\tag{20}
\]

such that

\[
g(y_i)=y_{i+u\bmod\ell}.
\tag{21}
\]

For any `ell` points on a circle of circumference `p`, the sum of the positive clockwise distances from `y_i` to `y_{i+u}` is exactly `up`: each elementary cyclic gap between consecutive `y_i` is crossed by exactly `u` of these arcs. Therefore

\[
up
=a(r+d)+(\ell-a)r
=\ell r+ad.
\tag{22}
\]

Using (17) and the resonance identity (5),

\[
\begin{aligned}
up
&=\ell(kd-hp)+ad\\
&=d(\ell k+a)-\ell hp\\
&=(dm-\ell h)p.
\end{aligned}
\tag{23}
\]

Cancelling `p` proves the exact formula

\[
\boxed{u=dm-\ell h.}
\tag{24}
\]

Because `0<u<ell`, this also yields

\[
\boxed{
h=\left\lfloor\frac{dm}{\ell}\right\rfloor,}
\tag{25}
\]

so the spatial rotation speed is the least positive residue of `dm modulo ell`. Since a cycle of length `ell` requires `gcd(u,ell)=1`, equation (9) follows immediately.

## 3. The resonance hierarchy loses every even denominator

WI-095's necessary resonance condition was

\[
k=\left\lfloor\frac{mp}{\ell}\right\rfloor,
\qquad
3\le\ell,
\qquad
1\le m\le\left\lfloor\frac\ell2\right\rfloor,
\tag{26}
\]

and therefore retained all possible denominators as a safe outer approximation. WI-099 already sharpened the endpoint and reduction conditions. Equations (6)--(10) now give the strictly smaller admissible set

\[
\boxed{
\begin{gathered}
\ell\ge3\text{ odd},
\qquad
\gcd(\ell,d)=1,
\qquad
\gcd(m,\ell)=1,\\
1\le m<\frac\ell2,
\qquad
k=\left\lfloor\frac{mp}{\ell}\right\rfloor.
\end{gathered}}
\tag{27}
\]

For a cutoff `L`, define the gap-sensitive resonance set

\[
\mathcal K_L^*(p,d)
=
\left\{
\left\lfloor\frac{mp}{\ell}\right\rfloor:
3\le\ell\le L,
\ \ell\text{ odd},
\ \gcd(\ell,d)=\gcd(m,\ell)=1,
\ 1\le m<\frac\ell2
\right\}.
\tag{28}
\]

If `k` is outside this set, no free cycle of length at most `L` can occur. Combining WI-096's exact `tau=c-1` with WI-099's common cycle length and packing `c ell<=t` gives the corresponding defect ceiling. In particular, if `ell_min` is the smallest denominator allowed by (27) at the given `(p,d,k)`, then

\[
\boxed{
\tau
\le
\max\left\{0,
\left\lfloor\frac{t}{\ell_{\min}}\right\rfloor-1
\right\}.
}
\tag{29}
\]

This is an arithmetic refinement of WI-095's denominator hierarchy: denominator availability depends not only on the boundary quotient `k` but also on the prime gap itself.

## 4. The universal first drop is one fifth, not one quarter

The only possible length-three resonance has `m=1` and

\[
k=\left\lfloor\frac p3\right\rfloor.
\tag{30}
\]

Equation (6) adds the necessary condition

\[
3\nmid d.
\tag{31}
\]

Therefore, if either

\[
k\ne\left\lfloor\frac p3\right\rfloor
\qquad\text{or}\qquad
3\mid d,
\tag{32}
\]

then `ell` cannot equal three. Because every free-cycle length is odd, necessarily `ell>=5`. Hence

\[
\boxed{
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{2p-q}{5}\right\rfloor-1
\right\}.
}
\tag{33}
\]

This strictly sharpens two earlier safe bounds. WI-089 obtained a one-quarter ceiling when `k!=floor(p/3)` by excluding three-cycles but still allowing hypothetical four-cycles. WI-090 obtained the same one-quarter ceiling for same-residue primes modulo three. Those four-cycle sectors do not exist.

For primes `p,q>3`, same nonzero residue modulo three is equivalent to `3|d`, so (33) upgrades WI-090 directly:

\[
\boxed{
 p\equiv q\pmod3
 \Longrightarrow
 \tau_{p,q}(\delta)
 \le
 \max\left\{0,
 \left\lfloor\frac{2p-q}{5}\right\rfloor-1
 \right\}.
}
\tag{34}
\]

Conversely a three-cycle requires `3` to be coprime to `q-p`, which is exactly the opposite-nonzero-residue condition behind the sharp families of WI-087/WI-090. Thus their mod-three structure is not an isolated feature of the explicit Loewner--Bezout construction: it is the first instance of the general gap-coprimality law (6).

The same pruning iterates. For example, if the length-three layer is unavailable and `5|d`, then a five-cycle is impossible as well, so the next possible denominator is at least seven. More generally every prime factor of `d` deletes the corresponding denominator multiples from the residual resonance spectrum.

## 5. Falsification and prior-art audit

The proof above is exact and uses only the already-established WI-088/WI-096 partial-bijection model, WI-099's cyclic-order-preserving recurrent restriction, elementary floor arithmetic, and the circular-gap identity in (22). It does not use numerical rank tolerance, distribution of prime gaps, a random-matrix model, or any unproved Yang input.

As falsification, the exact finite map was exhaustively enumerated for all odd-prime pairs `p<q<2p` with `p<120`, all admissible residual `k,s` in the nearest-boundary range, and every free cycle encountered. More than one hundred thousand free cycles were checked. No even cycle occurred, every cycle satisfied `gcd(d,ell)=1`, and the directly measured cyclic rotation step agreed with (24) in every case. These computations are not used as proof.

The surrounding dynamical system is a finite, partially defined two-translation analogue of a double rotation / interval translation map. Suzuki, Ito and Aihara, **Double rotations**, *Discrete and Continuous Dynamical Systems* 13:2 (2005), 515--532, DOI `10.3934/dcds.2005.13.515`, is classical background for piecewise translations by two rotations on a circle. Recent interval-translation work such as Drach--Staresinic--van Strien, **Transversality for Interval Translation Maps**, arXiv:2605.00173 (2026), studies a much broader continuous parameter setting. Neither located source gives the finite prime-gap no-carry lemma, the rotation-speed identity (24), or the coprimality conclusion (6).

The Ramanujan/Fourier prior art already recorded in `SOURCES.md` remains the relevant algebraic background: Vaidyanathan's Ramanujan subspaces, Ushiroya's exact Ramanujan-sum matrix identities, Tao/Chebotarev prime Fourier full-spark results, and Loukaki's composite-order Fourier-minor work. A targeted search across these literatures and finite interval-translation dynamics did not locate the specific gap-coprime denominator theorem above. This negative search is **not** used as a claim of priority.

## 6. Program consequence

The residual prime pairwise defect problem now has a sharper arithmetic normal form. A true defect cycle is not merely a low-denominator resonance of the boundary phase: its denominator must be odd and coprime to the actual prime gap, and its internal spatial rotation is fixed exactly by

\[
\boxed{u\equiv(q-p)m\pmod\ell.}
\tag{35}
\]

Thus the one-quarter layer appearing in the earlier cycle-counting relaxations was pure proof slack. After the sharp one-third/three-cycle sector, the next possible macroscopic pairwise rank-defect scale is one fifth. More generally, gap factorization deletes whole rational resonance families before any metric or source-weighted estimate is applied.

This does not by itself close the Yang welding remainder: WI-094 already shows that extensive-defect edges are metrically weak, and WI-100 controls near-saturated resonance incidence, while the low-/zero-defect sector and simultaneous source-labelled cancellation remain live. The useful new constraint is that any future aggregation over residual prime resonances may sum only over the reduced odd, gap-coprime spectrum (27), rather than the larger Farey outer approximation of WI-095.
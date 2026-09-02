# WI-095 — Prime Ramanujan rank defect is quantized by low-denominator boundary resonances

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It strengthens the prime pairwise obstruction chain WI-088--WI-094 in a different direction: residual rank defect cannot occur on a generic boundary quotient. A defect of size `tau` forces the nearest-`pq` boundary onto a rational resonance whose denominator is at most the inverse defect density. Equivalently, away from all low-denominator resonant quotients the rank-defect ceiling drops from the one-third scale to an arbitrarily deep `1/(L+1)` cycle-counting scale.

Let `p<q` be distinct odd primes and let

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)}
\]

be the finite-window primitive-frequency cross Gram. Put `delta=delta_N(p,q)` for the distance from `N` to the nearest multiple of `pq`, and work in the genuinely residual regime

\[
\delta>q-1.
\tag{1}
\]

If the residual defect

\[
\tau=(p-1)-\operatorname{rank}G_{p,q}^{(N)}
\tag{2}
\]

is positive, WI-088 already forces `p<q<2p` and the exceptional strip. Write

\[
d=q-p,
\qquad
t=2p-q=p-d,
\qquad
\delta=kq+s,
\qquad d<s<p.
\tag{3}
\]

Then there exist integers

\[
3\le \ell\le\left\lfloor\frac{t}{\tau+1}\right\rfloor,
\qquad
1\le m\le\left\lfloor\frac\ell2\right\rfloor
\tag{4}
\]

such that the boundary quotient is **exactly**

\[
\boxed{
 k=\left\lfloor\frac{mp}{\ell}\right\rfloor.
}
\tag{5}
\]

If

\[
\alpha:=\frac{\delta}{pq},
\tag{6}
\]

then the same cycle gives the normalized resonance

\[
\boxed{
\left|\alpha-\frac m\ell\right|<\frac1p.
}
\tag{7}
\]

Thus a positive-density defect is confined to finitely many quotient layers. For every fixed `theta>0`,

\[
\tau\ge\theta p
\quad\Longrightarrow\quad
\ell<\frac1\theta,
\tag{8}
\]

so `k` belongs to a set of only `O_theta(1)` possibilities of the form (5), and `alpha` lies within `1/p` of a rational with denominator `<1/theta`.

More generally, for an integer `L>=3` define the resonant quotient set

\[
\mathcal K_L(p)
:=
\left\{
\left\lfloor\frac{mp}{\ell}\right\rfloor:
3\le\ell\le L,
\ 1\le m\le\left\lfloor\frac\ell2\right\rfloor
\right\}.
\tag{9}
\]

If

\[
 k\notin\mathcal K_L(p),
\tag{10}
\]

then every free cycle in the WI-088 partial-permutation model has length at least `L+1`, and therefore

\[
\boxed{
\tau
\le
\max\left\{0,
\left\lfloor\frac{2p-q}{L+1}\right\rfloor-1
\right\}.
}
\tag{11}
\]

Equivalently, with

\[
\mathcal R_L
:=
\left\{
\frac m\ell:
3\le\ell\le L,
\ 1\le m\le\left\lfloor\frac\ell2\right\rfloor
\right\},
\tag{12}
\]

the Diophantine nonresonance condition

\[
\operatorname{dist}(\alpha,\mathcal R_L)\ge\frac1p
\tag{13}
\]

implies the same bound (11).

This gives a full resonance hierarchy behind WI-089. The first allowed denominator is `3`, with the unique relevant fraction `1/3`; excluding that layer gives the `1/4` cycle-counting ceiling. Excluding all denominator-`<=4` resonances lowers the ceiling to the `1/5` scale, and so on. The sharp WI-087 family is the first resonance: `ell=3`, `m=1`, `k=floor(p/3)`, and `alpha->1/3`.

## 1. Every positive defect supplies many free cycles

WI-088's exact partial-bijection model has `c` free directed cycles and proves

\[
\tau\le\max\{0,c-1\}.
\tag{14}
\]

Therefore `tau>0` implies

\[
c\ge\tau+1.
\tag{15}
\]

All free cycles avoid the forced-zero set of size `d=q-p`, so together they use at most

\[
t=p-d=2p-q
\tag{16}
\]

vertices. Hence at least one free cycle has length

\[
\boxed{
\ell\le\frac{t}{c}
\le\frac{t}{\tau+1}.
}
\tag{17}
\]

WI-088 also proves that free cycles of lengths one and two do not exist, so `ell>=3`. Since `tau>0`, equation (15) gives `c>=2`, and therefore `ell<t<p`; this strict inequality will be used below.

## 2. Cycle closure forces an exact Beatty/Farey quotient

On the exceptional strip, the WI-088 partial map advances by `(k+1)d` on the `A` region and by `kd` on the `B` region, all modulo the prime `p`. Let a free cycle of length `ell` contain exactly `a` vertices in `A`. Going once around the cycle gives total translation

\[
(\ell k+a)d.
\tag{18}
\]

Because `d` is invertible modulo `p`, closure forces

\[
p\mid \ell k+a.
\tag{19}
\]

The endpoint values `a=0` and `a=ell` are impossible. If `a=0`, then `p|ell k`; if `a=ell`, then `p|ell(k+1)`. But `0<ell<p`, `1<=k<p`, and `1<k+1<p` in the residual boundary range, so primality of `p` rules out both cases. Hence

\[
1\le a\le\ell-1.
\tag{20}
\]

Write

\[
\ell k+a=mp
\tag{21}
\]

with `m>=1`. Equation (20) gives

\[
k<\frac{mp}{\ell}<k+1,
\]

and therefore

\[
\boxed{k=\left\lfloor\frac{mp}{\ell}\right\rfloor.}
\tag{22}
\]

The nearest-boundary convention gives `k<= (p-1)/2`. Since `ell<p`, equation (22) rules out `m/ell>1/2`: for odd prime `p`, that would force `floor(mp/ell)>(p-1)/2`. Thus

\[
1\le m\le\left\lfloor\frac\ell2\right\rfloor,
\tag{23}
\]

which proves (4)--(5).

This is the general form of the three-cycle arithmetic used in WI-089. For `ell=3`, (23) forces `m=1`, so (22) reduces exactly to

\[
k=\left\lfloor\frac p3\right\rfloor.
\]

For `ell=4`, the only additional quotient layers are `floor(p/4)` and `floor(p/2)`. Higher cycle lengths produce the corresponding finite Farey/Beatty hierarchy.

## 3. The same closure gives a normalized rational resonance

Using `delta=kq+s` and (21),

\[
\begin{aligned}
\alpha
&=\frac{k}{p}+\frac{s}{pq},\\
\frac m\ell
&=\frac{k}{p}+\frac{a}{\ell p}.
\end{aligned}
\tag{24}
\]

Therefore the difference is **exactly**

\[
\boxed{
\alpha-\frac m\ell
=
\frac1p\left(\frac{s}{q}-\frac a\ell\right).
}
\tag{25}
\]

The exceptional strip gives `0<s/q<1`, while (20) gives `0<a/ell<1`. Hence

\[
\left|\alpha-\frac m\ell\right|<\frac1p,
\]

proving (7).

This should not be read as a converse: proximity to one of the rationals in `R_L` does not create a free cycle or a rank defect. It is a necessary resonance condition extracted from an already-existing cycle.

For an extensive defect `tau>=theta p`, equation (17) and `t<p` give

\[
\ell<\frac1\theta.
\tag{26}
\]

Thus the number of possible quotient layers is bounded independently of `p`:

\[
\#\mathcal K_{\lceil1/\theta\rceil-1}(p)
\le
\sum_{3\le\ell<1/\theta}\left\lfloor\frac\ell2\right\rfloor
=O(\theta^{-2}).
\tag{27}
\]

Along any sequence with `tau/p -> theta>0`, passage to a subsequence therefore fixes one pair `(m,ell)`, and

\[
\alpha\longrightarrow\frac m\ell.
\tag{28}
\]

So macroscopic prime rank defect has a finite rational boundary-phase support rather than a continuum of possible limiting phases.

## 4. Nonresonance gives a tunable defect ceiling

Fix `L>=3`. Suppose `k` is not in `K_L(p)`. If a free cycle had length `ell<=L`, Sections 1--2 would produce integers `m` in the allowed range with

\[
k=\left\lfloor\frac{mp}{\ell}\right\rfloor,
\]

contradicting (10). Hence every free cycle has length at least `L+1`.

Since all free cycles together use at most `t=2p-q` vertices,

\[
c(L+1)\le t,
\qquad
c\le\left\lfloor\frac{t}{L+1}\right\rfloor.
\tag{29}
\]

Combining with (14) proves (11).

The normalized version (13) is the same contrapositive applied to (7): a cycle of any length `ell<=L` would put `alpha` at distance strictly less than `1/p` from the corresponding `m/ell` in `R_L`.

The hierarchy can be summarized as

\[
\boxed{
\text{defect above }\frac{t}{L+1}
\Longrightarrow
\text{a boundary resonance of denominator at most }L.
}
\tag{30}
\]

Up to the harmless integer `-1` from the mean-zero constraint, this turns defect density into inverse Diophantine denominator.

## 5. Relation to WI-089, WI-093 and WI-094

WI-089 identified the first resonance by proving that every free 3-cycle forces `k=floor(p/3)` and that near-one-third defect is confined to that layer. WI-095 shows that this is not an isolated mod-3 accident: **every** free cycle length gives an exact quotient `floor(mp/ell)`, and the shortest cycle forced by a defect of size `tau` bounds `ell` by `t/(tau+1)`. Thus WI-089 is the `L=3` member of a complete denominator hierarchy.

WI-093 converted extensive defect into a long boundary (`k>=tau+1`) and then into bounded canonical overlap. The proof of WI-093 already contained the closure congruence `p | ell k + a` for one shortest cycle, but used only the crude inequality `p<=ell(k+1)` to obtain `k>=tau+1`. Retaining the congruence instead of discarding it yields the exact resonance (5) and the normalized phase constraint (7).

WI-094 then showed that positive-density defect edges have vanishing cumulative Hilbert--Schmidt coherence on a dyadic prime scale. WI-095 is complementary rather than another metric estimate: even before Frobenius normalization, an extensive rank defect can occur only on `O_theta(1)` boundary quotient layers. Optimizing the residual prime **rank-defect size** over generic boundary phase is therefore doubly blocked: large defects are both metrically weak (WI-093--WI-094) and arithmetically resonant (this finding).

For the live Yang interface this remains a negative/structural result, not a completion theorem. Full-rank or vanishing-defect prime pairs, the scalar operator outside the residual-defect sector, exact source labels, the deterministic `W`-main/full-local-main splice, and the unsimplified locked four-prime covariance are not controlled here.

## 6. Prior art and novelty boundary

The general surrounding Fourier facts are classical or established. Chebotarev's theorem and Tao's finite-group uncertainty principle imply full-spark behavior for prime-order Fourier matrices; see Terence Tao, **An uncertainty principle for cyclic groups of prime order**, *Mathematical Research Letters* 12 (2005), 121--127, DOI `10.4310/MRL.2005.v12.n1.a11`. Recent work of Maria Loukaki, **Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle**, *Bulletin of the London Mathematical Society* (published 12 Sep 2025), DOI `10.1112/blms.70192`, proves nonsingularity for certain principal Fourier submatrices at composite order under additional arithmetic hypotheses. Ramanujan-subspace literature, beginning with P. P. Vaidyanathan, **Ramanujan sums in the context of signal processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, supplies the exact-period subspace framework.

Those results do not supply the specialized finite-window prime-pair statement above: the object here is the rectangular cross Gram between two primitive-frequency subspaces after nearest-`pq` boundary reduction, and the load-bearing input is WI-088's exact partial-permutation kernel model. The new derivation is the retention of the full cycle-closure congruence to obtain (5), (7), and the hierarchy (11). A targeted search over Fourier-minor/uncertainty, Ramanujan-subspace, finite-window Vandermonde, and roots-of-unity rank-defect literature did not locate this exact consequence. This is **not** used as a claim of priority.

The result is exact but one-way. Membership in `K_L(p)` or proximity to `R_L` is only necessary for a short free cycle; it is not sufficient for one, still less for a true row-kernel vector after all residue-sum equations are imposed. Any future use must preserve that asymmetry.

## 7. Program consequence

A proposed scalar escape based on accumulating large prime pairwise rank defects can no longer treat the nearest-boundary phase as a generic continuous parameter. If `tau/p` stays bounded below, the phase is forced onto finitely many low-denominator resonances, while WI-094 says the resulting extensive-defect sector still has vanishing cumulative Hilbert--Schmidt coherence. Conversely, away from the first `L` resonance layers, equation (11) lowers the maximum possible defect to the `1/(L+1)` scale.

The live possibility is therefore pushed toward the **low-/zero-defect sector and source-specific labelled cancellation**, not toward more elaborate exploitation of macroscopic pairwise rank loss. A further useful theorem would have to use the exact Yang coefficient law or simultaneous consistency of the low-denominator resonance layers; merely refining the universal pairwise defect ceiling cannot recover a macroscopic cancellation resource.
# RE-195 — Chebyshev-balanced padding makes reciprocal variation non-coercive

**Status:** `EXACT-DERIVED + ARBITRARY-RECIPROCAL-VARIATION + FIXED-EULER-JET-MATCHING + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-194-LOOPHOLE + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-182, RE-194.

`RE-194` converts Robin-scale absolute resolution into the relative scalar-Euler tolerance `d_p/V`, where

\[
d_p\asymp \frac1{\sqrt p\log p},
\qquad
V(c)=\sum_q\frac{|c_q|}{q}.
\]

That leaves a decisive source question: can an honest `{0,1,2}` prime control make `V/d_p` arbitrarily large while retaining the fixed Korobov--Vinogradov fidelity, the transient selector excursion, and exact scalar matching?

For every **fixed** Euler-jet depth, yes. In fact reciprocal variation can be inflated by an arbitrarily prescribed finite amount while the added packet itself is almost invisible to every fixed Euler observable.

Fix `K>=0`. For every sufficiently large selector prime scale `p` and every prescribed finite number `Lambda_p>0`, there is an ordinary-prime-supported source `Q=Q_{p,K,Lambda_p}` with

\[
\boxed{m_Q(q)\in\{0,1,2\}}
\tag{1}
\]

such that:

1. `Q` agrees with the ordinary prime source below `2p`, contains a canonical selector deletion packet in `[2p,3p]`, and has no repair below `16p`;
2. every right-boundary Euler jet through depth `K` matches exactly,
   \[
   \boxed{D_Q^{(j)}(1+)=0\qquad(0\le j\le K),}
   \tag{2}
   \]
   with absolute convergence of all these jet series;
3. for every fixed `b>0`,
   \[
   \boxed{
   |\vartheta_Q(x)-\vartheta(x)|
   \ll_{b,K}x\exp[-bV_{\rm KV}(x)],
   \qquad
   V_{\rm KV}(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}};
   }
   \tag{3}
   \]
4. the `RE-173` selector-normalized Robin coordinate still has an order-one transient at height `8p`;
5. nevertheless the reciprocal variation can be prescribed arbitrarily large:
   \[
   \boxed{
   \sum_q\frac{|m_Q(q)-1|}{q}\ge \Lambda_p.
   }
   \tag{4}
   \]

The inflation in (4) comes from a **finite** remote packet `G_p` starting at `X=p^2`. It can be chosen so that

\[
\boxed{
V(G_p):=\sum_{q\in G_p}\frac1q\ge\Lambda_p,
\qquad
\left|\sum_{\substack{q\in G_p\\q\le x}}c_q\log q\right|\le\log x,
}
\tag{5}
\]

with every `c_q` equal to `+1` or `-1`. Despite its arbitrarily large total variation, for every fixed `U>0`,

\[
\boxed{
\sup_{1\le s\le1+U}
\left|
\sum_{q\in G_p}c_q[-\log(1-q^{-s})]
\right|
\ll_U \frac1{p^2}
=o(d_p),
}
\tag{6}
\]

and for every fixed `j`, using the exact boundary kernels `J_j` of `RE-182`,

\[
\boxed{
\left|\sum_{q\in G_p}c_qJ_j(q)\right|
\ll_j\frac{(\log p)^j}{p^2}
=o_j(d_p).
}
\tag{7}
\]

Thus the variation factor in `RE-194` is **not coercive source complexity**. A bounded-multiplicity prime source can carry arbitrarily large reciprocal variation in a Chebyshev-balanced direction that is invisible at Robin scale to every fixed scalar Euler panel. The `log(V/d_p)` term in the `RE-194` stable-rank upper bound is a worst-case norm tariff; large `V` by itself does not certify additional source-visible dimensions.

## 1. Split the ordinary primes into a repair channel and a padding channel

Write the ordinary primes increasingly as

\[
p_1<p_2<p_3<\cdots
\]

and split them by index parity:

\[
\mathcal P_{\rm odd}=\{p_1,p_3,p_5,\ldots\},
\qquad
\mathcal P_{\rm even}=\{p_2,p_4,p_6,\ldots\}.
\tag{8}
\]

Two elementary facts make this split useful.

First, every interval containing `N` consecutive ordinary primes contains `N/2+O(1)` primes of each parity. Hence every PNT-dense shell used in `RE-182` retains a fixed positive fraction of its available prime count and `H`-mass after restricting the repair construction to `P_even`. All shell-availability estimates therefore survive with only constants changed.

Second, the reciprocal series on `P_odd` still diverges. Pairing consecutive primes gives

\[
\frac1{p_{2n-1}}
\ge
\frac12\left(\frac1{p_{2n-1}}+\frac1{p_{2n}}\right),
\tag{9}
\]

so Euler's divergence of the reciprocal-prime series implies

\[
\boxed{
\sum_{q\in\mathcal P_{\rm odd}}\frac1q=\infty.
}
\tag{10}
\]

We may therefore reserve `P_even` for exact interpolation/quantization and use `P_odd` to inject as much reciprocal variation as desired, with disjoint supports.

## 2. Greedy sign balancing hides arbitrary reciprocal variation from Chebyshev mass

Set

\[
X:=p^2.
\tag{11}
\]

By (10), choose a finite `Y>X` such that

\[
\sum_{\substack{X\le q\le Y\\q\in\mathcal P_{\rm odd}}}\frac1q
\ge\Lambda_p.
\tag{12}
\]

Enumerate those odd-index primes increasingly as

\[
q_1<q_2<\cdots<q_N.
\]

Define signs greedily. Start from `S_0=0`; having chosen through `q_{n-1}`, put

\[
c_{q_n}=
\begin{cases}
-1,&S_{n-1}\ge0,\\
+1,&S_{n-1}<0,
\end{cases}
\qquad
S_n:=S_{n-1}+c_{q_n}\log q_n.
\tag{13}
\]

Then

\[
\boxed{|S_n|\le\log q_n\quad\text{for every }n.}
\tag{14}
\]

Indeed, if `|S_{n-1}|<=log q_{n-1}<=log q_n`, the new sign points against `S_{n-1}`, so

\[
|S_n|
=\bigl|\log q_n-|S_{n-1}|\bigr|
\le\log q_n.
\]

Consequently the padding Chebyshev primitive

\[
A_G(t):=\sum_{\substack{q\in G_p\\q\le t}}c_q\log q
\tag{15}
\]

satisfies

\[
\boxed{|A_G(t)|\le\log t}
\tag{16}
\]

throughout its support, and after the final padding prime it remains bounded by `log Y<=log t`. At the same time its reciprocal **total variation** is the unsigned sum in (12), hence at least `Lambda_p`.

This is the central separation: the current KV source fidelity sees the signed Chebyshev primitive, while `V` counts unsigned reciprocal mass. Rapid sign balancing can make the former tiny while the latter is arbitrarily large.

## 3. Abel summation makes the padding uniformly Euler-small

The separation is not limited to the Chebyshev coordinate. Let

\[
F_G(s):=\sum_{q\in G_p}c_qq^{-s},
\qquad 1\le s\le1+U.
\]

Since `c_q q^{-s}=(c_q\log q)f_s(q)` with

\[
f_s(t):=\frac{t^{-s}}{\log t},
\]

Abel summation and (16) give

\[
F_G(s)
=A_G(Y)f_s(Y)-\int_X^Y A_G(t)f_s'(t)\,dt.
\tag{17}
\]

Now

\[
|f_s'(t)|
=t^{-s-1}
\left(\frac{s}{\log t}+\frac1{(\log t)^2}\right),
\]

so uniformly for `1<=s<=1+U`,

\[
\boxed{|F_G(s)|\ll_U X^{-1}.}
\tag{18}
\]

The exact Euler factor differs from its first harmonic by an absolutely convergent prime-power remainder:

\[
0\le
-\log(1-q^{-s})-q^{-s}
\ll q^{-2s}.
\]

Therefore

\[
\sum_{q\in G_p}
\left|-\log(1-q^{-s})-q^{-s}\right|
\ll
\sum_{n\ge X}n^{-2}
\ll X^{-1},
\tag{19}
\]

which proves (6).

The same argument works for every fixed boundary derivative. For `j>=1`, the first harmonic of the exact `RE-182` kernel is

\[
J_j(q)=(-\log q)^jq^{-1}
+O_j\!\left(\frac{(\log q)^j}{q^2}\right).
\tag{20}
\]

Apply Abel summation to

\[
\sum_{q\in G_p}c_q\frac{(\log q)^j}{q}
=
\sum_{q\in G_p}(c_q\log q)
\frac{(\log q)^{j-1}}q.
\]

For fixed `j`, the derivative of `(log t)^(j-1)/t`, multiplied by the bound `|A_G(t)|<=log t`, is `O_j((log t)^j/t^2)`. Hence

\[
\left|
\sum_{q\in G_p}c_q\frac{(\log q)^j}{q}
\right|
\ll_j\frac{(\log X)^j}{X}.
\tag{21}
\]

The prime-power remainder in (20) has the same bound after absolute summation. With `X=p^2`, (7) follows. Since

\[
d_p\asymp\frac1{\sqrt p\log p},
\]

all fixed padding jets are `o_K(d_p)` independently of how large `Lambda_p` is or how far `Y` must be taken.

## 4. Exact fixed-depth matching survives the arbitrary padding

It remains to show that the large-variation packet can coexist with the exact constraints, rather than only approximate them.

Run the `RE-182` construction with two changes.

First, choose the canonical selector deletion set `D_p subset [2p,3p]` entirely from `P_even`. This is possible because PNT gives `gg p/log p` primes in that interval, while the selector needs only

\[
N_p\asymp\frac{\sqrt p}{\log p}.
\tag{22}
\]

Second, perform every interpolation/quantization repair step using only `P_even`. If a narrow repair shell contains `N` ordinary primes, it contains `N/2+O(1)` even-index primes. Since all primes in one such shell have comparable `H(q)`, the available `H`-mass remains a fixed positive fraction of that used in `RE-182`. The Vandermonde response matrix, the one-prime quantization scale, and the geometric contraction are unchanged apart from constants depending on `K`.

The only change to the initial exact-matching target is the centered residual contributed by `G_p`. At the first repair baseline `x_0=16p`, the centered kernels of `RE-182` are triangular combinations of the raw jets with coefficients polynomial in `log p`. Equations (7) and `X=p^2` therefore give, for every `m<=K`,

\[
\boxed{
\left|
\sum_{q\in G_p}c_qC_{m,\log(16p)}(q)
\right|
\ll_K\frac{(\log p)^m}{p^2}
=o_K(d_p).
}
\tag{23}
\]

Thus the selector residual of size `asymp_K d_p` still dominates the first generation. Every conditioning, sign, availability, and contraction estimate in `RE-182` survives. The infinite even-prime repair consequently drives the combined selector-plus-padding residual to zero **exactly**, yielding (2) with absolute convergence.

Because the repair support is even-indexed and the padding support odd-indexed, no prime is modified twice. Every final multiplicity therefore remains in `{0,1,2}`. The repair's total reciprocal variation is finite by the absolute `H`-mass summability already proved in `RE-182`, while the disjoint padding contributes at least `Lambda_p`; hence (4).

The Chebyshev accounting also survives. `RE-182` gives

\[
|\Delta\vartheta_{\rm repair}(x)|
\ll_K \sqrt p\log p+(\log x)^3,
\tag{24}
\]

and (16) contributes only `O(log x)`. This proves the same KV conclusion (3). Finally, the selector packet lies in `[2p,3p]`, the first repair still begins at `16p`, and the padding begins only at `p^2`; therefore the order-one measurement at `8p` is untouched.

## Representation audit

`RE-194` uses the total-variation norm because it gives a clean operator bound

\[
|D_c(1)|\le V_H(c)\asymp V(c).
\]

The new construction shows why that representation is one-sided. For signed bounded-multiplicity sources, the Euler channel also factors through the Chebyshev primitive by Abel summation. A source can therefore have enormous unsigned `ell^1` mass while its primitive stays logarithmic and its entire fixed Euler profile stays `O(1/X)`.

So there are two genuinely different quantities:

\[
\text{unsigned reciprocal variation }V
\qquad\text{versus}\qquad
\text{source-visible signed primitive / transform response}.
\]

The first controls a worst-case Lipschitz estimate; it does **not** lower-bound the second. Any future scalar complexity invariant must quotient out, or otherwise price, these balanced directions. Merely proving an upper bound on `V` would be sufficient, but the current KV envelope and every fixed exact Euler-jet panel do not provide such an upper bound.

## Adversarial self-review

**Does this contradict `RE-194`?** No. Its norm conversion remains a valid worst-case upper-bound mechanism. What fails is the converse interpretation that large `V` is itself evidence of many usable scalar coordinates. Here `V` can be inflated without producing a Robin-scale response in any fixed Euler observable.

**Is exact matching really preserved?** Yes for every fixed boundary depth `K`, by rerunning the exact `RE-182` quantizer on the disjoint even-index prime channel with the padding residual included in its target. The padding is finite, and the repair jet series retain the absolute convergence proved in `RE-182`.

**Does the parity split secretly destroy prime availability?** No. In any interval containing many consecutive primes, the two global index parities differ in count by at most one. Every PNT-dense shell in `RE-182` therefore retains half of its primes up to `O(1)`, and all shell weights are comparable.

**Can `Lambda_p` grow arbitrarily fast?** For each fixed `p`, yes, as any prescribed finite value: the odd-index reciprocal-prime series diverges, so a finite terminal `Y` exists. No useful upper bound on that `Y` is claimed. Large variation may require a very wide source support; the finding isolates non-coercivity, not an optimal variation-versus-diameter law.

**Does the result cover growing jet depth?** No. `K` is fixed before `p` tends to infinity. The constants in the `RE-182` interpolation and in (7), (23) may depend on `K`. The growing-depth regimes of `RE-184`--`RE-188` remain separate.

**Does it preserve exact matching of a continuum or an expanding temperature panel?** No such claim is made. It preserves every prescribed fixed finite boundary-jet panel. A genuinely growing or nonlocal family of exact constraints could still make variation coercive.

**Is the padding itself an actual Robin counterexample?** No. It is a matched-control falsification device. Its role is to test which source information can distinguish the ordinary source from bounded-multiplicity controls while the canonical selector excursion is kept alive.

## Prior-art audit

The generic ingredients are classical. Divergence of the reciprocal-prime series goes back to Euler; one-dimensional greedy sign balancing is elementary discrepancy control; Abel/partial summation is standard. Targeted searches also surface the literature on greedy signed harmonic sums and on Steinitz-type partial-sum balancing, but no external theorem from that literature is needed here and no novelty is claimed for those mechanisms.

The line-specific content is the splice: use a disjoint ordinary-prime channel to create arbitrarily large reciprocal variation with logarithmic Chebyshev primitive, prove that the exact Euler response of that padding is `o(d_p)`, and then absorb its fixed-dimensional residual inside the existing exact `{0,1,2}` `RE-182` repair without losing KV fidelity or the transient Robin excursion. No new load-bearing literature dependency is introduced, so `SOURCES.md` is unchanged.

## What this changes

The immediate variation-cap route left by `RE-194` fails for the current source package. **KV fidelity plus honest bounded multiplicity plus any fixed exact Euler-jet depth does not cap reciprocal variation at all.** In fact `V/d_p` can exceed any prescribed finite scale while the added variation remains below Robin resolution in every fixed scalar Euler observable.

The next scalar question therefore cannot be merely whether `V` grows. It must ask whether a **growing or nonlocal exact observable family** forbids these Chebyshev-balanced null directions, or whether one can replace raw total variation by an effective quotient norm that measures source-visible response rather than unsigned mass. A direct combinatorial restriction on how often multiplicities may alternate would also kill the present padding, but that information is not contained in the current KV envelope.

## Sources

- `RE-173`, canonical selector packet, exact Mertens/KV control, and transient Robin normalization.
- `RE-182`, exact fixed-depth Euler-jet repair on ordinary primes with multiplicities `{0,1,2}`.
- `RE-194`, Robin-scale precision conversion and the reciprocal-variation loophole tested here.

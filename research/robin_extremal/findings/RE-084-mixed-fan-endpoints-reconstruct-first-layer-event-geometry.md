# RE-084 — mixed-fan endpoints reconstruct the entire first-layer event geometry

**Status:** `EXACT-DERIVED + UNIFORM-ASYMPTOTIC + NEGATIVE/OBSTRUCTION + MIXED-FAN + FIRST-LAYER-GEOMETRY + PRIME-GAP-REDUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-083` proves an exact first-layer support-set identity on an arbitrary mixed fan segment, and leaves nonlinear event placement among the possible places where genuine CA assembly could still differ from endpoint prime bookkeeping. For the **first layer by itself**, however, there is no further hidden timing degree of freedom. Once the endpoint selector prime set and the two possible fringe primes are known, the complete labeled first-layer event configuration is determined exactly; sufficiently late, that configuration is uniformly a translated copy of the ordinary prime configuration by one half-unit, up to `O(1/log Z_0)`.

Assume RH is false, fix the compact threshold interval and a sufficiently late common positive CA block as in `RE-040`, and take two ordered selected fan states

\[
C_0<C_1,
\qquad
Z_0<Z_1.
\tag{1}
\]

Use the endpoint fringe notation of `RE-083`,

\[
\delta_\vartheta(Z_i)=\chi_i\log r_i,
\qquad \chi_i\in\{0,1\},
\tag{2}
\]

and let

\[
\mathcal S_{01}:=\{q\text{ prime}:Z_0<q\le Z_1\},
\qquad
\mathcal B_{01}:=\{p:p\nmid C_0,\ p\mid C_1\}
\tag{3}
\]

be respectively the selector primes and the first-layer births. `RE-083` gives the exact multiset identity

\[
\boxed{
\mathcal S_{01}\uplus\chi_0\{r_0\}
=
\mathcal B_{01}\uplus\chi_1\{r_1\}.
}
\tag{4}
\]

For each prime `p`, let `eta_p=eta_(p,1)` be its first-layer CA event and put

\[
d_p:=\eta_p-p.
\tag{5}
\]

The threshold equation fixes `eta_p` uniquely as a function of `p`. Therefore (4) reconstructs not only every additive statistic of the births but the **entire ordered first-layer event set**

\[
\boxed{
\mathcal E^{(1)}_{01}
:=\{(p,\eta_p):p\in\mathcal B_{01}\}
}
\tag{6}
\]

from the endpoint selector data. By `RE-004`, first-layer event order is exactly prime order, so no additional permutation data remain.

Moreover `RE-042`/`RE-069` give

\[
\boxed{
d_p
=\frac12-\frac1{2(\log p+1)}+O(p^{-1}).}
\tag{7}
\]

Every birth in (3) satisfies `p>Z_0` except possibly the lower fringe birth `r_0`; in that case `Z_0<eta_(r_0)<r_0+1/2`, hence `r_0>Z_0-1/2`. Consequently

\[
\boxed{
\sup_{p\in\mathcal B_{01}}
\left|\eta_p-\left(p+\frac12\right)\right|
\ll \frac1{\log Z_0}.
}
\tag{8}
\]

Thus the complete first-layer timeline on every sufficiently late mixed fan segment is uniformly `O(1/log Z_0)` from the ordinary-prime timeline translated by `1/2`. In particular, for any two births `p<q`,

\[
\boxed{
\eta_q-\eta_p
=(q-p)+O\!\left(\frac1{\log Z_0}\right).
}
\tag{9}
\]

If a genuine physical CA chamber has two nonexceptional first-layer boundaries, then its labels are consecutive ordinary primes by `RE-004`, and its physical width is therefore the corresponding ordinary prime gap plus `o(1)`. The first-layer CA staggering does not create a new asymptotic chamber metric beyond prime-gap geometry.

There is also a uniform nonlinear timing statement. For every fixed Lipschitz function `F` on `[0,1]` and arbitrary real weights `w(p)`, (8) gives

\[
\boxed{
\left|
\sum_{p\in\mathcal B_{01}}w(p)
\left(F(d_p)-F(1/2)\right)
\right|
\ll_F
\frac1{\log Z_0}
\sum_{p\in\mathcal B_{01}}|w(p)|.
}
\tag{10}
\]

Taking `w(p)=log p` and

\[
R_{01}:=\sum_{p\in\mathcal B_{01}}\log p
=\log\operatorname{rad}(C_1)-\log\operatorname{rad}(C_0),
\tag{11}
\]

we obtain, whenever `R_01>0`,

\[
\boxed{
\frac1{R_{01}}
\sum_{p\in\mathcal B_{01}}(\log p)F(d_p)
=F(1/2)+O_F\!\left(\frac1{\log Z_0}\right).
}
\tag{12}
\]

Equivalently, the radical-mass-weighted delay distribution collapses to the point mass at `1/2`. For every fixed integer `k>=1`,

\[
\boxed{
\sum_{p\in\mathcal B_{01}}
(\log p)(\eta_p-p)^k
=
2^{-k}R_{01}
+O_k\!\left(\frac{R_{01}}{\log Z_0}\right).
}
\tag{13}
\]

On the stretched same-block branch of `RE-080`, `RE-083` gives `R_01=(1+o(1))Y_1`; hence all fixed one-point timing moments have the universal leading values `2^{-k}Y_1`. The `k=1` case is the complete-pulse counterpart of the half-mass flat timing law in `RE-083`; (12)--(13) show that passing to nonlinear functions of the individual first-layer delays does not recover an independent arithmetic channel.

## 1. Endpoint support conservation reconstructs the first-layer timeline exactly

Equation (4) determines `B_01` as a finite prime multiset once the two selector endpoints and fringe states are fixed. This is stronger than knowing only its log-mass. The map

\[
p\longmapsto \eta_p
\tag{14}
\]

is fixed by the exact first-layer threshold equation

\[
\frac1{\eta_p\log\eta_p}
=
\frac{\log(1+p^{-1})}{\log p},
\tag{15}
\]

so applying (14) to the reconstructed prime set gives (6) with no approximation and no knowledge of the intervening higher-layer events.

The ordering also carries no extra first-layer datum. `RE-004` proves that if `p<q` are distinct primes, then `eta_p<eta_q`. Thus every nonlinear functional that depends only on the labeled first-layer point configuration is, in principle, already a functional of the endpoint selector prime set plus the two fringe bits. Such a functional may still exploit genuinely difficult ordinary-prime information, but it is not extracting additional information from the CA first-layer timing mechanism itself.

This statement does **not** reconstruct mixed support chambers from first-layer data alone. A higher-layer threshold may lie between two first-layer events, tie one of them, change the exponent vector, or become an adjacent supporting boundary. Those cross-layer incidences are not erased by (4).

## 2. The first-layer event map is uniformly a half-translation

The expansion (7) was derived in `RE-042` from (15). It implies, for all sufficiently large primes,

\[
\left|d_p-\frac12\right|
\ll \frac1{\log p}.
\tag{16}
\]

It remains only to make the lower scale uniform over an arbitrary mixed segment. If `p` is an ordinary selector prime in `S_01`, then `p>Z_0`. If `p` is a birth not in `S_01`, the exact multiset identity (4) shows that it can only be the lower fringe prime `r_0`. For that prime the fringe definition gives

\[
r_0\le Z_0<\eta_{r_0},
\tag{17}
\]

while the late first-layer bound `eta_p<p+1/2` gives

\[
r_0>Z_0-\frac12.
\tag{18}
\]

Hence every `p in B_01` satisfies `p>Z_0-1/2`. Substituting this into (16) proves (8). Subtracting the estimates for `p` and `q` gives (9).

There is a useful chamber corollary. Suppose two adjacent distinct physical CA transition coordinates bracketing one state are both nonexceptional first-layer events `eta_p<eta_q`. No ordinary prime can lie strictly between `p` and `q`, because its first-layer event would then lie strictly between the two physical boundaries. Thus `p,q` are consecutive primes and

\[
\eta_q-\eta_p
=(q-p)+O(1/\log p).
\tag{19}
\]

So pure first-layer support chambers are asymptotically ordinary prime-gap chambers, with the common half-shift cancelling from their width.

## 3. All fixed nonlinear one-point delay statistics have the same universal limit

Let `F` be Lipschitz with constant `L_F`. Equation (8) gives termwise

\[
|F(d_p)-F(1/2)|
\le
L_F|d_p-1/2|
\ll_F\frac1{\log Z_0}.
\tag{20}
\]

Multiplying by `|w(p)|` and summing proves (10). For the positive weights `w(p)=log p`, division by `R_01` proves (12). Taking `F(u)=u^k` on `[0,1]` gives (13).

This is stronger than the linear flat-area calculation only in the information-theoretic sense relevant to the current frontier: replacing the first moment by finitely many higher moments, a bounded nonlinear transform, or any other fixed Lipschitz one-prime statistic does not expose a new late timing distribution. All of them see the same point mass at the universal half-delay.

The exact statement is stronger still at the level of data ownership: because (6) is reconstructed from the endpoints, even an arbitrarily nonlinear first-layer-only functional is endpoint-determined. The Lipschitz limit (12) is useful because it identifies what its late metric geometry degenerates to without assuming a particular functional.

## 4. Consequence for the live Robin-extremal frontier

`RE-082` shows that smooth selector dilation alone can realize the required long-fan power front. `RE-083` then eliminates endpoint additive first-layer mismatch and the direct linear Robin timing tax. The present result closes one nearby escape: **making the one-prime first-layer timing functional nonlinear does not restore missing assembly information.** The first-layer event labels, order, positions, relative spans, and fixed nonlinear delay statistics are already determined by the endpoint ordinary-prime set; metrically they become the prime configuration translated by `1/2`.

What remains is necessarily joint. A viable discrete obstruction must use, for example, the relative placement of first-layer and higher-layer thresholds, the way those mixed thresholds alter adjacent supporting slopes and exposed threshold cells, or a state/barrier condition coupling event positions to which CA states the fan is allowed to select. Ordinary prime-gap information can also remain decisive, but then the mechanism is explicitly a prime-distribution restriction on the endpoint prime configuration rather than an unexplained first-layer CA timing effect.

This distinction matters for future tests: a candidate that can be written solely as a functional of `\{(p,eta_p):p in B_01\}` should first be reduced through (4)--(8). Unless it uses new prime-distribution input, it cannot distinguish two mixed fan assemblies having the same selected endpoints.

## 5. Falsification and prior-art boundary

Several stronger statements would be false and are not claimed.

- Zero density of higher-layer events does not make cross-layer interleaving harmless. A sparse higher-layer threshold can still become an adjacent physical boundary or alter the selected exponent vector.
- The result does not make ordinary prime gaps regular. Equation (19) transfers their irregularity almost unchanged to pure first-layer CA chambers.
- A functional whose sensitivity grows with `Z_0` can amplify the `O(1/log Z_0)` correction in (8). That correction is nevertheless a deterministic function of the prime label through (15), so amplification does not create independent first-layer assembly data.
- Equations (12)--(13) concern complete first-layer births. Truncating delay pulses at the two selector endpoints reintroduces the at-most-two fringe corrections quantified in `RE-083`.

The classical CA threshold map itself belongs to Alaoglu--Erdos, and the prime-layer event/workload framework is close to Mantovanelli's 2026 preprint already anchored in `SOURCES.md`; no novelty is claimed for those ingredients. A directed prior-art search found no source asserting the mixed-fan endpoint reconstruction (4)--(6) together with the uniform half-translation and nonlinear delay collapse (8)--(13). No external theorem beyond the sources already anchored for this line is load-bearing here, so `SOURCES.md` needs no new entry.

The durable narrowing is therefore specific: **first-layer timing geometry by itself is exhausted once endpoint prime support is known. The unresolved arithmetic assembly lives in cross-layer/state-selection coupling, not in a hidden nonlinear statistic of the first-layer delay.**

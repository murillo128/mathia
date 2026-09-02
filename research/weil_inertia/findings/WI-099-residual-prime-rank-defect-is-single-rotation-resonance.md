# WI-099 — Residual prime Ramanujan rank defect is supported on a single rotation resonance

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens WI-095--WI-096 by removing a hidden mixture that those findings still allowed: for one residual close-prime Ramanujan pair, different free cycles cannot live on different rational resonance denominators. The exact partial map is cyclic-order preserving on its recurrent set, so all free cycles have one common length, one common arithmetic rotation ratio, and one common `A/B` population. Thus every nonzero pairwise rank defect is phase-pure rather than a superposition of several Farey layers.

Let `p<q<2p` be distinct odd primes, put

\[
d=q-p,
\]

and let `delta=delta_N(p,q)` be the nearest-`pq` boundary length. Work in the genuinely residual exceptional strip of WI-088/WI-096,

\[
\boxed{
\delta=kq+s,
\qquad
\delta>q-1,
\qquad
d<s<p.
}
\tag{1}
\]

Use

\[
A=\{0,\ldots,s-d-1\},
\qquad
C=\{s-d,\ldots,s-1\},
\qquad
B=\{s,\ldots,p-1\},
\tag{2}
\]

with `D=A union B`, the forced-zero set

\[
Z=kd+\{0,1,\ldots,d-1\}\pmod p,
\tag{3}
\]

and the WI-088 partial bijection

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B
\end{cases}
\pmod p.
\tag{4}
\]

Let `F` be the union of the free directed cycles of `g`, and let `c` be their number. If `c>0`, then there exist integers `ell>=3` and `m>=1` such that:

\[
\boxed{\text{every free cycle has exactly }\ell\text{ vertices},}
\tag{5}
\]

\[
\boxed{
\gcd(m,\ell)=1,
\qquad
k=\left\lfloor\frac{mp}{\ell}\right\rfloor,
\qquad
0<\frac m\ell<\frac12,
}
\tag{6}
\]

and every free cycle contains the same number

\[
\boxed{a=mp-\ell k}
\tag{7}
\]

of vertices in `A`. In particular `1<=a<=ell-1` and the rational `m/ell` is the **same reduced resonance for every free cycle**.

WI-096 gives the exact row-rank defect

\[
\tau_{p,q}(\delta)=\max\{0,c-1\}.
\tag{8}
\]

Consequently, whenever `tau>0`,

\[
\boxed{
(\tau+1)\ell=|F|\le 2p-q,
\qquad
\ell\le
\left\lfloor\frac{2p-q}{\tau+1}\right\rfloor.
}
\tag{9}
\]

Thus the low-denominator resonance supplied existentially by WI-095 is actually global across the whole pairwise defect space. If `tau>=theta p`, then necessarily

\[
\boxed{\ell<\frac1\theta,}
\tag{10}
\]

and **all** free-cycle degrees of freedom belong to that one denominator, not merely one shortest witness cycle.

## 1. The partial map is an exact cyclic-order identification of two punctured arcs

The key observation is already latent in WI-088's image calculation but was not used there dynamically. Set

\[
t=p-d=2p-q,
\qquad
a_0=s-d.
\tag{11}
\]

Parameterize the domain `D` by the `t`-point cyclic set `0,...,t-1` via

\[
\iota_D(x)=
\begin{cases}
x,&0\le x<a_0,\\
x+d,&a_0\le x<t.
\end{cases}
\tag{12}
\]

This simply lists `A`, skips the deleted interval `C`, and then lists `B`. It therefore preserves the ambient cyclic order on `Z/pZ`.

WI-088 proves

\[
g(D)=(\mathbf Z/p\mathbf Z)\setminus Z.
\]

Parameterize that codomain by

\[
\iota_E(x)=kd+d+x\pmod p,
\qquad 0\le x<t.
\tag{13}
\]

which lists the consecutive cyclic arc complementary to `Z`. Direct substitution into (4) gives, on both pieces of (12),

\[
\boxed{
g(\iota_D(x))=\iota_E(x).}
\tag{14}
\]

Indeed, for `x<a_0` the left side is `x+(k+1)d`, while for `x>=a_0` one has `iota_D(x)=x+d` and the left side is `x+d+kd`; both equal (13).

Both `iota_D` and `iota_E` preserve cyclic order. Hence

\[
\boxed{g:D\longrightarrow (\mathbf Z/p\mathbf Z)\setminus Z
\text{ preserves cyclic order}.}
\tag{15}
\]

This is stronger structural information than the bare partial-bijection property used in WI-088--WI-096.

## 2. The recurrent restriction is a finite rotation, so every cycle has the same length

Every vertex of a free cycle lies in `D`, and because it also has a predecessor on the same cycle it lies in the image of `g`, hence in the complement of `Z`. Therefore

\[
F\subseteq D\cap((\mathbf Z/p\mathbf Z)\setminus Z),
\qquad
g(F)=F.
\tag{16}
\]

By (15), the restriction

\[
g_F:F\to F
\]

is an orientation-preserving permutation of a finite cyclically ordered set.

Label the `M=|F|` points in ambient cyclic order as

\[
x_0,x_1,\ldots,x_{M-1}.
\]

Once `g_F(x_0)=x_r` is fixed, preservation of cyclic order forces

\[
\boxed{g_F(x_i)=x_{i+r}\qquad(\bmod M)}
\tag{17}
\]

for every `i`. Thus `g_F` is literally a finite rotation. Its number of cycles and their common length are

\[
c=\gcd(M,r),
\qquad
\boxed{\ell=\frac{M}{c}.}
\tag{18}
\]

In particular all free cycles have the same length, proving (5). More precisely, writing `r=cu` gives `gcd(u,ell)=1`, and the free cycles are exactly the congruence classes of the cyclic index modulo `c`. They are therefore perfectly interlaced in the cyclic ordering of `F`.

The finite statement used here is the discrete form of the classical Poincare rotation-number principle that an orientation-preserving circle homeomorphism has a single rotation number and all of its periodic orbits have the same period when that rotation number is rational. See, for example, Boris Hasselblatt and Anatole Katok, *A First Course in Dynamics*, Cambridge University Press (2003), Proposition 4.3.8. The load-bearing point specific to the present Ramanujan problem is not that classical theorem but the exact arc factorization (12)--(15), which turns the WI-088 partial map into a cyclic-order automorphism on its recurrent set.

## 3. Equal cycle length forces one arithmetic resonance

Take any free cycle `C`. Let

\[
a_C:=|C\cap A|.
\tag{19}
\]

Every step contributes `kd` plus one additional `d` exactly when its source lies in `A`. Going once around a cycle of the common length `ell` therefore gives

\[
d(\ell k+a_C)\equiv0\pmod p.
\tag{20}
\]

Since `0<d<p` and `p` is prime,

\[
p\mid \ell k+a_C.
\tag{21}
\]

Also `ell<=|F|<=p-d<p`. The endpoint values `a_C=0` and `a_C=ell` are impossible: they would respectively imply `p|ell k` or `p|ell(k+1)`, while `0<ell<p` and WI-088 gives `1<=k<= (p-1)/2`. Hence

\[
1\le a_C\le\ell-1.
\tag{22}
\]

Now take two free cycles `C,C'`. Their lengths are both `ell`, so (21) gives

\[
p\mid a_C-a_{C'}.
\]

But `|a_C-a_{C'}|<ell<p`. Therefore

\[
\boxed{a_C=a_{C'}=:a.}
\tag{23}
\]

Consequently

\[
m:=\frac{\ell k+a}{p}
\tag{24}
\]

is the same integer for every cycle, and (22) gives

\[
k<\frac{mp}{\ell}<k+1,
\qquad
\boxed{k=\left\lfloor\frac{mp}{\ell}\right\rfloor.}
\tag{25}
\]

This already proves the single-resonance statement up to reduction of the fraction. WI-095's nearest-boundary argument gives `m/ell<=1/2`; Section 4 below shows that the fraction is reduced, so equality `m/ell=1/2` is impossible because `ell>=3`. Hence the strict final range in (6).

## 4. The common resonance denominator is exactly the common cycle length

It remains to rule out a common cycle of length `ell` whose arithmetic ratio `m/ell` reduces to a smaller denominator. Suppose

\[
h:=\gcd(m,\ell)>1,
\qquad
m=hu,
\qquad
\ell=hv.
\tag{26}
\]

Equation (24) becomes

\[
a=h(up-vk)=:hb.
\tag{27}
\]

By (22),

\[
0<b<v.
\tag{28}
\]

Follow one free cycle and record the cyclic binary word

\[
\epsilon_j=
\begin{cases}1,&g^j(x)\in A,\\0,&g^j(x)\in B,
\end{cases}
\qquad 0\le j<\ell.
\tag{29}
\]

It has total weight `a=hb`. For each cyclic starting position define the number of `A` visits in the next `v` steps,

\[
B_j:=\sum_{r=0}^{v-1}\epsilon_{j+r}.
\tag{30}
\]

Every `A` occurrence is counted in exactly `v` of these windows, so

\[
\frac1\ell\sum_{j=0}^{\ell-1}B_j
=\frac{va}{\ell}=b.
\tag{31}
\]

The `B_j` are integers and adjacent values differ by at most one. Since their average is the integer `b`, some cyclic window must satisfy

\[
B_j=b.
\tag{32}
\]

Starting at the corresponding cycle vertex, the displacement after exactly `v` iterates is therefore

\[
d(vk+b)=dup,
\tag{33}
\]

which is zero modulo `p`. Hence `g^v(x)=x` with `0<v<ell`, contradicting the fact that the cycle has minimal period `ell`. Thus

\[
\boxed{\gcd(m,\ell)=1.}
\tag{34}
\]

So the denominator of the common Farey/Beatty resonance is not merely bounded by the cycle length: it **is** the cycle length.

## 5. The rank-defect space has an equal-cycle normal form

WI-096 proves that the true row kernel consists exactly of functions which vanish on all path components, are constant on each free cycle, and satisfy the global zero-mean condition. It also proves (8).

The new equal-length result simplifies that last relation. Write the cycle constants as `z_1,...,z_c`. Since every free cycle has length `ell`, the mean condition is

\[
\ell\sum_{i=1}^{c}z_i=0,
\]

or simply

\[
\boxed{\sum_{i=1}^{c}z_i=0.}
\tag{35}
\]

Thus, when `c>0`, the row kernel has the exact normal form

\[
\boxed{
\ker_{\rm row}G_{p,q}^{(N)}
\cong
\left\{(z_1,\ldots,z_c)\in\mathbf C^c:
\sum_i z_i=0\right\},
}
\tag{36}
\]

with the `c` coordinates attached to `c` interlaced cycles of one common reduced rotation type `(m,ell)`.

If `tau>0`, WI-096 gives `c=tau+1`. Since the free cycles are disjoint and all lie outside the `d` forced-zero vertices,

\[
|F|=c\ell=(\tau+1)\ell\le p-d=2p-q,
\]

which proves (9). Equation (10) follows immediately from `2p-q<p`.

Compared with WI-095, the numerical denominator ceiling is unchanged, but its interpretation is substantially stronger. WI-095 extracted one short cycle from an average and therefore one low-denominator necessary resonance. Here there is no residual mixture: the entire defect kernel is built from copies of that single rational rotation type.

## 6. Stress tests, prior-art boundary, and what this does not prove

The exact proof is falsified by any residual close-prime example in which two free cycles have different lengths, or in which equal-length cycles have different `A` counts. A further sharp falsifier would be one cycle with `gcd(m,ell)>1`, because Section 4 would then predict a forbidden shorter return. An exhaustive exact enumeration of all admissible residual parameters for primes `p<120`, together with broader random finite sweeps, found no such example. These computations are only falsification; equations (12)--(36) are the evidence for the theorem.

The serious prior-art audit found the surrounding dynamical principle in classical rotation theory: orientation-preserving circle dynamics has one rotation number, rational rotation forces a common periodic-orbit period, and piecewise circle maps are commonly organized by Farey/rotation-number structure. A modern survey is Albert Granados, Lluis Alseda and Maciej Krupa, **The Period Adding and Incrementing Bifurcations: From Rotation Theory to Applications**, *SIAM Review* 59 (2017), 225--292, DOI `10.1137/140996598`. Those sources do not discuss finite-window Ramanujan cross Grams, the WI-088 deleted-domain/deleted-range map, or the exact identities (12)--(15). No priority claim is made for the resulting specialization.

This result also does **not** turn the one-pair resonance into a many-modulus estimate. In particular, it does not improve WI-094's `O_theta(1/log P)` cumulative-coherence bound by itself: at fixed observation length, many different prime pairs could in principle occupy the same allowed rational layer. WI-091's bounded-degree theorem still uses the much stronger near-sharp triangular information, not merely the existence of one common denominator. Nor does (36) identify the signed source coefficients of the Yang covariance or provide the missing four-prime welding estimate.

## 7. Program consequence

The residual prime pairwise-rank sector is now more rigid than the hierarchy in WI-095 suggested. For a given pair there is no choice of mixing three-cycles, five-cycles, and longer resonant cycles to manufacture a larger or more flexible defect space. Once a free recurrent sector exists, cyclic order forces it to be a finite rotation, and the exact arithmetic equations force every orbit of that rotation onto the same reduced Farey layer.

For an extensive defect `tau>=theta p`, all `tau` row-kernel dimensions therefore arise from `tau+1` equal, interlaced cycles of one denominator

\[
3\le\ell<1/\theta.
\]

The next genuinely new collective question is consequently **between pairs**, not within one pair: can the exact Yang coefficient law or a fixed-`N` simultaneous-consistency argument prevent enough pairwise defects from occupying compatible low-denominator rotation layers at once? Re-solving one pair in Loewner, Vandermonde, residue-sum, or mixed Farey coordinates cannot produce an additional internal resonance resource, because that resource has now been classified exactly.
# PL-485 — Prime-supported perturbations hide every-scale dispersion

**Evidence/status:** EXACT-DERIVED / LITERATURE+DERIVED / NEGATIVE CONTROL.
Classical prime-capacity, hidden-area and Borel–Cantelli arguments;
no external novelty claim. The dispersion below belongs to the
**perturbation from the exact prime source**, not to either positive
source separately. No small prime-energy estimate is established.

## Claim and quantifiers

Fix
\[
 s>4,\qquad \frac34<\kappa<1-\frac1s,\qquad
 a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}.
\tag{1}
\]
There are two deterministic infinite sources \(b_n^\pm=a_n\pm d_n\),
fixed before sampling, such that
\[
 |d_n|\le a_n/2,\qquad
 d_n=0\quad\text{unless }n\text{ is an actual prime},
\tag{2}
\]
\[
 F(x):=\sum_{n\le x}d_n=O_\kappa(x^\kappa),\qquad
 \sum_{n\le x}b_n^\pm=\psi(x;5,1)+O_\kappa(x^\kappa)
 =x/4+o(x).
\tag{3}
\]
Thus both sources have positive relative weights between \(1/2\) and
\(3/2\) on the exact prime-power support; all higher prime powers keep
their original coefficients.

For every integer \(X\) set
\[
 I_X=\{X,\ldots,2X-1\},\quad L_1=\lfloor X/20\rfloor,
 \quad L_2=\lfloor\sqrt2L_1\rfloor,
\]
\[
 U_i(j)=F(j+L_i)-F(j),\qquad
 D_i^d(X)=X^{-2}\sum_{j,r\in I_X}|U_i(j)-U_i(r)|.
\tag{4}
\]
For **both channels at every sufficiently large integer scale**,
\[
 \boxed{D_i^d(X)\asymp_\kappa X^{2\kappa-1},\qquad i=1,2.}
\tag{5}
\]
In particular its exponent exceeds \(1/2\). All overlapping
populations come from this one prefix \(F\).

At the prescribed scales \(X_k=\lceil k^s\rceil\), draw two uniform
starts with replacement per channel, independently across channels and
scales. Use the same starts for the three sources. Almost surely,
at every sufficiently late prescribed scale, all sampled values obey
\[
 S_{L_i}^{b^+}(R)=S_{L_i}^{b^-}(R)=S_{L_i}^{a}(R),\qquad
 S_L^b(j)=\sum_{j<n\le j+L}b_n.
\tag{6}
\]
The statement retains repeated draws and makes no favorable-subsequence
selection. In fact the proof of (6) needs only uniform marginal laws.

The local delta from
[[research/prime_lattice/findings/PL-483-fixed-prime-supported-sources-evade-subquarter-uniform-observations|PL-483]]
is a compatible dispersion floor on **every** integer block, together
with invisibility on the entire faster polynomial schedule. PL-483's
fixed signed-test separation concerned geometric scales. The local
Master clue explicitly grants the source-reading transfer from
[[research/mobius_cancellation/findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling|MC-540]].
Its every-block placement is reconstructed below with prime-capacity
selection; its square-free counting input is not used for primes.

## 1. A deterministic family of balanced prime packets

For integers \(m\ge m_0\), put
\[
 c_m=\lfloor(3/2)^m\rfloor,\qquad
 t_m=\lfloor101c_m/100\rfloor,\qquad
 B_m=\lfloor c_m^\kappa/100\rfloor.
\tag{7}
\]
Take \(m_0\) sufficiently large once and for all. The search intervals
\((c_m,t_m]\) are disjoint. Partition each into consecutive integer
cells of length \(B_m\), with a possibly shorter final cell. Assign
capacity \(w_p=(\log p)/2\) at primes \(p\equiv1\pmod5\), and zero
elsewhere. Choose the leftmost cell of maximal capacity; call it
\((l_m,r_m]\), with total mass \(W_m\).

The fixed-modulus prime number theorem, after removing the
\(O(\sqrt{c_m}\log^2 c_m)=o(c_m)\) higher-power contribution, gives
\[
 \sum_{c_m<p\le t_m\atop p\equiv1\ (5)}w_p
 =c_m/800+o(c_m).
\tag{8}
\]
There are \(O(c_m/B_m)\) cells, so \(W_m\gg B_m\). This selects
a rich cell from a fixed **macroscopic** interval; it assumes no
lower prime count in a prescribed short interval.

To prevent concentration inside that cell, use the unconditional
Brun–Titchmarsh bound
\[
 \pi(x+y;5,1)-\pi(x;5,1)<\frac{2y}{4\log(y/5)}
 \qquad(x\ge1,\ y>5).
\tag{9}
\]
For \(\mu_m=\sum_{l_m<p\le r_m}w_p\delta_p\), with the same residue
restriction, and \(T_m=\lceil c_m^{\kappa/2}\rceil\), it follows
that every real interval \(I\) satisfies
\[
 \mu_m(I)\le C_\kappa(|I|+T_m+2),\qquad C_\kappa=4/\kappa,
\tag{10}
\]
for all sufficiently large \(m\). Intersect with the selected cell
and enlarge to a half-open interval of length at least \(T_m\);
its length is at most \(|I|+T_m+2\). Equation (9), the bound
\(w_p\le\tfrac12\log(3c_m)\), and
\(\log(T_m/5)\ge(\kappa/4)\log c_m\) prove (10).
In particular \(W_m\ll_\kappa B_m\), and
\(E_m=C_\kappa(T_m+2)=o(B_m)\).

For \(l_m\le j\le r_m\), write
\[
 C_{m,j}=\sum_{l_m<n\le j}w_n,\qquad
 F_m(j)=\min(C_{m,j},W_m-C_{m,j}),
\tag{11}
\]
and set \(F_m=0\) outside this cell. Both endpoints vanish,
\(F_m\ge0\), and \(|F_m(n)-F_m(n-1)|\le w_n\).
The weighted-median identity gives
\[
 \mathcal A_m:=\sum_{j=l_m}^{r_m-1}F_m(j)
 =\min_{z\in\mathbb R}\int|x-z|\,d\mu_m(x).
\tag{12}
\]
Indeed summing cumulative mass to the left of a median and remaining
mass to its right gives the two sides. An atom straddling half the
mass contributes zero distance at the median, so no equal-weight or
no-tie assumption is needed. By (10) and layer cake, for a median \(z\),
\[
 \mathcal A_m\ge\int_0^\infty(W_m-E_m-2C_\kappa u)_+\,du
 =\frac{(W_m-E_m)_+^2}{4C_\kappa}.
\tag{13}
\]
Also \(\mathcal A_m\le B_mW_m/2\). Consequently
\[
 W_m\asymp_\kappa B_m,
 \qquad \mathcal A_m\asymp_\kappa B_m^2\asymp_\kappa c_m^{2\kappa}.
\tag{14}
\]
This is PL-483's capacity lemma, reused rather than claimed anew.
The arithmetic inputs are [Granville, Section 11.9](https://dms.umontreal.ca/~andrew/Courses/Chapter11.pdf)
(source 147) and Montgomery–Vaughan's bound as stated in
[Chirre–Pereira Júnior–de Laat, Section 2.2](https://arxiv.org/pdf/2005.02393)
(source 148). The latter paper's conditional interval-existence
results are not needed.

Set globally
\[
 F(j)=\sum_{m\ge m_0}F_m(j),\qquad d_n=F(n)-F(n-1).
\tag{15}
\]
The sum is locally finite and the packet cells are disjoint. Their
zero endpoint values ensure zero total perturbation in every packet,
with no artificial reset coefficient between packets. Nonzero
increments occur only at the selected primes. Equations (2)–(3)
follow from (11), (14) and telescoping. Completed packets contribute
nothing to the prefix, even though infinitely many have been installed.

## 2. A complete isolated packet in every observation block

Let \(J_m=\{l_m,\ldots,r_m-1\}\), an envelope of the support of
\(F_m\). For each large integer \(X\), choose the least \(m\) with
\(c_m\ge5X/4\). Then
\[
 5X/4\le c_m<15X/8+2,\qquad
 r_m\le101c_m/100<303X/160+3<2X.
\tag{16}
\]
Thus \(J_m\subset I_X\). Its width is \(O(X^\kappa)=o(X)\),
so both \(L_i\) eventually exceed it. Moreover
\[
 (J_m+L_i)\cap\bigcup_\ell J_\ell=\varnothing,
 \qquad i=1,2.
\tag{17}
\]
The translation clears the same packet. The next search interval starts
at \(c_{m+1}\ge3c_m/2-1\), leaving a gap at least
\(49c_m/100-1\) after the current search interval. This exceeds
\(L_i\le\sqrt2X/20\); previous packets lie to the left. This proves
(17) regardless of which maximal-capacity cell was selected.
Consequently
\[
 U_i(j)=-F_m(j)\qquad(j\in J_m).
\tag{18}
\]

Let
\[
 G_i(X)=\{j\in I_X:j,j+L_i\notin\bigcup_\ell J_\ell\}.
\tag{19}
\]
Only \(O(1)\) geometric search intervals meet the endpoint range
\([X,2X+L_i]\). Their centers are comparable to \(X\) and their
packet widths sum to \(O_\kappa(X^\kappa)\). Hence
\[
 |I_X\setminus G_i(X)|=O_\kappa(X^\kappa),\qquad
 U_i(r)=0\quad(r\in G_i(X)).
\tag{20}
\]
The sets \(J_m\) and \(G_i(X)\) are disjoint. Counting both
orientations of pairs between these two sets yields the finite bound
\[
 D_i^d(X)\ge\frac{2|G_i(X)|}{X^2}\mathcal A_m
 \gg_\kappa X^{2\kappa-1}.
\tag{21}
\]
There is no cancellation from a neighboring translated packet in this
lower bound; (17) is its essential geometric check.

For the upper bound, \(U_i\) vanishes off
\(O_\kappa(X^\kappa)\) starts and has magnitude
\(O_\kappa(X^\kappa)\). Therefore
\[
 D_i^d(X)\le\frac2X\sum_{j\in I_X}|U_i(j)|
 \ll_\kappa X^{2\kappa-1}.
\tag{22}
\]
This proves (5) for every large integer \(X\), not just the packet
centers or a lacunary set. The jump bounds also remain valid:
\(|\Delta U_i|\le\log(3X)\) and
\(|\Delta S_{L_i}^{b^\pm}|\le\tfrac32\log(3X)\).

## 3. The prescribed observations miss the endpoint support

At scale \(X_k\), the probability that any of the four starts lies
outside its channel's set \(G_i(X_k)\) is, by (20) and a union bound,
\[
 O_\kappa(X_k^{\kappa-1}).
\tag{23}
\]
The exponent condition in (1) gives
\[
 \sum_k X_k^{\kappa-1}\ll\sum_k k^{-s(1-\kappa)}<\infty.
\tag{24}
\]
The first Borel–Cantelli lemma, [Durrett, Theorem 2.3.1](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf)
(source 153), implies only finitely many such hits, without independence
requirements. Outside those events,
\[
 S_{L_i}^{b^\pm}(R)-S_{L_i}^a(R)=\pm U_i(R)=0,
\]
which proves (6). Windows may contain whole modified packets; only
their two endpoints matter because each packet has total mass zero.
The same sources work for any prescribed sequence satisfying
\(\sum_k X_k^{\kappa-1}<\infty\).

## Prior art, validation and consequence

The hidden-area mechanism belongs to classical optimal recovery;
compare [Baran–Demaine–Katz](https://erikdemaine.org/papers/Integration_Algorithmica/)
(source 152). Disjoint-bump randomized lower bounds also appear in
[Kunsch–Rudolf, Section 2.1, Lemmas 2.1–2.2](https://arxiv.org/html/1809.09890v1)
(source 154). These are methodological comparisons, not prime-specific
or infinite-scale theorems being imported. Coarse PNT, the upper sieve
bound, the median identity and the probability principle are classical.
The local contribution is their simultaneous realization with prime
support, bounded positive relative weights, one fixed source pair,
every-integer-scale perturbation dispersion and entire-polynomial-sequence
sample equality. No new number-theoretic estimate is asserted.

Finite exact checks used nine deterministically selected packets at
\(\kappa=4/5\), with capacities \(\lfloor\log_2p\rfloor/4\) on actual
primes \(p\equiv1\pmod5\), through a sieve bound of 2,000,000.
These rational capacities are below \((\log p)/2\); they test the
same finite construction without treating floating logarithms as exact.
The checks verified capacity-bounded prime-only increments and prefix
recovery at all 2,000,000 positions, plus the median area of every
packet. For every integer \(100000\le X\le600000\), both channels
passed packet containment and translated-support exclusion: 1,000,002
geometry checks. At 21 evenly spaced scales in that interval, 14,700,000
window evaluations and 42 exact sorted-population dispersion calculations
verified (21)–(22) and the good-start equalities, including repeated draws.
Four rational choices of \(s>4\) checked the strict exponent interval.
These are finite bookkeeping checks, not proofs of asymptotic prime
counts, almost-sure events, or low prime energies; those boundaries
remain those of the displayed derivation. No Lean verification or
independent adversarial approval is claimed. The reused finite lemma
and elementary placement give no separate high-value formalization target.

In (6), the ordinary sample-centered energies of all three sources
coincide exactly, but their common value is the **unknown baseline prime
energy**. Equation (5) neither supplies a small energy ceiling nor proves
an every-scale dispersion floor for either \(b^+\) or \(b^-\) separately.
It also does not provide a fixed signed pole-isolating test on every
scale. The conclusion is precisely that positive prime reweighting,
leading PNT and overlapping-window compatibility do not prevent this
hidden **perturbation** dispersion.

At \(s=4\) the strict interval (1) is empty. This is consistent with
[[research/prime_lattice/findings/PL-484-two-random-starts-detect-prime-poles-on-fourth-power-scales|PL-484]],
without proving optimal sampling for the single exact Mangoldt source.
The controls need not preserve canonical Euler factors, a completed
functional equation or the noncancelling isolated-pole formula. No
RH/GRH statement, arithmetic energy bound, or lower bound for adaptive
or accumulated cross-scale observations follows. The actual prime-energy
estimate remains a separate obligation.

# FD-139 — exact central-rank conditioning still hides the prime-color wall

**Status:** `LITERATURE+DERIVED + EXACT-MATCHED-CONTROL + SQUAREFREE-SATHE-SELBERG + JOINT-LOCAL-PRIME-FACTOR-LAW + EXACT-RANK-CONDITIONING + FACTOR-TWO-SCALE-LOCALIZATION + ALL-PRIME-UNIFORMITY + COMMON-SOURCE + ORTHOGONAL-PRIME-COLOR-WALL + NEGATIVE/BOUNDARY`.

`FD-137` showed that exact conditioning on the hidden `omega(n)` rank destroys the older moving-rank witness, while `FD-138` moved the sign wall into the independent prime-color coordinate

\[
D(n):=\sum_{q\mid n}\chi_4(q)
\]

and proved noncoercivity only after retaining a CLT-width window of `omega(n)`. The exact-rank case was left open because ordinary weak Erdős--Kac does not control a single rank cell, whose mass is only of order `1/sqrt(log log T)`.

The local input needed to cross that gap is classical. Squarefree Sathe--Selberg gives the correct size of one exact central-rank shell, while the joint local law for prime factors in disjoint prime sets shows that the two-value color boundary `D in {-1,0}` has one further factor `1/sqrt(log log T)` of codimension. Combining those two facts with the exact ancestry relation of `FD-138` shows that **even exact central-rank conditioning is noncoercive** for the same one global source.

Fix `K>=0`, `1<=r<infinity`, and reuse the `FD-138` source

\[
b_K(n):=
\begin{cases}
+1,&n\text{ squarefree and }(\omega(n)\le K\text{ or }D(n)\ge0),\\
-1,&n\text{ squarefree},\ \omega(n)>K,\ D(n)<0,
\end{cases}
\qquad
a_n^{(K)}:=\mu(n)b_K(n),
\tag{1}
\]

with `a_n^(K)=0` on nonsquarefree integers. For `T>=3`, put

\[
L_T:=\log\log T.
\tag{2}
\]

For a prime `p` and an integer rank `m`, define the exact joint scale-rank parent cell

\[
\mathcal C_{p,m}(T)
:=
\{n:T<n\le2T,\ n\text{ squarefree},\ p\nmid n,\ \omega(n)=m\},
\tag{3}
\]

and the exact-rank ancestry defect

\[
\mathfrak E_{p,m,r}(T;a)
:=
\frac1{|\mathcal C_{p,m}(T)|}
\sum_{n\in\mathcal C_{p,m}(T)}|a_{pn}+a_n|^r,
\tag{4}
\]

with value `0` when the cell is empty. Define also

\[
\mathfrak E^{\log}_{p,m,r}(T;a)
:=
\frac{\displaystyle\sum_{n\in\mathcal C_{p,m}(T)}|a_{pn}+a_n|^r/n}
{\displaystyle\sum_{n\in\mathcal C_{p,m}(T)}1/n}.
\tag{5}
\]

Then for every fixed `C>0`,

\[
\boxed{
\sup_{p\ \mathrm{prime}}
\sup_{\substack{m\in\mathbb Z\\|m-L_T|\le C\sqrt{L_T}}}
\mathfrak E_{p,m,r}(T;a^{(K)})
\ll_{C,r}\frac1{\sqrt{L_T}}
\longrightarrow0,
}
\tag{6}
\]

and

\[
\boxed{
\sup_{p\ \mathrm{prime}}
\sup_{\substack{m\in\mathbb Z\\|m-L_T|\le C\sqrt{L_T}}}
\mathfrak E^{\log}_{p,m,r}(T;a^{(K)})
\ll_{C,r}\frac1{\sqrt{L_T}}
\longrightarrow0.
}
\tag{7}
\]

The coefficient source nevertheless stays macroscopically wrong:

\[
\boxed{
\frac1H\#\{n\le H:a_n^{(K)}\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)},
}
\tag{8}
\]

with the same positive logarithmic density and the same positive `L^r` coefficient-error limits already established in `FD-138`.

Thus the distinction left open by `FD-137`--`FD-138` is resolved: the old moving-`omega` witness was killed by exact rank because its wall **was the rank coordinate itself**. Exact rank is not intrinsically coercive. A different common source can place its transition in a transverse prime-factor coordinate, and a single exact `omega=m` slice still averages that transverse boundary away.

## 1. Exact ancestry reduction: only two color values can be defective

For squarefree `n` with `p\nmid n`,

\[
\mu(pn)=-\mu(n),
\tag{9}
\]

so the Möbius gauge gives the exact identity

\[
a_{pn}^{(K)}+a_n^{(K)}
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr).
\tag{10}
\]

For every rank in the window of (6), `m>K` and `m+1>K` once `T` is large, so the finite anchor is inactive. The prime-color coordinate changes by

\[
D(pn)=D(n)+\chi_4(p).
\tag{11}
\]

With the tie convention `D>=0` on the positive side, exactly as in `FD-138`,

\[
|a_{pn}^{(K)}+a_n^{(K)}|
=
\begin{cases}
0,&p=2,\\
2\,\mathbf1_{\{D(n)=-1\}},&p\equiv1\pmod4,\\
2\,\mathbf1_{\{D(n)=0\}},&p\equiv3\pmod4.
\end{cases}
\tag{12}
\]

Hence every bad parent, simultaneously for every prime direction, belongs to the fixed arithmetic boundary

\[
\boxed{D(n)\in\{-1,0\}.}
\tag{13}
\]

The problem is therefore purely local: how large can this two-value boundary be **inside one exact central rank**?

## 2. The exact squarefree rank cell has size `T/sqrt(log log T)`, uniformly after excluding one prime

Let

\[
N^*_{m,p}(x)
:=
\#\{n\le x:\mu^2(n)=1,\ \omega(n)=m,\ p\nmid n\}.
\tag{14}
\]

The squarefree Sathe--Selberg formula is obtained from

\[
\sum_{n\ge1}\frac{\mu^2(n)z^{\omega(n)}}{n^s}
=
\prod_q\left(1+\frac z{q^s}\right)
=
\zeta(s)^z F(s,z),
\tag{15}
\]

where `F` is regular in the Selberg--Delange region. Its standard central-rank form is

\[
N_m^*(x)
=
G^*(z_x)
\frac{x}{\log x}
\frac{(\log\log x)^{m-1}}{(m-1)!}
\left(1+O_C\!\left(\frac1{\log\log x}\right)\right),
\tag{16}
\]

uniformly when

\[
z_x:=\frac{m-1}{\log\log x}
\tag{17}
\]

stays in a fixed compact subset of `(0,2)`, with

\[
G^*(z)
=
\frac1{\Gamma(1+z)}
\prod_q\left(1+\frac zq\right)\left(1-\frac1q\right)^z.
\tag{18}
\]

For the excluded-prime cell (14), the generating Dirichlet series differs from (15) by exactly one Euler factor:

\[
\prod_{q\ne p}\left(1+\frac z{q^s}\right)
=
\frac{\zeta(s)^zF(s,z)}{1+z/p^s}.
\tag{19}
\]

Running the same coefficient extraction therefore gives

\[
\boxed{
N^*_{m,p}(x)
=
\frac{G^*(z_x)}{1+z_x/p}
\frac{x}{\log x}
\frac{(\log\log x)^{m-1}}{(m-1)!}
\left(1+O_C\!\left(\frac1{\log\log x}\right)\right),
}
\tag{20}
\]

uniformly in the prime `p`. The uniformity costs nothing new: on every compact `z`-set used by Sathe--Selberg, the omitted factor `(1+z/p^s)^(-1)` and the finite number of derivatives required in the Selberg--Delange argument are bounded uniformly for `p>=2`. For `p>x`, the factor differs from `1` by `O(1/p)`, below the displayed error, consistently with the fact that such a prime cannot divide a central-rank integer `n<=x` once the rank tends to infinity.

Now assume

\[
|m-L_T|\le C\sqrt{L_T}.
\tag{21}
\]

Stirling's formula applied to (20) gives, uniformly in `p`,

\[
N^*_{m,p}(T)\asymp_C\frac{T}{\sqrt{L_T}},
\qquad
N^*_{m,p}(2T)\asymp_C\frac{T}{\sqrt{L_T}}.
\tag{22}
\]

More is true: `log log(2T)=L_T+o(1)`, so the two Sathe--Selberg main factors other than the leading `x` agree up to `1+o_C(1)`. Consequently

\[
\boxed{
|\mathcal C_{p,m}(T)|
=N^*_{m,p}(2T)-N^*_{m,p}(T)
\gg_C\frac{T}{\sqrt{L_T}}
}
\tag{23}
\]

uniformly over all primes and all ranks in (21).

This is the denominator that weak Erdős--Kac could not see in `FD-138`.

## 3. The color boundary has one additional local codimension

Split the odd prime divisors of `n` by their mod-4 color:

\[
\omega_+(n):=\#\{q\mid n:q\equiv1\pmod4\},
\qquad
\omega_-(n):=\#\{q\mid n:q\equiv3\pmod4\}.
\tag{24}
\]

Then

\[
D(n)=\omega_+(n)-\omega_-(n),
\qquad
\omega(n)=\omega_+(n)+\omega_-(n)+\mathbf1_{2\mid n}.
\tag{25}
\]

The reciprocal prime masses in the two color classes satisfy

\[
H_+(x)=\frac12\log\log x+O(1),
\qquad
H_-(x)=\frac12\log\log x+O(1).
\tag{26}
\]

The joint local prime-factor law of Tenenbaum, in the form summarized and sharpened in the literature on joint Poisson approximation, gives for the two disjoint prime sets an estimate of Poisson-product size whenever both requested counts are fixed positive multiples of their harmonic masses. In particular, if

\[
k_+=\frac12L_x+O_C(\sqrt{L_x}),
\qquad
k_-=\frac12L_x+O_C(\sqrt{L_x}),
\tag{27}
\]

then

\[
\boxed{
\mathbb P_{n\le x}
\bigl(\omega_+(n)=k_+,\ \omega_-(n)=k_-\bigr)
\ll_C\frac1{L_x}.
}
\tag{28}
\]

Indeed, each local Poisson factor at its central scale is `O_C(L_x^(-1/2))`, and the joint multiplicative correction remains bounded in the range (27).

Let

\[
B_m(x):=
\#\{n\le x:\omega(n)=m,\ D(n)\in\{-1,0\}\}.
\tag{29}
\]

For each choice of `D(n) in {-1,0}` and `1_(2|n) in {0,1}`, equations (25) determine at most one pair `(omega_+(n),omega_-(n))`. Thus there are at most four pairs. Under the central condition

\[
|m-L_x|\le C\sqrt{L_x}+O(1),
\tag{30}
\]

every such pair lies in the range (27). Equation (28) therefore gives

\[
\boxed{
B_m(x)\ll_C\frac{x}{\log\log x}.
}
\tag{31}
\]

This upper bound is deliberately taken over **all integers**, not merely squarefree integers. It consequently bounds every squarefree boundary numerator needed below without importing a squarefree bivariate local theorem.

The scale comparison is now transparent. A single exact squarefree central-rank cell has mass

\[
\asymp_C T L_T^{-1/2},
\tag{32}
\]

whereas imposing the extra color-boundary condition costs another square-root factor:

\[
\ll_C T L_T^{-1}.
\tag{33}
\]

Exact rank fixes the sum of the two prime-color populations; it does not fix their difference.

## 4. Exact-rank ancestry still vanishes uniformly in the prime direction

Fix `p`, `m` in (21), and consider the numerator of (4). By (12), every defective parent belongs to (13). Hence, using (31) with `x=2T`,

\[
\#\{n\in\mathcal C_{p,m}(T):a_{pn}^{(K)}+a_n^{(K)}\ne0\}
\le B_m(2T)
\ll_C\frac{T}{L_T}.
\tag{34}
\]

The numerator bound contains no `p`, while the denominator lower bound (23) is uniform in `p`. Since every nonzero defect has magnitude exactly `2`,

\[
\mathfrak E_{p,m,r}(T;a^{(K)})
\ll_{C,r}
\frac{T/L_T}{T/\sqrt{L_T}}
\ll_{C,r}L_T^{-1/2}.
\tag{35}
\]

Taking both suprema proves (6).

Inside `(T,2T]`, reciprocal weights vary by at most a factor `2`:

\[
\frac1{2T}<\frac1n<\frac1T.
\tag{36}
\]

Therefore

\[
\mathfrak E^{\log}_{p,m,r}(T;a^{(K)})
\le2\mathfrak E_{p,m,r}(T;a^{(K)}),
\tag{37}
\]

which proves (7).

For `p=2`, (12) already gives zero identically. For odd primes, the argument does not use the residue class of `p` except to choose which of the two boundary values is active. This is why the result is uniform over the entire prime set despite conditioning on a cell of vanishing marginal density.

In a finite ancestry graph with child cutoff `H`, restrict as usual to active primes with `2Tp<=H`. Equations (6)--(7) remain uniform on every such family. The all-prime formulation concerns the one infinite common source and does not assert that one finite graph contains children for arbitrarily large primes.

## 5. The matched source remains macroscopically non-Möbius

Nothing in the exact-rank localization changes the source itself. For squarefree `n` with `omega(n)>K`,

\[
a_n^{(K)}\ne\mu(n)
\quad\Longleftrightarrow\quad
D(n)<0.
\tag{38}
\]

The weighted Erdős--Kac input already audited in `FD-138` gives asymptotic half-mass to either sign of `D` among squarefree integers, while the bounded set of anchored ranks has density zero. Hence (8), its logarithmic analogue, and the positive `L^r` coefficient-error limits all persist unchanged.

The important matched-control feature is that **one fixed infinite source** works simultaneously for every shell, every central exact rank, and every prime direction. No horizon-dependent coloring, exceptional rank selection, or post-hoc sign choice is being used.

## 6. What exact rank does and does not buy

`FD-137` was not evidence that exact rank is generally coercive. It proved something narrower and sharper: the particular `FD-132` moving-threshold source placed its entire defect on one rank wall, so conditioning on that rank exposed it maximally.

`FD-139` separates that witness-specific fact from the information content of rank itself. The observed statistic

\[
\omega(n)=\omega_+(n)+\omega_-(n)+\mathbf1_{2\mid n}
\tag{39}
\]

fixes essentially the **sum** of the two colored prime populations. The source wall depends on their **difference**. Conditioned on an exact central sum, that difference still fluctuates on a square-root scale, and a one-step prime multiplication reaches the sign boundary only with probability `O(1/sqrt(log log T))`.

Thus the proposed repair

\[
\text{physical shell}
+\text{exact }\omega\text{ rank}
+\text{mean prime ancestry}
\Longrightarrow
\text{Möbius recovery}
\tag{40}
\]

is false in the squarefree-unit matched-control class.

This does **not** refute local `L^infinity` ancestry: `FD-135` already shows that once every active edge is controlled below magnitude `2`, ancestry becomes exact and rough-core rigidity takes over. Nor does it refute a law that conditions on sufficiently many genuinely source-native prime-factor coordinates, or a destination-side Fourier-skeleton coercivity theorem that bypasses coefficient recovery.

The next frontier is therefore no longer the width of the `omega` cell. It is **coordinate completeness**: whether a finite family of source-native additive coordinates can prevent a matched source from rotating its wall into a transverse prime-color direction without already approaching exact prime-by-prime reconstruction.

## 7. Prior-art audit and dependency boundary

The local number theory used here is classical rather than a novelty claim.

Gérald Tenenbaum's *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed. (AMS, 2015), Chapter II.6 and its squarefree Sathe--Selberg exercise give the central-rank formula obtained from the Euler product in (15). The only extension needed here is omission of one prime, and (19) shows explicitly that this multiplies the analytic factor by `(1+z/p^s)^(-1)`; the required uniform lower bound follows inside the same compact Selberg--Delange parameter range.

Tenenbaum's *Moyennes effectives de fonctions multiplicatives complexes*, Ramanujan Journal **44** (2017), 641--701, DOI `10.1007/s11139-017-9949-7`, gives local laws for prime-factor counts in arbitrary disjoint prime sets. Kevin Ford's *Joint Poisson distribution of prime factors in sets*, Mathematical Proceedings of the Cambridge Philosophical Society **173** (2022), 189--200, DOI `10.1017/S0305004121000499`, explicitly records the joint local-law background and the resulting approximately binomial behavior of prime factors from a subset after conditioning on total `omega`. Thus `FD-139` does **not** claim novelty for Sathe--Selberg, conditional binomial prime-factor statistics, or joint Poisson/local laws.

The new contribution is the splice with the exact `FD-138` Möbius-gauge ancestry representation: the literature local laws quantify the transverse codimension of the fixed two-value prime-color wall, turning the existing common source into an exact-rank noncoercivity control. The two Tenenbaum inputs are load-bearing and are anchored in `research/farey_discrepancy/SOURCES.md`; Ford is a prior-art boundary and consistency check rather than a separate load-bearing hypothesis.

## 8. Adversarial audit

- **Exact rank really is exact.** No rank window is averaged in (4)--(7); the supremum is over individual integer values `m`.
- **The denominator is not inferred from weak Erdős--Kac.** It comes from squarefree Sathe--Selberg at one local rank, with the excluded-prime Euler factor tracked explicitly.
- **The numerator does not assume squarefree independence.** It is bounded by a joint local count over all integers, which is only larger than the squarefree boundary set actually used.
- **The factor `2` is handled.** Its character value is zero, so that direction has identically zero defect; in the local count it contributes only the binary term `1_(2|n)` in (25).
- **Parity causes no gap.** For each `D in {-1,0}` and each value of `1_(2|n)`, there is either no compatible pair `(omega_+,omega_-)` or exactly one; at most four joint local events cover the boundary.
- **Prime exclusion is uniform.** Omitting one Euler factor cannot collapse a central squarefree rank cell; `(1+z/p)^(-1)` stays uniformly bounded away from zero for central positive `z` and every `p>=2`.
- **Shell subtraction is legitimate.** `log log(2T)-log log T=o(1)`, so the `T` and `2T` Sathe--Selberg factors other than the leading `x` agree uniformly up to `1+o(1)` in the fixed CLT band.
- **No local rigidity is contradicted.** The defect is small only in conditional mean. It remains exactly `2` on the rare boundary edges, so `FD-135`'s `L^infinity` threshold is untouched.
- **No Farey/RH consequence is claimed.** The result is a no-go theorem for a proposed coefficient-side coercive interface. It neither constructs a physical Farey discrepancy counterexample nor weakens any RH-equivalent criterion.

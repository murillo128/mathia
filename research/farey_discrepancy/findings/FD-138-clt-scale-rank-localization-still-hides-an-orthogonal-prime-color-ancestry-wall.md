# FD-138 — CLT-scale rank localization still hides an orthogonal prime-color ancestry wall

**Status:** `LITERATURE+DERIVED + EXACT-MATCHED-CONTROL + SQUAREFREE-WEIGHTED-ERDOS-KAC + JOINT-SCALE-RANK-LOCALIZATION + ALL-PRIME-UNIFORMITY + COMMON-SOURCE + ORTHOGONAL-PRIME-COLOR-WALL + NEGATIVE/BOUNDARY`.

`FD-137` isolates multiplicative rank as the coordinate missed by the common moving-threshold witness: factor-two scale localization still averages away its central `omega(n)` wall, while exact conditioning on the hidden rank exposes the maximal defect. A natural next repair is therefore to keep a genuine amount of central-rank information rather than marginalizing `omega(n)` completely.

A CLT-scale rank window is still not enough. There is a different common squarefree-unit source whose coefficient error has positive density, while its mean prime-ancestry defect tends to zero **inside one factor-two physical shell and inside a fixed two-standard-deviation `omega` window**, uniformly in the prime direction. The hidden transition has simply moved into an independent additive prime-color coordinate.

The construction uses the real nonprincipal character modulo `4`. Put
\[
\chi_4(q)=
\begin{cases}
0,&q=2,\\
+1,&q\equiv1\pmod4,\\
-1,&q\equiv3\pmod4,
\end{cases}
\tag{1}
\]
and define the strongly additive prime-color imbalance
\[
D(n):=\sum_{q\mid n}\chi_4(q).
\tag{2}
\]
For a fixed anchor depth `K>=0`, define on squarefree integers
\[
b_K(n):=
\begin{cases}
+1,&\omega(n)\le K\text{ or }D(n)\ge0,\\
-1,&\omega(n)>K\text{ and }D(n)<0,
\end{cases}
\qquad
a_n^{(K)}:=\mu(n)b_K(n),
\tag{3}
\]
with `a_n^(K)=0` on nonsquarefree integers. This is one infinite source for each fixed `K`; it does not depend on the horizon, shell, or monitored prime.

For `T` large let
\[
L_T:=\log\log T
\tag{4}
\]
and, for every prime `p`, define the joint scale-rank parent cell
\[
\mathcal C_p(T):=
\left\{
T<n\le2T:\
n\text{ squarefree},\ p\nmid n,\
|\omega(n)-L_T|\le2\sqrt{L_T}
\right\}.
\tag{5}
\]
For fixed `1<=r<infinity`, put
\[
\mathfrak J_{p,r}(T;a):=
\frac1{|\mathcal C_p(T)|}
\sum_{n\in\mathcal C_p(T)}|a_{pn}+a_n|^r,
\tag{6}
\]
with value `0` if the cell is empty, and define its harmonic analogue
\[
\mathfrak J^{\log}_{p,r}(T;a):=
\frac{\displaystyle\sum_{n\in\mathcal C_p(T)}|a_{pn}+a_n|^r/n}
{\displaystyle\sum_{n\in\mathcal C_p(T)}1/n}.
\tag{7}
\]

Then
\[
\boxed{
\sup_{p\ \mathrm{prime}}
\mathfrak J_{p,r}(T;a^{(K)})\longrightarrow0,
\qquad
\sup_{p\ \mathrm{prime}}
\mathfrak J^{\log}_{p,r}(T;a^{(K)})\longrightarrow0.
}
\tag{8}
\]
Nevertheless
\[
\boxed{
\frac1H\#\{n\le H:a_n^{(K)}\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)},
}
\tag{9}
\]
and for every fixed finite `r`,
\[
\boxed{
\frac1H\sum_{n\le H}|a_n^{(K)}-\mu(n)|^r
\longrightarrow\frac{2^{r-1}}{\zeta(2)}.
}
\tag{10}
\]
The same limit in (10) holds after weighting numerator and denominator by `1/n`.

Thus simultaneous localization in physical scale and in a **positive-Gaussian-mass central rank window** still does not make approximate prime ancestry coercive. `FD-137` killed the old moving-`omega` witness by exposing its hidden rank wall; `FD-138` shows that a source can move that wall into another additive prime-factor coordinate while remaining almost ancestry-consistent on the entire CLT-scale rank cell.

## 1. Weighted Erdős--Kac supplies the two required Gaussian laws

The only new load-bearing literature input is the general weighted Erdős--Kac theorem of Kai (Steve) Fan, *Weighted Erdős--Kac theorems via computing moments*, Acta Arithmetica **217** (2025), 99--158, DOI `10.4064/aa231014-9-8`, especially Theorem 2.1 and the normal-distribution consequence of its moment estimates.

Fan considers bounded strongly additive functions `f` under nonnegative multiplicative weights `alpha` in a class `M*`; the paper explicitly lists
\[
\alpha(n)=\mu(n)^2
\tag{11}
\]
as an admissible weight. For this weight the normalization is exactly counting measure on squarefree integers. With
\[
A_f(x):=\sum_{p\le x}\frac{f(p)}p,
\qquad
B_f(x):=\sum_{p\le x}\frac{f(p)^2}p,
\tag{12}
\]
Fan's theorem gives a standard Gaussian limit whenever `B_f(x)->infinity`.

Apply it first to
\[
f(n)=D(n).
\tag{13}
\]
Since `chi_4` is nonprincipal,
\[
A_D(x)=\sum_{p\le x}\frac{\chi_4(p)}p
=A_\infty+o(1),
\tag{14}
\]
while
\[
B_D(x)
=\sum_{\substack{p\le x\\p\ne2}}\frac1p
=\log\log x+O(1).
\tag{15}
\]
The convergence in (14) is the classical first-order Euler-product consequence of the finiteness and nonvanishing of `L(1,chi_4)`; no quantitative prime race is needed.

Let
\[
Q(x):=\#\{n\le x:n\text{ squarefree}\}
=\frac{x}{\zeta(2)}+O(\sqrt x).
\tag{16}
\]
The weighted Gaussian law implies, for every fixed real `v`,
\[
\frac1{Q(x)}
\#\left\{
n\le x:n\text{ squarefree},\
\frac{D(n)-A_D(x)}{\sqrt{B_D(x)}}\le v
\right\}
\longrightarrow\Phi(v).
\tag{17}
\]
In particular, because `A_D(x)=O(1)` and `B_D(x)->infinity`,
\[
\boxed{
\#\{n\le x:n\text{ squarefree},\ D(n)\in\{-1,0\}\}=o(x),
}
\tag{18}
\]
and
\[
\boxed{
\#\{n\le x:n\text{ squarefree},\ D(n)<0\}
=\frac{x}{2\zeta(2)}+o(x).
}
\tag{19}
\]
Equation (18) uses only weak convergence to a continuous Gaussian: for any fixed `eta>0`, the two values `-1,0` eventually lie in the normalized interval `[-eta,eta]`, whose limiting Gaussian mass tends to zero with `eta`. No local limit theorem is imported.

Apply the same theorem to `f=omega`. Then
\[
A_\omega(x)=B_\omega(x)=\log\log x+O(1),
\tag{20}
\]
so the squarefree integers in a two-standard-deviation central rank window have asymptotic relative mass
\[
G_2:=\mathbb P(|Z|\le2)
=2\Phi(2)-1
\approx0.9544997361.
\tag{21}
\]
Since `log log(2T)=L_T+o(1)`, subtracting the two prefix asymptotics gives
\[
\boxed{
\#\left\{
T<n\le2T:n\text{ squarefree},\
|\omega(n)-L_T|\le2\sqrt{L_T}
\right\}
=\left(\frac{G_2}{\zeta(2)}+o(1)\right)T.
}
\tag{22}
\]
Numerically,
\[
\frac{G_2}{\zeta(2)}
\approx0.5802662583.
\tag{23}
\]
This constant being strictly larger than `1/2` is what will make the parent cells uniformly macroscopic even after excluding an arbitrary prime divisor.

## 2. Every prime direction sees only a two-value color boundary

Fix a large `T`, a prime `p`, and `n in C_p(T)`. Since
\[
L_T-2\sqrt{L_T}\longrightarrow\infty,
\tag{24}
\]
we have `omega(n)>K` and `omega(pn)>K` uniformly on these cells once `T` is large. The finite anchor in (3) is therefore inactive.

Because `n` is squarefree and `p` does not divide `n`,
\[
\mu(pn)=-\mu(n),
\tag{25}
\]
so
\[
a_{pn}^{(K)}+a_n^{(K)}
=\mu(n)\bigl(b_K(n)-b_K(pn)\bigr).
\tag{26}
\]
The prime-color coordinate changes by exactly one character value:
\[
D(pn)=D(n)+\chi_4(p).
\tag{27}
\]
With the tie convention `D>=0` on the `+1` side, (27) gives the exact trichotomy
\[
|a_{pn}^{(K)}+a_n^{(K)}|
=
\begin{cases}
0,&p=2,\\
2\,\mathbf1_{\{D(n)=-1\}},&p\equiv1\pmod4,\\
2\,\mathbf1_{\{D(n)=0\}},&p\equiv3\pmod4.
\end{cases}
\tag{28}
\]
Thus every defective parent for every prime direction lies in the **same fixed two-value set**
\[
D(n)\in\{-1,0\}.
\tag{29}
\]
By (18), the number of such squarefree parents in `(T,2T]` is `o(T)`. This numerator estimate is already uniform in `p`; no prime-uniform Erdős--Kac theorem is being smuggled into the argument.

## 3. The central-rank parent cells are uniformly macroscopic in every prime

Let the unrestricted central cell counted in (22) have cardinality `C(T)`. Excluding parents divisible by `p` removes at most
\[
\frac Tp+O(1)\le\frac T2+O(1)
\tag{30}
\]
integers from the factor-two shell. Therefore, uniformly over **all primes**,
\[
|\mathcal C_p(T)|
\ge
\left(
\frac{G_2}{\zeta(2)}-\frac12+o(1)
\right)T.
\tag{31}
\]
The limiting coefficient is
\[
c_*:=\frac{G_2}{\zeta(2)}-\frac12
\approx0.0802662583>0.
\tag{32}
\]
Hence
\[
\inf_{p\ \mathrm{prime}}|\mathcal C_p(T)|\gg T.
\tag{33}
\]
This is deliberately crude. Its advantage is that all prime dependence has disappeared into the elementary bound (30).

Combining (18), (28), and (33),
\[
\sup_{p\ \mathrm{prime}}
\mathfrak J_{p,r}(T;a^{(K)})
\le
\frac{2^r\,o(T)}{(c_*+o(1))T}
=o(1),
\tag{34}
\]
which proves the first half of (8).

On `(T,2T]`,
\[
\frac1{2T}\le\frac1n\le\frac1T.
\tag{35}
\]
Consequently
\[
\mathfrak J^{\log}_{p,r}(T;a^{(K)})
\le2\mathfrak J_{p,r}(T;a^{(K)}),
\tag{36}
\]
uniformly in `p`, proving the harmonic half of (8).

The all-prime supremum in (8) is a statement about the shell functional for the one global source. In a finite ancestry graph with child cutoff `H`, simply restrict to primes satisfying `2Tp<=H`; (8) remains valid for every such active-prime family. No finite horizon is claimed to contain edges for literally every prime simultaneously.

## 4. The source stays a positive distance from Möbius

For squarefree `n` of rank larger than `K`, equation (3) gives
\[
a_n^{(K)}\ne\mu(n)
\quad\Longleftrightarrow\quad
D(n)<0.
\tag{37}
\]
The squarefree integers with `omega(n)<=K` have density zero. Therefore (19) proves (9).

Whenever the two coefficients disagree, their values are opposite unit signs, so
\[
|a_n^{(K)}-\mu(n)|^r=2^r.
\tag{38}
\]
Equations (9) and (38) give (10). Partial summation applied to the counting function in (9) also yields
\[
\sum_{\substack{n\le H\\a_n^{(K)}\ne\mu(n)}}\frac1n
=\left(\frac1{2\zeta(2)}+o(1)\right)\log H,
\tag{39}
\]
and hence
\[
\boxed{
\frac{\displaystyle\sum_{n\le H}|a_n^{(K)}-\mu(n)|^r/n}
{\displaystyle\sum_{n\le H}1/n}
\longrightarrow\frac{2^{r-1}}{\zeta(2)}.
}
\tag{40}
\]
Thus the same physical-scale weight used in `FD-136` sees a fixed coefficient error even though the joint scale-rank ancestry defect in (8) vanishes.

## 5. Why this is genuinely beyond FD-137 but not yet exact-rank conditioning

The `FD-132`--`FD-137` witness hid its ancestry failure by putting the sign boundary at a moving threshold in `omega(n)`. `FD-137` therefore exposes it immediately once the observer retains the hidden rank. The new source removes that dependency: within the central `omega` window, the sign is controlled by
\[
D(n)=\#\{q\mid n:q\equiv1\pmod4\}
-
\#\{q\mid n:q\equiv3\pmod4\}.
\tag{41}
\]
The observed `omega` coordinate records the **sum** of the two prime-color populations, while `D` records their **difference**. A CLT-scale window for the sum still leaves a transverse fluctuation of square-root size in the difference. Prime ancestry changes `D` by only one unit, so the transition set has vanishing marginal mass.

This is not a claim that exact-rank conditioning fails. To prove that stronger statement one would need a local or bivariate theorem showing that, inside a single central `omega=m` slice, the exact color boundary `D in {-1,0}` has vanishing relative mass. Ordinary weak Erdős--Kac is insufficient because the exact-rank denominator itself has only order `T/sqrt(log log T)`. No such local-limit input is used here, and `FD-138` leaves that exact-rank question open.

Likewise, this does not refute a source law that conditions simultaneously on enough independent prime-factor coordinates, a shrinking rank window whose mass is quantified sharply enough, a quantile norm that detects the color boundary, or a destination-side Fourier-skeleton coercivity theorem. It only rules out the first broad joint repair: factor-two physical localization plus a fixed positive-Gaussian-mass `omega` window.

## 6. Adversarial checks and prior-art boundary

The main quantifier risk is the all-prime supremum. It does **not** come from a uniform probabilistic theorem in a growing modulus or excluded prime. The numerator is bounded by the global two-value color event (18), independent of `p`, and the denominator is bounded below by subtracting at most `T/p<=T/2` parents from an unrestricted central cell whose density is strictly larger than one half. This is why the fixed width `2 sqrt(L_T)` was chosen; narrower windows would require a less crude denominator analysis.

The anchor cannot create hidden extra defects, because (24) removes all fixed ranks from the observed cell. The squarefree condition is stable along an admissible edge because `p` is excluded from the parent. The special prime `2` is harmless rather than exceptional: `chi_4(2)=0`, so that direction has identically zero defect in the observed high-rank cell. The tie at `D=0` has been fixed explicitly, which is why the two odd-prime transition values in (28) are `-1` and `0` respectively.

Fan's 2025 weighted Erdős--Kac theorem is load-bearing only for the two Gaussian laws on the squarefree weight. The general normality of bounded strongly additive functions, the mod-4 prime-color interpretation, and multivariate/bivariate Erdős--Kac phenomena are classical or established neighboring theory; no novelty is claimed for them. A targeted literature search also found Granville--Soundararajan's sieve-theoretic Erdős--Kac framework and Mangerel's bivariate Erdős--Kac work as neighboring probabilistic machinery. Neither is needed for the proof above, and no source located in the audit states this line-specific common-source ancestry obstruction.

The durable delta is therefore not a new probabilistic theorem. It is the matched-control consequence for the Farey/Möbius source frontier: **once one marginal arithmetic coordinate is made visible, approximate ancestry can remain noncoercive by placing its sparse transition wall in an independent prime-factor coordinate.** This sharply limits what “joint scale-rank localization” can mean if it is to bridge to the physical Möbius source.

No RH estimate follows. The constructed source is not asserted to satisfy the physical Mertens envelope, the repeated-square Fourier target, or any other destination-side condition that would imply Franel--Landau. The result is an ancestry-to-source obstruction and should be used only at that boundary.

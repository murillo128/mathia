# FD-051 — finite square sieves extend universal terminal occupation to the square-root boundary

**Status:** `EXACT-DERIVED + SOURCE-INDEPENDENT + JOINT-NONSQUAREFREE-OCCUPATION + FINITE-SQUARE-SIEVE + TERMINAL-QUOTIENT-BULK + SQUARE-ROOT-BLOCK-BOUNDARY + MATCHED-CONTROL`.

`FD-038` proves that the complete nonsquarefree Jordan weight has the universal terminal occupation ratio

\[
\delta_{\rm ns}
=1-\zeta(3)c_{\rm sf}
=0.3558\ldots
\]

uniformly over arbitrary nonnegative shell profiles on quotient ranges `k<=H^alpha` with `alpha<1/3`. The cube-root restriction there comes from controlling the **entire** squarefree/nonsquarefree counting error by a square-root-plus remainder. For the accepted occupation clue, however, an exact asymptotic for the complete nonsquarefree union is stronger than necessary: a lower frame bound only needs a large fixed subset of nonsquarefree rows.

Keeping finitely many prime-square divisibility classes before taking the terminal block limit removes the square-root counting remainder completely. Each fixed finite square sieve has an `O(1)` weighted counting remainder, and finite square sieves exhaust the full weighted nonsquarefree density from below. Consequently the same constant `delta_ns` remains a universal **lower** terminal occupation barrier throughout every quotient range whose shortest block length tends to infinity:

\[
\boxed{
K_H^2/H\longrightarrow0
\quad\Longrightarrow\quad
\liminf_{H\to\infty}
\frac{U^{\rm term}_{H,D}(K_H)}
     {E^{\rm term}_{H,D}(K_H)}
\ge \delta_{\rm ns}.
}
\tag{1}
\]

This is uniform over arbitrary nonnegative shell profiles, even profiles depending on `H`. In particular it applies to the physical choice `F_H(k)=\mathcal H(k)^2` for every `K_H=o(\sqrt H)`. Already the single divisibility class `4\mid r` gives the explicit source-independent barrier `3/14`; adding finitely many prime squares raises the barrier monotonically to `delta_ns`.

The square-root scale is a genuine source-independent block boundary. At `H=r^2`, `k=r`, the quotient block is the singleton `{r}`. For squarefree `r` a profile concentrated on that block has positive terminal energy and zero nonsquarefree terminal energy. Thus the hypothesis that the minimum quotient-block length tends to infinity cannot simply be removed for arbitrary profiles.

The result does **not** settle the global occupation clue. A physical escape can still concentrate its energy on low Jordan rows / long quotient arguments, as already isolated more sharply by `FD-037`. What changes is the interpretation of the `1/3` threshold in `FD-038`: it is a boundary for identifying the complete nonsquarefree density by one global squarefree-counting asymptotic, not a boundary for a positive terminal occupation lower bound. No source-specific analysis is needed to retain the full density constant from below all the way to `o(\sqrt H)` quotient depth.

## 1. Terminal energies for an arbitrary nonnegative shell profile

Write

\[
w(r):=\frac{J_2(r)}{r^2}
=\prod_{p\mid r}(1-p^{-2}),
\qquad
a:=\frac1{\zeta(3)}.
\tag{2}
\]

Let `G_H(k)>=0` be any nonnegative profile; it may depend on `H`. For fixed `D` and an integer cutoff `K<H/(D+1)`, define

\[
E^{\rm term,G}_{H,D}(K)
:=
\sum_{\substack{D<r\le H\\ \lfloor H/r\rfloor\le K}}
 w(r)G_H(\lfloor H/r\rfloor),
\tag{3}
\]

\[
U^{\rm term,G}_{H,D}(K)
:=
\sum_{\substack{D<r\le H\\ \lfloor H/r\rfloor\le K\\ \mu(r)=0}}
 w(r)G_H(\lfloor H/r\rfloor).
\tag{4}
\]

The physical energy is recovered by

\[
G_H(k)=\mathcal H(k)^2.
\tag{5}
\]

Put

\[
Q_G(K):=
\sum_{k\le K}\frac{G_H(k)}{k(k+1)}.
\tag{6}
\]

For the exact quotient block

\[
\Gamma_H(k)
:=\left\{r:\frac{H}{k+1}<r\le\frac Hk\right\},
\tag{7}
\]

`FD-038` derives from

\[
w(n)=\sum_{d\mid n}\frac{\mu(d)}{d^2}
\tag{8}
\]

the bounded-remainder summatory law

\[
W(x):=\sum_{n\le x}w(n)=ax+O(1).
\tag{9}
\]

Hence the total Jordan weight of one quotient block is

\[
A_H(k):=\sum_{r\in\Gamma_H(k)}w(r)
=
\frac{aH}{k(k+1)}+O(1).
\tag{10}
\]

Summing (10) against `G_H(k)` gives

\[
\boxed{
E^{\rm term,G}_{H,D}(K)
=
aH Q_G(K)
+O\!\left(\sum_{k\le K}G_H(k)\right).
}
\tag{11}
\]

The head cutoff is absent from the block calculation because `K<H/(D+1)` implies every row in every block `k<=K` is already larger than `D`.

## 2. Every fixed finite square sieve has bounded weighted discrepancy

Let `\mathcal P` be a finite set of primes and define the fixed nonsquarefree row set

\[
\mathcal N_{\mathcal P}
:=
\{n:\ p^2\mid n\text{ for at least one }p\in\mathcal P\}.
\tag{12}
\]

For a squarefree integer

\[
m=\prod_{p\in S}p,
\qquad S\subseteq\mathcal P,
\]

put `q=m^2`. The Jordan weight on multiples of this fixed square has an `O(1)` summatory remainder. Indeed, using (8),

\[
\begin{aligned}
W_q(x)
&:=\sum_{\substack{n\le x\\q\mid n}}w(n)\\
&=
\sum_{d\ge1}\frac{\mu(d)}{d^2}
\left\lfloor\frac{x}{\operatorname{lcm}(q,d)}\right\rfloor\\
&=
c(q)x+O(1),
\end{aligned}
\tag{13}
\]

because the total floor error is bounded by `sum d^(-2)`, while extending the main term beyond `d<=x` costs

\[
x\sum_{d>x}d^{-3}=O(1).
\]

The Euler factors give

\[
\boxed{
c(m^2)
=a\prod_{p\mid m}
\frac{p^{-2}-p^{-4}}{1-p^{-3}}.}
\tag{14}
\]

Finite inclusion--exclusion over `\mathcal P` therefore yields

\[
\boxed{
W_{\mathcal P}(x)
:=\sum_{\substack{n\le x\\n\in\mathcal N_{\mathcal P}}}w(n)
=a\delta_{\mathcal P}x+O_{\mathcal P}(1),
}
\tag{15}
\]

where

\[
\boxed{
\delta_{\mathcal P}
:=
1-
\prod_{p\in\mathcal P}
\frac{1-p^{-2}-p^{-3}+p^{-4}}
     {1-p^{-3}}.
}
\tag{16}
\]

This is a finite sieve statement only; no squarefree short-interval theorem enters it. Taking the difference of (15) at the two endpoints of `Gamma_H(k)` gives

\[
B_{\mathcal P,H}(k)
:=
\sum_{\substack{r\in\Gamma_H(k)\\r\in\mathcal N_{\mathcal P}}}w(r)
=
\frac{a\delta_{\mathcal P}H}{k(k+1)}
+O_{\mathcal P}(1).
\tag{17}
\]

Every row counted in (17) is nonsquarefree. Therefore, after multiplying by an arbitrary `G_H(k)>=0` and summing,

\[
\boxed{
U^{\rm term,G}_{H,D}(K)
\ge
a\delta_{\mathcal P}H Q_G(K)
-O_{\mathcal P}\!\left(\sum_{k\le K}G_H(k)\right).
}
\tag{18}
\]

For the smallest sieve `\mathcal P={2}`, equation (16) gives

\[
\boxed{
\delta_{\{2\}}
=
\frac{2^{-2}-2^{-4}}{1-2^{-3}}
=
\frac3{14}.
}
\tag{19}
\]

Thus multiples of four alone already retain more than `21%` of the terminal Jordan energy asymptotically whenever the block-length condition below holds.

## 3. Long blocks upgrade every finite sieve to a uniform energy lower bound

Positivity of `G_H` gives the elementary comparison

\[
\sum_{k\le K}G_H(k)
\le
K(K+1)Q_G(K).
\tag{20}
\]

Assume now that `Q_G(K)>0` and

\[
\boxed{\frac{K(K+1)}H\longrightarrow0.}
\tag{21}
\]

Equivalently, the shortest quotient block in the terminal range has length tending to infinity. Equations (11), (18), and (20) give, for every fixed finite `\mathcal P`,

\[
E^{\rm term,G}_{H,D}(K)
=(a+o(1))H Q_G(K),
\tag{22}
\]

\[
U^{\rm term,G}_{H,D}(K)
\ge
(a\delta_{\mathcal P}-o_{\mathcal P}(1))H Q_G(K).
\tag{23}
\]

The errors are uniform in the choice and concentration of the nonnegative profile. Consequently

\[
\boxed{
\liminf_{H\to\infty}
\frac{U^{\rm term,G}_{H,D}(K)}
     {E^{\rm term,G}_{H,D}(K)}
\ge\delta_{\mathcal P}.
}
\tag{24}
\]

The constants increase monotonically as more primes are admitted. Since

\[
c_{\rm sf}
=
\prod_p(1-p^{-2}-p^{-3}+p^{-4}),
\qquad
a=\prod_p(1-p^{-3})=\frac1{\zeta(3)},
\tag{25}
\]

one has

\[
\delta_{\mathcal P}\uparrow
1-rac{c_{\rm sf}}a
=1-\zeta(3)c_{\rm sf}
=\delta_{\rm ns}
\tag{26}
\]

as `\mathcal P` exhausts the primes. Taking the liminf in `H` first and then enlarging the fixed finite sieve proves

\[
\boxed{
\liminf_{H\to\infty}
\frac{U^{\rm term,G}_{H,D}(K)}
     {E^{\rm term,G}_{H,D}(K)}
\ge\delta_{\rm ns}.
}
\tag{27}
\]

In particular, every `K_H=o(\sqrt H)` satisfies (21). Unlike `FD-038`, no restriction `K_H<=H^{1/3-o(1)}` is needed for this one-sided occupation theorem.

The order of limits is important. The finite prime set is fixed while `H` tends to infinity, so its block discrepancy remains `O_P(1)`. Only after the terminal-energy liminf is taken is the finite sieve enlarged. No uniform error estimate over a growing primorial is being assumed.

## 4. Why `FD-038` stops earlier and why this does not contradict it

`FD-038` proves the stronger asymptotic identity

\[
\frac{U^{\rm term}_{H,D}(K)}
     {E^{\rm term}_{H,D}(K)}
\longrightarrow\delta_{\rm ns}
\tag{28}
\]

for `K=H^alpha`, `alpha<1/3`. To obtain both sides of (28), it counts the **complete** nonsquarefree union, equivalently the complete squarefree complement. The available weighted squarefree summatory law has an `x^(1/2+o(1))` remainder. In a quotient block near `k`, the main block length is `H/k^2` while the endpoint size is `H/k`; balancing those scales produces the cube-root threshold.

For a lower occupation bound there is no need to control the large-prime-square tail from above. A fixed finite collection of prime squares already gives a subset of nonsquarefree rows with bounded counting discrepancy, and these finite subsets recover an arbitrarily large fraction of the limiting nonsquarefree density. The only geometric requirement left is that every terminal block be long compared with a fixed `O_P(1)` discrepancy, namely `H/K^2 -> infinity`.

Thus the two thresholds answer different questions:

\[
K\ll H^{1/3-o(1)}
\quad\text{supports exact complete-union density,}
\]

whereas

\[
K=o(\sqrt H)
\quad\text{already supports the full density constant as a lower bound.}
\]

The second statement is the one relevant to a frame/occupation obstruction.

## 5. The square-root block boundary is real for source-independent statements

The condition (21) cannot simply be extended to the full square-root endpoint for arbitrary profiles. Let `r>D` be squarefree and put

\[
H=r^2,
\qquad K=r.
\tag{29}
\]

Then

\[
\Gamma_{r^2}(r)
=
\left(\frac{r^2}{r+1},r\right]\cap\mathbb Z
=\{r\},
\tag{30}
\]

because

\[
\frac{r^2}{r+1}=r-1+\frac1{r+1}.
\]

Choose a nonnegative profile supported only at `k=r`. The terminal total energy is then

\[
E^{\rm term,G}_{r^2,D}(r)=w(r)G(r)>0,
\tag{31}
\]

while the unique contributing row is squarefree, so

\[
\boxed{
U^{\rm term,G}_{r^2,D}(r)=0.
}
\tag{32}
\]

Taking an unbounded sequence of squarefree `r` gives a matched source-independent obstruction exactly at `K=\sqrt H`. This does not say that the physical Mertens shell realizes such a profile. It shows only that the diverging-block hypothesis in (27) is genuine and that any theorem at the exact square-root boundary must use additional information about the source values.

## 6. Consequence for the physical occupation frontier

Return to

\[
G_H(k)=\mathcal H(k)^2.
\tag{33}
\]

For every deterministic `K_H=o(\sqrt H)` with `K_H->infinity`, (27) gives

\[
\boxed{
U^{\rm term}_{H,D}(K_H)
\ge
(\delta_{\rm ns}-o(1))
E^{\rm term}_{H,D}(K_H).
}
\tag{34}
\]

Hence any sequence with global occupation

\[
\frac{U_{H,D}}{E_{H,D}}\longrightarrow0
\tag{35}
\]

must satisfy

\[
\boxed{
\frac{E^{\rm term}_{H,D}(K_H)}{E_{H,D}}
\longrightarrow0
\qquad
\text{for every prescribed }K_H=o(\sqrt H).
}
\tag{36}
\]

This is not stronger than the source-specific cube-root-row concentration theorem `FD-037`; that result uses the physical one-Lipschitz increment law and already localizes a vanishing occupation sequence much farther into the low-row core. The new content is orthogonal: the positive terminal occupation law itself is **source-independent** and persists much deeper than the exact-density range of `FD-038`.

That distinction matters for the remaining program. Improving the complete squarefree counting remainder is not necessary merely to keep a positive nonsquarefree fraction in long quotient blocks. The surviving difficulty is genuinely the low-row hyperbola-sampling amplification and arithmetic placement isolated in `FD-037`, `FD-048`, and `FD-050`, not a loss of nonsquarefree density as terminal blocks approach the cube-root scale.

## 7. Prior-art and falsification boundary

Jordan totients, finite inclusion--exclusion over divisibility by prime squares, and the density of squarefree/nonsquarefree integers are classical. A targeted search around weighted Jordan-totient squarefree density, squarefree numbers in short intervals, and Farey/Mertens discrepancy located the expected classical squarefree-distribution literature, but no external theorem is needed for (13)--(27): the decisive `O_P(1)` remainder comes from fixing the square divisors before taking the block limit. No new literature dependency is therefore required in `SOURCES.md`, and no novelty is claimed for finite sieve algebra in isolation.

The durable line-level claim is the separation between **exact complete-union density** and a **one-sided occupation frame bound** in the quotient-shell geometry, together with the sharp source-independent singleton obstruction at the square-root endpoint.

The main falsification checks are exact. Equation (13) must retain an `O(1)` remainder for every fixed `q`; this follows only because `sum d^(-2)` converges and `lcm(q,d)>=d`. The finite prime set must stay fixed during the `H` limit. Positivity of the shell profile is essential in (18) and (20); signed profiles are outside the energy problem. Finally, (27) is a statement about the terminal quotient range only. It must not be cited as proving the global clue `U_(H,D)>=c_D E_(H,D)`, as improving a Franel--Landau exponent, or as ruling out the sparse low-row physical escape already matched by `FD-048`.

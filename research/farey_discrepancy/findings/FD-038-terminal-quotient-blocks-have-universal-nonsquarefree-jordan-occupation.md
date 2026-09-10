# FD-038 — terminal quotient blocks have universal nonsquarefree Jordan occupation

**Status:** `EXACT-DERIVED + WEIGHTED-SQUAREFREE-DENSITY + TERMINAL-QUOTIENT-BULK + JOINT-NONSQUAREFREE-OCCUPATION + CUBE-ROOT-BLOCK-THRESHOLD + PHYSICAL-SCHUR-TAIL`.

`FD-037` shows that a vanishing full nonsquarefree occupation ratio can only occur if essentially all of the physical Schur energy moves into the first `O(H^(1/3))` Jordan rows. That reduction leaves open whether the complementary high-row region already has a stable occupation law, or whether the physical quotient-shell values can bias even long Jordan blocks toward squarefree rows.

They cannot. In every quotient block that is long enough for the elementary weighted squarefree counting law to be uniform, the nonsquarefree Jordan weight has an asymptotically fixed positive density, independently of the quotient-shell source value carried by that block. Consequently every growing terminal quotient range `k<=H^alpha` with `alpha<1/3` has a universal nonsquarefree energy fraction.

Let

\[
w(r):=\frac{J_2(r)}{r^2},\qquad
\mathcal H(X):=\sum_{s\le X}\frac{\mathbf M(\lfloor X/s\rfloor)}s,
\]

and put

\[
Q(K):=\sum_{k\le K}\frac{\mathcal H(k)^2}{k(k+1)}.
\tag{1}
\]

For `K<H/(D+1)`, define the terminal quotient-shell energies

\[
E^{\mathrm{term}}_{H,D}(K)
:=\sum_{\substack{D<r\le H\\ \lfloor H/r\rfloor\le K}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\tag{2}
\]

\[
U^{\mathrm{term}}_{H,D}(K)
:=\sum_{\substack{D<r\le H\\ \lfloor H/r\rfloor\le K\\ \mu(r)=0}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\tag{3}
\]

Write

\[
a:=\frac1{\zeta(3)},
\tag{4}
\]

\[
c_{\mathrm{sf}}
:=\prod_p\left(1-p^{-2}-p^{-3}+p^{-4}\right),
\qquad
b:=a-c_{\mathrm{sf}}>0,
\tag{5}
\]

and

\[
\delta_{\mathrm{ns}}:=\frac ba
=1-\zeta(3)c_{\mathrm{sf}}
=0.3558\ldots .
\tag{6}
\]

Then for every fixed `D` and every fixed `0<alpha<1/3`, with `K_H=floor(H^alpha)`, one has

\[
\boxed{
E^{\mathrm{term}}_{H,D}(K_H)
=(a+o(1))H Q(K_H),
}
\tag{7}
\]

\[
\boxed{
U^{\mathrm{term}}_{H,D}(K_H)
=(b+o(1))H Q(K_H),
}
\tag{8}
\]

and therefore

\[
\boxed{
\frac{U^{\mathrm{term}}_{H,D}(K_H)}
{E^{\mathrm{term}}_{H,D}(K_H)}
\longrightarrow \delta_{\mathrm{ns}}>0.
}
\tag{9}
\]

The convergence is stronger than a statement about the physical Mertens source: the block argument below is uniform over every nonnegative shell profile replacing `mathcal H(k)^2`. The physical input is needed only for the consequence that `Q(K)->infinity`, already proved in `FD-033`.

Thus the terminal rows

\[
r>\frac{H}{K_H+1}=H^{1-\alpha+o(1)}
\tag{10}
\]

alone carry superlinear physical energy and a fixed positive nonsquarefree fraction. Any sequence with `U_(H,D)/E_(H,D)->0` must therefore exhibit a much stronger anomaly than low global nonsquarefree density: its sparse low-row energy must overwhelm the entire canonical terminal Mellin-energy bulk.

## 1. The full Jordan weight has an `O(1)` summatory remainder

The Jordan weight is

\[
w(n)=\prod_{p\mid n}(1-p^{-2})
=\sum_{d\mid n}\frac{\mu(d)}{d^2}.
\tag{11}
\]

Hence, for real `x>=1`,

\[
\begin{aligned}
W(x)
&:=\sum_{n\le x}w(n)\\
&=\sum_{d\le x}\frac{\mu(d)}{d^2}\left\lfloor\frac xd\right\rfloor\\
&=x\sum_{d\le x}\frac{\mu(d)}{d^3}+O\left(\sum_{d\le x}\frac1{d^2}\right)\\
&=\boxed{\frac{x}{\zeta(3)}+O(1)}.
\end{aligned}
\tag{12}
\]

No prime number theorem or cancellation estimate is used. The last error is bounded because the omitted tail in `sum mu(d)/d^3` contributes `O(1)` after multiplication by `x`.

Consequently the total Jordan weight in the exact quotient block

\[
\Gamma_H(k)
:=\left\{r:\frac{H}{k+1}<r\le\frac Hk\right\}
\tag{13}
\]

satisfies

\[
A_H(k)
:=\sum_{r\in\Gamma_H(k)}w(r)
=rac{aH}{k(k+1)}+O(1).
\tag{14}
\]

This already says that the full row weight in a quotient block is its Euclidean block length times the fixed mean `a`, up to a bounded discrepancy.

## 2. Weighted squarefree rows have a square-root-plus summatory remainder

Let

\[
f_{\mathrm{sf}}(n):=\mu(n)^2w(n).
\tag{15}
\]

This multiplicative function has Euler factor

\[
1+(1-p^{-2})p^{-s}.
\tag{16}
\]

Factor its Dirichlet series as

\[
\sum_{n\ge1}\frac{f_{\mathrm{sf}}(n)}{n^s}
=\zeta(s)H_{\mathrm{sf}}(s),
\tag{17}
\]

where

\[
H_{\mathrm{sf}}(s)
=\prod_p
\left(1-p^{-s}\right)
\left(1+(1-p^{-2})p^{-s}\right)
\tag{18}
\]

\[
=\prod_p
\left(1-p^{-(s+2)}-(1-p^{-2})p^{-2s}\right).
\tag{19}
\]

The Euler product in (19) is absolutely convergent for every `Re(s)>1/2`. Equivalently, if

\[
H_{\mathrm{sf}}(s)=\sum_{d\ge1}\frac{h(d)}{d^s},
\]

then for every fixed `sigma>1/2`,

\[
\sum_{d\ge1}\frac{|h(d)|}{d^\sigma}<\infty.
\tag{20}
\]

Since `f_sf=1*h`, elementary summation gives

\[
\begin{aligned}
W_{\mathrm{sf}}(x)
&:=\sum_{n\le x}f_{\mathrm{sf}}(n)\\
&=\sum_{d\le x}h(d)\left\lfloor\frac xd\right\rfloor\\
&=c_{\mathrm{sf}}x+O_\sigma(x^\sigma),
\end{aligned}
\tag{21}
\]

where

\[
c_{\mathrm{sf}}=H_{\mathrm{sf}}(1)
=\prod_p(1-p^{-2}-p^{-3}+p^{-4}).
\tag{22}
\]

Subtracting (21) from (12), the nonsquarefree weighted counting function

\[
W_{\mathrm{ns}}(x)
:=\sum_{\substack{n\le x\\\mu(n)=0}}w(n)
\]

satisfies, for every `sigma>1/2`,

\[
\boxed{
W_{\mathrm{ns}}(x)=bx+O_\sigma(x^\sigma).
}
\tag{23}
\]

The constant `b` is strictly positive. Indeed each Euler factor in (22) is strictly smaller than `1-p^{-3}`, so `c_sf<prod_p(1-p^{-3})=1/zeta(3)=a`. Thus the weighted nonsquarefree density is not merely positive; its proportion inside the full Jordan weight is the explicit constant `delta_ns` in (6).

For the quotient block (13), (23) gives

\[
B_H(k)
:=\sum_{\substack{r\in\Gamma_H(k)\\\mu(r)=0}}w(r)
=rac{bH}{k(k+1)}
+O_\sigma\left((H/k)^\sigma\right).
\tag{24}
\]

The error scale is the precise reason a cube-root threshold appears below: the block length is about `H/k^2`, while the unconditional weighted-squarefree counting discrepancy is square-root-plus in its endpoint size `H/k`.

## 3. Every growing terminal range below the cube-root quotient scale has a universal occupation ratio

The argument is source-independent. Let `F(k)>=0` be arbitrary and set

\[
Q_F(K):=\sum_{k\le K}\frac{F(k)}{k(k+1)}.
\tag{25}
\]

Equations (14) and (24) imply

\[
\sum_{k\le K}A_H(k)F(k)
=aHQ_F(K)+O\left(\sum_{k\le K}F(k)\right),
\tag{26}
\]

and

\[
\sum_{k\le K}B_H(k)F(k)
=bHQ_F(K)
+O_\sigma\left(
H^\sigma\sum_{k\le K}F(k)k^{-\sigma}
\right).
\tag{27}
\]

Positivity gives the uniform comparisons

\[
\sum_{k\le K}F(k)
\le K(K+1)Q_F(K),
\tag{28}
\]

and

\[
\sum_{k\le K}F(k)k^{-\sigma}
\le 2K^{2-\sigma}Q_F(K).
\tag{29}
\]

Therefore

\[
\sum_{k\le K}A_H(k)F(k)
=aHQ_F(K)
\left(1+O(K^2/H)\right),
\tag{30}
\]

while

\[
\sum_{k\le K}B_H(k)F(k)
=bHQ_F(K)
\left(1+O_\sigma(H^{\sigma-1}K^{2-\sigma})\right).
\tag{31}
\]

Now set `K=floor(H^alpha)` with `alpha<1/3`. Choose `sigma>1/2` so close to `1/2` that

\[
\sigma-1+\alpha(2-\sigma)<0.
\tag{32}
\]

Such a choice exists exactly because `alpha<1/3`. Then both relative errors in (30)--(31) tend to zero. Taking

\[
F(k)=\mathcal H(k)^2
\tag{33}
\]

proves (7)--(9). For fixed `D`, the terminal range eventually lies entirely above `D`, so the head cutoff does not alter the block calculation.

The exponent `1/3` in this theorem is again a method boundary, not an asserted arithmetic phase transition. At `k` near `H^(1/3)`, the quotient block has length of order `H^(1/3)` and sits near row size `H^(2/3)`; this is exactly where a generic `x^(1/2+o(1))` squarefree-counting remainder becomes comparable with the block length. No statement is made here about individual thinner blocks beyond that threshold.

## 4. The physical terminal bulk is already superlinear

For the physical source, (1) is the critical square sum already isolated in `FD-033`. That finding proves

\[
Q(K)\longrightarrow\infty.
\tag{34}
\]

Therefore (7)--(8) immediately give, for every fixed `0<alpha<1/3`,

\[
\boxed{
\frac{E^{\mathrm{term}}_{H,D}(\lfloor H^\alpha\rfloor)}H
\longrightarrow\infty,
}
\tag{35}
\]

\[
\boxed{
\frac{U^{\mathrm{term}}_{H,D}(\lfloor H^\alpha\rfloor)}H
\longrightarrow\infty.
}
\tag{36}
\]

Thus the unconditional superlinear energy of `FD-033` is already present in a terminal family of very high Jordan rows, and a fixed proportion `delta_ns` of that terminal energy is forced onto nonsquarefree rows. The effect does not depend on short-interval regularity of `mathcal H`; it comes from the fact that all rows in one quotient block carry exactly the same value `mathcal H(k)^2` while the row block itself is long enough to sample the weighted squarefree/nonsquarefree densities.

This also cleanly separates two mechanisms. `FD-037` uses source regularity to pair individual rows outside a low-row core. The present result uses no source regularity at all: it identifies a high-row bulk where occupation is automatic from block multiplicity.

## 5. A vanishing global occupation fraction now requires hyperbola-sampling amplification

Suppose along an unbounded sequence of horizons

\[
\frac{U_{H,D}}{E_{H,D}}\longrightarrow0.
\tag{37}
\]

Since `U_term<=U`, equation (8) forces, for every fixed `alpha<1/3`,

\[
\boxed{
\frac{E_{H,D}}
{H Q(\lfloor H^\alpha\rfloor)}
\longrightarrow\infty.
}
\tag{38}
\]

On the same sequence, `FD-037` gives

\[
\frac{S_{H,D}(\lceil H^{1/3}\rceil)}{E_{H,D}}
\longrightarrow1.
\tag{39}
\]

Combining (38)--(39),

\[
\boxed{
\frac{S_{H,D}(\lceil H^{1/3}\rceil)}
{H Q(\lfloor H^\alpha\rfloor)}
\longrightarrow\infty
\qquad(0<\alpha<1/3).
}
\tag{40}
\]

This is a sharper description of the only remaining escape. The high-row bulk has the expected nonsquarefree occupation automatically, so a bad horizon must be dominated by the sparse hyperbola samples

\[
\mathcal H(\lfloor H/r\rfloor),
\qquad r\le H^{1/3},
\tag{41}
\]

and those samples must outweigh by an unbounded factor every growing terminal critical square prefix `H Q(H^alpha)` with `alpha<1/3`.

Equivalently, any bound of the form

\[
E_{H,D}\ll H Q(\lfloor H^\alpha\rfloor)
\tag{42}
\]

for one fixed `alpha<1/3` would immediately imply a positive lower bound for `U/E` and hence, through `rho^2>=U`, a fixed projective gap. The live issue is therefore no longer weighted nonsquarefree density in ordinary quotient blocks. It is whether the actual Mertens quotient-shell source can create the exceptional **hyperbola-sampling amplification** in (38)--(41) on an unbounded sequence.

## 6. Prior-art, scope, and falsification boundary

The weighted mean identities used above are elementary consequences of the Euler products of `J_2(n)/n^2` and of the squarefree indicator. A targeted prior-art audit found classical Jordan-totient and squarefree mean-value formulas consistent with (12) and (21), but no external theorem is load-bearing: the required summatory estimates are derived directly in Sections 1--2. `SOURCES.md` therefore does not need a new dependency.

The durable contribution is not the existence of the weighted density constant in isolation. It is its uniform transfer through exact Farey/Mertens quotient blocks to the Schur-tail energy, including the source-independent threshold `alpha<1/3`, the physical superlinear terminal bulk (35)--(36), and the hyperbola-sampling necessary condition (38)--(40) for any vanishing global occupation fraction.

The finding is falsified if the weighted squarefree summatory remainder in (21), the uniform block errors in (30)--(31), or the identification of the terminal row range with `k<=K` is incorrect. It must not be cited as proving a positive lower bound for the full ratio `U_(H,D)/E_(H,D)`, as controlling individual quotient blocks at or beyond the cube-root quotient threshold, as improving the Franel--Landau exponent, or as proving RH. Its exact effect is to show that any remaining occupation failure is a sparse low-row sampling anomaly rather than a failure of nonsquarefree density in the long terminal quotient blocks.

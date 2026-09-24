# FD-304 — RH pushes capacity shells past `x^(2c)` and removes moving-start freedom

- **Date:** 2026-09-24
- **Status:** proved RH-conditional shell-depth localization, large-block population, and fixed-window correlation transfer
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / RH Mertens envelope / shell-depth localization / large-block population / common-window Möbius correlations / capacity obstruction
- **Depends on:** FD-300, FD-303
- **Classification:** `RH-CONDITIONAL + SHELL-DEPTH-LOCALIZATION + LARGE-BLOCK-POPULATION + COMMON-WINDOW-TRANSFER + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

Continue with

\[
U_N(q)=M(Nq)-M(N(q-1)),
\qquad
G_N(d)=\sum_{q\mid d}U_N(q),
\tag{1}
\]

\[
L_N(x)=\sum_{x<d\le2x}|G_N(d)|,
\qquad
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{2}
\]

and the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)}.
\tag{3}
\]

FD-300 then supplies a dyadic shell `Q<q<=2Q`, with `Q<=2x`, for which

\[
E_Q
:=
\frac1Q\sum_{Q<q\le2Q}|U_N(q)|^2
\ge
N x^{2c-o(1)}.
\tag{4}
\]

Assume RH and work in a fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)},
\qquad \lambda>0.
\tag{5}
\]

The RH Mertens estimate

\[
M(y)=O_\varepsilon(y^{1/2+\varepsilon})
\tag{6}
\]

forces every shell satisfying (4) to lie at depth

\[
\boxed{
Q\ge x^{2c-o(1)}.
}
\tag{7}
\]

Moreover, for every fixed `eta>0`, the same shell contains at least

\[
\boxed{
x^{2c-o(1)}}
\tag{8}

indices `q` for which

\[
\boxed{
|U_N(q)|
\ge
N^{1/2}x^{c-\eta}.
}
\tag{9}
\]

Consequently there are at least `x^(2c-o(1))` endpoint incidences, and at least half as many distinct grid points `Nj`, with

\[
\boxed{
|M(Nj)|
\ge
\frac12N^{1/2}x^{c-\eta}.
}
\tag{10}
\]

Thus the near-capacity route cannot be carried by one exceptional aligned block. Under RH it requires a population of power-many large aligned blocks, while the carrying shell itself cannot occur before denominator depth `x^(2c-o(1))`.

The shell-depth information also removes the residual **moving-start freedom** from the untwisted correlation family of FD-303. Define the canonical fixed-window correlation

\[
C_h^0(X)
:=
\sum_{X\le n<2X}\mu(n)\mu(n+h),
\qquad 1\le h<N,
\tag{11}
\]

where

\[
X=NQ.
\tag{12}
\]

FD-303 shows, once `lambda>1/(6c)`, that (3) forces at least

\[
N^{-1/2}x^{3c-o(1)}
\tag{13}
\]

distinct shifts `h=s-r` represented by positive moving-start correlations

\[
C_{r,s}(X)
:=
\sum_{X\le y<2X}\mu(y+r)\mu(y+s)
\ge
Q N^{-1/2}x^{3c-o(1)}.
\tag{14}
\]

For every such pair,

\[
|C_{r,s}(X)-C_h^0(X)|\le 2r\le2N.
\tag{15}
\]

Combining (7) and (14), the forced correlation scale dominates this boundary error by a fixed power whenever

\[
\boxed{
\lambda>
\frac{3}{10c}
=0.7228262519\ldots .
}
\tag{16}
\]

Hence, under RH and (3), every fixed depth satisfying (16) forces at least

\[
\boxed{
N^{-1/2}x^{3c-o(1)}
}
\tag{17}

distinct shifts `1<=h<N` with the **common-window, untwisted** lower bound

\[
\boxed{
C_h^0(X)
\ge
Q N^{-1/2}x^{3c-o(1)}.
}
\tag{18}
\]

The Farey reduction has therefore lost another degree of freedom: above (16), a near-capacity block-Mertens field cannot hide in correlations whose summation windows depend on `(r,s)`. It forces a power-sized family of ordinary two-point Möbius correlations on the same canonical interval `[X,2X)`.

## 1. RH localizes every capacity-bearing shell

Under RH, the standard Littlewood criterion gives (6) for every fixed `epsilon>0`. If `q~Q`, then

\[
\begin{aligned}
|U_N(q)|
&\le |M(Nq)|+|M(N(q-1))|\\
&\ll_\varepsilon (NQ)^{1/2+\varepsilon}.
\end{aligned}
\tag{19}
\]

In the fixed polynomial scaling (5), with `Q<=2x`, the arbitrary `epsilon` loss can be absorbed into `x^{o(1)}`. Therefore

\[
\max_{Q<q\le2Q}|U_N(q)|^2
\le
NQ x^{o(1)}.
\tag{20}
\]

Since an average cannot exceed its maximum, (4) and (20) imply

\[
N x^{2c-o(1)}
\le
NQx^{o(1)},
\tag{21}
\]

which proves (7).

This is a localization statement, not a contradiction. Since `2c=0.8300749986...<1`, the allowed range `Q<=2x` still contains such shells. What RH excludes is a shallower source of the required energy.

If one writes

\[
Q=x^{\alpha+o(1)},
\tag{22}
\]

then every capacity-bearing shell must satisfy

\[
\boxed{
\alpha\ge2c=0.8300749986\ldots .
}
\tag{23}
\]

At the shallow endpoint `alpha=2c`, the block amplitude required by FD-300 is already at the RH square-root envelope `(NQ)^(1/2)` up to subpolynomial factors.

## 2. The shell contains power-many large blocks

Fix `eta>0` and set

\[
t_\eta:=N^{1/2}x^{c-\eta}.
\tag{24}
\]

Let

\[
\mathcal H_\eta
:=
\{q\in(Q,2Q]:|U_N(q)|\ge t_\eta\}.
\tag{25}
\]

The complementary blocks contribute at most

\[
\sum_{q\notin\mathcal H_\eta}|U_N(q)|^2
\le
QNx^{2c-2\eta}.
\tag{26}
\]

while (4) gives total shell energy

\[
\sum_{Q<q\le2Q}|U_N(q)|^2
\ge
QNx^{2c-o(1)}.
\tag{27}
\]

Thus (26) is negligible compared with (27), and for sufficiently large parameters

\[
\sum_{q\in\mathcal H_\eta}|U_N(q)|^2
\ge
\frac12QNx^{2c-o(1)}.
\tag{28}
\]

Using the pointwise RH ceiling (20),

\[
|\mathcal H_\eta|\,NQx^{o(1)}
\ge
\sum_{q\in\mathcal H_\eta}|U_N(q)|^2,
\tag{29}
\]

so

\[
|\mathcal H_\eta|
\ge
x^{2c-o(1)}.
\tag{30}
\]

This proves (8)--(9). In the shell parametrization (22), the high-amplitude fraction is at least

\[
x^{2c-\alpha-o(1)},
\tag{31}
\]

and each selected block has amplitude at least the fraction

\[
x^{c-\alpha/2-\eta-o(1)}
\tag{32}
\]

of the RH square-root envelope at scale `NQ`. The population becomes densest and the amplitudes closest to the RH envelope precisely at the minimum shell depth `alpha=2c`.

For every `q` counted by (30),

\[
|M(Nq)-M(N(q-1))|\ge t_\eta
\tag{33}
\]

forces at least one endpoint to satisfy

\[
\max\{|M(Nq)|,|M(N(q-1))|\}
\ge\frac12t_\eta.
\tag{34}
\]

A grid point `Nj` can be an endpoint of at most two adjacent blocks. Therefore (30) yields at least `x^(2c-o(1))` distinct endpoint values after an immaterial factor two, proving (10).

## 3. RH converts the FD-303 family to one common window

FD-303 works with

\[
C_{r,s}(X)
=
\sum_{X\le y<2X}\mu(y+r)\mu(y+s),
\qquad 1\le r<s\le N.
\tag{35}
\]

Put `h=s-r` and make the change of variable `n=y+r`. Then

\[
C_{r,s}(X)
=
\sum_{X+r\le n<2X+r}\mu(n)\mu(n+h).
\tag{36}
\]

The intervals `[X+r,2X+r)` and `[X,2X)` have symmetric difference of exactly `2r` integer positions up to endpoint conventions. Since `|mu|<=1`,

\[
|C_{r,s}(X)-C_h^0(X)|\le2r\le2N,
\tag{37}
\]

which is (15).

The selected correlations supplied by FD-303 have size

\[
A_Q
:=
Q N^{-1/2}x^{3c-o(1)}.
\tag{38}
\]

Using the new shell floor (7),

\[
\frac{A_Q}{N}
\ge
N^{-3/2}x^{5c-o(1)}.
\tag{39}
\]

Under (5),

\[
N^{-3/2}x^{5c-o(1)}
=
N^{5c\lambda-3/2-o(1)}.
\tag{40}
\]

Therefore `A_Q/N` tends to infinity by a fixed power exactly when

\[
5c\lambda-\frac32>0,
\tag{41}
\]

which is (16). In that range the `2N` boundary discrepancy in (37) is `o(A_Q)`, so every selected positive moving-start correlation remains positive and of the same order after transfer to the canonical interval. Since FD-303 already paid the worst-case multiplicity of pairs sharing the same shift, its distinct-shift lower bound (13) passes unchanged to (17)--(18).

The threshold (16) automatically implies the weaker FD-303 prerequisite

\[
\lambda>\frac1{6c}=0.4015701399\ldots .
\tag{42}
\]

No additional correlation theorem is used in the transfer.

At balanced depth `lambda=1`, (7) reads

\[
Q\ge N^{0.8300749986\ldots-o(1)},
\qquad
X=NQ\ge N^{1.8300749986\ldots-o(1)}.
\tag{43}
\]

The forced canonical family then contains at least

\[
N^{3c-1/2-o(1)}
=
N^{0.7451124978\ldots-o(1)}
\tag{44}
\]

distinct shifts, and at the minimum shell depth each selected fixed-window correlation has size at least

\[
N^{5c-1/2-o(1)}
=
N^{1.5751874964\ldots-o(1)}.
\tag{45}
\]

Relative to the common interval length `X`, this is

\[
C_h^0(X)
\ge
X N^{-0.2548875022\ldots-o(1)}.
\tag{46}
\]

## 4. Prior-art boundary and ownership

The RH input in (6) is the classical Littlewood Mertens criterion already anchored in `SOURCES.md` through Titchmarsh--Heath-Brown. No stronger RH theorem is imported here.

A fresh prior-art check included Matomäki--Radziwiłł--Tao, *An averaged form of Chowla's conjecture*, Algebra & Number Theory **9** (2015), 2167--2196, DOI `10.2140/ant.2015.9.2167`, arXiv `1503.05121`. Their theorem gives averaged cancellation over growing boxes of shifts, with qualitative `o(H^kX)` and quantitative savings of roughly logarithmic strength. It does not by itself exclude the power-sized but polynomially sparse family at the polynomially shrinking correlation scale in (17)--(18). No averaged-Chowla result is used as an input to the proof, so no new external theorem becomes load-bearing here.

The Farey-owned content is the chain from the near-capacity premise to the shell energy of FD-300, then through RH to (7)--(10), and finally through the exact interval comparison to the common-window family (17)--(18). Once the latter family has been forced, proving that it cannot exist is a generic Möbius-correlation problem rather than a Farey-geometric one.

## 5. Adversarial audit and failure modes

The use of RH is essential to the new shell-depth and population conclusions. Without (6), the trivial block bound `|U_N(q)|<=N` recovers only the older source-energy ceiling and gives no denominator-depth floor comparable to (7).

The notation `x^{o(1)}` in (20) is legitimate only in the fixed polynomial scaling (5). For any requested power margin one first chooses the `epsilon` in (6) sufficiently small and then lets the parameters grow. No uniform statement over arbitrary relations between `N`, `Q`, and `x` is claimed.

The population bound (30) is stated for every fixed `eta>0`. The fixed margin is needed so that the energy below the threshold in (24) is genuinely negligible relative to (27). It is not claimed with `eta=o(1)` without further bookkeeping.

The endpoint consequence (10) loses at most a factor two because one grid value `M(Nj)` can serve the blocks `q=j` and `q=j+1`. No independence or sign assumption on neighboring blocks is used.

The common-window transfer is also one-way. Equation (37) is only a deterministic boundary comparison. The strict inequality in (16) is needed to make its `O(N)` cost polynomially smaller than the selected FD-303 correlation scale; no endpoint claim is made at `lambda=3/(10c)`.

The shell floor (7) is used in its weakest possible form in (39). A deeper actual shell only increases the correlation amplitude `A_Q`, so it makes the common-window transfer easier, not harder.

The averaged-Chowla literature does not create a contradiction by itself. A theorem asserting merely that the mean absolute correlation is `o(X)` can coexist with a family of `N^{-1/2}x^{3c-o(1)}` exceptional shifts whose individual correlations are a negative power of `X`. A quantitative comparison must beat the exact polynomial exponents forced here.

Finally, every implication remains necessary rather than sufficient. Large RH-scale Mertens endpoints, a deep shell, or even the fixed-window correlation family do not reconstruct large `L_N(x)`. They are increasingly source-generic consequences that any near-capacity Farey repair scenario must satisfy.

## Consequences for the research line

FD-300 reduced near-capacity block-Mertens mass to an anomalously energetic aligned shell. FD-303 showed that, above `lambda=1/(6c)`, that aligned energy necessarily spreads into a thick family of ordinary moving-start correlations.

FD-304 adds two RH-conditional rigidities. First, the carrying shell itself must occur at denominator depth at least `x^(2c-o(1))` and must contain `x^(2c-o(1))` genuinely large blocks. Second, once `lambda>3/(10c)=0.7228262519...`, that shell-depth floor makes the `O(N)` reindexing boundary negligible, so the whole FD-303 distinct-shift family can be placed on one common interval `[X,2X)`.

The live deep-regime obstruction is therefore sharper than “some source-selected two-point correlations are large.” Above (16), near-capacity Farey mass forces a polynomially thick family of standard fixed-window Chowla-type correlations at a source-selected scale `X=NQ`. Any theorem strong enough to exclude that family would close this branch of the Farey route there; obtaining such a theorem is now cleanly a Möbius-cancellation problem.
# FD-303 — Near-capacity aligned variance forces a thick untwisted correlation family

- **Date:** 2026-09-24
- **Status:** proved deterministic block-to-sliding amplification and ordinary-correlation population consequence
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / aligned short intervals / sliding Möbius energy / ordinary two-point correlations / capacity obstruction
- **Depends on:** FD-300, FD-301, FD-302
- **Classification:** `EXACT-DERIVED + SLIDING-ENERGY-AMPLIFICATION + ORDINARY-CORRELATION-POPULATION + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

Continue with

\[
U_N(q)=M(Nq)-M(N(q-1))
=\sum_{r=1}^{N}\mu(N(q-1)+r),
\tag{1}
\]

\[
G_N(d)=\sum_{q\mid d}U_N(q),
\qquad
L_N(x)=\sum_{x<d\le2x}|G_N(d)|,
\tag{2}
\]

and

\[
c:=1-\log_2(3/2)=0.4150374992\ldots .
\tag{3}
\]

Use the near-capacity scale

\[
B_{N,x}=\frac{N^{1/2}x^{1+c}}{\ell(x)},
\qquad
\ell(x)=x^{o(1)},
\tag{4}
\]

and assume, for some fixed `delta>0`,

\[
L_N(x)\ge \delta B_{N,x}.
\tag{5}
\]

FD-300 then supplies a dyadic shell `Q<q<=2Q` such that

\[
E_Q
:=
\frac1Q\sum_{Q<q\le2Q}|U_N(q)|^2
\gg
\frac{\delta^2 N x^{2c}}
{\ell(x)^2(\log x)^2}.
\tag{6}
\]

The new observation is that large energy only on the **aligned** starts `N(q-1)` cannot remain confined to those starts. Define the sliding length-`N` Möbius sum

\[
S_N(y):=M(y+N)-M(y)
=\sum_{y<n\le y+N}\mu(n),
\tag{7}
\]

put

\[
X=NQ,
\tag{8}
\]

and define its complete sliding second moment over the corresponding dyadic start interval by

\[
J_\mu(X,N)
:=
\sum_{X\le y<2X}|S_N(y)|^2.
\tag{9}
\]

Then, in every fixed polynomial-depth regime in which the right side of (6) tends to infinity,

\[
\boxed{
J_\mu(X,N)
\gg
Q E_Q^{3/2}.
}
\tag{10}
\]

Consequently the near-capacity premise (5) forces

\[
\boxed{
J_\mu(X,N)
\gg
\frac{\delta^3 Q N^{3/2}x^{3c}}
{\ell(x)^3(\log x)^3}.
}
\tag{11}
\]

If

\[
x=N^{\lambda+o(1)},
\qquad \lambda>0,
\tag{12}
\]

then, since `XN=N^2Q`,

\[
\boxed{
\frac{J_\mu(X,N)}{XN}
\ge
N^{3c\lambda-1/2-o(1)}.
}
\tag{13}
\]

Thus as soon as

\[
\boxed{
\lambda>\frac1{6c}
=0.4015701399\ldots,
}
\tag{14}
\]

a near-capacity Farey block field forces the complete sliding short-interval second moment to be **polynomially larger** than the diagonal scale `XN`.

This superdiagonal sliding energy has a second consequence that removes the periodic mask and the rational additive twist from the necessary obstruction altogether. For `1<=r<s<=N` define the ordinary untwisted correlation

\[
C_{r,s}(X)
:=
\sum_{X\le y<2X}
\mu(y+r)\mu(y+s).
\tag{15}
\]

When (14) holds, there is a set `P` of pairs `(r,s)` such that

\[
\boxed{
|P|
\gg
\frac{\delta^3 N^{1/2}x^{3c}}
{\ell(x)^3(\log x)^3}
}
\tag{16}
\]

and every pair in `P` satisfies the **positive** lower bound

\[
\boxed{
C_{r,s}(X)
\gg
\frac{\delta^3 QN^{-1/2}x^{3c}}
{\ell(x)^3(\log x)^3}.
}
\tag{17}
\]

Since a fixed shift `h=s-r` occurs for at most `N` pairs, the anomaly must occupy at least

\[
\boxed{
\frac{\delta^3 N^{-1/2}x^{3c}}
{\ell(x)^3(\log x)^3}
}
\tag{18}
\]

distinct shifts.

Therefore the near-capacity route cannot hide solely in one source-selected aligned interval, one same-block mask, or one rational Fourier mode. Above the threshold (14) it necessarily creates a polynomially thick family of ordinary, untwisted, moving-shift Möbius correlations on complete intervals of length `X`.

## 1. One large aligned block thickens into many nearby sliding starts

Let

\[
y_q=N(q-1),
\qquad
u_q:=|U_N(q)|=|S_N(y_q)|.
\tag{19}
\]

For every integer `t>=0`, shifting the start by `t` removes exactly `t` terms from the left end and introduces exactly `t` terms at the right end. Hence

\[
|S_N(y_q+t)-S_N(y_q)|\le 2t.
\tag{20}
\]

If

\[
0\le t\le \frac{\nu_q}{8},
\tag{21}
\]

then

\[
|S_N(y_q+t)|
\ge
\nu_q-2t
\ge
\frac{3\nu_q}{4}.
\tag{22}
\]

This is only the `2`-Lipschitz property of a sliding sum of coefficients bounded by one. No Möbius cancellation theorem is being used.

Because `nu_q<=N`, the interval of starts in (21) has length at most `N/8`. Distinct aligned starts `y_q` are separated by exactly `N`, so these one-sided thickening intervals are disjoint for distinct `q`. Moreover, for `Q<q<=2Q`,

\[
NQ\le y_q<2NQ,
\tag{23}
\]

and adding at most `N/8` still leaves the start below `2NQ`. Thus every thickened start counted below lies inside exactly the start interval defining (9); there is no endpoint leakage.

For `nu_q>=16`, the integer set

\[
0\le t\le \left\lfloor\frac{\nu_q}{8}\right\rfloor
\tag{24}
\]

contains `gg nu_q` starts, each contributing `gg nu_q^2` to (9). Therefore

\[
J_\mu(X,N)
\gg
\sum_{\substack{Q<q\le2Q\\ \nu_q\ge16}}
\nu_q^3.
\tag{25}
\]

The cutoff `16` is immaterial. The omitted blocks contribute at most `256Q` to the aligned second moment. Under (6) in a fixed polynomial-depth regime, `E_Q` tends polynomially to infinity, so for sufficiently large parameters

\[
\sum_{\substack{Q<q\le2Q\\ \nu_q\ge16}}
\nu_q^2
\ge
\frac12QE_Q.
\tag{26}
\]

For any nonnegative finite sequence, monotonicity of normalized `l^p` norms gives

\[
\sum \nu_q^3
\ge
Q\left(\frac1Q\sum \nu_q^2\right)^{3/2},
\tag{27}
\]

with the same inequality valid after restricting to the high-amplitude subset and padding by zeros. Combining (25)--(27) proves (10).

The exponent `3/2` is the crucial amplification. Energy at one aligned start of height `nu` buys not only `nu^2` at that point but `gg nu` nearby starts of comparable height, and therefore `gg nu^3` sliding energy.

## 2. FD-300 energy becomes superdiagonal sliding energy

Insert (6) into (10):

\[
\begin{aligned}
J_\mu(X,N)
&\gg
Q
\left(
\frac{\delta^2 N x^{2c}}
{\ell(x)^2(\log x)^2}
\right)^{3/2}\\
&=
\frac{\delta^3 QN^{3/2}x^{3c}}
{\ell(x)^3(\log x)^3},
\end{aligned}
\tag{28}
\]

which is (11).

Under (12), the fixed `delta`, logarithmic factors, and `ell(x)=x^{o(1)}` are swallowed by `N^{o(1)}`. Dividing by

\[
XN=N^2Q
\tag{29}
\]

gives (13).

The benchmark `XN` is not an imported probabilistic assertion. It is the exact scale of the diagonal contribution when the square in (9) is expanded, because there are `N` diagonal terms for each of `X` starts. Equation (13) therefore says something stronger and cleaner than merely “some aligned blocks are unusually large”: above (14), the **off-diagonal two-point contribution must dominate the entire diagonal by a power**.

At balanced depth `lambda=1`,

\[
3c-\frac12
=0.7451124978\ldots,
\tag{30}
\]

so near-capacity mass would force

\[
J_\mu(X,N)
\ge
XN\,N^{0.7451124978\ldots-o(1)}.
\tag{31}
\]

This is a much more distributed source anomaly than the existence of a single large aligned block.

## 3. Superdiagonal sliding energy forces many ordinary correlations

Expanding (9) exactly gives

\[
J_\mu(X,N)
=
\sum_{r,s=1}^{N}
\sum_{X\le y<2X}
\mu(y+r)\mu(y+s).
\tag{32}
\]

Separate the diagonal

\[
D
:=
\sum_{r=1}^{N}
\sum_{X\le y<2X}
\mu(y+r)^2
\le NX,
\tag{33}
\]

and use (15) for the off-diagonal terms. Since the expression is real and symmetric,

\[
J_\mu(X,N)
=
D+2\sum_{1\le r<s\le N}C_{r,s}(X).
\tag{34}
\]

When (14) holds, (13) implies `J_mu/(NX)->infinity` by a fixed power. Thus, for all sufficiently large parameters,

\[
T
:=
\sum_{1\le r<s\le N}C_{r,s}(X)
=
\frac{J_\mu-D}{2}
\gg J_\mu.
\tag{35}
\]

In particular `T` is positive; large sliding energy cannot be manufactured by negative pair correlations.

Let

\[
P_N=\frac{N(N-1)}2
\tag{36}
\]

be the number of pairs and set

\[
\theta:=\frac{T}{2P_N}.
\tag{37}
\]

Every correlation in (15) is at most `X`. If `K` pairs satisfy `C_{r,s}(X)>=theta`, then

\[
T
\le
KX+(P_N-K)\theta
\le
KX+\frac T2.
\tag{38}
\]

Therefore

\[
K\ge\frac{T}{2X}\gg\frac{J_\mu(X,N)}X.
\tag{39}
\]

Using (11) proves (16). For every one of these pairs,

\[
C_{r,s}(X)
\ge\theta
\gg
\frac{J_\mu(X,N)}{N^2},
\tag{40}
\]

which proves (17).

Finally, a given shift `h=s-r` can occur for at most `N` pairs `(r,s)`. Dividing (16) by `N` proves (18). No independence between shifts or intervals is assumed.

At balanced depth, the consequences calibrate to

\[
|P|
\ge
N^{1.7451124978\ldots-o(1)},
\tag{41}
\]

at least

\[
N^{0.7451124978\ldots-o(1)}
\tag{42}
\]

distinct shifts, and each selected pair has

\[
C_{r,s}(X)
\ge
X\,N^{-0.2548875022\ldots-o(1)}.
\tag{43}
\]

These exponents also respect the trivial combinatorial ceilings. At the FD-300 source-energy ceiling `lambda=1/(2c)`, the lower bounds in (16) and (18) reach `N^{2-o(1)}` pairs and `N^{1-o(1)}` distinct shifts respectively, but do not exceed them.

## 4. Relation to FD-301 and FD-302

FD-301 and FD-302 follow a sharp route: one large same-block correlation is Fourier-demasked into either an untwisted correlation or a low rational additive twist. That retains a strong per-correlation amplitude, but in the twisted branch it leaves a source-selected additive character to control.

The present argument takes a different projection of the same FD-300 source energy. Instead of selecting one same-block shift and Fourier-demasking its mask, it first **thickens the large aligned block sums in the start variable** and then expands the resulting complete sliding second moment. The price is a weaker individual correlation threshold and the depth condition (14). The gain is that the conclusion contains no mask and no additive character at all: it is a large family of ordinary products `mu(n)mu(n+h)`.

This route is especially useful in the entire frequency-localized regime of FD-302. That regime begins at

\[
\lambda>\frac1{4c}
=0.6023552099\ldots,
\tag{44}
\]

which is strictly above (14). Therefore every near-capacity scenario to which FD-302's shrinking Fourier arc applies already satisfies the stronger structural statement that a polynomially thick **untwisted** correlation family exists. The rational-twist branch may still carry additional information, but it is no longer the only generic arithmetic obstruction exposed by the Farey reduction.

Equivalently, any generic Möbius theorem giving the natural-scale estimate

\[
J_\mu(X,N)
\le
XN\,N^{o(1)}
\tag{45}
\]

uniformly for the source-selected `(X,N)` would immediately falsify the near-capacity route for every fixed

\[
\lambda>\frac1{6c}.
\tag{46}
\]

A correspondingly strong averaged two-point theorem over the family (15) would do the same. Once formulated in either of these ways, however, that missing estimate is a generic Möbius-cancellation statement rather than a Farey-geometric one.

## 5. Prior-art boundary and ownership

Classical and modern short-interval Möbius theory already studies cancellation of sums like (7), while averaged Chowla-type work studies families of ordinary shifted products like (15). The line's existing source anchors include quantitative almost-all short-interval results and higher-uniformity results, and prior-art search also finds the standard averaged-Chowla literature for growing shift boxes.

Those results define the correct boundary but are not imported into the proof above. The present obstruction asks for enough quantitative uniformity to beat a **polynomially shrinking** correlation threshold on a source-selected pair of scales, or equivalently to keep (9) near its diagonal scale. The currently anchored almost-all short-interval estimates and qualitative/logarithmic averaged-correlation savings do not by themselves supply that polynomial saving in the full moving-parameter regime forced here.

Accordingly, no new external theorem is load-bearing in FD-303 and `SOURCES.md` does not need a new dependency. The line-owned contribution is the exact reduction from the Farey capacity premise to (11), (16), and (18). Proving a sufficiently strong generic estimate for (9) or (15) is a neighboring Möbius-cancellation problem once this reduction has been made.

## 6. Adversarial audit and failure modes

The block-to-sliding step has several details that matter.

First, the thickening is one-sided. This is deliberate: for `Q<q<=2Q`, the aligned starts lie in `[NQ,2NQ)`, and a right shift of at most `N/8` stays inside that same start interval. A symmetric thickening would require restoring endpoint losses.

Second, (20) costs `2t`, not `t`, because `t` summands leave the window and `t` enter. The constants `1/8` and `3/4` in (21)--(22) already pay for both changes.

Third, thickening intervals from distinct aligned blocks are genuinely disjoint because their centers are `N` apart while every interval has length at most `N/8`. No overlap multiplicity is hidden in (25).

Fourth, the fixed cutoff `nu_q>=16` is harmless only because (6) makes the aligned mean square tend to infinity in the polynomial-depth near-capacity regime. Outside such an asymptotic regime the exact statement should retain the correction from blocks with `nu_q<16`; (10) is not claimed uniformly for arbitrary finite `(N,x)`.

Fifth, neither (10) nor the ordinary-correlation conclusion uses RH. RH entered earlier findings for other population and remainder statements, but the present implication is deterministic once the FD-300 shell-energy consequence is granted.

Sixth, (32)--(34) are exact on the common start variable `y`. Reindexing one pair by `n=y+r` would move its interval to `[X+r,2X+r)`, but no boundary approximation is needed or used while it remains in the form (15).

Seventh, a large number of anomalous pairs does not automatically mean the same number of distinct shifts. Equation (18) pays the worst-case multiplicity `N` explicitly.

Eighth, known averaged-Chowla statements cannot be compared only at the level `o(N^2X)`. The forced family may have individual correlations that are polynomially smaller than `X`; a qualitative or logarithmic averaged saving need not beat the power demanded by (17). No contradiction with existing averaged-correlation theory is claimed.

Ninth, the threshold `lambda>1/(6c)` is a threshold of this **cubic thickening plus diagonal comparison**. It is not asserted to be intrinsic. Better use of the exact sliding geometry, higher moments, or arithmetic cancellation could move it.

Finally, every implication is one-way. Superdiagonal sliding energy and thick ordinary correlation families are necessary consequences of near-capacity `L_N`; neither is sufficient to reconstruct the divisor-convolved field or its one-sided repair demand.

## Consequences for the research line

FD-299 removed sign polarization as an independent escape. FD-300 then reduced the magnitude problem to anomalously large aligned block variance. FD-301 and FD-302 converted one resulting same-block correlation into a sharply localized rational-twist obstruction.

FD-303 adds a complementary reduction: **aligned variance at the Farey capacity scale cannot remain an aligned phenomenon**. The elementary stability of a sliding bounded sum turns it into cubic sliding energy. Above `lambda=1/(6c)`, that energy cannot be absorbed by the diagonal and therefore forces a power-sized population of positive, ordinary, untwisted Möbius correlations across a power-sized family of shifts.

For the currently live deeper regime `lambda>1/(4c)`, any near-capacity scenario must therefore satisfy both the low-Fourier-arc obstruction of FD-302 and the thick untwisted-correlation obstruction here. A future falsification theorem may attack whichever representation is cheaper. In particular, a natural-scale bound for the complete sliding second moment (9) would eliminate the whole near-capacity block-Mertens route throughout that regime without analyzing the Farey divisor convolution any further.
# MC-201 — Small primorial support covariance is RH-scale harmless, leaving the mixed source aggregate as the hard mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `BOUNDARY/CONDITIONAL-GAIN`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-200` introduced the logarithmic-primorial sign/support decoder

\[
S=\frac{E_{1,2}-C_{1,2}}{Q/\phi-1},
\tag{1}
\]

where `S=G_y(X)` is the rough Möbius principal mode, `C_{1,2}` is the centered covariance between signed residue mass and square-free support, and `E_{1,2}` is the corresponding uncentered same-residue mixed source correlation. The previous finding correctly isolated the source aggregate as a new input, but left both numerator terms as potentially quantitative obstacles.

The support-covariance term can in fact be removed from the RH-scale budget by an elementary square-free progression estimate and the freedom to choose a sufficiently small fixed primorial exponent.

Fix a target `epsilon>0` and choose

\[
0<c<\min\left(\frac12,\frac\varepsilon4\right),
\qquad
y=c\log X,
\qquad
q=q_y=\prod_{p\le y}p,
\tag{2}
\]

with the notation of `MC-200`. Put

\[
P_y:=\prod_{p>y}\left(1-\frac1{p^2}\right).
\tag{3}
\]

For every reduced residue class `a mod q`, the square-free support count satisfies uniformly

\[
\boxed{
B_a=\frac Xq P_y+O(\sqrt X).
}
\tag{4}
\]

Consequently

\[
\boxed{
\left|v_a\right|
=\left|B_a-\frac Q\phi\right|
\ll\sqrt X
}
\tag{5}
\]

and, since `|u_a|\le 2(X/q+1)`, one gets

\[
\boxed{
|C_{1,2}|
\ll
\phi\left(\frac Xq+1\right)\sqrt X.
}
\tag{6}
\]

Moreover `(4)` implies

\[
\frac Q\phi-1
=(1+o(1))\frac Xq,
\tag{7}
\]

because `P_y\to1`, `q=X^{c+o(1)}`, and `c<1/2`, so the `O(\sqrt X)` error is smaller than `X/q`. Dividing `(6)` by `(7)` therefore gives

\[
\boxed{
\frac{|C_{1,2}|}{Q/\phi-1}
\ll
\phi\sqrt X
\le q\sqrt X
=X^{1/2+c+o(1)}.
}
\tag{8}
\]

With the choice `(2)`, the right side is `O_\varepsilon(X^{1/2+\varepsilon/2})` for sufficiently large `X`. Thus the decoder sharpens to

\[
\boxed{
S
=
\frac{E_{1,2}}{Q/\phi-1}
+O_\varepsilon(X^{1/2+\varepsilon/2}).
}
\tag{9}
\]

At the RH scale the transverse square-free-support covariance is therefore **already harmless**. The entire unresolved target-level burden of this quadratic route can be placed on the uncentered source aggregate `E_{1,2}`. In particular, it is enough to prove

\[
E_{1,2}
=O_\varepsilon\!\left(
\left(\frac Q\phi-1\right)X^{1/2+\varepsilon/2}
\right),
\tag{10}
\]

while any proof of `(10)` must remain independent of an assumed bound for `S`.

A complete-block audit shows why this is a real narrowing but not a hidden solution. Replacing `X` by

\[
X_0=q\left\lfloor\frac Xq\right\rfloor=Nq
\tag{11}
\]

changes the rough sum by at most `q=X^{c+o(1)}=o(X^{1/2})`, so square-root-scale control is unaffected. At this endpoint every reduced class contains exactly `N` source sites. Define the large-prime-square defect count

\[
D_a:=N-B_a,
\qquad
D:=\sum_aD_a=N\phi-Q.
\tag{12}
\]

Then `D_a` counts precisely the `q`-coprime sites that fail square-freeness; every such failure contains a square factor `p^2` with `p>y`. The support fluctuation is exactly the negative centered defect field,

\[
\boxed{
v_a=-\left(D_a-\frac D\phi\right).
}
\tag{13}
\]

If

\[
F:=\sum_a A_aD_a,
\tag{14}
\]

then direct expansion gives

\[
\boxed{
C_{1,2}=-F+\frac D\phi S,
\qquad
E_{1,2}=(N-1)S-F.
}
\tag{15}
\]

Hence

\[
E_{1,2}
=\left(N-1-\frac D\phi\right)S+C_{1,2}
=\left(\frac Q\phi-1\right)S+C_{1,2},
\tag{16}
\]

which is exactly `MC-200`'s decoder. The block form reveals the information content: the transverse support channel is only the variation of the square-defect field, while the uncentered source statistic retains the principal signed sum with coefficient asymptotic to `N`.

Therefore square-free support regularity does not make `(10)` automatic. Once `(8)` has discharged `C_{1,2}`, an RH-scale estimate for `E_{1,2}` is, up to the harmless covariance term and epsilon slack, quantitatively equivalent to the rough Mertens target itself. A useful continuation of this route must obtain `(10)` from arithmetic structure of the mixed source sum that does not reconstruct `S` through `(16)` or through the `d=1` term of the square-divisor expansion.

No improved estimate for `G_y(X)`, `M(X)`, or the Riemann zero set is claimed.

## 1. Uniform square-free support in each reduced class

For a reduced residue class `a mod q`, every `n\equiv a mod q` is coprime to `q`. Using the classical identity

\[
\mu^2(n)=\sum_{d^2\mid n}\mu(d),
\tag{17}
\]

one obtains

\[
B_a
=
\sum_{\substack{d\le\sqrt X\\(d,q)=1}}
\mu(d)
\#\left\{
 m\le\frac X{d^2}:
 d^2m\equiv a\pmod q
\right\}.
\tag{18}
\]

Because `(d,q)=1`, multiplication by `d^2` is invertible modulo `q`, so the inner set occupies one residue class modulo `q`. Uniformly in `a` and `d`,

\[
\#\left\{
 m\le\frac X{d^2}:
 d^2m\equiv a\pmod q
\right\}
=
\frac X{qd^2}+O(1).
\tag{19}
\]

Therefore

\[
B_a
=
\frac Xq
\sum_{\substack{d\le\sqrt X\\(d,q)=1}}
\frac{\mu(d)}{d^2}
+O(\sqrt X).
\tag{20}
\]

The absolutely convergent tail beyond `sqrt(X)` contributes `O(X^{-1/2})` to the sum, and for the primorial `q=q_y`,

\[
\sum_{(d,q)=1}\frac{\mu(d)}{d^2}
=
\prod_{p\nmid q}\left(1-\frac1{p^2}\right)
=P_y.
\tag{21}
\]

Equations `(20)`--`(21)` prove `(4)`. Averaging `(4)` over the `phi` reduced classes gives

\[
\frac Q\phi
=
\frac XqP_y+O(\sqrt X),
\tag{22}
\]

so subtracting proves `(5)`.

This is deliberately elementary. It uses no cancellation in `mu`, no zero-free continuation of `1/zeta`, and no correlation theorem.

## 2. The support covariance fits below the requested square-root budget

For every reduced class,

\[
|A_a|\le\frac Xq+1.
\tag{23}
\]

Also

\[
\frac{|S|}{\phi}
\le
\frac1\phi\sum_a|A_a|
\le\frac Xq+1,
\tag{24}
\]

so

\[
|u_a|\le2\left(\frac Xq+1\right).
\tag{25}
\]

Combining `(5)` and `(25)`,

\[
|C_{1,2}|
\le
\sum_a|u_a||v_a|
\ll
\phi\left(\frac Xq+1\right)\sqrt X,
\]

which is `(6)`.

The prime number theorem gives

\[
q_y=\exp(\vartheta(y))=X^{c+o(1)}.
\tag{26}
\]

Since `c<1/2`, `(22)` has main term `X^{1-c-o(1)}` and error `X^{1/2}`, while `P_y\to1`. Hence `(7)` follows. Dividing `(6)` by `(7)` and using `phi<=q` proves `(8)`.

The parameter freedom is load-bearing. For a fixed target `epsilon>0`, choosing any fixed `c<epsilon/4` leaves enough room to absorb the `o(1)` in `(26)` and gives

\[
\frac{|C_{1,2}|}{Q/\phi-1}
=O_\varepsilon(X^{1/2+\varepsilon/2}).
\tag{27}
\]

Thus a route targeting the usual `1/2+epsilon` exponent does not need a new theorem for `C_{1,2}`. It may spend the remaining epsilon slack on the source term `E_{1,2}`.

This does **not** say that `(6)` is strong enough for a fixed `c` near `1/2`. The conclusion uses the fact that the logarithmic-primorial exponent is a free fixed parameter that may be selected after the target epsilon is fixed.

## 3. Complete blocks identify the transverse support field with square defects

Let `X_0=Nq` as in `(11)` and redefine `A_a,B_a,S,Q,u_a,v_a` at `X_0`. Each reduced class has exactly `N` representatives in `[1,X_0]`, so

\[
B_a=N-D_a.
\tag{28}
\]

Averaging gives `Q=Nphi-D`; subtracting the means proves `(13)` immediately.

The same elementary estimate `(4)` now reads

\[
D_a
=N(1-P_y)+O(\sqrt X).
\tag{29}
\]

The prime number theorem and partial summation give

\[
\sum_{p>y}\frac1{p^2}
\sim\frac1{y\log y},
\tag{30}
\]

and because this tail tends to zero,

\[
1-P_y
\sim\frac1{y\log y}.
\tag{31}
\]

Since `N=X^{1-c+o(1)}` with `c<1/2`, the main term in `(29)` dominates `sqrt(X)`, and therefore uniformly in the reduced class

\[
\boxed{
D_a
\sim
\frac N{y\log y}.
}
\tag{32}
\]

Thus the square-free support field is extremely close to the constant field `N`; all of its nonprincipal information is carried by small fluctuations in a sparse population of failures caused by prime squares above the pre-sieving cutoff.

This is consistent with `MC-184`, which independently showed that logarithmic pre-sieving does not make unsigned square-free support a fixed-power short-interval variance obstruction. Here the same support regularity is used in a different geometry: reduced residue classes of the primorial and the specific mixed decoder of `MC-200`.

## 4. The uncentered source statistic retains the principal mode

At a complete block, write

\[
F=\sum_aA_aD_a.
\]

Because `B_a=N-D_a`,

\[
\sum_aA_aB_a
=N\sum_aA_a-\sum_aA_aD_a
=NS-F.
\tag{33}
\]

The diagonal identity from `MC-200`, `E_{1,2}=sum_a A_aB_a-S`, therefore gives

\[
E_{1,2}=(N-1)S-F.
\tag{34}
\]

Meanwhile `(13)` and `sum_a u_a=0` give

\[
C_{1,2}
=
-\sum_a
\left(A_a-\frac S\phi\right)
\left(D_a-\frac D\phi\right)
=-F+\frac D\phi S.
\tag{35}
\]

Subtracting `(35)` from `(34)` proves `(16)`.

The square-divisor expansion in `MC-200` makes the same point source-by-source. If its shift formula is summed over `r=hq`, `1<=h<=N-1`, the `d=1` terms are

\[
\sum_{h=1}^{N-1}
\left(
G_y((N-h)q)+G_y(Nq)-G_y(hq)
\right).
\tag{36}
\]

The first and third sums cancel under `h <-> N-h`, so `(36)` equals exactly

\[
(N-1)S.
\tag{37}
\]

The aggregate of all `d>=2` square-divisor terms is therefore exactly `-F`. If this residual is denoted by `R`, then

\[
R=-F,
\qquad
C_{1,2}-R=\frac D\phi S.
\tag{38}
\]

So deleting the obvious circular `d=1` contribution does not leave a free source estimate: it leaves the signed coupling to large-prime-square defects, and its difference from the centered covariance is again exactly the principal mode. Defect sparsity alone cannot create a power saving because the same factor `D` appears in the available numerator scale and in the decoder coefficient.

## 5. Prior art and novelty audit

The identity `(17)` and the `O(sqrt(X))` progression estimate `(4)` are classical elementary square-free counting mechanisms. `MC-S12` already anchors ordinary square-free counting in Montgomery--Vaughan; the argument above is its immediate reduced-residue-class specialization and is not claimed as new.

The literature on square-free integers in arithmetic progressions is substantially stronger than `(4)`. Hooley's 1975 work, Nunes's later refinements, and especially Alexander P. Mangerel, *Squarefree Integers in Arithmetic Progressions to Smooth Moduli*, Forum of Mathematics, Sigma 9 (2021), e72, DOI `10.1017/fms.2021.67`, prove asymptotic distribution results far beyond the elementary range. Mangerel's Theorem 1.1 gives a power-saving error for squarefree, sufficiently smooth moduli through `q<=X^(196/261-epsilon_0)`; the logarithmic primorial with any fixed `c<1/2` lies well inside that regime for large `X`. Thus there is no novelty claim in saying that the support field is well distributed modulo this `q`.

The project-level contribution is the quantitative insertion of that classical support fact into `MC-200`: because `c` is free, even the elementary `O(sqrt(X))` classwise error already makes the centered support covariance negligible at the requested `1/2+epsilon` output scale. This is distinct from `MC-184`, which concerns short-interval variance, and from `MC-188`, which controls the signed residue vector transversely but leaves its principal mode untouched.

A targeted prior-art search over square-free integers in arithmetic progressions, smooth moduli, squarefree/squarefull distributions, and mixed Möbius-support correlations found established square-free progression theory and the correlation results already recorded in `MC-200`, but no theorem that independently supplies the target growing-shift estimate `(10)` for the pre-sieved mixed source aggregate. This absence is not a novelty or impossibility claim; it marks the remaining literature-audit boundary.

## 6. Boundaries and falsification tests

- The RH-scale harmlessness statement is parameterized by the requested epsilon. The elementary bound does not make `C_{1,2}` harmless uniformly for every fixed `c<1/2`; choose `c` sufficiently smaller than the final exponent slack.
- Equation `(4)` concerns square-free support in **reduced** residue classes. Invertibility of `d^2 mod q` is essential; the same formula must not be transferred unchanged to non-coprime classes.
- The asymptotic denominator `(7)` uses `c<1/2`; this ensures the elementary `O(sqrt(X))` support error is smaller than the class main term `X/q`.
- The block reduction `(11)` changes the rough signed sum by fewer than `q` bounded terms. It is harmless only because the chosen `c<1/2`; no claim is made that block endpoints are exact replacements at larger primorial scales.
- `D_a` counts failures of square-freeness, not squarefull integers. A counted site need only contain at least one prime square `p^2`, and because it is coprime to `q`, such a prime satisfies `p>y`.
- The defect asymptotic `(32)` uses the prime-number-theorem tail `(30)`. The main term dominates the elementary `O(sqrt(X))` error only for fixed `c<1/2`.
- The estimate `(27)` controls only the **centered support covariance**. It gives no cancellation for `E_{1,2}` and therefore no new bound for `S` by itself.
- Equation `(38)` is an exact diagnostic, not a proposed way to estimate `S`: using it backwards with an assumed principal-mode bound would be circular.
- Mangerel's smooth-modulus theorem is prior-art orientation here, not a load-bearing input. No value of its unspecified power-saving exponent is assumed, and no RH-scale consequence is extracted from that theorem.

The elementary estimate is falsified if the congruence in `(19)` does not occupy exactly one class for `(d,q)=1`, or if the `O(1)` counting errors fail to sum to `O(sqrt(X))`. The covariance reduction is falsified if `(6)`--`(8)` fail after inserting those uniform support errors. The block diagnosis is falsified if `(13)`, `(34)`, or `(35)` fails on any finite ternary residue array with exactly `N` source sites per class.

## Consequence for the active frontier

The quadratic sign/support route has one fewer live quantitative obligation than `MC-200` left explicit. **There is no need to seek a new RH-scale theorem for the transverse support covariance:** at a sufficiently small logarithmic primorial it is already below the final `1/2+epsilon` budget by elementary square-free arithmetic.

The hard object is now the uncentered mixed source aggregate `E_{1,2}` itself. At complete blocks it retains the rough principal mode with coefficient asymptotic to the class length, while its genuinely transverse correction is carried only by large-prime-square defects. The next useful step is therefore not stronger unsigned support equidistribution. It is either a noncircular arithmetic estimate for the growing-shift aggregate `(10)`, or a different source relation whose principal contamination cancels before the target Mertens mode is inserted.
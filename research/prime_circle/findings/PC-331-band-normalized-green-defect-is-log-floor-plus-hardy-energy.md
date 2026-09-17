# PC-331 — band-normalized Green defect is a logarithmic floor plus Hardy-square energy

**Status:** `EXACT-DERIVED` + `STRUCTURAL-REDUCTION` + `PRIOR-ART-CLASSICALIZATION` for the growing-conductor Green branch of PC-323/PC-327/PC-328/PC-330.

PC-327 proves that, after the canonical cross-level Green operator is normalized by its universal Hilbert-band scale, the offset defect has a source-independent Hilbert-Schmidt divergence of order at least `log min(q,r)`. PC-328 then finds much larger normalized outliers for the raw canonical prime source, while PC-330 shows that subtracting the complete smooth Li/PNT profile removes every fixed low Fourier mode without removing the universal Hilbert channel.

The missing structural question is therefore: **what source-dependent quantity measures the excess above the universal logarithmic floor?** For comparable prime conductors the answer is exact up to absolute constants. It is the positive Hankel/Hardy-square energy of the two Fourier **energy profiles** with kernel `(i+j)^{-2}`.

More precisely, for distinct primes `q <= r <= 2q` and any nonzero centered periodic sources `a,b`, let `S_{a,b}` be the PC-327 Green offset defect and let

\[
D_{q,r}(a,b):=
\frac{\|S_{a,b}\|_2^2}{\mu(a)\mu(b)}.
\tag{1}
\]

With the same Fourier normalization as PC-327,

\[
\frac1q\sum_{i=1}^{q-1}|\widehat a(i)|^2=\mu(a),
\qquad
\frac1r\sum_{j=1}^{r-1}|\widehat b(j)|^2=\mu(b),
\tag{2}
\]

define

\[
\boxed{
E_{q,r}(a,b):=
\frac1{\mu(a)\mu(b)}
\sum_{i=1}^{q-1}\sum_{j=1}^{r-1}
\frac{|\widehat a(i)|^2|\widehat b(j)|^2}{(i+j)^2}.
}
\tag{3}
\]

Then there are absolute constants `c,C>0` and `q_0` such that, for `q>=q_0`,

\[
\boxed{
c\bigl(\log q+E_{q,r}(a,b)\bigr)
\le D_{q,r}(a,b)
\le
C\bigl(1+\log q+E_{q,r}(a,b)\bigr).
}
\tag{4}
\]

Thus the normalized Green defect has two quantitatively distinct pieces: a **universal logarithmic Hilbert floor**, already isolated in PC-327, and a **source-sensitive positive low-frequency concentration energy**. No phase information enters this second piece, consistently with the phase-gauge theorem of PC-325.

## 1. Exact PC-327 reduction

PC-327 gives probability weights

\[
p_i:=\frac{|\widehat a(i)|^2}{q\mu(a)},
\qquad
p'_j:=\frac{|\widehat b(j)|^2}{r\mu(b)},
\tag{5}
\]

and the exact representation

\[
D_{q,r}(a,b)
=
\sum_{i=1}^{q-1}\sum_{j=1}^{r-1}
 p_i p'_j\,T_{q,r}(i+j),
\tag{6}
\]

where

\[
T_{q,r}(\delta)
=
\frac1{qr}
\sum_{u=0}^{r-1}\sum_{v=0}^{q-1}
 g\!\left(
 \frac ur+\frac vq+\frac{\delta}{qr}
\right),
\tag{7}
\]

and

\[
g(\alpha)
=
(1-\alpha)^2
\sum_{s\ge0}
\frac1{(s+\alpha)^2(s+1)}.
\tag{8}
\]

The universal estimate from PC-327 is

\[
D_{q,r}(a,b)
\ge
\frac14\log\!\frac{q}{128},
\qquad q\le r,
\tag{9}
\]

for sufficiently large `q`. Equation (6) lets us isolate the source-sensitive part without introducing any new operator or arbitrary spectral wrapper.

## 2. A single corner cell forces the Hardy-square energy

Put `\delta=i+j`. Since `q<=r` and `1<=i<=q-1`, `1<=j<=r-1`,

\[
0<\frac{\delta}{qr}
\le \frac1q+\frac1r.
\tag{10}
\]

For `q,r>=5` the right-hand side is below `1/2`. Keeping only the `s=0` term of (8) gives, for `0<\alpha<=1/2`,

\[
g(\alpha)
\ge
\frac{(1-\alpha)^2}{\alpha^2}
\ge
\frac1{4\alpha^2}.
\tag{11}
\]

Now keep only the corner cell `u=v=0` in (7). Then

\[
T_{q,r}(\delta)
\ge
\frac1{qr}\,
 g\!\left(\frac{\delta}{qr}\right)
\ge
\frac{qr}{4\delta^2}.
\tag{12}
\]

Substitution in (6) and (5) yields the exact-scale lower bound

\[
\boxed{
D_{q,r}(a,b)
\ge
\frac14 E_{q,r}(a,b).
}
\tag{13}
\]

Combining (13) with the source-independent PC-327 bound (9),

\[
D_{q,r}(a,b)
\ge
\max\!\left\{
\frac14E_{q,r}(a,b),
\frac14\log\frac q{128}
\right\}
\ge
\frac18\left(
E_{q,r}(a,b)+\log\frac q{128}
\right).
\tag{14}
\]

This already proves the lower half of (4), after increasing the absolute threshold `q_0`.

## 3. The same energy controls the full defect from above

For the arguments occurring in (7), `0<\alpha<3` when `q<=r<=2q` and `q>=5`. From (8), using `(1-\alpha)^2<=4`, separating `s=0`, and bounding the remaining positive series by `\zeta(3)`,

\[
g(\alpha)
\le
4\left(\alpha^{-2}+\zeta(3)\right).
\tag{15}
\]

It remains to average `\alpha^{-2}` over the `(u,v)` rectangle. Write

\[
A_{q,r}(\delta)
:=
\frac1{qr}\sum_{u=0}^{r-1}\sum_{v=0}^{q-1}
\left(
\frac ur+\frac vq+\frac{\delta}{qr}
\right)^{-2}.
\tag{16}
\]

For fixed `u`, put

\[
A_u:=\frac ur+\frac{\delta}{qr}.
\tag{17}
\]

Since `x\mapsto(A_u+x)^{-2}` is positive and decreasing, the elementary sum-integral comparison gives

\[
\frac1q\sum_{v=0}^{q-1}
\left(A_u+\frac vq\right)^{-2}
\le
\frac1{qA_u^2}+\frac1{A_u}.
\tag{18}
\]

Averaging the first term in `u`, separating `u=0`, and using `r/q<=2`,

\[
\frac1r\sum_{u=0}^{r-1}\frac1{qA_u^2}
\le
\frac{qr}{\delta^2}+2\zeta(2).
\tag{19}
\]

For the second term,

\[
\frac1r\sum_{u=0}^{r-1}\frac1{A_u}
=
q\sum_{u=0}^{r-1}\frac1{qu+\delta}
\le
\frac q\delta+1+\log r.
\tag{20}
\]

Because `\delta=i+j<=q+r-2<=2r`,

\[
\frac q\delta
\le
\frac{2qr}{\delta^2}.
\tag{21}
\]

Hence

\[
A_{q,r}(\delta)
\le
\frac{3qr}{\delta^2}+\log r+C_0
\tag{22}
\]

with an absolute constant `C_0`. Equations (15)--(16) therefore imply

\[
T_{q,r}(\delta)
\le
\frac{12qr}{\delta^2}+4\log r+C_1.
\tag{23}
\]

Averaging against the probability weights in (6),

\[
\boxed{
D_{q,r}(a,b)
\le
12E_{q,r}(a,b)+4\log r+C_1.
}
\tag{24}
\]

Since `r<=2q`, this proves the upper half of (4).

The comparable-conductor hypothesis is used only to keep the harmless bulk term logarithmic in one scale. The corner term (12), and therefore the lower bound (13), does not require comparability.

## 4. Why this is the correct source-sensitive quantity

The kernel in (3) has the positive moment representation

\[
\frac1{(i+j)^2}
=
\int_0^1 t^{i+j-1}(-\log t)\,dt.
\tag{25}
\]

Consequently

\[
E_{q,r}(a,b)
=
\frac1{\mu(a)\mu(b)}
\int_0^1\frac{-\log t}{t}
\left(\sum_i|\widehat a(i)|^2t^i\right)
\left(\sum_j|\widehat b(j)|^2t^j\right)dt.
\tag{26}
\]

So `E_{q,r}` is a positive Hankel/Hardy-type bilinear energy of the normalized Fourier magnitude-square profiles. It strongly weights simultaneous concentration near the low-frequency corner `i+j<<q`, while diffuse energy gives only logarithmic size.

For example, if the normalized Fourier energies are spread at roughly constant density over their available frequencies, then the double sum of `(i+j)^{-2}` is `Theta(log q)`, and (4) gives

\[
D_{q,r}(a,b)=\Theta(\log q).
\tag{27}
\]

Source-dependent growth beyond the PC-327 floor therefore requires corresponding concentration of Fourier energy toward small `i+j`.

## 5. PC-328 and PC-330 become two regimes of the same formula

For the raw canonical prime source, PC-328 gives at every fixed nonzero frequency `h`

\[
\widehat a_q(h)
=
\frac{C_h}{\log q}+O_h\!\left(\frac1{\log^2 q}\right),
\qquad
\mu(a_q)\asymp\frac{\log q}{q},
\tag{28}
\]

with nonzero fixed coefficients for suitable `h`. A single fixed pair `(i,j)` in (3) then contributes

\[
E_{q,r}(a_q,a_r)
\gg
\frac{qr}{\log^3 q\,\log^3 r}
\tag{29}
\]

for comparable conductors. Its square-root scale is exactly the escaping normalized-outlier scale isolated in PC-328. Thus the PNT/Li packet of PC-328 is not an unrelated defect: it is a low-frequency concentration of the Hardy-square energy in (3).

PC-330 proves that subtracting the full Li/PNT profile makes every fixed residual mode absolutely much smaller than `1/log q`. However, the residual energy scale remains

\[
\mu(e_q)\asymp\frac{\log q}{q}.
\tag{30}
\]

Therefore fixed-frequency cancellation alone does **not** imply

\[
E_{q,r}(e_q,e_r)=O(\log q).
\tag{31}
\]

The normalization in (3) amplifies whatever Fourier energy remains relative to the shrinking source energy. The next quantitative obstruction after PC-330 is now explicit: one must control the **growing or mesoscopic Fourier-energy profile** strongly enough to show that its Hardy-square energy has no super-logarithmic excess. Fixed-`h` PNT transport estimates cannot establish that by themselves.

## 6. Novelty audit and falsification boundary

The kernel `(i+j)^{-2}`, its positive moment representation, and Hilbert/Hardy/Hankel inequalities are classical operator-theoretic territory; the Hilbert-matrix literature already anchored in `SOURCES.md` is the relevant prior-art boundary. Mean-square and Fourier-energy questions for exponential sums over primes are likewise classical analytic-number-theory territory. **No novelty claim is made for either ingredient separately.**

The project-local content is the exact reduction (6) inherited from the intrinsic prime-circle Green geometry together with the two-sided estimate (4): at comparable conductors, all Hilbert-Schmidt growth of the normalized canonical Green defect is, up to absolute constants, the universal logarithmic floor plus the single positive energy (3). This identifies what PC-327's universal divergence and PC-328's arithmetic outliers are measuring in one formula.

The reduction also strengthens the falsification boundary rather than producing an RH criterion. By PC-325, the complete Green relative spectral package is invariant under independent Fourier phases; (3) is even more explicitly phase-blind. A non-arithmetic matched control with the same Fourier magnitude profile has exactly the same `E_{q,r}` and the same Green defect bounds. Thus a large, small, or critically scaled Hardy-square energy is **not by itself a zeta-zero discriminator**.

A substantive continuation of this branch now needs one of two things:

- a theorem showing that the Li-subtracted canonical prime source has a distinctive mesoscopic Fourier-energy law, surviving matched magnitude-spectrum controls, whose failure/equivalence is genuinely tied to zero location; or
- a further intrinsic invariant that retains information discarded by the magnitude-square reduction of PC-325.

Without one of those destination theorems, further manipulation of the scalar quantity `E_{q,r}` would remain a classical positive-energy reformulation rather than progress toward RH.

# PC-332 — Green Hardy excess is a dyadic low-frequency concentration square function

**Status:** `EXACT-DERIVED` + `STRUCTURAL-REDUCTION` + `BOUNDARY` for the source-sensitive Hardy term isolated in PC-331.

PC-331 reduces the source-dependent part of the band-normalized cross-level Green defect to

\[
E_{q,r}(a,b)
=
\frac1{\mu(a)\mu(b)}
\sum_{i=1}^{q-1}\sum_{j=1}^{r-1}
\frac{|\widehat a(i)|^2|\widehat b(j)|^2}{(i+j)^2}.
\tag{1}
\]

The remaining question there is whether the Li-subtracted canonical prime source has enough mesoscopic Fourier concentration for this term to exceed the universal logarithmic Hilbert floor. The Hardy kernel admits an exact multiscale reduction that makes that question concrete.

Define the probability weights already used in PC-331,

\[
p_i:=\frac{|\widehat a(i)|^2}{q\mu(a)},
\qquad
p'_j:=\frac{|\widehat b(j)|^2}{r\mu(b)},
\tag{2}
\]

and their cumulative distributions

\[
A(x):=\sum_{1\le i\le x}p_i,
\qquad
B(x):=\sum_{1\le j\le x}p'_j.
\tag{3}
\]

For integer `H>=1`, put

\[
\Gamma_a(H)
:=\frac{qA(H)}H
=\frac1{H\mu(a)}\sum_{1\le i\le H}|\widehat a(i)|^2,
\tag{4}
\]

with the sum truncated at `q-1`, and define `\Gamma_b(H)` analogously. Then

\[
\boxed{
\frac{3}{16}
\sum_{m\ge0}\Gamma_a(2^m)\Gamma_b(2^m)
\le
E_{q,r}(a,b)
\le
3
\sum_{m\ge0}\Gamma_a(2^m)\Gamma_b(2^m).
}
\tag{5}
\]

For comparable conductors `q<=r<=2q`, the part of the dyadic sum after `2^m` exceeds both Fourier supports is `O(1)`. Thus only `O(log q)` scales can contribute materially. In particular, the surviving PC-331 problem is not merely cancellation of each fixed Fourier coefficient: it is a **uniform multiscale spectral-flatness problem**.

## 1. Exact layer-cake reduction

Let independent random variables `I,J` have laws `p,p'`, and set

\[
K:=\mathbb E\frac1{(I+J)^2}
=\frac{E_{q,r}(a,b)}{qr}.
\tag{6}
\]

The elementary layer-cake identity

\[
\frac1{(i+j)^2}
=2\int_{i+j}^{\infty}t^{-3}\,dt
\tag{7}
\]

gives

\[
K
=2\int_2^{\infty}t^{-3}\Pr(I+J\le t)\,dt.
\tag{8}
\]

Monotonicity gives, for every `t`,

\[
A(t/2)B(t/2)
\le
\Pr(I+J\le t)
\le
A(t)B(t).
\tag{9}
\]

Consequently,

\[
\frac12\int_1^{\infty}\frac{A(u)B(u)}{u^3}\,du
\le K\le
2\int_1^{\infty}\frac{A(u)B(u)}{u^3}\,du.
\tag{10}
\]

Now split the integral into dyadic intervals. Since `A,B` are increasing and

\[
\int_{2^m}^{2^{m+1}}u^{-3}\,du
=\frac38\,4^{-m},
\tag{11}
\]

we obtain, with

\[
S:=\sum_{m\ge0}4^{-m}A(2^m)B(2^m),
\tag{12}
\]

the bounds

\[
\frac38S
\le
\int_1^{\infty}A(u)B(u)u^{-3}\,du
\le
\frac32S.
\tag{13}
\]

Equations (10)--(13) imply

\[
\frac{3}{16}S\le K\le3S.
\tag{14}
\]

Finally, `qr S=\sum_m\Gamma_a(2^m)\Gamma_b(2^m)`, proving (5).

## 2. Diffuse profiles and escape must be multiscale

Equation (5) gives a direct sufficient condition for the generic PC-331 scale. If

\[
\Gamma_a(2^m),\Gamma_b(2^m)\le M
\tag{15}
\]

through all dyadic scales below the Fourier supports, then for comparable `q,r`,

\[
E_{q,r}(a,b)=O(M^2\log q).
\tag{16}
\]

Conversely, if `E_{q,r}` is superlogarithmic, then because only `O(log q)` relevant dyadic scales occur, at least one scale `H=2^m` satisfies

\[
\Gamma_a(H)\Gamma_b(H)
\gg \frac{E_{q,r}(a,b)}{\log q}.
\tag{17}
\]

Thus any escaping Green-Hardy excess has a concrete low/mesoscopic frequency scale where cumulative spectral mass is anomalously concentrated; it cannot remain a purely global or fixed-mode phenomenon.

For the algebraic diagonal diagnostic obtained by setting the two profiles equal,

\[
E_{q,q}(a,a)
\asymp
\sum_{m\lesssim\log q}\Gamma_a(2^m)^2+O(1).
\tag{18}
\]

This is literally a dyadic square function of cumulative Fourier-energy concentration. Equation (18) is a diagnostic for the Hardy kernel; it is not an assertion that the distinct-conductor Green block of PC-331 has become a same-shell operator.

## 3. It recovers the raw-prime outlier scale

PC-328 supplies a fixed nonzero mode `h_0` for the raw canonical prime source `a_q` with

\[
|\widehat a_q(h_0)|\asymp\frac1{\log q},
\qquad
\mu(a_q)\asymp\frac{\log q}{q}.
\tag{19}
\]

At any fixed dyadic `H>=h_0`, (4) therefore gives

\[
\Gamma_{a_q}(H)
\gg\frac{q}{\log^3 q}.
\tag{20}
\]

Equation (5) then reproduces the PC-328/PC-331 scale

\[
E_{q,r}(a_q,a_r)
\gg
\frac{qr}{\log^3q\,\log^3r},
\tag{21}
\]

up to absolute constants. The large raw-prime outlier is therefore the extreme first-scale failure of the same multiscale-flatness criterion.

## 4. The Li-subtracted frontier becomes a concrete theorem target

For the smooth-Li-subtracted residual `e_q` of PC-330, fixed-frequency cancellation alone does not decide (1). Equation (5) shows that the uniform dyadic estimate

\[
\boxed{
\sum_{1\le h\le H}|\widehat e_q(h)|^2
\lesssim
H\mu(e_q)
\qquad
(1\le H\lesssim q,\ H\text{ dyadic})
}
\tag{22}
\]

is sufficient to force

\[
E_{q,r}(e_q,e_r)=O(\log q)
\tag{23}
\]

for comparable conductors. Conversely, any superlogarithmic Hardy excess must exhibit a dyadic scale violating the corresponding bounded-concentration condition. This replaces the vague question of a surviving “mesoscopic Fourier profile” by a falsifiable cumulative-energy estimate.

The reduction also preserves the information-loss obstruction of PC-325: `\Gamma_a`, (5), and hence this entire diagnostic depend only on Fourier magnitudes/autocorrelation. Any non-prime control with matched magnitude spectrum has the same multiscale profile and the same Hardy excess. Even a failure of (22) for primes would therefore not by itself produce an RH mechanism; it would still have to survive matched-autocorrelation controls and acquire an independent connection to zeta zeros or the critical line.

## 5. Prior-art audit and research consequence

The analytic mechanism behind (7)--(14) is classical Hardy/Hankel territory: layer-cake representations, cumulative-mass criteria, and dyadic decompositions of positive decreasing kernels are standard tools in weighted Hardy inequalities. A representative anchor is G. Sinnamon and V. D. Stepanov, *The Weighted Hardy Inequality: New Proofs and the Case p=1*, J. London Math. Soc. 54 (1996), 89--101, DOI `10.1112/jlms/54.1.89`. The Hilbert/Hankel background already anchored in `SOURCES.md` supplies the surrounding operator-theoretic context.

Accordingly, **the Hardy/dyadic inequality itself is not claimed as novel**. The durable line-local result is the exact constant-factor identification of the specific PC-331 prime-circle Green Hardy term with cumulative low-frequency concentration across dyadic scales. It sharpens the surviving branch to one concrete question: after canonical Li subtraction, does the prime-circle source satisfy (22) uniformly, or is there a genuine mesoscopic scale where normalized cumulative Fourier energy escapes? Either outcome is testable without introducing a new operator, normalization, or spectral wrapper.
# FD-301 — Aligned masked Möbius correlation demasks to a rational additive-twist anomaly

- **Date:** 2026-09-24
- **Status:** proved exact Fourier demasking and RH-conditional shell-population consequence
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / aligned short intervals / periodic mask / discrete Fourier decomposition / shifted Möbius correlation / capacity obstruction
- **Depends on:** FD-298, FD-299, FD-300
- **Classification:** `EXACT-DERIVED + FOURIER-DEMASKING + RH-CONDITIONAL-POPULATION + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

Let

\[
U_N(q)=M(Nq)-M(N(q-1))
=\sum_{r=1}^{N}\mu(N(q-1)+r),
\tag{1}
\]

and

\[
G_N(d)=\sum_{q\mid d}U_N(q),
\qquad
L_N(x)=\sum_{x<d\le2x}|G_N(d)|.
\tag{2}
\]

Write

\[
c=1-\log_2(3/2)=0.4150374992\ldots
\tag{3}
\]

and use the near-capacity scale

\[
B_{N,x}=\frac{N^{1/2}x^{1+c}}{\ell(x)},
\qquad \ell(x)=x^{o(1)}.
\tag{4}
\]

Assume, as in the fixed-margin form of FD-300, that for some fixed `delta>0`,

\[
L_N(x)\ge \delta B_{N,x}.
\tag{5}
\]

Then FD-300 supplies a dyadic shell `Q<q<=2Q` and a shift `1<=h<N` for which

\[
\frac1Q\sum_{Q<q\le2Q}|U_N(q)|^2
\gg
\frac{\delta^2 N x^{2c}}
{\ell(x)^2(\log x)^2}
= N x^{2c-o(1)},
\tag{6}
\]

and the aligned same-block correlation

\[
C_{Q,h}
:=
\sum_{Q<q\le2Q}
\sum_{r=1}^{N-h}
\mu(N(q-1)+r)\mu(N(q-1)+r+h)
\tag{7}
\]

satisfies

\[
C_{Q,h}
\gg
\frac{\delta^2 Q x^{2c}}
{\ell(x)^2(\log x)^2}
=Qx^{2c-o(1)}.
\tag{8}
\]

The new point is that the growing-period **same-block mask in (7) can be removed exactly at only logarithmic cost**. Define `e(t)=exp(2 pi i t)`. Then there is some residue `a mod N` such that

\[
\boxed{
\left|
\sum_{NQ<n\le2NQ}
\mu(n)\mu(n+h)e(an/N)
\right|
\gg
\frac{\delta^2 Qx^{2c}}
{\ell(x)^2(\log x)^2(2+\log N)}
=Qx^{2c-o(1)}.
}
\tag{9}
\]

The frequency may be zero and, when nonzero, its reduced denominator may divide `N`; no primitive-frequency claim is made. The shift may also depend on `N,Q,x`.

Moreover (8) itself forces

\[
\boxed{N-h\ge x^{2c-o(1)}.}
\tag{10}
\]

Under RH, in any fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{11}
\]

the same near-capacity premise also forces the shell to be deep and the large block increments to have power-sized population:

\[
\boxed{Q\ge x^{2c-o(1)},}
\tag{12}
\]

and

\[
\boxed{
\#\left\{
q\in(Q,2Q]:
|U_N(q)|\ge N^{1/2}x^{c-o(1)}
\right\}
\ge x^{2c-o(1)}.
}
\tag{13}
\]

A quantifier-safe version of (13) is: for every fixed `eta>0`, for all sufficiently large `x`, one may choose the FD-300 shell so that

\[
\#\left\{
q\in(Q,2Q]:
|U_N(q)|\ge N^{1/2}x^{c-\eta}
\right\}
\gg_{\eta,\lambda,\delta}
 x^{2c-2\eta}.
\tag{14}
\]

Thus a near-capacity Farey block-Mertens field cannot be supported by a few isolated aligned intervals. Under RH it requires a power-sized family of nearly extremal block sums, while unconditionally its masked two-point consequence already forces a single large **unmasked rational additive mode**.

## 1. Exact Fourier removal of the same-block mask

For fixed `N` and `h`, let `w_{N,h}` be the `N`-periodic function whose values on representatives `1,...,N` are

\[
w_{N,h}(r)
=
\begin{cases}
1,&1\le r\le N-h,\\
0,&N-h<r\le N.
\end{cases}
\tag{15}
\]

Then (7) is exactly

\[
C_{Q,h}
=
\sum_{NQ<n\le2NQ}
\mu(n)\mu(n+h)w_{N,h}(n).
\tag{16}
\]

The last `h` residue classes in each aligned block receive weight zero, so (16) includes exactly the pairs whose two endpoints remain in the same length-`N` block. There is no endpoint approximation here.

Use the normalized discrete Fourier coefficients

\[
\widehat w(a)
=
\frac1N\sum_{r=1}^{N-h}e(-ar/N),
\qquad a\in\mathbb Z/N\mathbb Z.
\tag{17}
\]

Fourier inversion gives

\[
w_{N,h}(n)
=
\sum_{a\bmod N}
\widehat w(a)e(an/N),
\tag{18}
\]

hence

\[
C_{Q,h}
=
\sum_{a\bmod N}
\widehat w(a)S_{Q,h}(a),
\tag{19}
\]

where

\[
S_{Q,h}(a)
:=
\sum_{NQ<n\le2NQ}
\mu(n)\mu(n+h)e(an/N).
\tag{20}
\]

It remains to price the Fourier mask. The zero coefficient obeys

\[
|\widehat w(0)|=\frac{N-h}{N}\le1.
\tag{21}
\]

For `a` nonzero modulo `N`, write

\[
k=\min(a,N-a),
\qquad 1\le k\le N/2.
\tag{22}
\]

The geometric-sum formula gives

\[
|\widehat w(a)|
\le
\frac1{N|\sin(\pi a/N)|}.
\tag{23}
\]

Since `sin y >= 2y/pi` for `0<=y<=pi/2`,

\[
|\sin(\pi a/N)|
=\sin(\pi k/N)
\ge \frac{2k}{N},
\tag{24}
\]

and therefore

\[
|\widehat w(a)|\le\frac1{2k}.
\tag{25}
\]

At most two residues have a given `k`, so

\[
\boxed{
\sum_{a\bmod N}|\widehat w(a)|
\le 2+\log N.
}
\tag{26}
\]

Combining (19), (26), and the positive lower bound (8),

\[
\max_{a\bmod N}|S_{Q,h}(a)|
\ge
\frac{C_{Q,h}}{2+\log N},
\tag{27}
\]

which proves (9).

The logarithm in (26) is the ordinary `l^1` Fourier cost of a sharp interval mask on a cyclic group. No arithmetic estimate is used in this demasking step.

## 2. The overlap length is itself power-sized

Every summand in (7) has absolute value at most one, and there are at most `Q(N-h)` of them. Hence

\[
C_{Q,h}\le Q(N-h).
\tag{28}
\]

Together with (8),

\[
N-h
\gg
\frac{\delta^2 x^{2c}}
{\ell(x)^2(\log x)^2}
=x^{2c-o(1)},
\tag{29}
\]

which is (10).

Thus the correlation forced by FD-300 cannot be hidden in an overlap containing only a subpower number of pairs per block. Even if the selected shift is close to `N`, the surviving same-block overlap has length at least the same `x^(2c-o(1))` scale that appears in the capacity tariff.

## 3. RH forces a power-sized population of large aligned blocks

Now assume RH and (11). The standard Littlewood criterion, already anchored in `SOURCES.md`, gives for every fixed `epsilon>0`

\[
M(y)=O_\epsilon(y^{1/2+\epsilon}).
\tag{30}
\]

Uniformly for `q in (Q,2Q]`, this implies

\[
|U_N(q)|^2
\le
\bigl(|M(Nq)|+|M(N(q-1))|\bigr)^2
\ll
NQ\,x^{o(1)}.
\tag{31}
\]

The `x^{o(1)}` form is uniform because `NQ` is polynomial in `x` under (11) and `Q<=2x`.

Comparing (31) with the shell average (6) immediately yields

\[
Q\ge x^{2c-o(1)},
\tag{32}
\]

proving (12).

For the population statement, fix `eta>0`. Absorb the subpolynomial factors in (6) so that, for all sufficiently large `x`,

\[
\sum_{Q<q\le2Q}|U_N(q)|^2
\gg
QNx^{2c-\eta}.
\tag{33}
\]

Choose the `epsilon` in (30) small enough, in terms of `eta` and the fixed polynomial-depth exponent, that

\[
\max_{Q<q\le2Q}|U_N(q)|^2
\ll
NQx^{\eta}.
\tag{34}
\]

Let

\[
\mathcal A
=
\left\{
q\in(Q,2Q]:
|U_N(q)|^2\ge Nx^{2c-2\eta}
\right\},
\qquad K=|\mathcal A|.
\tag{35}
\]

The complement contributes at most

\[
QNx^{2c-2\eta},
\tag{36}
\]

which is negligible compared with (33). The set `mathcal A` contributes at most, by (34),

\[
K\,NQx^{\eta}.
\tag{37}
\]

Consequently

\[
K\,NQx^{\eta}
\gg
QNx^{2c-\eta},
\tag{38}
\]

and therefore

\[
K\gg x^{2c-2\eta}.
\tag{39}
\]

This is (14), hence (13). Since `K<=Q`, it also reproves the shell-depth floor (12).

The conclusion is stronger than the statement that one anomalous block exists. Near-capacity post-convolution mass forces at least `x^(2c-o(1))` aligned blocks whose Mertens increments are at the FD-300 near-extremal scale.

## 4. Balanced-depth calibration

At balanced depth `x=N^{1+o(1)}`, the three forced scales become

\[
2c
=0.8300749985\ldots,
\qquad
\frac12+c
=0.9150374992\ldots,
\qquad
1-2c
=0.1699250014\ldots.
\tag{40}
\]

Thus, under RH, a near-capacity scenario requires a shell with

\[
Q\ge N^{0.8300749985\ldots-o(1)},
\tag{41}
\]

at least

\[
N^{0.8300749985\ldots-o(1)}
\tag{42}
\]

aligned blocks satisfying

\[
|U_N(q)|
\ge
N^{0.9150374992\ldots-o(1)}.
\tag{43}
\]

The selected correlation shift also satisfies

\[
N-h\ge N^{0.8300749985\ldots-o(1)},
\tag{44}
\]

and some rational additive mode obeys

\[
|S_{Q,h}(a)|
\ge
Q N^{0.8300749985\ldots-o(1)}.
\tag{45}
\]

Relative to the `NQ` terms in the full twisted sum, this is a bias of size at least

\[
N^{-0.1699250014\ldots-o(1)}.
\tag{46}
\]

This remains a polynomially decaying relative bias, so there is no contradiction with the trivial bound. It is nevertheless far stronger than a merely logarithmic anomaly.

## 5. Prior-art boundary

The Fourier decomposition (17)--(27) is elementary harmonic analysis on the cyclic group `Z/NZ`; no novelty is claimed for that identity or for the `O(log N)` Fourier `l^1` norm of an interval.

The mathematical delta is its application to the exact FD-300 mask. The same-block qualification there looked, a priori, like a special growing-period correlation that might require a separate arithmetic theory. Equations (19)--(27) show that it cannot hide the required capacity-sized mass: a large masked correlation necessarily exposes a comparably large ordinary shifted Möbius product against one rational additive character.

The short-interval Möbius results already anchored in `SOURCES.md` do not directly close (9). Matomäki--Teräväinen gives logarithmic cancellation for single Möbius sums in sufficiently long individual short intervals. Matomäki--Radziwiłł and the later almost-all higher-uniformity results give powerful exceptional-set or phase-uniformity information for single multiplicative-function sums, but (20) contains the product `mu(n)mu(n+h)` with a shift that may grow with `N`. The product is not itself a multiplicative function in `n`, and the required pointwise growing-shift two-point estimate is not supplied by those one-function theorems.

Likewise, a fixed-shift or logarithmically averaged Chowla statement would not by itself control (20): here both `h` and the rational frequency `a/N` may vary with the scale, and the average is an ordinary dyadic interval average. No claim is made that this hybrid correlation problem is new in analytic number theory; the durable claim is the exact reduction of the Farey capacity scenario to it.

No new external theorem is load-bearing, so `SOURCES.md` does not need a new anchor for this finding.

## 6. Adversarial audit and failure modes

The demasking conclusion is only necessary. A large twisted mode in (9) does not imply that the Fourier combination (19) is large with the correct positive sign, and it certainly does not imply that the original divisor convolution `G_N` has near-capacity `l^1` mass.

The frequency selected by (27) need not be nonzero. If `a=0`, the anomaly is an untwisted shifted correlation. If `a!=0`, the fraction `a/N` may reduce to a smaller denominator. The result therefore gives a rational additive mode of denominator dividing `N`, not a primitive denominator-`N` mode.

The full sum (20) includes pairs that cross the original aligned block boundaries. Those contributions are not being asserted small. Their exact cancellation across Fourier modes reconstructs the mask in (19). The point of (27) is only that at least one unmasked mode must itself be large.

The RH population conclusion is separate from the unconditional Fourier step. Equations (12)--(14) use only the RH half-power growth bound for `M`; without such a pointwise envelope, the shell second moment could in principle be concentrated on fewer blocks.

The population lower bound does not say that a positive proportion of all `Q` blocks are large. When `Q` is near `x`, the forced `x^(2c-o(1))` population is still sparse. Existing almost-all short-interval theorems therefore cannot be invoked merely by comparing proportions; their quantitative threshold and exceptional-set hypotheses must match the aligned deterministic grid and the much smaller polynomial amplitude in (43).

Finally, the result does not remove the Farey divisor-replication problem. FD-300 used the exact physical replication ledger to derive the source-energy and masked-correlation tariff. FD-301 only shows that the **last mask itself costs at most a logarithm**. Once one reaches (20), however, the remaining estimate is a generic growing-shift Möbius-correlation problem rather than additional Farey geometry.

## Consequences for the research line

FD-300 left two possible interpretations of its masked positive correlation requirement: either the aligned block boundary was an essential new obstruction, or it was only a presentation of a more standard arithmetic anomaly. FD-301 resolves that distinction:

\[
\boxed{
\text{near-capacity Farey mass}
\Longrightarrow
\text{large rationally twisted two-point Möbius mode},
}
\tag{47}
\]

with only a logarithmic loss after the exact Farey-to-block reduction has already been made.

Under RH, the same premise additionally forces a power-sized population of large aligned block sums and locates the responsible dyadic shell at

\[
Q\ge x^{2c-o(1)}.
\tag{48}
\]

So a future source-side falsification can now attack two sharper necessary signatures: the shell must contain `x^(2c-o(1))` near-extremal block increments, and its aggregate positive same-block correlation must survive in at least one rational additive Fourier mode at size `Qx^(2c-o(1))`.

This also marks the ownership boundary more cleanly. Establishing (47) belongs to `farey_discrepancy` because its premise and mask arise from the physical divisor-replication/capacity mechanism. Proving a general theorem that rules out the resulting growing-shift rationally twisted Möbius correlation after the Farey geometry has disappeared is naturally a `mobius_cancellation` problem under the line mandate.

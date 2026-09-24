# FD-302 — Near-capacity demasking collapses to a low block-Fourier arc

- **Date:** 2026-09-24
- **Status:** proved exact low-frequency localization and zero-mode/twisted dichotomy for the FD-301 anomaly
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / same-block mask / finite Fourier tail / shifted Möbius correlation / capacity obstruction / frequency localization
- **Depends on:** FD-300, FD-301
- **Classification:** `EXACT-DERIVED + FOURIER-TAIL-LOCALIZATION + ZERO-MODE-DICHOTOMY + CAPACITY-BOUNDARY + ROUTE-REDUCTION`

## Claim

Continue with the near-capacity scenario of FD-301. Thus

\[
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{1}
\]

and for some dyadic shell `Q<q<=2Q` and some `1<=h<N`, the same-block correlation

\[
C_{Q,h}
:=
\sum_{Q<q\le2Q}
\sum_{r=1}^{N-h}
\mu(N(q-1)+r)\mu(N(q-1)+r+h)
\tag{2}
\]

is positive and satisfies

\[
C_{Q,h}\ge QY,
\tag{3}
\]

where, after shrinking the fixed implied constant from FD-301 if necessary,

\[
Y
\asymp
\frac{\delta^2x^{2c}}
{\ell(x)^2(\log x)^2}
=x^{2c-o(1)}.
\tag{4}
\]

FD-301 expands the sharp same-block mask in additive characters modulo `N` and obtains

\[
C_{Q,h}
=
\sum_{a\bmod N}\widehat w(a)S_{Q,h}(a),
\tag{5}
\]

with

\[
S_{Q,h}(a)
:=
\sum_{NQ<n\le2NQ}
\mu(n)\mu(n+h)e(an/N).
\tag{6}
\]

The new point is that a capacity-sized value in (3) cannot be carried only by arbitrary or high block-Fourier modes. Put

\[
k(a):=\min(a,N-a)
\qquad (0\le a<N)
\tag{7}
\]

and

\[
K_0:=
\left\lceil
2\left(\frac{N}{Y}\right)^2
\right\rceil.
\tag{8}
\]

Whenever `K_0<=N/2`, the complete contribution of all frequencies with `k(a)>K_0` has modulus at most `QY/2`. Consequently one has the following dichotomy:

\[
\boxed{
|S_{Q,h}(0)|\ge \frac{QY}{4}
}
\tag{9}
\]

or there exists a **nonzero** residue `a mod N` with

\[
\boxed{
1\le k(a)\le K_0,
\qquad
|S_{Q,h}(a)|
\ge
\frac{QY}{4(1+\log K_0)}.
}
\tag{10}
\]

Thus the rational twist exposed by FD-301 may be taken either to be the ordinary untwisted two-point correlation, or to lie inside a quantitatively small arc around frequency zero. It is not necessary to search all `N` additive characters.

Moreover, in the genuinely twisted branch, where (9) fails, the selected shift is forced away from **both** block endpoints:

\[
\boxed{
 h>\frac{3Y}{4},
 \qquad
 N-h\ge Y.
}
\tag{11}
\]

The second inequality was implicit in FD-301; the first follows from comparing the unmasked zero mode with the same-block prefix. Therefore escaping the untwisted correlation forces a power-sized growing shift as well as a low block-Fourier frequency.

In a fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)},
\tag{12}
\]

one has

\[
Y=N^{2c\lambda-o(1)},
\qquad
K_0=N^{2-4c\lambda+o(1)}.
\tag{13}
\]

Hence a genuine power localization occurs as soon as

\[
\boxed{
\lambda>\frac1{4c}
=0.6023552099\ldots.
}
\tag{14}
\]

In this range the nonzero alternative satisfies

\[
\boxed{
\left\|\frac aN\right\|_{\mathbb R/\mathbb Z}
\le
N^{1-4c\lambda+o(1)}=o(1).
}
\tag{15}
\]

FD-300 already shows that the near-capacity block-Mertens route is impossible for

\[
\lambda>\frac1{2c}=1.2047104198\ldots.
\tag{16}
\]

Thus throughout the live depth interval

\[
\frac1{4c}<\lambda\le\frac1{2c},
\tag{17}
\]

the arbitrary rational-twist family of FD-301 collapses to a shrinking block-Fourier arc; at the upper endpoint only `N^{o(1)}` Fourier indices remain.

## 1. Fourier-tail energy of the sharp same-block mask

Let

\[
m=N-h
\tag{18}
\]

and let `w=w_{N,h}` be the `N`-periodic interval mask from FD-301,

\[
w(r)=1_{1\le r\le m}.
\tag{19}
\]

Its normalized discrete Fourier coefficients are

\[
\widehat w(a)
=
\frac1N\sum_{r=1}^{m}e(-ar/N).
\tag{20}
\]

For `a!=0 mod N`, FD-301 already derived

\[
|\widehat w(a)|
\le
\frac1{2k(a)}.
\tag{21}
\]

The `l^1` consequence of (21) gave the logarithmic demasking cost in FD-301. For localization we instead use its `l^2` tail. For every integer `K>=1`,

\[
\begin{aligned}
\sum_{k(a)>K}|\widehat w(a)|^2
&\le
2\sum_{k>K}\frac1{4k^2}\\
&\le
\frac1{2K}.
\end{aligned}
\tag{22}
\]

No arithmetic information has entered. This is only the square-summable tail of the discrete Fourier transform of an interval.

## 2. The full twisted spectrum has a trivial but sufficient Parseval budget

Set

\[
v(n)=\mu(n)\mu(n+h)
\tag{23}
\]

for `NQ<n<=2NQ`, and group it by residue class modulo `N`:

\[
V(r)
:=
\sum_{\substack{NQ<n\le2NQ\\ n\equiv r\pmod N}}
v(n).
\tag{24}
\]

Because the interval `(NQ,2NQ]` consists of exactly `Q` complete blocks of length `N`, every residue class contains exactly `Q` values of `n`. Since `|v(n)|<=1`,

\[
|V(r)|\le Q.
\tag{25}
\]

Equation (6) is precisely the discrete Fourier transform of `V`:

\[
S_{Q,h}(a)
=
\sum_{r\bmod N}V(r)e(ar/N).
\tag{26}
\]

Parseval, with this unnormalized transform, gives

\[
\sum_{a\bmod N}|S_{Q,h}(a)|^2
=
N\sum_{r\bmod N}|V(r)|^2
\le
N^2Q^2.
\tag{27}
\]

This estimate deliberately uses no Möbius cancellation. It is the worst-case energy budget for an arbitrary bounded two-point sequence on the `Q` aligned blocks.

Combining (22) and (27) by Cauchy-Schwarz yields the key tail estimate

\[
\boxed{
\left|
\sum_{k(a)>K}
\widehat w(a)S_{Q,h}(a)
\right|
\le
\frac{NQ}{\sqrt{2K}}.
}
\tag{28}
\]

Thus the high-frequency contribution is small once `K` exceeds the square of `N/Y`. This is the step that FD-301's pure `l^1` demasking did not retain.

## 3. Capacity-sized correlation must enter the low arc

Choose `K=K_0` from (8), and suppose `K_0<=N/2`. Then

\[
\frac{NQ}{\sqrt{2K_0}}
\le
\frac{QY}{2}.
\tag{29}
\]

Since `C_{Q,h}>=QY`, equations (5) and (28) imply

\[
\left|
\sum_{k(a)\le K_0}
\widehat w(a)S_{Q,h}(a)
\right|
\ge
\frac{QY}{2}.
\tag{30}
\]

If (9) holds, the first branch of the claim is proved. Otherwise

\[
|S_{Q,h}(0)|<\frac{QY}{4}.
\tag{31}
\]

Since `|\widehat w(0)|=m/N<=1`, subtracting the zero-frequency term from (30) leaves

\[
\left|
\sum_{\substack{0<k(a)\le K_0}}
\widehat w(a)S_{Q,h}(a)
\right|
\ge
\frac{QY}{4}.
\tag{32}
\]

For the nonzero low modes, (21) gives

\[
\sum_{0<k(a)\le K_0}|\widehat w(a)|
\le
\sum_{k\le K_0}\frac1k
\le
1+\log K_0.
\tag{33}
\]

Pigeonholing (32) against (33) proves (10).

The point is not merely that some Fourier mode is large; FD-301 already showed that. The new information is that, once the masked correlation reaches the Farey capacity scale, the square-summable high-frequency tail is too small to carry it. The anomaly must already be visible among only `O(K_0)` modes nearest zero.

## 4. If the zero mode is small, the shift is power-sized on both sides

The zero mode is the complete untwisted shifted correlation

\[
S_{Q,h}(0)
=
\sum_{NQ<n\le2NQ}\mu(n)\mu(n+h).
\tag{34}
\]

The masked correlation `C_{Q,h}` contains exactly the first `m=N-h` residue positions of each of the `Q` aligned blocks. Therefore

\[
S_{Q,h}(0)-C_{Q,h}
=
\sum_{Q<q\le2Q}
\sum_{r=N-h+1}^{N}
\mu(N(q-1)+r)
\mu(N(q-1)+r+h).
\tag{35}
\]

There are exactly `Qh` summands in (35), each of modulus at most one, so

\[
|S_{Q,h}(0)-C_{Q,h}|\le Qh.
\tag{36}
\]

If the zero-mode branch (9) fails, then by (3), (31), and (36),

\[
Qh
\ge
C_{Q,h}-|S_{Q,h}(0)|
>
\frac{3QY}{4},
\tag{37}
\]

which gives the first inequality in (11).

The second follows directly from the number of terms in (2):

\[
C_{Q,h}\le Q(N-h),
\tag{38}
\]

so (3) implies

\[
N-h\ge Y.
\tag{39}
\]

Hence a putative escape from a large ordinary two-point correlation cannot move to a microscopic or endpoint shift. It must use a shift whose two same-block sides both retain the same capacity power scale.

## 5. Polynomial-depth calibration

Under (12), equation (4) becomes

\[
Y=N^{2c\lambda-o(1)}.
\tag{40}
\]

Substitution into (8) gives

\[
K_0
=N^{2-4c\lambda+o(1)}.
\tag{41}
\]

The localization is genuinely smaller than the full `N`-frequency family exactly when

\[
2-4c\lambda<1,
\tag{42}
\]

which is (14). In that range

\[
\frac{K_0}{N}
=N^{1-4c\lambda+o(1)}
=o(1),
\tag{43}
\]

proving (15).

At balanced depth `lambda=1`,

\[
2c=0.8300749985\ldots,
\tag{44}
\]

and

\[
2-4c=0.3398500029\ldots,
\qquad
1-4c=-0.6601499971\ldots.
\tag{45}
\]

Therefore a near-capacity scenario forces either

\[
|S_{Q,h}(0)|
\ge
Q N^{0.8300749985\ldots-o(1)},
\tag{46}
\]

or a genuinely nonzero mode satisfying

\[
1\le k(a)
\le
N^{0.3398500029\ldots+o(1)},
\tag{47}
\]

\[
\left\|\frac aN\right\|
\le
N^{-0.6601499971\ldots+o(1)},
\tag{48}
\]

and

\[
h,\;N-h
\ge
N^{0.8300749985\ldots-o(1)}.
\tag{49}
\]

The logarithm in (10) is swallowed by the `o(1)` exponent. Thus FD-301's `N` possible rational characters reduce, at balanced depth, to only `N^(0.33985...+o(1))` characters nearest zero, unless the untwisted correlation is already large.

At the source-energy ceiling `lambda=1/(2c)`, equation (41) becomes

\[
K_0=N^{o(1)}.
\tag{50}
\]

So immediately before the block-length ceiling kills the route altogether, the only possible demasked anomaly lies in a subpolynomial family of block-Fourier modes.

## 6. Prior-art boundary and ownership

The harmonic analysis in (20)--(33) is classical. The `1/k` coefficients are the finite cyclic version of the usual Dirichlet-kernel/interval Fourier profile, and (27) is ordinary Parseval. No novelty is claimed for either statement in isolation.

The mathematical delta is the capacity calibration forced by FD-300 and FD-301. Their same-block Möbius correlation has amplitude `Qx^(2c-o(1))`; at that scale, the generic Fourier tail estimate becomes strong enough to discard a polynomial fraction of the rational-twist family. This information is specific to the exact Farey-derived mask and threshold.

The Möbius short-interval inputs already anchored in `SOURCES.md` do not close (9) or (10). They concern single Möbius sums, exceptional-set control, or higher uniformity of a multiplicative function; here the object is the two-point product `mu(n)mu(n+h)` with a shift that may grow with the scale. Neighboring Chowla-type literature gives important fixed-shift or almost-all-scale information, but it does not provide the uniform pointwise estimate simultaneously in the growing shift and moving rational frequency required here.

A direct theorem bounding (34) and (6) for arbitrary source-selected `h` and `a` would therefore be a generic Möbius-cancellation theorem once the Farey mask has been removed. By the line mandate, that arithmetic theorem is not owned here. The line-owned contribution is the reduction of the family that such a theorem would actually need to control: zero frequency plus a shrinking low block-Fourier arc, with a central power-sized shift in the genuinely twisted branch.

No new external theorem is load-bearing in this finding, so `SOURCES.md` does not need a new anchor.

## 7. Adversarial audit and failure modes

Several stronger interpretations are not justified.

First, a small block-Fourier index is **not** the same as a small reduced denominator. Even if `k(a)<<N`, the fraction `a/N` may remain primitive with denominator `N`. Equation (15) asserts proximity to zero in `R/Z`, not a classical small-denominator major-arc statement.

Second, the tail estimate (28) is worst-case. It uses only `|mu(n)mu(n+h)|<=1`; no hidden Chowla cancellation, RH input, or averaging theorem enters. This is why the conclusion is a necessary localization rather than an upper bound for the anomaly itself.

Third, exact grouping into `Q` values per residue class uses the aligned interval `(NQ,2NQ]`. If the endpoints are moved independently of the length-`N` block partition, boundary terms have to be restored before applying (27).

Fourth, the zero-mode/twisted dichotomy is one-way. A large untwisted correlation does not imply near-capacity `L_N`, and a low nonzero twisted mode does not reconstruct the positive masked correlation with the required phase. Both are only necessary consequences of the Farey capacity premise.

Fifth, the genuinely twisted branch forces `h` and `N-h` to be power-sized, but it does not pin `h/N` away from zero or one by a fixed constant. At the upper live depth the quantity `Y` may still be `N/x^{o(1)}` rather than a fixed fraction of `N`.

Finally, the threshold `lambda>1/(4c)` is the point at which this **particular worst-case `l^2` tail argument** produces a sublinear frequency family. It is not claimed to be an intrinsic barrier. Any nontrivial improvement in the total twist-energy budget (27), or additional arithmetic information on the residue-class sums `V(r)`, would move the localization threshold further into shallower depths.

## Consequences for the research line

FD-300 reduced near-capacity block-Mertens mass to a large aligned same-block correlation. FD-301 removed the mask but left an arbitrary rational additive mode modulo `N`. FD-302 now shows that this apparent `N`-mode freedom is mostly artificial at the capacity scale.

In the live polynomial-depth range above `lambda=1/(4c)`, a near-capacity scenario must satisfy one of only two source anomalies:

\[
\boxed{
\text{large untwisted moving-shift correlation}
}
\tag{51}
\]

or

\[
\boxed{
\text{large nonzero correlation in the low block-Fourier arc }
 k(a)\le N^{2-4c\lambda+o(1)},
}
\tag{52}
\]

with the second branch additionally forcing

\[
h,\;N-h\ge N^{2c\lambda-o(1)}.
\tag{53}
\]

Thus a falsification theorem no longer needs uniform control over every rational character modulo `N`. At balanced depth it is enough, on the demasked side, to eliminate the zero mode and the first `N^(0.33985...+o(1))` block-Fourier modes for the source-selected power-sized shifts. Conversely, if those modes can carry the anomaly, the remaining difficulty has crossed the line boundary into a sharply specified moving-shift Möbius-correlation problem rather than a generic Farey-mask effect.

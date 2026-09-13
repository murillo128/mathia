# WI-281 — complete one-signed prime screening forces log-2 support packing and a smaller archimedean budget

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-BOOTSTRAP + CLASSICAL-REARRANGEMENT + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** a necessary condition for the **one-signed** branch of a hypothetical first unrestricted Suzuki null mode under complete active prime-power screening. The prime-power subfamily `2^k` alone forces the nonzero set of the mode to be a measurable lattice selector of covolume `log 2`. That packing constraint strictly lowers the maximum positive archimedean source budget available in the simultaneous-cut inequality of `WI-274`.
- **What it does not claim:** this is not RH, does not prove that a first null mode is one-signed, does not exclude complete screening by itself, and does not produce a numerical lower bound for the first-crossing spectral area. The new constant is exact but is defined spectrally rather than numerically.
- **Novelty boundary:** lattice fundamental-domain packing and the Riesz rearrangement inequality are classical. Suzuki supplies the localized Weil operator and source; `WI-274` supplies the saturated first-crossing reserve. The line-local deduction is their combination with the von-Mangoldt fact that every `2^k` is an active prime-power source whenever its lag fits inside the aperture. No priority claim is made.

## Claim

Assume RH is false and retain the first unrestricted crossing setup of `WI-253` and `WI-274`:

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\},
\qquad
q_a\ge0,
\qquad
\|v\|_2=1,
\qquad
A_av=0,
\tag{1}
\]

with `v` real and extended by zero outside `(-a,a)`. Assume the one-signed branch and replace `v` by `-v` if necessary, so

\[
v\ge0\quad\text{a.e.}
\tag{2}
\]

Suppose every active prime-power autocorrelation is screened:

\[
C_v(\log n)
:=\int_{\mathbb R}v(x+\log n)v(x)\,dx
=0
\tag{3}
\]

whenever `\Lambda(n)>0` and `\log n<2a`.

Put

\[
L:=\log2.
\tag{4}
\]

Then the measurable nonzero set

\[
E:=\{x\in\mathbb R:v(x)>0\}
\tag{5}
\]

obeys the exact packing bound

\[
\boxed{|E|\le L=\log2.}
\tag{6}
\]

More strongly, for almost every residue `r\in[0,L)`, at most one point in the lattice fiber

\[
r+L\mathbb Z
\tag{7}
\]

belongs to `E`. Thus complete one-signed screening forces the null mode to be a measurable selector modulo `log 2`.

Now use the Suzuki source from `WI-269`--`WI-274`,

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{8}
\]

and let

\[
h_0=\log\rho,
\qquad
\rho^3-\rho-1=0,
\tag{9}
\]

so that `w(h)>0` on `(0,h_0)` and `w(h)<0` for `h>h_0`. Define the even positive kernel

\[
K(t)
:=|t|w(|t|)\mathbf1_{\{|t|<h_0\}},
\qquad
K(0):=\frac12.
\tag{10}
\]

Let

\[
I_L:=(-L/2,L/2)
\tag{11}
\]

and let `T_L` be the compact self-adjoint integral operator on `L^2(I_L)`

\[
(T_Lf)(x)=\int_{I_L}K(x-y)f(y)\,dy.
\tag{12}
\]

Write

\[
\boxed{
K_{\rm pack}:=\frac12\lambda_{\max}(T_L).
}
\tag{13}
\]

Then `K_pack` is exactly the largest positive archimedean budget among normalized nonnegative functions whose `log 2`-lattice autocorrelations all vanish:

\[
\boxed{
K_{\rm pack}
=
\sup_{\substack{f\ge0,\ \|f\|_2=1\\
C_f(kL)=0\ (k\ge1)}}
\int_0^{h_0}h\,w(h)C_f(h)\,dh.
}
\tag{14}
\]

Moreover, if

\[
K_+:=\int_0^{h_0}h\,w(h)\,dh
\tag{15}
\]

is the unrestricted positive archimedean budget of `WI-274`, then

\[
\boxed{0<K_{\rm pack}<K_+.}
\tag{16}
\]

Consequently complete active prime screening on the one-signed first-crossing branch forces the strictly stronger spectral-area condition

\[
\boxed{
2\int_{a/2}^{a}\lambda_r\,dr
\le K_{\rm pack}
<K_+.
}
\tag{17}
\]

The older `WI-274` screening condition was only

\[
2\int_{a/2}^{a}\lambda_r\,dr\le K_+.
\tag{18}
\]

Thus the assumption of complete arithmetic screening feeds back into the continuous source itself: the same prime-power vanishing needed to remove the discrete source forces a support-packing constraint that makes the available archimedean screening budget **strictly smaller**.

## 1. Powers of two force a fundamental-domain packing

For every integer `k>=1`, the lag

\[
kL=\log(2^k)
\tag{19}
\]

is a von-Mangoldt lag. If `kL<2a`, hypothesis (3) gives

\[
C_v(kL)=0.
\tag{20}
\]

Because `v>=0`, the integrand is nonnegative, hence

\[
v(x+kL)v(x)=0
\quad\text{for almost every }x.
\tag{21}
\]

If instead `kL>=2a`, (21) is automatic: the zero extension of `v` is supported in an interval of length `2a`, and a shift by at least that length has only a null endpoint overlap. Therefore

\[
\boxed{v(x+kL)v(x)=0\quad\text{a.e. for every }k>=1.}
\tag{22}
\]

Equivalently,

\[
|E\cap(E-kL)|=0
\qquad(k\in\mathbb Z\setminus\{0\}).
\tag{23}
\]

Decompose Lebesgue measure over a fundamental interval for `L\mathbb Z`:

\[
|E|
=\int_0^L
\sum_{j\in\mathbb Z}
\mathbf1_E(r+jL)\,dr.
\tag{24}
\]

The countable family of null-overlap identities (23) implies that for almost every `r`, the sum in (24) is at most one. Hence

\[
|E|\le\int_0^L1\,dr=L,
\]

which proves (6) and the selector statement.

The same argument works for any fixed prime `p`, giving `|E|<=log p` from the `p^k` subfamily. The prime `2` gives the strongest member of this elementary family.

There is an additional first-crossing geometric consequence. Since `\lambda_r>0` for every `r<a`, the null vector `v` cannot be supported inside any translated interval of length `2r<2a`; otherwise translation invariance would give

\[
0=q_a(v)\ge\lambda_r\|v\|_2^2>0.
\tag{25}
\]

Thus a completely screened one-signed first mode must simultaneously have nonzero-set measure at most `log 2` **and** essential span equal to the full aperture `2a`. It is not a compact short bump: it must be a sparse full-span selector.

## 2. The positive saturated Suzuki kernel is already symmetric decreasing

For `0<h<h_0`, rewrite

\[
w(h)
=\kappa(h)-e^{h/2},
\qquad
\kappa(h):=\frac{e^{-h/2}}{e^{2h}-1}.
\tag{26}
\]

The first part of `h w(h)` is strictly decreasing. Indeed,

\[
\frac{d}{dh}\log\bigl(h\kappa(h)\bigr)
=\frac1h-\frac12-
\frac{2e^{2h}}{e^{2h}-1}.
\tag{27}
\]

For `h>0`,

\[
\frac{2e^{2h}}{e^{2h}-1}
=\frac2{1-e^{-2h}}
>\frac1h,
\tag{28}
\]

because `1-e^{-2h}<2h`. Therefore the right side of (27) is strictly less than `-1/2`. Meanwhile `h e^{h/2}` is strictly increasing. Hence

\[
h\mapsto h w(h)
\tag{29}
\]

is strictly decreasing on `(0,h_0)`. Its endpoint values are

\[
\lim_{h\downarrow0}h w(h)=\frac12,
\qquad
h_0w(h_0)=0.
\tag{30}
\]

Thus the even kernel `K` in (10) is nonnegative, compactly supported, symmetric decreasing, and positive almost everywhere on `(-h_0,h_0)`.

For any nonnegative `f\in L^2` with compact support,

\[
\begin{aligned}
B_+(f)
&:=\int_0^{h_0}h\,w(h)C_f(h)\,dh\\
&=\frac12
\iint_{\mathbb R^2}
 f(x)f(y)K(x-y)\,dx\,dy.
\end{aligned}
\tag{31}
\]

This is precisely the positive continuous budget that was bounded in `WI-274` by the scalar estimate `C_f(h)<=1`.

## 3. Riesz rearrangement converts the selector into the exact packing budget

Let `f>=0`, `||f||_2=1`, and suppose

\[
C_f(kL)=0\qquad(k>=1).
\tag{32}
\]

The proof of §1, now without any zeta input, gives

\[
|\{f>0\}|\le L.
\tag{33}
\]

Let `f^*` be the symmetric decreasing rearrangement. Since `K` is already symmetric decreasing, the classical Riesz rearrangement inequality gives

\[
\iint f(x)f(y)K(x-y)dxdy
\le
\iint f^*(x)f^*(y)K(x-y)dxdy.
\tag{34}
\]

Rearrangement preserves the `L^2` norm and the measure of the nonzero set, so `f^*` is supported in the centered interval of length at most `L`, hence in `I_L`. Equations (31), (34), and the Rayleigh principle therefore give

\[
B_+(f)
\le\frac12\langle f^*,T_Lf^*\rangle
\le\frac12\lambda_{\max}(T_L)
=K_{\rm pack}.
\tag{35}
\]

This upper bound is sharp for the **packing relaxation**. The kernel of `T_L` is nonnegative, so a top Rayleigh maximizer can be chosen nonnegative. Let `\phi>=0` be a normalized top eigenfunction, extend it by zero outside `I_L`, and note that

\[
C_\phi(kL)=0
\qquad(k>=1),
\tag{36}
\]

because `I_L` and `I_L-kL` overlap only in a null endpoint set for `k=1` and are disjoint for `k>=2`. Then

\[
B_+(\phi)
=\frac12\langle\phi,T_L\phi\rangle
=K_{\rm pack}.
\tag{37}
\]

This proves the exact variational identity (14). In particular, no argument using only the power-of-two packing consequence can replace `K_pack` by a smaller universal constant. Further improvement must use the other prime lags, firstness/null-equation compatibility, or another source-specific invariant.

## 4. Finite support makes the packing budget strictly smaller than `K_+`

The unrestricted convolution mass of `K` is

\[
M:=\int_{\mathbb R}K(t)dt
=2\int_0^{h_0}h\,w(h)dh
=2K_+.
\tag{38}
\]

Young's inequality only gives `lambda_max(T_L)<=M`; the strict inequality is also exact and elementary.

The operator `T_L` is Hilbert--Schmidt because `K` is bounded and compactly supported, so its top eigenvalue is attained. Extend a nonzero `f\in L^2(I_L)` by zero to `\mathbb R`. With the usual Fourier normalization,

\[
\langle f,T_Lf\rangle
=\frac1{2\pi}
\int_{\mathbb R}
\widehat K(\xi)|\widehat f(\xi)|^2d\xi.
\tag{39}
\]

Since `K` is even and nonnegative,

\[
\widehat K(\xi)
=\int K(t)\cos(\xi t)dt.
\tag{40}
\]

For every `\xi\ne0`, positivity of `K` on an interval implies

\[
\widehat K(\xi)<\widehat K(0)=M,
\tag{41}
\]

because `1-\cos(\xi t)` is strictly positive on a set of positive `K(t)dt` measure. A nonzero `L^2` Fourier transform cannot be supported on the singleton `{0}`. Hence every nonzero `f` satisfies

\[
\langle f,T_Lf\rangle<M\|f\|_2^2.
\tag{42}
\]

If `lambda_max(T_L)=M`, an attaining top eigenfunction would contradict (42). Therefore

\[
\lambda_{\max}(T_L)<M=2K_+,
\]

which proves (16).

The strict loss has a simple interpretation. The scalar bound `C_v(h)<=1` in `WI-274` behaves as though the positive source could use a translation-invariant constant profile over the whole line. Power-of-two screening forbids that geometry: all mass must fit into one representative per `log 2` orbit, and after rearrangement the worst possible positive-source interaction is a finite-interval Wiener--Hopf compression. A finite compression cannot attain the full convolution mass.

## 5. Insert the packing budget into the first-crossing reserve

The saturated source of `WI-274` is

\[
\mathcal S_v
=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}(\log n)C_v(\log n)
+
\int_0^{2a}h\,w(h)C_v(h)dh,
\tag{43}
\]

and the simultaneous-cut argument proves

\[
\boxed{
\mathcal S_v
\ge2\int_{a/2}^{a}\lambda_rdr>0.
}
\tag{44}
\]

Under complete prime screening, the discrete sum in (43) is zero. Since `v>=0`, one also has

\[
C_v(h)\ge0,
\tag{45}
\]

while `w(h)<0` for `h>h_0`. Therefore the negative tail can only decrease the source:

\[
\mathcal S_v
\le
\int_0^{h_0}h\,w(h)C_v(h)dh
=B_+(v).
\tag{46}
\]

The power-of-two subfamily of the same screening hypothesis gives (22), so the exact packing budget (14) applies:

\[
B_+(v)\le K_{\rm pack}.
\tag{47}
\]

Combining (44), (46), and (47) proves (17):

\[
\boxed{
0<2\int_{a/2}^{a}\lambda_rdr
\le\mathcal S_v
\le K_{\rm pack}
<K_+.
}
\tag{48}
\]

This is a genuine defect-to-structure bootstrap, though not yet a contradiction. The hypothesis that all arithmetic overlap disappears no longer leaves the archimedean side unchanged; it forces a fixed strict reduction of the continuous compensation budget.

## 6. Stress tests and exact boundary

The argument is deliberately one-signed. If `v` changes sign, `C_v(kL)=0` does not imply pointwise disjointness at lag `kL`, so the selector theorem fails. Nothing here narrows the sign-changing branch beyond `WI-269` and the subsequent Hilbert-cut findings.

The packing result uses only the powers of two. Other primes are needed in §5 to make the entire discrete sum in (43) vanish, but they are not used in the support estimate. Consequently `K_pack` is best viewed as the exact cost of the **first arithmetic feedback layer**, not the final complete-screening optimum.

The constant is exact without a numerical eigenvalue certificate. No floating-point estimate for `lambda_max(T_L)` is used in the claim. A later certified enclosure could decide whether the strengthened budget already crosses any independently established lower bound for the spectral area, but such a computation is not needed for the present structural result.

The first-crossing span statement after (25) prevents an actual null mode from being the compact interval optimizer that realizes the packing relaxation. This suggests that `K_pack` itself may not be sharp for the **Suzuki-null** subclass. Obtaining a uniform further gap, however, requires quantitative compatibility between near-extremizers of the rearrangement problem and the null/firstness equation; mere strict nonattainment is not enough.

## 7. Prior art and novelty audit

The localized Weil operator and its source are from Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), especially Theorem 1.1 and the distributional source formulas in §2.5. The first-crossing and saturated-cut consequences used here are line-local deductions already persisted in `WI-253`, `WI-269`, and `WI-274`.

The rearrangement step is classical. The Riesz rearrangement inequality dates to F. Riesz and Sobolev, with the general multiple-integral framework of Brascamp--Lieb--Luttinger; for equality structure see Almut Burchard, **Cases of equality in the Riesz rearrangement inequality**, *Annals of Mathematics* 143 (1996), 499--527, DOI `10.2307/2118534`. The lattice-selector estimate (24) is the elementary fundamental-domain packing identity for `L\mathbb Z`.

A targeted audit around Riesz rearrangement, finite-interval convolution/Wiener--Hopf compressions, translational packing, autocorrelation zero sets, Suzuki's localized Weil operator, and prime-power screening found the classical ingredients but no statement coupling complete one-signed von-Mangoldt screening to the `log 2` selector or to the reduced saturated source budget (17). Search absence is audit context only and is not a priority claim.

No part of the classical rearrangement or packing machinery is claimed as new. The durable mathematical content here is the exact feedback chain

\[
\text{complete prime screening}
\Longrightarrow
\text{power-of-two lattice selector}
\Longrightarrow
|\{v\ne0\}|\le\log2
\Longrightarrow
B_+(v)\le K_{\rm pack}<K_+,
\tag{49}
\]

inserted into the source-specific first-crossing reserve.

## Research implication

`WI-278` and `WI-280` show that neither a scalar `lambda_r` profile nor generic PSD cut covariance can by itself force the `WI-274` reserve through the unrestricted archimedean budget. The present result escapes those exact relaxations in a different way: it conditions the budget on the **arithmetic hypothesis being tested**. If all prime overlap is screened, the powers of two force spatial sparsity, and that sparsity reduces how much positive archimedean source can remain available to perform the screening.

The next useful gate is therefore source/eigenfunction-specific rather than another generic covariance mixture: quantify the additional loss forced by the fact that a first Suzuki null mode has full essential span and satisfies the exact null equation, whereas the packing optimizer in (37) is a compact interval mode. A quantitative stability theorem for the rearrangement/Wiener--Hopf extremizer coupled to firstness would turn the strict qualitative separation after (25) into another fixed budget decrement. The present finding does not assume such a stability theorem.
